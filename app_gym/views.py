# --- START OF FILE views.py (CORREGIDO) ---

from django.shortcuts import render, redirect, get_object_or_404
from .models import Miembro, Clase, Empleado
from django.contrib import messages
from django.http import HttpResponse


def inicio_gym(request):
    context = {}
    # CORRECCIÓN AQUÍ: 'app_gym/inicio.html'
    return render(request, 'app_gym/inicio.html', context)


def agregar_miembro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono', '')
        membresia_activa = request.POST.get('membresia_activa') == 'on'
        imagen = request.FILES.get('imagen')

        Miembro.objects.create(
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            telefono=telefono,
            membresia_activa=membresia_activa,
            imagen=imagen
        )
        messages.success(request, 'Miembro agregado exitosamente!')
        return redirect('ver_miembros')
    # CORRECCIÓN AQUÍ: 'app_gym/miembros/agregar_miembros.html'
    return render(request, 'miembros/agregar_miembros.html')


def ver_miembros(request):
    print("\n--- INICIANDO VISTA: ver_miembros ---") # Mantén los prints para depurar
    try:
        miembros = Miembro.objects.all().order_by('apellido', 'nombre')
        print(f"DEBUG: Queryset de Miembros obtenido. Cantidad: {miembros.count()}")
        
        if miembros.exists():
            print("DEBUG: Hay miembros en la base de datos. Listando los primeros 5:")
            for i, miembro in enumerate(miembros[:5]):
                print(f"  - [{i+1}] ID: {miembro.id}, Nombre: {miembro.nombre} {miembro.apellido}, Email: {miembro.email}")
        else:
            print("DEBUG: ¡No se encontraron miembros en la base de datos!")
            messages.info(request, "No hay miembros registrados para mostrar. ¡Añade algunos!")

        context = {'miembros': miembros}
        print("DEBUG: Contexto preparado para renderizar la plantilla.")
        # CORRECCIÓN AQUÍ: 'app_gym/miembros/ver_miembros.html'
        return render(request, 'miembros/ver_miembros.html', context)

    except Exception as e:
        print(f"ERROR: Se produjo un error en ver_miembros: {e}")
        messages.error(request, f"Ocurrió un error al cargar los miembros: {e}")
        return render(request, 'app_gym/inicio.html', {'error_message': str(e)})
    finally:
        print("--- FINALIZANDO VISTA: ver_miembros ---\n")


def actualizar_miembro(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    if request.method == 'POST':
        print("====================================")
        print("Método POST detectado para actualizar miembro:", miembro.id)
        print("Datos recibidos:", request.POST)
        print("Archivos recibidos:", request.FILES)
        print("Nombre antes:", miembro.nombre)

        miembro.nombre = request.POST.get('nombre')
        miembro.apellido = request.POST.get('apellido')
        miembro.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        miembro.email = request.POST.get('email')
        miembro.telefono = request.POST.get('telefono', '')
        miembro.membresia_activa = request.POST.get('membresia_activa') == 'on'

        if 'imagen' in request.FILES:
            if miembro.imagen:
                miembro.imagen.delete(save=False)
            miembro.imagen = request.FILES['imagen']
        elif 'borrar_imagen' in request.POST:
            if miembro.imagen:
                miembro.imagen.delete(save=False)
            miembro.imagen = None

        miembro.save()
        print("Miembro guardado. Nuevo nombre:", miembro.nombre)
        print("====================================")
        messages.info(request, 'Miembro actualizado exitosamente!')
        return redirect('ver_miembros')
    
    # CORRECCIÓN AQUÍ: 'app_gym/miembros/actualizar_miembros.html'
    return render(request, 'miembros/actualizar_miembros.html', {'miembro': miembro})


def borrar_miembro(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    if request.method == 'POST':
        if miembro.imagen:
            miembro.imagen.delete()
        miembro.delete()
        messages.error(request, 'Miembro eliminado correctamente.')
        return redirect('ver_miembros')
    context = {'miembro': miembro}
    # CORRECCIÓN AQUÍ: 'app_gym/miembros/borrar_miembro.html'
    return render(request, 'miembros/confirmar_borrar_miembros.html', context)

# --- END OF FILE views.py (CORREGIDO) ---