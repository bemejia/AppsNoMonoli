from async_comunication.pulsar_comunication import configurar_pulsar, escucha_mensajes

client = configurar_pulsar()
escucha_mensajes(client)