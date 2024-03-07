from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('Productos/', views.productos, name='Productos'),
    path('buscar/', views.buscar_producto, name='Buscar'),
    path('registro/', views.registro, name='Registro'),
    path('login/', views.login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='myApp/home.html'), name='Logout'),
    
     #____________________________________________________________________#
    #____________________VISTAS BASADAS EN CLASES________________________#   
    
    path('lista', views.ListaProductoView.as_view(), name='Lista'),   
    path('vender', views.ProductoCreateView.as_view(), name='Vender'),
    
    path('borrar/<int:pk>', views.BorrarProductoView.as_view(), name='Borrar'),
    path('editar/<int:pk>', views.EditarProductoView.as_view(), name='Editar'),
    path('detalle/<int:pk>', views.DetalleProductoView.as_view(), name='Ver'),
    
]