from auditoria_datos.modulos.aplicacion.async_comunication.pulsar_comunication import configurar_pulsar, escucha_mensajes
import asyncio
from auditoria_datos.modulos.aplicacion.async_comunication.pulsar_comunication import suscribirse_a_topico
from auditoria_datos.modulos.aplicacion.servicios import ServicioMajenoEventos

#client = configurar_pulsar()
#escucha_mensajes(client)

tasks = list()

async def app_startup():
    sr = ServicioMajenoEventos()
    print("Iniciando app")
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("auditoria", "sub-auditoria-111111", sr.majenarevento))
    task2 = asyncio.ensure_future(suscribirse_a_topico("catastro", "sub-catastro-1111111", sr.majenarevento))
    task3 = asyncio.ensure_future(suscribirse_a_topico("legal", "sub-legal-111111", sr.majenarevento))
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)

async def main():
    await app_startup()
    try:
    # Loop infinito para mantener el script ejecutándose
        while True:
            await asyncio.sleep(3600)  # Espera  de verificar de nuevo, ajusta según sea necesario
    except KeyboardInterrupt:
        print("Cerrando la aplicación...")
        for task in tasks:
            task.cancel()  # Cancelar todas las tareas de fondo cuando se interrumpe el programa
        await asyncio.gather(*tasks, return_exceptions=True)  # Esperar a que todas las tareas finalicen
        print("Aplicación cerrada con éxito.")

asyncio.run(main())
