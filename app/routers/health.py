# Endpoints de monitoreo de la aplicacion.
from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/", summary="Health Check")
def health_check():
    # Respuesta minima para verificar disponibilidad.
    return {"status": "ok"}
