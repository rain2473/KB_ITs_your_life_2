from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index , name="main"),
    path('create/',views.ArticleCreateView.as_view(), name="create" ),
    path('list/',views.ArticleListView.as_view(), name="list" ),
    path('detail/<int:pk>',views.ArticleDetailView.as_view(), name="detail" ),
    path('delete/<int:pk>',views.ArticleDeleteView.as_view(), name="delete" ),
    path('update/<int:pk>',views.ArticleUpdateView.as_view(), name="update" ),
]
