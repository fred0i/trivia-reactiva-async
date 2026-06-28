import asyncio
import urllib
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import select

# Base para mapear las tablas a clases de Python
Base = declarative_base()

class SQLServerORM:
    def __init__(self, server, database, username=None, password=None, trusted_connection=False):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.trusted_connection = trusted_connection
        self.engine = None
        self.AsyncSession = None

        self._create_async_engine()

    def _create_async_engine(self):
        """Crea un motor de conexión asíncrono para SQLAlchemy."""
        driver = "ODBC Driver 17 for SQL Server"
        
        if self.trusted_connection:
            params = f"DRIVER={{{driver}}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;"
        else:
            params = f"DRIVER={{{driver}}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password};"
        
        params_encoded = urllib.parse.quote_plus(params)
        # Se cambia el dialecto a 'mssql+aioodbc' para soportar asyncio
        connection_url = f"mssql+aioodbc:///?odbc_connect={params_encoded}"
        
        try:
            self.engine = create_async_engine(connection_url, echo=False)
            # Se crea una fábrica de sesiones asíncronas
            self.AsyncSession = async_sessionmaker(bind=self.engine, expire_on_commit=False)
            print("🚀 Motor ORM Asíncrono SQLAlchemy configurado correctamente.")
        except Exception as e:
            print(f"❌ Error al inicializar el motor ORM asíncrono: {e}")
            raise

    def get_session(self):
        """Devuelve una nueva sesión asíncrona para interactuar con la BD."""
        if not self.AsyncSession:
            raise Exception("El motor ORM no está inicializado.")
        return self.AsyncSession()

# --- MODO DE USO ASÍNCRONO ---

# 1. Definir un modelo (Tabla)
class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    email = Column(String(50), unique=True)

async def main():
    # 2. Inicializar el ORM (Autenticación Windows en este ejemplo)
    db_orm = SQLServerORM(
        server="localhost\\SQLEXPRESS",
        database="MiBaseDatos",
        trusted_connection=True
    )
    
    # 3. Operar con la base de datos usando una sesión asíncrona
    # 'async with' se encarga de cerrar la sesión automáticamente
    async with db_orm.get_session() as session:
        try:
            # Insertar un nuevo usuario
            nuevo_usuario = Usuario(nombre="Ana Async", email="ana.async@email.com")
            session.add(nuevo_usuario)
            await session.commit()
            await session.refresh(nuevo_usuario) # Refresca el objeto para obtener el ID asignado por la BD
            print(f"✅ Usuario insertado: ID {nuevo_usuario.id}")
            
            # Consultar usuarios de forma asíncrona
            # Se usa select() en lugar de query()
            stmt = select(Usuario).where(Usuario.nombre.like("Ana%"))
            result = await session.execute(stmt)
            usuarios = result.scalars().all()

            print("\n--- Usuarios encontrados ---")
            for u in usuarios:
                print(f"ID: {u.id} - Nombre: {u.nombre}, Email: {u.email}")
            
        except Exception as e:
            await session.rollback()
            print(f"❌ Error en la transacción: {e}")

if __name__ == "__main__":
    # Para ejecutar una función 'async', se utiliza asyncio.run()
    # Nota: Asegúrate de que la tabla 'usuarios' exista en tu BD.
    print("Ejecutando operaciones asíncronas con la base de datos...")
    asyncio.run(main())
