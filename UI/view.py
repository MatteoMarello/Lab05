import flet as ft
from UI.controller import Controller


class View(ft.UserControl):
    def __init__(self, page: ft.Page, model) -> None:
        super().__init__()
        self._page = page
        self._model = model
        self._controller = Controller(self, model)
        self._page.title = "APP GESTIONE STUDENTI"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK


        # Inizializzazione dei componenti
        self._title = ft.Text("APP GESTIONE STUDENTI", color="blue", size=24)

        # Dropdown per i corsi
        self.dropdown = ft.Dropdown(
            label="Scegli un corso",
            width=500,
            options=[]  # Le opzioni vengono caricate dal controller
        )

        # Bottone per cercare iscritti
        self.btn_hello = ft.ElevatedButton(
            text="Cerca iscritti",
            icon_color=ft.colors.BLUE_50,
            on_click=self._controller.handle_cerca_iscritti
        )

        # Campi di input per matricola, nome, e cognome
        self.matricolaField = ft.TextField(label="Matricola",on_focus=self._controller.handle_matricola_focus)
        self.nomefield = ft.TextField(label="Nome", read_only=True)
        self.cognomefield = ft.TextField(label="Cognome", read_only=True)

        # Bottone per cercare studente
        self.btn_search_student = ft.ElevatedButton(
            text="Cerca studente",
            icon_color=ft.colors.BLUE_50,
            on_click=self._controller.handle_search_student_by_matricola
        )

        # Bottone per cercare corsi
        self.btn_search_course = ft.ElevatedButton(
            text="Cerca corsi",
            icon_color=ft.colors.BLUE_50,
            on_click=self._controller.handle_search_course
        )

        # Bottone per iscrizione
        self.btn_search_signup = ft.ElevatedButton(
            text="Iscriviti",
            icon_color=ft.colors.BLUE_50
        )

        # Lista per mostrare i risultati
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    def load_interface(self):
        """Costruisce l'interfaccia utente."""
        self._page.controls.append(self._title)

        # Aggiungi la prima riga: Dropdown e bottone per cercare iscritti
        row1 = ft.Row([self.dropdown, self.btn_hello], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # Aggiungi la seconda riga: Matricola, nome e cognome
        row2 = ft.Row([self.matricolaField, self.nomefield, self.cognomefield], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # Aggiungi la terza riga: Bottone per cercare studente, corsi e iscrizione
        row3 = ft.Row([self.btn_search_student, self.btn_search_course, self.btn_search_signup], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # Aggiungi la lista per i risultati
        self._page.controls.append(self.txt_result)

        # Carica i dati del dropdown
        self.dropdown.options = self._controller.get_dropdown_options()

        self._page.update()

    def show_banner(self, message):
        self._page.banner = ft.Banner(
            bgcolor=ft.colors.RED_500,
            leading=ft.Icon(ft.icons.ERROR, color=ft.colors.RED),
            content=ft.Text(message),
            actions=[
                ft.TextButton("Chiudi", on_click=lambda e: self._close_banner())
            ]
        )
        self._page.banner.open = True
        self._page.update()

    def _close_banner(self):
        self._page.banner.open = False
        self._page.update()



    @property
    def controller(self):
        """Permette di accedere al controller."""
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Imposta un nuovo controller."""
        self._controller = controller

    def set_controller(self, controller):
        """Imposta un nuovo controller."""
        self._controller = controller

    def create_alert(self, message):
        """Mostra un messaggio di alert come popup."""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        """Aggiorna la pagina con i nuovi dati."""
        self._page.update()
