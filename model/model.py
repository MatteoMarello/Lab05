from database.corso_DAO import CorsoDAO
from database.studente_DAO import StudenteDAO


class Model:
    def __init__(self):
        self.corsoDAO = CorsoDAO()
        self.studentDAO = StudenteDAO()

    def get_studenti_iscritti(self):
        return self.studentDAO.get_all_studenti()

    def get_corsi(self):
        return self.corsoDAO.get_all_corsi()

    def getStudenteByMatricola(self, matricola):
        return self.studentDAO.get_studente_by_matricola(matricola)

    def getStudentiIscrittiACorso(self, codin):
        return self.corsoDAO.iscritti_corso(codin)

    def getCorsiStudente(self,matricola):
        return self.studentDAO.get_corsi_studente(matricola)
