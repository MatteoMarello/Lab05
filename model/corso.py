from pywin32_testutil import non_admin_error_codes

from dataclasses import dataclass

@dataclass (frozen=True)
class Corso:
    codins: str
    nome: str
    crediti: int = None
    pd: int = None

    def __str__(self):
        return f"{self.codins} {self.nome}"
