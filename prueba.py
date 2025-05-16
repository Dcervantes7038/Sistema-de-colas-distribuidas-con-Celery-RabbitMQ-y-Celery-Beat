from celery_app import mensaje_con_retraso

mensaje_con_retraso.delay("Hola desde Celery con RabbitMQ")
