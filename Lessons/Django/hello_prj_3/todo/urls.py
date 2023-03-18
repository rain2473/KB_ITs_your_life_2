from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='main'),
    path('<int:pk>/', views.todo_view ,name='view'),
    path('create/', views.todo_create, name='create'),
    path('list/', views.todo_list, name='list'),
    path('update/<int:pk>', views.todo_update, name='update'),
    path('delete/<int:pk>', views.todo_delete, name='delete'),
    path('detail/<int:pk>', views.todo_detail, name='detail'),
]
