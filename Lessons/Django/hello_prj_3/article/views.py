from django.shortcuts import render
from django.views.generic.edit import CreateView,  ListView, DetailView, DeleteView, UpdateView
from .models import Article

def index(request):
    return render(request,'article/index.html')

class ArticleCreateView(CreateView):
    model = Article
    fields = ["title","content"]
    template_name = "article/article_create.html"   #앱/모델_기능
    success_url = "main"

class ArticleListView(ListView):
    model = Article
    template_name = "article/article_list.html"   #앱/모델_기능
    ordering = "-pk"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/article_detail.html"   #앱/모델_기능

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article/article_delete.html"   #앱/모델_기능

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article/article_update.html"   #앱/모델_기능