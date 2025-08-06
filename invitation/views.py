from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from invitation.logic.invitation_logic import ingresarFirebase, confirmacionfunction

@csrf_exempt  # Solo para pruebas locales
def ingreso(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        if not codigo:
            return JsonResponse({'error': 'Código no proporcionado'}, status=400)
        
        return ingresarFirebase(codigo)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt  # Solo para pruebas locales
def confirmacion(request):
    if request.method == 'PATCH':
        datos = request.PATCH.get()
        if not datos:
            return JsonResponse({'error': 'Datos no encontrados'}, status=400)
        
        return confirmacionfunction(datos)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
