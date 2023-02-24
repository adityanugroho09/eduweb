from django.urls import path, re_path
from librariesApp.views import addtoLibrary, deleteItemLibrary

urlpatterns = [
    path('course/<int:course_id>/add/', addtoLibrary, name='add_to_library'),
    path('course/<int:course_id>/library/delete/', deleteItemLibrary, name='delete_item_library'),
]