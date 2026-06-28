import asyncio
import datetime
from SQLServerORM import SQLServerORM, Usuario
from sqlalchemy import select

async def tarea_periodica(db_orm: SQLServerORM):
    """
    Esta es una tarea en segundo plano que se ejecuta cada 15 segundos.
    Simula un "evento automático".
    """
    while True:
        print(f"\n--- ⏰ Evento Automático Disparado ({datetime.datetime.now().strftime('%H:%M:%S')}) ---")
        
        try:
            async with db_orm.get_session() as session:
                # Tarea: Contar el número total de usuarios en la base de datos.
                stmt = select(Usuario)
                result = await session.execute(stmt)
                total_usuarios = len(result.scalars().all())
                print(f"📊 Reporte: Hay {total_usuarios} usuarios registrados en la base de datos.")
        except Exception as e:
            print(f"❌ Error en la tarea periódica: {e}")
            
        # Espera 15 segundos antes de la siguiente ejecución
        await asyncio.sleep(15)


async def aplicacion_principal(db_orm: SQLServerORM):
    """
    Simula la lógica principal de la aplicación, que se ejecuta
    independientemente de las tareas en segundo plano.
    """
    print("➡️  La aplicación principal ha iniciado y está en funcionamiento.")
    print("    (Mientras tanto, la tarea periódica se ejecuta en segundo plano cada 15 segundos)")
    
    # Simulamos que la aplicación está ocupada haciendo otras cosas
    # Por ejemplo, podría estar atendiendo peticiones de una API, etc.
    for i in range(1, 6):
        await asyncio.sleep(10)
        print(f"   -> Lógica principal sigue activa... (ciclo {i}/5)")
    
    print("➡️  La aplicación principal ha terminado su ciclo.")


async def main():
    """
    Punto de entrada que inicializa la BD y lanza las tareas.
    """
    # Inicializar el ORM
    db_orm = SQLServerORM(
        server="localhost\\SQLEXPRESS",
        database="MiBaseDatos",
        trusted_connection=True
    )

    # Crear la tarea en segundo plano sin esperarla (se ejecuta en "background")
    tarea_background = asyncio.create_task(tarea_periodica(db_orm))

    # Ejecutar la lógica principal de la aplicación
    await aplicacion_principal(db_orm)

    # Opcional: Cancelar la tarea en segundo plano cuando la app principal termina
    tarea_background.cancel()
    try:
        await tarea_background
    except asyncio.CancelledError:
        print("\n✅ Tarea periódica cancelada correctamente. Finalizando programa.")


if __name__ == "__main__":
    print("Iniciando la aplicación con eventos automáticos...")
    asyncio.run(main())
