from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Diseñadores)

admin.site.register(Diseños)

admin.site.register(Empresas)



