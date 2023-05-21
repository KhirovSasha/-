import time
from kafka import KafkaProducer

# Конфігурація Kafka
bootstrap_servers = 'kafka:9092'
topic = 'common'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

while True:
        # Отримуємо поточний час
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # Відправляємо повідомлення у топік
    producer.send(topic, value=current_time.encode())
    producer.flush()

        # Затримка на 5 секунд
    time.sleep(5)
