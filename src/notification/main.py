import pika
import os
import json
import time

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "rabbitmq")

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"\n🔔 [Notification Service] SMS Alert! House predicted at ${data.get('price')}!\n", flush=True)

while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
        channel = connection.channel()
        channel.queue_declare(queue='price_notifications')
        channel.basic_consume(queue='price_notifications', on_message_callback=callback, auto_ack=True)
        print("✅ [Notification Service] Connected to RabbitMQ. Waiting for messages...", flush=True)
        channel.start_consuming()
    except Exception as e:
        print(f"RabbitMQ connection failed, retrying in 5s... ({e})", flush=True)
        time.sleep(5)
