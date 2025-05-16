from celery import Celery
from celery.schedules import crontab
import time

app = Celery("tareas", broker="pyamqp://guest@localhost//", backend="rpc://")

@app.task
def mensaje_con_retraso(mensaje):
    print(f"Ejecutando tarea: {mensaje}")
    time.sleep(5)
    return f"Tarea completada: {mensaje}"

app.conf.beat_schedule = {
    "tarea-diaria-a-las-6am": {
        "task": "celery_app.mensaje_con_retraso",
        "schedule": crontab(hour=6, minute=0),  # Aquí está el cambio
        "args": ["¡Tarea programada a las 6:00 a.m.!"],
    }
}

app.conf.timezone = "America/Bogota"





