import json
import time
import paho.mqtt.client as mqtt
BROKER_HOST = "localhost"
BROKER_PORT = 1883
SUB_TOPIC = "bf/campo/+/sensor/+/telemetry"
FIELD_ID = 1
ZONE_ID = "zone_1"
PUB_TOPIC = f"bf/campo/{FIELD_ID}/irrigation/{ZONE_ID}/cmd"
THRESHOLD = 30.0  # %
QOS_SUB = 1
QOS_PUB = 2
client = mqtt.Client(client_id="irrigation_controller", clean_session=True)
def on_connect(client, userdata, flags, rc):
    print(f"[CTRL] Connected with result code {rc}")
    client.subscribe(SUB_TOPIC, qos=QOS_SUB)
    print(f"[CTRL] Subscribed to {SUB_TOPIC} (QoS={QOS_SUB})")
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))
        humidity = float(data.get("humidity"))
        sensor_id = data.get("sensor_id", "unknown")
        field_id = data.get("field_id", "unknown")
        print(f"[CTRL] RX from {sensor_id} (field {field_id}): humidity={humidity}%")
        if humidity < THRESHOLD:
            command = {
                "action": "START",
                "zone": ZONE_ID,
                "reason": "Low soil humidity",
                "humidity": humidity,
                "threshold": THRESHOLD,
                "timestamp_epoch": time.time()
            }
            client.publish(PUB_TOPIC, json.dumps(command), qos=QOS_PUB)
            print(f"[CTRL] TX CMD -> {PUB_TOPIC} (QoS={QOS_PUB}): {command}")
    except Exception as e:
        print(f"[CTRL] ERROR parsing message: {e}")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
client.loop_forever()
