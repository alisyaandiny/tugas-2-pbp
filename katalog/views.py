from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_catalog_item(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'nama' : 'Alisya Alhabsyi',
        'NPM' : '2106706281',
        'list_catalog': data_catalog_item
    }

    return render(request, "katalog.html", context)

from django.shortcuts import render
from katalog.models import CatalogItem