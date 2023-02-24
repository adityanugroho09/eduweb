from django.contrib import admin

# Register your models here.
from .models import Unit, Video, Course, Topic, ContentType, Publisher
import nested_admin

class VideoInline(nested_admin.NestedTabularInline):
    model = Video
    extra = 0

class UnitInline(nested_admin.NestedStackedInline):
    model = Unit
    extra = 0
    inlines = [VideoInline]

class CourseAdmin(nested_admin.NestedModelAdmin):
    list_display = ('course_name', 'created', 'updated')
    search_fields = ['course_name']
    fieldsets = [
        ('Data', {'fields': ['course_name', 'description', 'topic', 'content_type', 'publisher', 'hero']})
    ]
    inlines = [UnitInline]

class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_name', 'course')
    list_filter = ['course']
    search_fields = ['course__course_name', 'unit_name']
    inlines = [VideoInline]

class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_name', 'unit')
    search_fields = ['unit__unit_name', 'video_name']

admin.site.register(Course, CourseAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Topic)
admin.site.register(ContentType)
admin.site.register(Publisher)