from django.shortcuts import render, redirect
from .models import Library, LibraryItem
from courses.models import Course
from django.contrib.auth.decorators import login_required

# Create your views here.
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