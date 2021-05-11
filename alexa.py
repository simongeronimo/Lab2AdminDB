import sys
import json
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
import pyowm

def main():
        APIKEY = "ccc7adc71d5e74a7764a2afeaf9608b4"
        OpenWMap = pyowm.OWM(APIKEY)
        Weather = OpenWMap.weather_manager()
        Data = Weather.weather_at_place('Caracas,VE').weather
        temp_dict_celsius = Data.temperature('celsius')
        client = paho.mqtt.client.Client("Casa", False)
        client.qos = 0
        client.connect(host='localhost')
        hora = datetime.datetime.now().replace(minute=0, second=0)
        hora = hora + datetime.timedelta(hours=1)
        while (True):
            temperatura = np.random.normal(temp_dict_celsius.get("temp"), 3)
            payload = {
                "fecha": str(hora),
                "temperatura": str(temperatura)
            }
            jsonString = json.dumps(payload)
            client.publish('casa/sala/alexa_echo', json.dumps(payload), qos=0)
            print(jsonString)
            hora = hora + datetime.timedelta(minutes=1)
            time.sleep(1)


if __name__ == '__main__':
    main()
    sys.exit(0)
