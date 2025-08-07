import json
from invitation.utils.response.build_response import build_response
from invitation.firebase.firebase_init import db  # conexión a Firestore

""" Logica ingreso con firebase  """
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

""" Logica confirmación de asistencia con firebase  """
def confirmacionfunction(data: dict):
    if not data:
        return build_response("Error de integridad: No se recibió la información.", 400)

    try:
        codigo = data.get("codigo")
        invitados_confirmados = data.get("invitados", [])
        total_confirmados = data.get("confirmados", 0)

        if not codigo or not isinstance(invitados_confirmados, list):
            return build_response("Datos incompletos o inválidos.", 400)

        # Obtener documento
        doc_ref = db.collection("invitaciones").document(codigo)
        doc = doc_ref.get()

        if not doc.exists:
            return build_response("Invitación no encontrada.", 404)

        # Actualizar campos en Firestore.
        doc_ref.update({
            "Confirmados": total_confirmados,
            "estadoConfirmacion": "confirmado",
            "nombresConfirmados": invitados_confirmados 
        })

        return build_response("Asistencia confirmada correctamente.", 200, data={
            "confirmados": total_confirmados,
            "nombresConfirmados": invitados_confirmados
        })

    except Exception as e:
        return build_response(f"Error inesperado: {str(e)}", 500)
