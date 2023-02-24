from django.shortcuts import render, redirect
from .models import Course
from librariesApp.models import Library, LibraryItem
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random

# Create your views here.
def courseIntro (request, course_id):
    course = Course.objects.get(pk=course_id)
    user = request.user
    library = None
    library_items = None
    obj = None

    if user.is_authenticated:
        try:
            library = Library.objects.get(student=user)
        except Library.DoesNotExist:
            library = None

        try:
            library_items = library.libraryitem_set.all()
        except AttributeError:
            library_items = None

        obj = None

        if library_items is not None:
            for item in library_items:
                if item.course.id == course_id:
                    obj = item
                    break
                else:
                    obj = None

    # Handle Recomendations
    course_type = course.content_type.type_name
    course_topic = course.topic.topic_name

    courses = Course.objects.all()
    recomendations = courses.filter(
        Q(content_type__type_name=course_type) &
        Q(topic__topic_name=course_topic) |
        Q(topic__topic_name=course_topic)
    ).exclude(pk=course_id)

    recomendations = list(recomendations)
    recomendations = random.sample(recomendations, len(recomendations))[:3]
    context = {
        'course':course, 
        'library_items':library_items, 
        'obj':obj, 
        'recomendations':recomendations
    }

    return render(request, 'courses/course_intro.html', context)

@login_required(login_url='login_page')
def courseHome (request, course_id):
    course = Course.objects.get(pk=course_id)
    units = course.unit_set.all()
    context = {'course':course, 'units':units}
    
    return render(request, 'courses/course_home.html', context)

@login_required(login_url='login_page')
def focusUnit (request, course_id, unit_id, video_id):
    course = Course.objects.get(pk=course_id)
    units = course.unit_set.all()
    unit = course.unit_set.get(pk=unit_id)
    video = unit.video_set.get(pk=video_id)

    context = {'course':course, 'units':units, 'unit':unit, 'video':video}

    return render(request, 'courses/course_home.html', context)\

@login_required(login_url='login_page')
def addtoLibrary (request, course_id):
    course = Course.objects.get(pk = course_id)
    user = request.user
    library, created = Library.objects.get_or_create(student=user)
    library_item, created = LibraryItem.objects.get_or_create(library=library, course=course)
    library_item.save()

    return redirect('course_home', course_id)

@login_required(login_url='login_page')
def deleteItemLibrary(request, course_id):
    course = Course.objects.get(pk = course_id)

    user = request.user
    library = Library.objects.get(student=user)
    library_item = library.libraryitem_set.get(course=course)
    library_item.delete()

    return redirect('profile_page')
