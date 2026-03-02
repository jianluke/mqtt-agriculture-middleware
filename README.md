\# MQTT Agriculture Middleware (Project Work)

Prototipo di middleware di messaggistica asincrona basato su MQTT per un contesto agricolo (monitoraggio suolo e irrigazione automatizzata).

\## Architettura (sintesi)

\- \*\*Broker MQTT\*\*: Eclipse Mosquitto (Docker)

\- \*\*Publisher\*\*: sensore simulato (telemetria umidità)

\- \*\*Consumer/Producer\*\*: controller irrigazione (decide e pubblica comandi)

\- \*\*Consumer\*\*: logger/dashboard (osserva telemetria e comandi)

\## Topic

\- Telemetria: `bf/campo/{campoId}/sensor/{sensorId}/telemetry` (QoS 1)

\- Comandi: `bf/campo/{campoId}/irrigation/{zonaId}/cmd` (QoS 2)

\- Allarmi: `bf/campo/{campoId}/alerts` (QoS 2)

\## Avvio rapido

\### 1) Avvio broker Mosquitto

```bash

cd broker

docker compose up -d



