from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('category/<str:ctitle>/', views.catredirect, name='category-filter'),
    path('blog/', views.blog, name='bloghome'),
    path('blog/<int:id>/', views.detail, name='article_detail'),
]