from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms

Topic_CHOICES= [
    ('politics', 'Politics'),
    ('philosophy', 'Philosophy'),
    ('sports', 'Sports'),
    ('literature', 'Literature'),
    ('tech', 'Tech'),
    ('physics', 'Physics'),
    ('biology', 'Biology'),
    ('chemistry', 'Chemistry'),
    ('mathematics', 'Mathematics'),
    ('identity', 'Identity'),
    ]

Language_CHOICES= [
    (' Chinese', ' Chinese'),
    ('Spanish', 'Spanish'),
    ('English', 'English'),
    ('Hindi', 'Hindi'),
    ('Arabic', 'Arabic'),
    ('Portuguese', 'Portuguese'),
    ('Bengali', 'Bengali'),
    ('Russian', 'Russian'),
    ('Japanese', 'Japanese'),
    ('Punjabi', 'Punjabi'),
    ('Norwegian', 'Norwegian'),
    ('German', 'German'),
    ('French', 'French'),
    ('Dutch', 'Dutch'),
        ]



#forms.CharField(label='Topic', widget=forms.Select(choices=Topic_CHOICES))


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=15, choices=Topic_CHOICES)
    launguage = models.CharField(max_length=15, choices=Language_CHOICES, default = 'English')



    def __str__(self):
        return self.title



