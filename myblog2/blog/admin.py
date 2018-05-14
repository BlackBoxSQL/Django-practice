from django.contrib import admin
from .models import Article,Aboutme, Guitar, BlogTutorial, VideoTutorial, Code, Poetry, Projects, Stories

# Register your models here.
admin.site.register(Article)
admin.site.register(Code)
admin.site.register(Projects)
admin.site.register(BlogTutorial)
admin.site.register(VideoTutorial)
admin.site.register(Poetry)
admin.site.register(Stories)
admin.site.register(Guitar)
admin.site.register(Aboutme)

# ckeditor works
# tinymce works
# trixworks
