from dataclasses import dataclass

@dataclass
class Studente:
    matricola: str
    nome: str
    cognome: str
    cds: str = None

    def __str__(self):
        return f"{self.nome} {self.cognome}"
