import json
import os
from ensurepip import bootstrap
from kafka import KafkaConsumer
from app.service.splite_data_to_db import split_report


def consume(mode='latest'):
    consumer = KafkaConsumer(
        os.environ["NEO4J_TOPIC"],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset=mode
    )

    for message in consumer:
        split_report(message.value)
