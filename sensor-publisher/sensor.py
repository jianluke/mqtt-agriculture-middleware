import json
import random
import time
import paho.mqtt.client as mqtt
BROKER_HOST = "broker.hivemq.com"
BROKER_PORT = 1883
FIELD_ID = 1
SENSOR_ID = "soil_01"
TOPIC = f"bf/campo/{FIELD_ID}/sensor/{SENSOR_ID}/telemetry"
PUBLISH_EVERY_SEC = 5
QOS = 1
client = mqtt.Client(client_id=f"sensor_{SENSOR_ID}", clean_session=True)
client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
print(f"[SENSOR] Publishing to {TOPIC} every {PUBLISH_EVERY_SEC}s (QoS={QOS})")
while True:
    humidity = round(random.uniform(20.0, 60.0), 2)
    payload = {
        "sensor_id": SENSOR_ID,
        "field_id": FIELD_ID,
        "humidity": humidity,
        "unit": "%",
        "timestamp_epoch": time.time()
    }
    client.publish(TOPIC, json.dumps(payload), qos=QOS)
    print(f"[SENSOR] Sent: {payload}")
    time.sleep(PUBLISH_EVERY_SEC)
