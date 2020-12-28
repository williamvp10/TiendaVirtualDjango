from django.db import models
import datetime
from django.db.models.aggregates import Max

from django.db.models.deletion import PROTECT
# Create your models here.
class Categorias(models.Model):
    codigo=models.CharField(max_length=5,verbose_name='Código de la categoría')
    nombre=models.CharField(max_length=20,verbose_name='Nombre de la categoría')
    descripcion=models.TextField(verbose_name='Texto descriptivo de la categoría')
    TRUE_FALSE_CHOICES=(
        ('Si','Activo'),
        ('No','Inactivo')
    )
    activo=models.CharField(max_length=2,choices=TRUE_FALSE_CHOICES,default='Si')

    def __str__(self):
        return 'Categoría {categoria} con código {codigo}, activa:{activo}'.format(
            categoria=self.nombre,codigo=self.codigo,activo=self.activo)

    class Meta:
        verbose_name_plural= "Categorias"

class Productos(models.Model):
    codigo=models.CharField(max_length=5,verbose_name='Código del producto')
    nombre=models.CharField(max_length=20,verbose_name='Nombre del producto')
    descripcion=models.TextField(verbose_name='Texto descriptivo del producto')
    UNIDAD_CHOICES=(
        ('Kg','Kilogramo'),
        ('Lb','Libra'),
        ('Un','Unidad'),
        ('Pa','Paquete'),
    )
    unidad=models.CharField(max_length=2,choices=UNIDAD_CHOICES,default='Kg')
    fecha_registro=models.DateField(default=datetime.date.today,verbose_name='Fecha de registro')
    precio_unidad=models.DecimalField(decimal_places=2,max_digits=10)
    fecha_precio=models.DateField(default=datetime.date.today,verbose_name='Fecha de modificación')
    TRUE_FALSE_CHOICES=(
        ('Si','Activo'),
        ('No','Inactivo')
    )
    activo=models.CharField(max_length=2,choices=TRUE_FALSE_CHOICES,default='Si')
    imagen=models.CharField(max_length=100, null=True,blank=True)
    #relacion 1 a muchos
    categoria = models.ForeignKey(Categorias,on_delete=models.PROTECT)
    def __str__(self):
        return 'Producto {prod} con código {codigo}, activo:{activo}, precio: {precio}'.format(
            prod=self.nombre,codigo=self.codigo,activo=self.activo,precio=self.precio_unidad)

    class Meta:
        verbose_name_plural= "Productos"

class Clientes(models.Model):
    nombre=models.CharField(max_length=20,verbose_name='Nombres')
    apellido=models.CharField(max_length=20,verbose_name='Apellidos')
    correo=models.EmailField(verbose_name='Correo electrónico')
    DOC_CHOICES=(
        ('Cc','Cédula'),
        ('Pa','Pasaporte'),
        ('Ce','Cédula de extranjería'),
    )
    tipo_doc=models.CharField(max_length=2,choices=DOC_CHOICES,default='Cc',verbose_name="Tipo Doc. Identidad")
    doc_identificacion=models.CharField(max_length=15,verbose_name='Documento identificación')
    dir_env=models.CharField(max_length=100,verbose_name='Dirección de envío')
    fecha_registro=models.DateField(default=datetime.date.today,verbose_name='Fecha de registro')
    TRUE_FALSE_CHOICES=(
        ('Si','Activo'),
        ('No','Inactivo')
    )
    activo=models.CharField(max_length=2,choices=TRUE_FALSE_CHOICES,default='Si')
    
    def __str__(self):
        return 'Cliente {nombre} {apellido} con correo {correo}, activo:{activo}'.format(
            nombre=self.nombre,apellido=self.apellido,correo=self.correo,activo=self.activo)

    class Meta:
        verbose_name_plural= "Clientes"

class Pedidos(models.Model):
    fecha_pedido=models.DateField(default=datetime.date.today,verbose_name='Fecha del pedido')
    PAGO_CHOICES=(
        ('PSE','PSE'),
        ('Tj','Tarjeta de crédito'),
        ('Py','Paypal'),
        ('Mp','Mercado pago'),
    )
    forma_pago=models.CharField(max_length=3,choices=PAGO_CHOICES,default='PSE',verbose_name="Forma de pago")
    valor_total=models.DecimalField(decimal_places=2,max_digits=15,verbose_name='Valor total')
    impuestos=models.DecimalField(decimal_places=2,max_digits=15)
    total=models.DecimalField(decimal_places=2,max_digits=15)
    ESTADO_CHOICES=(
        ('Rg','Registrado'),
        ('Pr','Preparación'),
        ('En','Enviado'),
        ('Re','Recibido cliente'),
        ('Fn','Finalizado sin reclamaciones'),
        ('Fr','Finalizado con reclamaciones'),
        ('Ca','Cancelado')
    )
    estado=models.CharField(max_length=2,choices=ESTADO_CHOICES,default='Rg')
    # relacion 1 a muchos
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural= "Pedidos"


class ProductosPedido(models.Model):
    
    #relacion 1 a muchos
    pedido=models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    producto=models.ForeignKey(Productos,on_delete=models.PROTECT)
    cantidad=models.PositiveIntegerField()
    subtotal=models.DecimalField(decimal_places=2,max_digits=10)


class Inventario(models.Model):
    BODEGA_CHOICES=(
        ('CeB','Bogeda Centro Cr 3b 12-23 Bog'),
        ('SuB','Bogeda Sur Calle 34c 14-13 Bog'),
        ('NoB','Bogeda Norte Calle 3b 64-23 Bog'),
    )
    producto=models.OneToOneField(Productos,on_delete=models.PROTECT)
    cantidad=models.PositiveIntegerField()
    ubicacion=models.CharField(max_length=3,choices=BODEGA_CHOICES,default='NoB')
    precio_entrada=models.DecimalField(decimal_places=2,max_digits=10)
    fecha_registro=models.DateField(default=datetime.date.today)

    def __str__(self):
        return 'Producto {prod}, cantidad {cantidad}'.format(
            prod=self.producto.nombre,cantidad=self.cantidad)

class Calificaciones(models.Model):

    CAL_CHOICES=(
        ('1','[1] estrella'),
        ('2','[2] estrellas'),
        ('3','[3] estrellas'),
        ('4','[4] estrellas'),
        ('5','[5] estrellas'),
    )
    calificacion=models.CharField(max_length=1,choices=CAL_CHOICES,default='5')
    fecha_calificacion=models.DateField(default=datetime.date.today)
    comentario=models.TextField()
    producto=models.ForeignKey(Productos,on_delete=models.CASCADE)
    cliente=models.ForeignKey(Clientes,on_delete=models.CASCADE)
    def __str__(self):
        return 'Producto {prod}, calificacion {calificacion}'.format(
            prod=self.producto.nombre,calificacion=self.calificacion)
    class Meta:
        verbose_name_plural="Calificaciones"

     