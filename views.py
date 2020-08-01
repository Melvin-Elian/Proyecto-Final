from django.shortcuts import render, redirect
from .models import Productos, Cuadernos, Lapices, Mochilas, Juguetes, Obsequios, Piñateria
from .forms import ProductosForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
#import pdfkit
from django.http import HttpResponse
from io import  BytesIO
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, C0
from reportlab.lib.styles import getSampleStyleSheet
from reportlab. platypus import Paragraph, Table, Table, Image
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
this_path =os.getcwd()+'/polls/'

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
    return render(request,"obsequios.html",contexto)
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
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            messages.info(request,'Datos incorrectos')
            return redirect('login')
    else:
        return render(request,'login.html')
def report(request):
        response = HttpResponse(content_type='application/pdf')
        response ['Content-Disposition']='attachment; filename= Diego-Inventario-report.pdf'
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        #CABECERA
        pdf.setFont("Helvetica", 24)
        pdf.drawString(180, 780, u"--LIBRERIA DIEGO--")
        pdf.setFont("Helvetica", 9)
        pdf.drawString(250, 760, u"REPORTE DE ALMACEN")
        #CUERPO


        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response