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

def report(request):
        response = HttpResponse(content_type='application/pdf')
        #response ['Content-Disposition']='attachment; filename= Diego-Inventario-report.pdf'
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)
        #CABECERA
        c.setLineWidth(.3)
        c.setFont("Helvetica", 24)
        c.drawString(200, 780, "LIBRERIA DIEGO")
        c.setFont("Helvetica", 9)
        c.drawString(250, 760, "REPORTE DE ALMACEN")
        c.line(30,747,570,747)
        #CUERPO

        cuadernos= Cuadernos.objects.all()
        contexto ={
            'cuadernos':cuadernos
        }

        c.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template= get_template('cuadernos.html')
        context= {
            "invoce_id": 123,
            "customer_name": "Jhon Cooper",
            "amount": 1299.99,
            "today":"Today",
        }
        html=template.render(context)
        pdf=render_to_pdf('cuadernos.html',context)
        if pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            filename= "Invoice_%s.pdf"%{"12341231"}
            content= "inline; filename='%s'"%{filename}
            dowland= request.GET.get("dowland")
            if dowland:
                content="attachment; filename='%s'"%{filename}
            response['Content-Disposition']=content
            return response
        return HttpResponse("Not found")
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

def documentpdf(request):
    from django.template.loader import get_template 
    from django.template import Context
    
    template = get_template("cuadernos.html")
    context = {"template": template} # data is the context data that is sent to the html file to render the output. 
    html = template.render(context)  # Renders the template with the context data.
    pdfkit.from_string(html, 'out.pdf')
    pdf = open("out.pdf")
    response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
    response['Content-Disposition'] = 'attachment; filename=output.pdf'
    pdf.close()
    os.remove("out.pdf")  # remove the locally created pdf file.
    return response  # returns the response.
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
