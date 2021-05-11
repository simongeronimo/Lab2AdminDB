import sys
import json
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime

def on_connect(client, userdata, flags, rc):
    print('conectado publicador')


def main():
    client = paho.mqtt.client.Client("Casa", False)
    client.qos = 0
    client.connect(host='localhost')
    hora = datetime.datetime.now().replace(minute=0, second=0)
    temperatura = np.random.uniform(0, 150)
    uso=True
    hora = hora + datetime.timedelta(hours=1)
    while (uso):
        payload = {
            "fecha": str(hora),
            "temperatura": str(temperatura)
        }
        if(temperatura>100):
            payload = {
                "fecha": str(hora),
                "temperatura": str(temperatura),
                "mensaje": "El agua esta hirviendo"
            }
        client.publish('casa/cocina/temperatura_olla', json.dumps(payload), qos=0)
        temperatura = np.random.uniform(0, 150)
        print(payload)
        hora = hora + datetime.timedelta(seconds=1)
        time.sleep(1)


if __name__ == '__main__':
    main()
    sys.exit(0)
