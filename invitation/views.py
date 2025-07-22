from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

@csrf_exempt  # Para pruebas locales sin CSRF token. Quita esto en producción.
def ingreso(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        if not codigo:
            return JsonResponse({'error': 'Código no proporcionado'}, status=400)
        
        # Aquí puedes hacer tu lógica de validación
        if codigo == 'ABC123':
            return HttpResponse(codigo, status=200)
        else:
            return HttpResponse("Código incorrecto", status=401)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
