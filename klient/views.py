from django.shortcuts import render, redirect
from .models import Klient
from .forms import AddForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class LoginPage(LoginView):
    template_name = 'klient/login.html'


class IndexListView(LoginRequiredMixin, ListView):
    model = Klient


class IndexSearchedListView(LoginRequiredMixin,ListView):
    model = Klient
    template_name = 'klient/search.html'

    def get_queryset(self):
        query = self.request.GET.get("sv","")
        object_list = Klient.objects.filter(nazwa__icontains=query)
        return object_list


@login_required()
def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.instance.grupa = request.user
            form.save()
            return redirect('index')
    else:
        form = AddForm()
    return render(request,'klient/add.html',{'form':form})

@login_required()
def delete(request, id):
    klient = Klient.objects.get(id=id,grupa=request.user)
    klient.delete()
    return redirect('index')
