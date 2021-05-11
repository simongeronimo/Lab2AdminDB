import sys
import paho.mqtt.client
import psycopg2


def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='casa/#', qos=2)


def on_message(client, userdata, message):
    print('------------------------------')
    print('topic: %s' % message.topic)
    print('payload: %s' % message.payload)
    print('qos: %d' % message.qos)
    conn = psycopg2.connect(database="bbbrfhhj",
                            user="bbbrfhhj",
                            password="3Pt4Dq8IZ92WbIpXXZs4MEZoPIex8f8i",
                            host="queenie.db.elephantsql.com",
                            port="5432"
                            )
    cursor = conn.cursor()
    if (message.topic == 'casa/cocina/temperatura_nevera'):
        dispositivo = 1
    elif (message.topic == 'casa/cocina/temperatura_olla'):
        dispositivo = 2
    elif (message.topic == 'casa/sala/contador_personas'):
        dispositivo = 3
    elif (message.topic == 'casa/sala/alexa_echo'):
        dispositivo = 4
    elif (message.topic == 'casa/bano/nivel_tanque'):
        dispositivo = 5
    cursor.execute("INSERT INTO mensajes (dispositivo_id, mensaje) VALUES(%s, %s)", (dispositivo, str(message.payload)))
    conn.commit()

def main():
    client = paho.mqtt.client.Client(client_id='Casa-subs', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='127.0.0.1', port=1883)
    client.loop_forever()


if __name__ == '__main__':
    main()

sys.exit(0)
