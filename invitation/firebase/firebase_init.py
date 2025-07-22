import firebase_admin
from firebase_admin import credentials, firestore
from decouple import config

# Cargar ruta desde el .env
cred_path = config('FIREBASE_CREDENTIALS')

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    print("✅ Firebase conectado con credenciales:", cred_path)
    firebase_admin.initialize_app(cred)

db = firestore.client()

