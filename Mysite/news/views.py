from django.shortcuts import render, redirect
from .models import Beer
from .forms import BeerForm
from django.views.generic import DeleteView


class BeerDelete(DeleteView):
    model = Beer
    success_url = '/news/'
    template_name = 'news/beer_delete.html'



def news_home(request):
    news = Beer.objects.order_by('-date')
    return render(request, 'news/news.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = BeerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Вы ошиблись пивом"
    form = BeerForm()
    data = {"form": form,
            'error': error }
    return render(request, 'news/create.html', data)
# Create your views here.
