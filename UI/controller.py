import flet as ft
from model.model import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_cerca_iscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        codin = self._view.dropdown.value
        iscritti = self._model.getStudentiIscrittiACorso(codin)
        if len(iscritti) == 0:
            self._view.show_banner("nessun iscritto per il corso selezionato")
        else:
            for student in iscritti:
                self._view.txt_result.controls.append(
                    ft.Text(student)
                )
        self._view.update_page()


    def get_dropdown_options(self):
        opzioni = self._model.get_corsi()
        self._view.update_page()
        return [ft.dropdown.Option(key=corso.codins, text=str(corso)) for corso in opzioni]

    def handle_search_student(self, e):
        selected_course = self._view.dropdown.value
        if selected_course:
            students = self._model.get_students_by_course(selected_course)

            # Pulisci i risultati precedenti
            self._view.txt_result.controls.clear()

            if students:
                # Aggiungi i risultati trovati nella lista
                for student in students:
                    self._view.txt_result.controls.append(
                        ft.Text(f"Matricola: {student.matricola}, Nome: {student.nome}, Cognome: {student.cognome}")
                    )
            else:
                # Aggiungi un messaggio se non ci sono studenti
                self._view.txt_result.controls.append(ft.Text("Nessuno studente iscritto al corso selezionato."))

            # Aggiorna la pagina per visualizzare i nuovi dati
            self._view.update_page()
        else:
            self._view.create_alert("Seleziona un corso prima di cercare gli studenti.")
            return

    def handle_search_student_by_matricola(self, e):
        studente_daCercare = self._view.matricolaField.value.strip().split(" ")

        if len(studente_daCercare) == 1:
            trovato = self._model.getStudenteByMatricola(studente_daCercare[0])
            if trovato is not None:
                self._view.nomefield.value = trovato.nome
                self._view.cognomefield.value = trovato.cognome
                self._view.matricolaField.value = ""
            else:
                self._view.show_banner("Studente non trovato.")
                return
        else:
            self._view.show_banner(f"Impossibile trovare nome e cognome di {studente_daCercare}")
            return

        self._view.update_page()

    def handle_search_course(self, e):
        matricola_input = self._view.matricolaField.value.strip()
        selected_matricola = matricola_input.split()

        self._view.txt_result.controls.clear()

        if len(selected_matricola) == 1:
            corsi_trovati = self._model.getCorsiStudente(selected_matricola[0])

            if corsi_trovati:
                for corso in corsi_trovati:
                    self._view.txt_result.controls.append(ft.Text(corso))
            else:
                self._view.txt_result.controls.append(ft.Text("Nessun corso trovato."))
        else:
            self._view.show_banner(f"Matricola non valida: '{matricola_input}'")

        self._view.update_page()


    def handle_matricola_focus(self, e):
        self._view.nomefield.value = ""
        self._view.cognomefield.value = ""
        self._view.update_page()


