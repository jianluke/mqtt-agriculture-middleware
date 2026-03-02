import json
import paho.mqtt.client as mqtt
BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPICS = [
    ("bf/campo/+/sensor/+/telemetry", 1),
    ("bf/campo/+/irrigation/+/cmd", 2),
    ("bf/campo/+/alerts", 2),
]
client = mqtt.Client(client_id="logger_dashboard", clean_session=True)
def on_connect(client, userdata, flags, rc):
    print(f"[LOG] Connected with result code {rc}")
    for t, qos in TOPICS:
        client.subscribe(t, qos=qos)
        print(f"[LOG] Subscribed to {t} (QoS={qos})")
def on_message(client, userdata, msg):
    payload_raw = msg.payload.decode("utf-8")
    try:
        payload = json.loads(payload_raw)
        print(f"[LOG] {msg.topic} -> {json.dumps(payload, ensure_ascii=False)}")
    except Exception:
        print(f"[LOG] {msg.topic} -> {payload_raw}")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
client.loop_forever()
