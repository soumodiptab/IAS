from kafka import KafkaConsumer
consumer = KafkaConsumer('users', group_id='my-group', bootstrap_servers=['localhost:9092'])
for message in consumer:
    print(message.value.decode('utf-8'))