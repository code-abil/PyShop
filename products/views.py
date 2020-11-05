from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# By convention, the view function of homepage is named index.
def index(request):
    products = Product.objects.all()
    # all(), filter(), get(), save() are few methods of model class.
    return render(request, 'index.html',
                  {"products": products})


def trending(request):
    return HttpResponse('Trending')

