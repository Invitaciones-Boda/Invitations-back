from django.http import JsonResponse

def build_response(message, status=200, data=None):
    response_data = {
        "message": message,
        "data": data or {}
    }
    return JsonResponse(response_data, status=status)
