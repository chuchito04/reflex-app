import reflex as rx
##from .database.models import get_all_data
from .pages import routes



app = rx.App()

app.add_page(routes.index)
