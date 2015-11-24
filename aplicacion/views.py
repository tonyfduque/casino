from django.http import HttpResponse,HttpResponseRedirect
from aplicacion.models import *
from aplicacion.forms import  EmpleadoForm
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response,redirect
from django.contrib.auth import authenticate, login
def index(request):
    if request.user.is_authenticated():
        return render_to_response("aplicacion/index.html",{},
        context_instance=RequestContext(request))  
    else: 
       return redirect("/login")


def  empleados(request):
    empleados=Empleado.objects.all()
    y=40.5 *200
    """x="<h1>Lista de Empleados </h1><br>"
    x+="<br>".join(["idRol:%s,nombre: %s," %(e.idRol,e.nombres) for e in empleados ])
    return HttpResponse(x)"""
    return render_to_response("aplicacion/listarEmpleados.html",{'empleados':empleados ,'total':y},
        context_instance=RequestContext(request))

def  consumos(request):
    consumos=Consumo.objects.all()
    y=40.5 *200
    """x="<h1>Lista de Consumos </h1><br>"
    x+="<br>".join(["idConsumo:%s,idEmpleado:%s,fecha: %s,hora:%s,descripcionConsumo:%s,valorConsumo:%s" %(c.idConsumo,c.idEmpleado,c.fecha,c.hora,c.descripcionConsumo,c.valorConsumo) for c in consumos ])
    return HttpResponse(x)"""
    return render_to_response("aplicacion/listarConsumos.html",{'consumos':empleados ,'total':y},
        context_instance=RequestContext(request))

def  cargos(request):
    cargos=Cargo.objects.all()
    y=40.5 *200
    """x="<h1>Lista de Cargos </h1><br>"
    x+="<br>".join(["idCargo:%s,tipo:%s,salario:%s,turno:%s,rango:%s,email:%s, descuento:%s" %(cg.idCargo,cg.tipo,cg.salario,cg.turno,cg.rango,cg.email, cg.descuento) for cg in cargos ])
    return HttpResponse(x)"""
    return render_to_response("aplicacion/listarCargos.html",{'consumos':empleados ,'total':y},
        context_instance=RequestContext(request))

def prueba(request,id):
    x="<h1>"+id+"</h1>"
    #return render_to_response("login",{})
    return HttpResponse(x)


def Crear_empleado(request):
    if request.method =="POST":
        form=EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/empleados")
    else:
        form=EmpleadoForm()
        return  render_to_response("aplicacion/CrearEmpleados.html",
                                  {'form':form},
                                  context_instance=RequestContext(request))

def Crear_consumo(request):
    if request.method =="POST":
        form=ConsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/consumos")
    else:
        form=ConsumoForm()
        return  render_to_response("aplicacion/CrearConsumos.html",
                                  {'form':form},
                                  context_instance=RequestContext(request))

def Crear_cargo(request):
    if request.method =="POST":
        form=CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/cargos")
    else:
        form=EmpleadoForm()
        return  render_to_response("aplicacion/CrearCargos.html",
                                  {'form':form},
                                  context_instance=RequestContext(request))


def Crear_parametro(request):
    if request.method =="POST":
        form=ParametroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/parametro")
    else:
        form=ParametroForm()
        return  render_to_response("aplicacion/CrearParametro.html",
                                  {'form':form},
                                  context_instance=RequestContext(request))
        