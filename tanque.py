import sys
import json
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime

def main():
    client = paho.mqtt.client.Client("Casa", False)
    client.qos = 0
    client.connect(host='localhost')
    hora = datetime.datetime.now().replace(minute=0, second=0)
    nivel = 100
    contador = 0
    hora = hora + datetime.timedelta(hours=1)
    while (True):
        payload = {
            "fecha": str(hora),
            "nivel": str(nivel)
        }
        if(nivel==0):
            payload = {
                "fecha": str(hora),
                "nivel": str(nivel),
                "mensaje": "El tanque esta vacio"
            }
        elif(nivel<50):
            payload = {
                "fecha": str(hora),
                "nivel": str(nivel),
                "mensaje": "El tanque esta a menos del 50% de capacidad"
            }
        client.publish('casa/bano/nivel_tanque', json.dumps(payload), qos=0)
        print(payload)
        contador = contador + 1
        nivel = nivel - np.random.normal(10, 5)
        if(nivel<0):
            nivel=0
        if(contador==3):
            contador=0
            nivel= nivel + np.random.normal(20, 5)
            if (nivel > 100):
                nivel = 100
        hora = hora + datetime.timedelta(minutes=10)
        time.sleep(1)


if __name__ == '__main__':
    main()
    sys.exit(0)
