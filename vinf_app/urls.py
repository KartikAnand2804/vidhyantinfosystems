from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='ContactPage'),
    path('gallery/', views.gallery, name='Gallery'),
    path('blog/', views.blog, name='Blog'),
    path('blog-page/', views.blogPage, name='BlogPage'),
    path('courses/', views.courses, name='Courses'),

]