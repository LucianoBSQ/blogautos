import http
from http.client import HTTPResponse
from django.shortcuts import render
from AppBlog.forms import *
from AppBlog.models import *



def inicio(request):

      return render(request, "AppBlog/inicio.html")

def about(request):

      return render(request, "AppBlog/about.html")


def diseñadores(request):

      if request.method == 'POST':

            miFormulario = DiseñadoresFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  nombre = Diseñadores (nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'] ) 

                  nombre.save()

                  return render(request, "AppBlog/inicio.html") 
      else: 
            miFormulario= DiseñadoresFormulario() 

      return render(request, "AppBlog/diseñadores.html", {"miFormulario":miFormulario})


def empresas(request):

      if request.method == 'POST':

            miFormulario = EmpresasFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  nombre = Empresas (nombre=informacion['nombre'], ubicacion=informacion['ubicacion'] ) 

                  nombre.save()

                  return render(request, "AppBlog/inicio.html") 
      else: 
            miFormulario= EmpresasFormulario() 

      return render(request, "AppBlog/empresas.html", {"miFormulario":miFormulario})      


def diseños(request):

      if request.method == 'POST':

            miFormulario = DiseñosFormulario(request.POST) 

            print(miFormulario)

            if miFormulario.is_valid:   

                  informacion = miFormulario.cleaned_data

                  diseños = Diseños (modelo=informacion['modelo'], autor=informacion['autor'] ) 

                  diseños.save()

                  return render(request, "AppBlog/inicio.html") 
      else: 
            miFormulario= DiseñosFormulario() 

      return render(request, "AppBlog/diseños.html", {"miFormulario":miFormulario})            


def busquedaEmpresa(request):
      return render(request, "AppBlog/busquedaEmpresa.html")

def buscar(request):

      if request.GET ['ubicacion']:
      
            ubicacion = request.GET['ubicacion']
            nombre = Empresas.objects.filter(ubicacion=ubicacion)

            return render(request, "AppBlog/resultados.html", {"empresas":nombre, "ubicacion":ubicacion})
      
      

      else:   
            respuesta = "No enviaste Datos"

            return render (request, "AppBlog/resultados.html",{"respuesta":respuesta})

