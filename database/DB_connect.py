import mysql.connector
from mysql.connector import errorcode


def get_connection() -> mysql.connector.connection:
    try:
        cnx = mysql.connector.connect(
            option_files='connector.cnf'
        )
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            return None
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return None
        else:
            print(err)
            return None

# una classe madre (una base), pensata per:
#📡 Connettersi al database appena viene creata
#🧾 Eseguire query SQL (sia SELECT che INSERT/UPDATE/DELETE)
#❌ Gestire automaticamente gli errori
#🧹 Chiudere la connessione quando non serve più

class DBConnect:
    def __init__(self):
        # All'avvio, prova ad aprire la connessione, CON LA FUNZIONE CREATA PRIMA
        self.conn = get_connection()  # Crea la connessione quando la classe viene istanziata

        if self.conn:
            print("Connessione al DB avvenuta con successo! 🎉")
        else:
            print("Connessione al DB fallita 😢")

    def execute_query(self, query, params=None):
        """Esegue una query INSERT/UPDATE/DELETE"""
        cursor = self.conn.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            print("Query eseguita con successo ✅")
            return cursor.rowcount
        except mysql.connector.Error as err:
            print("Errore durante l'esecuzione della query: ", err)
            self.conn.rollback()
            return None
        finally:
            cursor.close()

    def fetch_query(self, query, params=None):
        #params è una lista (o tupla) di valori che vengono inseriti nella query SQL quando usi dei segnaposto (%s) nella stringa.
        """Esegue una query SELECT e restituisce i risultati"""
        cursor = self.conn.cursor(dictionary=True)
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()#legge i risultati
            print("Query recuperata con successo 📥")
            return result
        except mysql.connector.Error as err:
            print("Errore durante il recupero della query: ", err)
            return None
        finally:
            cursor.close()

    def close(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Connessione chiusa 🔒")

