from django.db import reset_queries
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from tiendavirtualapp.models import Categorias,Calificaciones,Productos,ProductosPedido,Pedidos,Inventario,Clientes
# Create your views here.
def home(request):
    validate_sesion(request)
    all_cat=Categorias.objects.all().order_by('id')
    latest_prod=Productos.objects.all().order_by('-id')[:6]
    top_prod=Calificaciones.objects.all().order_by('-calificacion')[:6]
    latest_review=Calificaciones.objects.all().order_by('-id')[:6]
    return render(request,"home.html",{
        "all_cat":all_cat,"latest_prod":latest_prod,"top_prod":top_prod,"latest_review":latest_review
    })

def lista_activos(request):
    validate_sesion(request)
    return render(request,"listaactivos.html")

def producto_detalles(request,product_id):
    print("entroo prod")
    validate_sesion(request)
    producto=get_object_or_404(Productos,pk=product_id)
    productos_relacionados =Productos.objects.filter(categoria_id=producto.categoria.id)
    calificaciones=Calificaciones.objects.filter(producto=product_id)
    totalcal=0.0
    average=0.0
    for cal in calificaciones:
        totalcal+=float(cal.calificacion)
    if totalcal:
        average=totalcal/len(calificaciones)
    promedio=range(int(average))
    return render(request,"shop_details.html",{"producto":producto,
    "productos_relacionados":productos_relacionados,
    "calificaciones":calificaciones,
    "totalcal":totalcal,"promedio":promedio,
    "range":range(6)
    })

def lista_categorias(request):
    validate_sesion(request)
    return HttpResponse("Lista de categorias")

def shopping_cart(request):
    validate_sesion(request)
    shopping_list=[]
    print(request.session["shop_cart"]["productos"])
    for prod_id, prod_quantity in request.session["shop_cart"]["productos"].items():
        producto=get_object_or_404(Productos,pk=int(prod_id))
        total_producto=float(producto.precio_unidad)*prod_quantity
        shopping_list.append({"quantity":prod_quantity,"product_id":prod_id,"nombre":producto.nombre,
            "precio":producto.precio_unidad,"total":total_producto })
    return render(request,"shopping_cart.html",{"shopping_list":shopping_list})

def checkout(request):
    validate_sesion(request)
    return render(request,"checkout.html")

def contact(request):
    validate_sesion(request)
    return render(request,"contact.html")

def add_product(request):
    if request.POST["product_id"] and request.POST["quantity"]:
        product_id=request.POST["product_id"]
        producto=get_object_or_404(Productos,pk=product_id)
        validate_sesion(request)
        print(product_id)
        if str(product_id) in request.session["shop_cart"]:
            request.session["shop_cart"]["productos"][str(product_id)] += int(request.POST["quantity"])
        else:
            request.session["shop_cart"]["productos"][str(product_id)] = int(request.POST["quantity"])
        request.session["shop_cart"]["total_productos"]+= int(request.POST["quantity"])
        total_var=(producto.precio_unidad* int(request.POST["quantity"]))
        request.session["shop_cart"]["total_valor"]+=float(total_var)

        request.session.modified=True#obliga la actualizacion en db de session
        return redirect('productodetalles',product_id=product_id)
    else:
        return HttpResponse("Error no se ha seleccionado producto")

def changeproductquantity(request):
    if request.POST["product_id"] and request.POST["quantity"]:
        product_id=request.POST["product_id"]
        producto=get_object_or_404(Productos,pk=product_id)
        validate_sesion(request)
        if str(product_id) in request.session["shop_cart"]["productos"]:
            #se hace un reset de los totales
            original_quantity=request.session["shop_cart"]["productos"][str(product_id)]
            original_total_pro=producto.precio_unidad * original_quantity

            request.session["shop_cart"]["total_productos"] -=original_quantity
            request.session["shop_cart"]["total_valor"]-=float(original_total_pro)

            #se actualiza segun la cantidad
            if int(request.POST["quantity"])>0:
                request.session["shop_cart"]["productos"][str(product_id)]=int(request.POST["quantity"])
                request.session["shop_cart"]["total_productos"]+=int(request.POST["quantity"])
                total_var= (producto.precio_unidad*int(request.POST["quantity"]))
                request.session["shop_cart"]["total_valor"]+=float(total_var)
            else:
                request.session["shop_cart"]["productos"].pop(str(product_id))
            
            request.session.modified=True#obliga la actualizacion en db de session
            return redirect('shoppingcart')
        else:
            return HttpResponse("El producto no se encuentra en la canasta")
    else:
        return HttpResponse("Error no se ha seleccionado producto")

def deleteproduct(request):
    if request.POST["product_id"]:
        validate_sesion(request)
        product_id=request.POST["product_id"]
        producto=get_object_or_404(Productos,pk=product_id)

        if str(product_id) not in request.session["shop_cart"]["productos"]:
            return HttpResponse("El producto no se encuentra actualmente en la canasta")
        
        # se hace un reset
        original_quantity=request.session["shop_cart"]["productos"][str(product_id)]
        original_total_pro=producto.precio_unidad * original_quantity


        request.session["shop_cart"]["total_productos"]-= int(original_quantity)
        request.session["shop_cart"]["total_valor"]-=float(original_total_pro)
        request.session["shop_cart"]["productos"].pop(str(product_id))

        request.session.modified=True#obliga la actualizacion en db de session
        return redirect('shoppingcart')
    else:
        return HttpResponse("Error no se ha seleccionado producto")

def validate_sesion(request):
    if 'shop_cart' not in request.session:
        request.session["shop_cart"]={'total_productos':0,'total_valor':0.0,'productos':{}}
