from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def lista_activos(request):
    return HttpResponse("Lista de productos")

def producto_detalles(request,product_id):
    return HttpResponse("Detalle product {}".format(product_id))

def lista_categorias(request):
    return HttpResponse("Lista de categorias")