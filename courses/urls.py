from django.urls import path, re_path
from courses.views import courseIntro, focusUnit, courseHome

urlpatterns = [
    path('course/<int:course_id>/', courseIntro, name='course_intro'),
    path('course/<int:course_id>/home/', courseHome, name='course_home'),
    re_path(r'^course/(?P<course_id>[0-9]+)/home/(?P<unit_id>[0-9]+)/(?P<video_id>[0-9]+)/$', focusUnit, name='focus-unit'),
]