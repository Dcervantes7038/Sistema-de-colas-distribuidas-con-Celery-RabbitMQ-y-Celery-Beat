from celery_app import mensaje_con_retraso

if __name__ == "__main__":
    resultado = mensaje_con_retraso.delay("¡Tarea ejecutada!")
    print(f"Tarea enviada, id: {resultado.id}")




