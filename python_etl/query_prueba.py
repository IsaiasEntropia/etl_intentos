import json
import psycopg2 
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="*",
    password="*")

# Create a new cursor
cur = conn.cursor()

# Crear la consulta
cur.execute( 'SELECT * FROM cvu_info' )

# Mostrar la consulta via Fetch
    # fetchone(),  fetchall(), or  fetchmany() method.
#tabla_1 = cur.fetchall()
#print(tabla_1)

###########
# Columnas del Json
columns = ( 'persona_id', 'cvu_num', 'nombre' )
# Resultado
resultado = []
# Poblar los resultados

for row in cur.fetchall():
    resultado.append(dict(zip(columns, row)))

# Resultados 
#print(resultado)

print (json.dumps (resultado, indent=2))


### Mètodo 2
#from psycopg2.extras import RealDictCursor
# cur = conn.cursor(cursor_factory=RealDictCursor)
# print json.dumps(cur.fetchall(), indent=2)
