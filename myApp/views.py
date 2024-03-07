from django.shortcuts import render, redirect
from .models import Producto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BuscarProducto, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'myApp/home.html')

def about(request):
    return render(request, 'myApp/about.html')

def productos(request):
    producto = Producto.objects.all()
    data = {
        'producto':producto
    }
    return render(request, 'myApp/productos.html', data)

def login_request(request):
    msg_login=""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request, user)
                return render(request, 'myApp/home.html')
        msg_login ="Usuario o contgraseña incorrectos"
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form, 'msg_login':msg_login})

@login_required
def buscar_producto(request):
    if request.method == 'POST':
        mi_formulario = BuscarProducto(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            descripcion = Producto.objects.filter(descripcion__icontains=info['descripcion'])
            return render(request, 'myApp/busqueda.html', {'descripcion':descripcion})
    else:
        mi_formulario = BuscarProducto()
    return render(request, 'myApp/busqueda.html', {'formu':mi_formulario })

def registro(request):
    data= {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect(to='/')
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)
         
class ListaProductoView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'myApp/lista.html'

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    success_url = 'lista'
    fields = '__all__'
    
class EditarProductoView(LoginRequiredMixin, UpdateView):
    model = Producto
    success_url = '/lista'
    fields = '__all__'
    
class BorrarProductoView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'myApp/borrar.html'
    success_url = '/lista'
    
class DetalleProductoView(LoginRequiredMixin, DetailView):
    model = Producto
    template_name = 'myApp/detalles.html'