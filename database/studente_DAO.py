from funcy import empty
from oauthlib.uri_validate import query
from model.studente import Studente
from database.DB_connect import DBConnect

class StudenteDAO(DBConnect):
    def __init__(self):
        super().__init__()  # eredita la connessione da DBConnect
#HO utilizzato la ereditarietà per fare oop fatta bene e per

    def get_studente_by_matricola(self, matricola):
        """
        Restituisce un singolo studente (oggetto Studente) dato il numero di matricola.
        Se non trovato, restituisce None.
        """
        query = "SELECT matricola, cognome, nome, CDS FROM studente WHERE matricola = %s"
        params = (matricola,)
        risultato = self.fetch_query(query, params)

        if risultato and len(risultato) > 0:
            r = risultato[0]  # risultato è una lista di dizionari, quindi prendo il primo
            studente = Studente(
                matricola=r["matricola"],
                nome=r["nome"],
                cognome=r["cognome"],
                cds=r["CDS"]
            )
            return studente
        else:
            return None

    # FUNZIONE OPZIONALE: restituisce tutti gli studenti (per test o lista completa)
    def get_all_studenti(self):
        query = "SELECT * FROM studente"
        return self.fetch_query(query)

    # FUNZIONE OPZIONALE: inserimento di uno studente (non richiesto dalla traccia)
    def insert_studente(self, matricola, nome, cognome):
        """
        Inserisce un nuovo studente nel database.
        """
        query = "INSERT INTO studente (matricola, nome, cognome) VALUES (%s, %s, %s)"
        params = (matricola, nome, cognome)
        return self.execute_query(query, params)

    def get_corsi_studente(self, matricola):
        """Dato una matricola, ritorna i corsi oggetto a cui è iscritto lo studente"""
        from database.corso_DAO import CorsoDAO
        self.corsoDAO = CorsoDAO()
        query = "SELECT codins FROM iscrizione WHERE matricola = %s"
        params = (matricola,)
        risultati = self.fetch_query(query, params)

        oggetti_risultati = []
        for risultato in risultati:
            oggCorso = self.corsoDAO.get_corso_by_id(risultato["codins"])
            if oggCorso:
                oggetti_risultati.append(oggCorso)

        return oggetti_risultati  # Restituisci direttamente la lista (vuota o piena)


