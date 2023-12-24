import time

import psycopg2
from pprint import pprint


    # Функция, создающая структуру БД (таблицы)
def create_db(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS Clients(
                Id SERIAL PRIMARY KEY,
                Name VARCHAR(40),
                LastName VARCHAR(40),
                Email VARCHAR (40)
                );
                """)
    cur.execute("""CREATE TABLE IF NOT EXISTS PhoneNumber(
                client_id INTEGER REFERENCES Clients(id),
                Number varchar(11) PRIMARY KEY
                );
                """)
    
    
### Функция, позволяющая добавить нового клиента
    
def new_client(cur, name, last_name, email, phones=None):
    cur.execute("""INSERT INTO Clients(name, lastname, email)
                    VALUES (%s, %s, %s)
                     RETURNING id, name, lastname;""",
                    (name, last_name, email))
        
    client = cur.fetchone()

    if phones is not None:
            cur.execute("""INSERT INTO PhoneNumber(client_id, number)
                        VALUES(%s, %s);
                        """,(client[0], phones))
    return 

    
    


### Функция, позволяющая добавить телефон для существующего клиента.
def add_phone(cur, client_id, phone):
    cur.execute("""INSERT INTO PhoneNumber(client_id, number)
                    VALUES (%s, %s);
                """,(client_id, phone))
    return

    
    
### Функция, позволяющая изменить данные о клиенте.
def change_client(cur, client_id, name=None, lastname=None, email=None, phones=None):
    if name is not None:
            cur.execute("""UPDATE Clients SET name=%s WHERE id=%s
                        """, (name, client_id))
    if lastname is not None:
            cur.execute("""UPDATE Clients SET lastname=%s WHERE id=%s
                        """, (lastname, client_id))
    if email is not None:
            cur.execute("""UPDATE Clients SET email=%s WHERE id=%s
                        """, (email, client_id))
    if phones is not None:
            new_client(cur, client_id, phones)

        
    # Функция, позволяющая удалить телефон для существующего клиента
def delete_phone(cur, client_id, phones):
    cur.execute("""DELETE FROM PhoneNumber
                    WHERE client_id=%s and number=%s
                    """, (client_id, phones)) 
           
    
#  Функция, позволяющая удалить существующего клиента       
def delete_client(cur, client_id):
    cur.execute("""DELETE FROM PhoneNumber
                    WHERE PhoneNumber.client_id=%s
                    """, (client_id))
    cur.execute("""DELETE FROM Clients
                    WHERE id=%s"""
                    , (client_id))
        
    return
    
    
# Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
def find_client(cur, name=None, last_name=None, email=None, phones=None):
        
    
    
    
    

    
    
# conn = psycopg2.connect(database = 'ClientBD', user = 'postgres', password = 'psql1488')

# with conn.cursor() as cur: 
#     conn.commit()   
# conn.close()