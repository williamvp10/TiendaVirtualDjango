from django import forms
from django.forms import fields
from tiendavirtualapp.models import Clientes, Pedidos

class FormularioCliente(forms.ModelForm):

    class Meta:
        model=Clientes
        fields=['nombre', 'apellido', 'correo','tipo_doc','doc_identificacion','dir_env', 'telefono']

class FormularioPedido(forms.ModelForm):

    class Meta:
        model=Pedidos
        fields=['forma_pago','valor_total','impuestos','total']