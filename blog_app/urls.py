from django.urls import path
from . import views

urlpatterns = [
    # path('blog_list/', views.blog_list, name='blog_list'),
    # path('blog_detail/<int:pk>/', views.blog_detail, name='blog_detail'),
    
    # class based Views urls
    path('class_blog_list/', views.BlogListView.as_view(), name='blog_list'),
    path('class_blog_detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]