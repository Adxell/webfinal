from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from personas.models import Personas, Reporte
# Create your views here.
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http.response import HttpResponse
# Create your views here.

from jinja2 import Template


def index(request):
    return render(request, 'home.html')


def registro(request):
    if request.method == 'POST':
        persona = Personas()
        persona.nombre = request.POST.get('nombre')
        persona.apellido = request.POST.get('apellido')
        persona.correo = request.POST.get('correo')
        persona.fecha_nacimiento = request.POST.get('fecha')
        persona.save()
    return render(request, 'registro.html')


@login_required(login_url='/account/login/')
def mostrar(request):
    personas = Personas.objects.all()
    data = {"personas": personas}
    return render(request, 'reportes.html', data)


@login_required(login_url='/account/login/')
def delatepersona(request, id):
    estado = Personas.objects.filter(id=id).delete()
    lotes = Personas.objects.all()
    data = {'lotes': lotes}
    if estado:
        data['msg'] = 'Persona eliminada'
    return render(request, 'reportes.html', data)


@login_required(login_url='/account/login/')
def editpersona(request, id):
    personas = Personas.objects.filter(
        id=id).first()  # selecciona el lote del id
    template = Template("{{date.strftime('%Y-%m-%d')}}")
    formated_date = template.render(date=personas.fecha_nacimiento)
    personas.fecha_nacimiento = formated_date
    data = {'personas': personas}
    if request.method == 'POST':
        personas.nombre = request.POST.get('nombre')
        personas.apellido = request.POST.get('apellido')
        personas.correo = request.POST.get('correo')
        personas.fecha_nacimiento = request.POST.get('fecha')
        personas.save()
        # adiciona una clave y un valor al diccionario
        data['msg'] = 'Registro guardado con exito!'
    return render(request, 'edit.html', data)


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def PDF(request, id):
    personas = Personas.objects.filter(id=id).first()
    reportes = Reporte.objects.filter(persona_id=id)
    data = {'personas': personas, "reportes": reportes}
    pdf = render_to_pdf('IndexPDF/PDF.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def PDFtodos(request):
    personas = Personas.objects.filter()
    data = {'personas': personas}
    pdf = render_to_pdf('IndexPDF/PDFtodos.html', data)
    return HttpResponse(pdf, content_type='application/pdf')
