from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import AccountBook

def account_book_main(request):
    return render(request, "account_book/main.html")

class AccountBookCreateIncomeView(CreateView):
    model = AccountBook
    fields = ["title","amount",'contents']
    template_name = "account_book/create_income.html"   #앱/모델_기능
    success_url = "/account_book/list"
    def get_initial(self):
        initial = super(AccountBookCreateIncomeView, self).get_initial()
        initial['contents'] = "수입"
        return initial

class AccountBookCreateOutcomeView(CreateView):
    model = AccountBook
    fields = ["title","amount",'contents']
    template_name = "account_book/create_outcome.html"   #앱/모델_기능
    success_url = "/account_book/list"
    def get_initial(self):
        initial = super(AccountBookCreateOutcomeView, self).get_initial()
        initial['contents'] = "지출"
        return initial


class AccountBookListView(ListView):
    model = AccountBook
    template_name = "account_book/list.html"   #앱/모델_기능
    ordering = "-pk"

class AccountBookDetailView(DetailView):
    model = AccountBook
    template_name = "account_book/detail.html"   #앱/모델_기능

class AccountBookDeleteView(DeleteView):
    model = AccountBook
    template_name = "account_book/delete.html"   #앱/모델_기능
    success_url = "/account_book/list"

class AccountBookUpdateView(UpdateView):
    model = AccountBook
    fields = ["title","amount","contents"]
    template_name = "account_book/update.html"   #앱/모델_기능
    success_url = "/account_book/list"
