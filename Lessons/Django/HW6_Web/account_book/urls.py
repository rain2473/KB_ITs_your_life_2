from django.urls import path
from . import views
urlpatterns = [
    path('', views.account_book_main, name="main"),
    path('create_income/', views.AccountBookCreateIncomeView.as_view() ,name='create_income'),
    path('create_outcome/', views.AccountBookCreateOutcomeView.as_view() ,name='create_outcome'),
    path('list/', views.AccountBookListView.as_view(), name='list'),
    path('detail/<int:pk>', views.AccountBookDetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.AccountBookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.AccountBookDeleteView.as_view(), name='delete'),
]