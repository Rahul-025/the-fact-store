from gallery.models import *
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *


def not_found_404(request, exception):
    return render(request, '404_page.html')

def home(request):
    posts = GalleryPost.objects.all().order_by('-date_posted')[0:12]
    articles = Article.objects.all().order_by('-date_posted')[0:3]
    return render(request, 'home.html', {'posts': posts, 'articles':articles})

def about(request):
    return render(request, 'about.html')


def gallery(request):
    posts = GalleryPost.objects.all().order_by('-date_posted')
    return render(request, 'gallery.html', {'posts': posts})

def blog(request):
    articles = Article.objects.all()
    return render(request, 'blog.html', {'articles': articles})

def detail(request, id):
    article = Article.objects.get(article_id = id)
    article_images = ArticleImages.objects.filter(article = article)
    article_contents = ArticleContent.objects.filter(article = article)
    data = {'article':article, 'article_images':article_images, 'article_contents':article_contents}
    return render(request, 'detail.html', data)

def catredirect(request, ctitle):

    if(ctitle == "All"):
        filtered_posts = GalleryPost.objects.all().order_by('-date_posted')
        paginator = Paginator(filtered_posts, 4)
        page = request.GET.get('page')
        filtered_posts = paginator.get_page(page)
        return render(request, 'catredirect.html', {'filtered_posts': filtered_posts, 'ctitle':'All Posts'})
    else:
        category = GalleryCategory.objects.get(cat_title=ctitle)
        filtered_posts = GalleryPost.objects.filter(post_cat=category).order_by('-date_posted')
        paginator = Paginator(filtered_posts, 4)
        page = request.GET.get('page')
        filtered_posts = paginator.get_page(page)
        data = {'filtered_posts':filtered_posts, 'ctitle':ctitle}
        return render(request, 'catredirect.html', data)