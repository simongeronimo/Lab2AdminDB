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
    personas = int(np.random.uniform(0, 10))
    hora = hora + datetime.timedelta(hours=1)
    while (True):
        payload = {
            "fecha": str(hora),
            "personas": str(personas)
        }
        if(personas>5):
            payload = {
                "fecha": str(hora),
                "personas": str(personas),
                "mensaje": "Hay mas de 5 personas"
            }
        client.publish('casa/sala/contador_personas', json.dumps(payload), qos=0)
        personas = int(np.random.uniform(0, 10))
        print(payload)
        hora = hora + datetime.timedelta(minutes=1)
        time.sleep(1)


if __name__ == '__main__':
    main()
    sys.exit(0)
