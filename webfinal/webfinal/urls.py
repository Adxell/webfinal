from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from personas.views import index, registro, mostrar, delatepersona, editpersona, PDF, PDFtodos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', registro),
    path('registros/', mostrar),
    path('registros/', mostrar),
    path('registros/<id>', delatepersona),
    path('editar/<id>', editpersona),
    path('indexPDF/PDF/<id>', PDF),
    path('indexPDF/PDFtodos/', PDFtodos),
    path('account/', include('django.contrib.auth.urls')),
    url(r'^$', index),
]
