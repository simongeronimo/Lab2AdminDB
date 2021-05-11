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
    meanTemp = 10
    stdTemp = 2
    hora = datetime.datetime.now().replace(minute=0, second=0)
    temperatura = np.random.normal(meanTemp, stdTemp)
    intervalo = True

    hora = hora + datetime.timedelta(hours=1)
    while (temperatura > 0):
        hielo = np.random.uniform(0, 10)
        if temperatura > 12: temperatura = 12
        if temperatura < 8: temperatura = 8
        payload = {
            "fecha": str(hora),
            "temperatura": str(temperatura)
        }
        if(intervalo):
            payload = {
                "fecha": str(hora),
                "temperatura": str(temperatura),
                "hielo": str(hielo)
            }
            intervalo=False
        else: intervalo=True
        client.publish('casa/cocina/temperatura_nevera', json.dumps(payload), qos=0)
        temperatura = np.random.normal(meanTemp, stdTemp)
        print(payload)
        hora = hora + datetime.timedelta(minutes=5)
        time.sleep(1)


if __name__ == '__main__':
    main()
    sys.exit(0)
