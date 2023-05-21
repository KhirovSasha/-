from kafka import KafkaConsumer

# Конфігурація Kafka
bootstrap_servers = 'kafka:9092'
topic = 'common'

consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)

for message in consumer:
    content = message.value.decode()

        
    print(f"Received message: {content}")
