"""tiendavirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#views
from tiendavirtualapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('listaactivos/', views.lista_activos, name="listaactivos"),
    path('productodetalles/<int:product_id>', views.producto_detalles, name="productodetalles"),
    path('listacategorias/', views.lista_categorias,name="listacategorias"),
    path('shoppingcart/', views.shopping_cart, name="shoppingcart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('addproduct/', views.add_product, name="addproduct"),
    path('changeproductquantity/', views.changeproductquantity, name="changeproductquantity"),
    path('deleteproduct/', views.deleteproduct, name="deleteproduct"),
]
