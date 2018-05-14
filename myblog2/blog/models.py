from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    time_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Article Name: {}, Added: {}'.format(self.title, self.time_added)

    class Meta:
        ordering = ["-pk"]


class Code(models.Model):
    problemname = models.CharField(max_length=25)
    codesol = RichTextField(blank=True, null=True)
    sitename = models.CharField(max_length=25)

    def __str__(self):
        return 'Site: {}, Problem_id: {}'.format(self.sitename, self.problemname)


class Projects(models.Model):
    name_of_project = models.CharField(max_length=30)
    details_of_project = RichTextField(blank=True, null=True)
    see_it = models.URLField(blank=True, null=True)
    added = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Name of project: {}, Added: {}'.format(self.name_of_project, self.added)


class BlogTutorial(models.Model):
    blog_tut_name = models.CharField(max_length=100)
    blog_tut = RichTextField(blank=True, null=True)
    blog_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Added: {}, Name: {}'.format(self.blog_added, self.blog_tut_name)


class VideoTutorial(models.Model):
    video_tut_name = RichTextField(blank=True, null=True)
    video_link = models.TextField()
    video_added = models.DateField(default=timezone.now)


    def __str__(self):
        return 'Added: {}, Name: {}'.format(self.video_added, self.video_tut_name)


class Stories(models.Model):
    nameofstory = models.CharField(max_length=100)
    story = RichTextField(blank=True, null=True)
    written_in = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Added: {}, Name: {}'.format(self.written_in, self.nameofstory)


class Poetry(models.Model):
    heading = models.CharField(max_length=20)
    thepoetry = RichTextField(blank=True, null=True)
    written_in = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Added: {}, Name: {}'.format(self.written_in, self.heading)


class Guitar(models.Model):
    song_name = models.CharField(max_length=50)
    artist = models.CharField(max_length=25)
    chords = RichTextField(blank=True, null=True)
    added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Added: {}, Name: {}'.format(self.added, self.song_name)

class Aboutme(models.Model):
    content = RichTextField(blank=True, null=True)
    time_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Added: {}'.format(self.time_added)
