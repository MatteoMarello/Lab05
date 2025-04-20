from database.DB_connect import DBConnect
from model.studente import Studente
from model.corso import Corso

class CorsoDAO(DBConnect):
    def __init__(self):
        super().__init__()  # Eredita la connessione da DBConnect

    def get_corso_by_id(self, corso_id):
        """
        Restituisce un singolo oggetto corso, dato l'ID del corso.
        Se non trovato, restituisce None.
        """
        query = "SELECT * FROM corso WHERE codins = %s"
        params = (corso_id,)
        risultato = self.fetch_query(query, params)

        if risultato and len(risultato) > 0:
            # Crea un oggetto Corso con i dati estratti dal risultato della query
            corso = Corso(
                codins=risultato[0]['codins'],
                nome=risultato[0]['nome'],
                crediti=risultato[0]['crediti'],
                pd=risultato[0]['pd']
            )
            return corso  # Ritorna l'oggetto Corso
        else:
            return None

    def get_all_corsi(self):
        """Restituisce una lista di oggetti Corso"""
        query = "SELECT codins, nome, crediti, pd FROM corso"
        risultati = self.fetch_query(query)

        if risultati and len(risultati) > 0:
            listaCorsi = []
            for riga in risultati:
                corso = Corso(
                    codins=riga['codins'],
                    nome=riga['nome'],
                    crediti=riga['crediti'],
                    pd=riga['pd']
                )
                listaCorsi.append(corso)
            return listaCorsi
        else:
            return []

    def iscritti_corso(self, corso_id):
        from database.studente_DAO import StudenteDAO
        self.studente_dao = StudenteDAO()
        query = "SELECT matricola FROM iscrizione WHERE codins = %s"
        params = (corso_id,)
        risultati = self.fetch_query(query, params)

        studenti = []

        if risultati:
            for riga in risultati:
                studente = self.studente_dao.get_studente_by_matricola(riga["matricola"])
                if studente:
                    studenti.append(studente)

        return studenti
