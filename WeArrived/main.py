import flet as ft
'''
from paginaInicio import view_home
from inicioSesion import view_login
'''

def main(page: ft.Page):
    page.title = "Ejemplo de Navegación"
    '''
    def navigate(route):
        page.views.clear()
        if route == "/":
            page.views.append(view_home(page))
        elif route == "/login":
            page.views.append(view_login(page))
        page.update()
    '''
    page.on_route_change = lambda e: navigate(e.route)
    page.go("/")  # Carga la vista inicial

ft.app(target=main)
