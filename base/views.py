from django.shortcuts import render
from courses.models import Course
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

def homePage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    courses = Course.objects.filter(
        Q(course_name__icontains=q) |
        Q(description__icontains=q) |
        Q(content_type__type_name__icontains=q) |
        Q(topic__topic_name__icontains=q)
    )

    course_count = courses.count() 

    p = Paginator(courses, 8)
    page = request.GET.get('page')
    courses_list = p.get_page(page)
    pages = courses_list.paginator.num_pages

    context = {
        'courses':courses,
        'course_count':course_count, 
        'courses_list':courses_list, 
        'pages':pages
        }

    return render(request, 'base/home_page.html', context)