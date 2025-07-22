from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from invitation.logic.invitation_logic import ingresarFirebase

@csrf_exempt  # Solo para pruebas locales
def ingreso(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        if not codigo:
            return JsonResponse({'error': 'Código no proporcionado'}, status=400)
        
        return ingresarFirebase(codigo)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
