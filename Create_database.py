
import psycopg2
from CREATE_TABLES_QUERIS.Create_tables_queris import create_queries

conn = psycopg2.connect("dbname='cinemadb' user='hristo'")


cur = conn.cursor()
cur.execute(create_queries.create_movie())
conn.commit()
cur.execute(create_queries.create_projection())
conn.commit()
cur.execute(create_queries.create_user())
cur.execute(create_queries.create_reservation())
conn.commit()
conn.close()
