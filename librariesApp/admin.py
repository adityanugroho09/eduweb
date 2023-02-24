from django.contrib import admin
from librariesApp.models import Library, LibraryItem
# Register your models here.
admin.site.register(Library)
admin.site.register(LibraryItem)