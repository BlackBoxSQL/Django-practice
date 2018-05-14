from django.utils import timezone
from .models import Article,Aboutme, Code, Poetry, Projects, Guitar, BlogTutorial, VideoTutorial, Stories
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)


# Create your views here.
class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/articles.html'
    paginate_by = 10
    queryset = Article.objects.all()



class LatestArticle(ListView):
    model = Article
    context_object_name = 'latestarticles'
    template_name = 'blog/home.html'
    queryset = Article.objects.filter(time_added__lte=timezone.now()).order_by('-time_added')[:5]


class VideoTutListView(ListView):
    model = VideoTutorial
    context_object_name = 'vidtut'
    template_name = 'blog/video.html'
    paginate_by = 10

    def get_queryset(self):
        return VideoTutorial.objects.filter(video_added__lte=timezone.now()).order_by('-video_added')

class StoriesListView(ListView):
    model = Stories
    context_object_name = 'story'
    template_name = 'blog/stories.html'
    paginate_by = 5
    queryset = Stories.objects.all().order_by('-written_in')

class CodeListView(ListView):
    model = Code
    context_object_name = 'codes'
    template_name = 'blog/codes.html'
    paginate_by = 20
    queryset = Code.objects.order_by('sitename')

class PoetryListView(ListView):
    model = Poetry
    context_object_name = 'poetries'
    template_name = 'blog/poetry.html'
    paginate_by = 10
    queryset = Poetry.objects.order_by('-written_in')

class ProjectsListView(ListView):
    model = Projects
    context_object_name = 'project'
    template_name = 'blog/projects.html'
    paginate_by = 8
    queryset = Projects.objects.order_by('-added')

class GuitarListView(ListView):
    model = Guitar
    context_object_name = 'chords'
    template_name = 'blog/guitars.html'
    paginate_by = 8
    queryset = Guitar.objects.order_by('-added')

class BlogTutorialListView(ListView):
    model = BlogTutorial
    context_object_name = 'blogs'
    template_name = 'blog/blogtuts.html'
    paginate_by = 8
    queryset = BlogTutorial.objects.order_by('-blog_added')

class About(ListView):
    model = Aboutme
    context_object_name = 'contents'
    template_name = 'blog/aboutme.html'
    queryset = Aboutme.objects.order_by('-time_added')