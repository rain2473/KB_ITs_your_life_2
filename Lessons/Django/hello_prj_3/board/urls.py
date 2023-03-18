from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='main'),
    path('<int:pk>/', views.board_view ,name='view'),
    path('create/', views.board_create, name='create'),
    path('list/', views.board_list, name='list'),
    path('update/<int:pk>', views.board_update, name='update'),
    path('delete/<int:pk>', views.board_delete, name='delete'),
]
