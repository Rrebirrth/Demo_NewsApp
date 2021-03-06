# Generated by Django 2.1 on 2019-07-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='launguage',
            field=models.CharField(choices=[(' Chinese', ' Chinese'), ('Spanish', 'Spanish'), ('English', 'English'), ('Hindi', 'Hindi'), ('Arabic', 'Arabic'), ('Portuguese', 'Portuguese'), ('Bengali', 'Bengali'), ('Russian', 'Russian'), ('Japanese', 'Japanese'), ('Punjabi', 'Punjabi'), ('Norwegian', 'Norwegian'), ('German', 'German'), ('French', 'French'), ('Dutch', 'Dutch')], default='English', max_length=15),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.CharField(choices=[('current events', 'Current Events'), ('politics', 'Politics'), ('philosophy', 'Philosophy'), ('sports', 'Sports'), ('literature', 'Literature'), ('tech', 'Tech'), ('physics', 'Physics'), ('biology', 'Biology'), ('chemistry', 'Chemistry'), ('mathematics', 'Mathematics'), ('identity', 'Identity')], default='Current Events', max_length=15),
        ),
    ]
