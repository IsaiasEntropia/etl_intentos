import pandas as pd
import psycopg2 
#print(3 + 3)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="*",
    password="*")

print(conn)

from configparser import ConfigParser
