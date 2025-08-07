import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from invitation.logic.invitation_logic import ingresarFirebase, confirmacionfunction
from django.http import JsonResponse

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
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)  # Accede al JSON enviado
            print(datos)  # {'invitado1': true, 'invitado2': false, ...}
            # Procesamiento aquí...
            return confirmacionfunction(datos)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
