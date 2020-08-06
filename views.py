from django.shortcuts import render, redirect
from .models import Productos, Cuadernos, Lapices, Mochilas, Juguetes, Obsequios, Piñateria
from .forms import ProductosForm,LapicesForm,JuguetesForm, MochilasForm, PiñateriaForm,  ObsequiosForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.views.generic import View
from .utils import render_to_pdf
from django.template.loader import get_template
from .forms import CuadernosForm
import pdfkit
from xhtml2pdf import pisa 
from django.http import HttpResponse
from io import  BytesIO
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, C0
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab. platypus import Paragraph, Table, TableStyle, Image, SimpleDocTemplate, Spacer
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors

#porfssvor
from reportlab.lib.units import inch,mm

# Create your views here.
def home(request):
    dest = Productos.objects.all()
    contexto ={
        'dest':dest
    }
    return render(request, 'home.html', contexto)
def cuadernos(request):
    cuadernos= Cuadernos.objects.all()
    contexto ={
        'cuadernos':cuadernos
    }
    return render(request,"cuadernos.html",contexto)
def piñateria(request):
    piñateria= Piñateria.objects.all()
    contexto ={
        'piñateria':piñateria
    }
    return render(request,"piñateria.html",contexto)
def obsequios(request):
    obsequios= Obsequios.objects.all()
    contexto ={
        'obsequios':obsequios
    }
    return render(request,"obsequios.html",contexto)
def mochilas(request):
    mochilas= Mochilas.objects.all()
    contexto ={
        'mochilas':mochilas
    }
    return render(request,"mochilas.html",contexto)
def lapices(request):
    lapices= Lapices.objects.all()
    contexto ={
        'lapices':lapices
    }
    return render(request,"lapices.html",contexto)
def juguetes(request):
    juguetes= Juguetes.objects.all()
    contexto ={
        'juguetes':juguetes
    }
    return render(request,"juguetes.html",contexto)
