from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Topic(models.Model):
    topic_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.topic_name

class ContentType(models.Model):
    type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.type_name

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200)

    def __str__(self):
        return self.publisher_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, default='course')
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    hero = models.ImageField(null=True, blank=True, default='hero_default.jpg', upload_to='course_hero')
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.course_name

class Unit(models.Model):
    unit_name = models.CharField(max_length=100, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.unit_name

class Video(models.Model):
    video_name = models.CharField(max_length=100, blank=True)
    video_link = models.URLField(max_length=500, blank=True)
    description = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.video_name
