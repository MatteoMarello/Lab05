import flet as ft
print("Flet viene da:", ft.__file__)


from model.model import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    my_model = Model()
    my_view = View(page, my_model)
    my_controller = Controller(my_view, my_model)
    my_view.load_interface()


ft.app(target=main)
