from invitation.utils.response.build_response import build_response
from invitation.firebase.firebase_init import db  # conexión a Firestore

def ingresarFirebase(codigo: str):
    if not codigo or codigo.strip() == "":
        return build_response("Error de integridad: No se recibió el código.", 400)

    try:
        # Consulta la colección 'invitaciones' buscando el código
        doc_ref = db.collection("invitaciones").document(codigo).get()

        if not doc_ref.exists:
            return build_response("Código no válido o no encontrado.", 404)

        data = doc_ref.to_dict()
        data["id"] = doc_ref.id
        return build_response("Invitación encontrada.", 200, data=data)


    except Exception as e:
        return build_response(f"Error al consultar Firestore: {str(e)}", 500)


def confirmacionfunction(data: str):
    if not data or data.strip() == "":
        return build_response("Error de integridad: No se recibió la información.", 400)

    try:
        
        return build_response("Datos recibidos", 200, data=data)


    except Exception as e:
        return build_response(f"Error: {str(e)}", 500)