def loginPage(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is None:
            return redirect('home')
        else:
            login(request,user)
            return redirect('login')
    context={}
    return render(request,'login.html',context)
def crearCuadernos(request):
    if request.method == 'GET':
        form = CuadernosForm()
        contexto ={
            'form':form
        }
    else:
        form= CuadernosForm(request.POST)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('cuadernos')
    return render(request, 'crearCuadernos.html', contexto)
def crearLapices(request):
    if request.method == 'GET':
        form = LapicesForm()
        contexto ={
            'form':form
        }
    else:
        form= LapicesForm(request.POST)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('lapices')
    return render(request, 'crearLapices.html', contexto)
def crearPiñateria(request):
    if request.method == 'GET':
        form = PiñateriaForm()
        contexto ={
            'form':form
        }
    else:
        form= PiñateriaForm(request.POST)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('piñateria')
    return render(request, 'crearPiñateria.html', contexto)
def crearMochilas(request):
    if request.method == 'GET':
        form = MochilasForm()
        contexto ={
            'form':form
        }
    else:
        form= MochilasForm(request.POST)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('mochilas')
    return render(request, 'crearMochilas.html', contexto)
def crearObsequios(request):
    if request.method == 'GET':
        form = ObsequiosForm()
        contexto ={
            'form':form
        }
    else:
        form= ObsequiosForm(request.POST)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('obsequios')
    return render(request, 'crearObsequios.html', contexto)
def crearJuguetes(request):
    if request.method == 'GET':
        form = JuguetesForm()
        contexto ={
            'form':form
        }
    else:
        form= JuguetesForm(request.POST)
        contexto ={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('juguetes')
    return render(request, 'crearJuguetes.html', contexto)

def editarJuguetes (request, id):
    juguetes= Juguetes.objects.get(id=id)
    if request.method == 'GET':
        form= JuguetesForm(instance= juguetes)
        contexto = {
            'form': form
        }
    else :
        form= JuguetesForm(request.POST, instance= juguetes)
        contexto = {
            'form': form
        }
        if form.is_valid() :
            form.save()
            return redirect('juguetes')
    return render(request, 'crearJuguetes.html', contexto)
def editarObsequios (request, id):
    obsequios= Obsequios.objects.get(id=id)
    if request.method == 'GET':
        form= ObsequiosForm(instance= obsequios)
        contexto = {
            'form': form
        }
    else :
        form= ObsequiosForm(request.POST, instance= obsequios)
        contexto = {
            'form': form
        }
        if form.is_valid() :
            form.save()
            return redirect('obsequios')
    return render(request, 'crearObsequios.html', contexto)
def editarPiñateria (request, id):
    piñateria= Piñateria.objects.get(id=id)
    if request.method == 'GET':
        form= PiñateriaForm(instance= piñateria)
        contexto = {
            'form': form
        }
    else :
        form= PiñateriaForm(request.POST, instance= piñateria)
        contexto = {
            'form': form
        }
        if form.is_valid() :
            form.save()
            return redirect('piñateria')
    return render(request, 'crearPiñateria.html', contexto)
def editarCuadernos (request, id):
    cuadernos= Cuadernos.objects.get(id=id)
    if request.method == 'GET':
        form= CuadernosForm(instance= cuadernos)
        contexto = {
            'form': form
        }
    else :
        form= CuadernosForm(request.POST, instance= cuadernos)
        contexto = {
            'form': form
        }
        if form.is_valid() :
            form.save()
            return redirect('cuadernos')
    return render(request, 'crearCuadernos.html', contexto)
def editarLapices (request, id):
    lapices= Lapices.objects.get(id=id)
    if request.method == 'GET':
        form= LapicesForm(instance= lapices)
        contexto = {
            'form': form
        }
    else :
        form= LapicesForm(request.POST, instance= lapices)
        contexto = {
            'form': form
        }
        if form.is_valid() :
            form.save()
            return redirect('lapices')
    return render(request, 'crearLapices.html', contexto)
def editarMochilas (request, id):
    mochilas= Mochilas.objects.get(id=id)
    if request.method == 'GET':
        form= MochilasForm(instance= mochilas)
        contexto = {
            'form': form
        }
    else :
        form= MochilasForm(request.POST, instance= mochilas)
        contexto = {
            'form': form
        }
        if form.is_valid() :
            form.save()
            return redirect('mochilas')
    return render(request, 'crearMochilas.html', contexto)
#ELIMINAR
def eliminarMochilas (request, id):
    mochilas= Mochilas.objects.get(id=id)
    mochilas.delete()
    return render(request, 'mochilas.html', contexto)
def eliminarCuadernos (request, id):
    cuadernos= Cuadernos.objects.get(id=id)
    cuadernos.delete()
    return render(request, 'cuadernos.html', contexto)
def eliminarLapices (request, id):
    lapices= Lapices.objects.get(id=id)
    lapices.delete()
    return render(request, 'lapices.html', contexto)
#REPORTES
def reporteCuadernos (request) :
    cuadernos = Cuadernos.objects.all()
    data= {'cuadernos' : cuadernos}
    template= get_template('reportCuadernos.html')
    data1= template.render(data)
    response= BytesIO()
    pdfPage= pisa.pisaDocument(BytesIO(data1.encode('UTF-8')),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('error al generar')
def reporteLapices (request) :
    lapices = Lapices.objects.all()
    data= {'lapices' : lapices}
    template= get_template('reportLapices.html')
    data1= template.render(data)
    response= BytesIO()
    pdfPage= pisa.pisaDocument(BytesIO(data1.encode('UTF-8')),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('error al generar')
def reporteMochilas (request) :
    mochilas = Mochilas.objects.all()
    data= {'mochilas' : mochilas}
    template= get_template('reportMochilas.html')
    data1= template.render(data)
    response= BytesIO()
    pdfPage= pisa.pisaDocument(BytesIO(data1.encode('UTF-8')),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('error al generar')
def reportePiñateria (request) :
    piñateria = Piñateria.objects.all()
    data= {'piñateria' : piñateria}
    template= get_template('reportPiñateria.html')
    data1= template.render(data)
    response= BytesIO()
    pdfPage= pisa.pisaDocument(BytesIO(data1.encode('UTF-8')),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('error al generar')
def reporteJuguetes (request) :
    juguetes = Juguetes.objects.all()
    data= {'juguetes' : juguetes}
    template= get_template('reportJuguetes.html')
    data1= template.render(data)
    response= BytesIO()
    pdfPage= pisa.pisaDocument(BytesIO(data1.encode('UTF-8')),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('error al generar')
def reporteObsequios (request) :
    obsequios = Obsequios.objects.all()
    data= {'obsequios' : obsequios}
    template= get_template('reportObsequios.html')
    data1= template.render(data)
    response= BytesIO()
    pdfPage= pisa.pisaDocument(BytesIO(data1.encode('UTF-8')),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse('error al generar')