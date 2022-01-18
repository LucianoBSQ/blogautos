from django.urls import path
from AppBlog import views

urlpatterns = [
   
    path('', views.inicio, name= "Inicio"), 
    path('diseñadores', views.diseñadores, name= "Diseñadores"),
    path('empresas', views.empresas, name= "Empresas"),
    path('diseños', views.diseños, name= "Diseños"),
    path('about', views.about, name="About"),
    path('busquedaEmpresa', views.busquedaEmpresa, name="BusquedaEmpresa"),
    path('buscar/', views.buscar, name="buscar"),
]


