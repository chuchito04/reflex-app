import reflex as rx
from prueba_reflex.database.models import get_all_data

@rx.page(
    title="Marcianito",
    route="/marcianito",
)
def marciano() -> rx.Component:

    
    return rx.container(
        rx.color_mode.button(position="top-right"),
        
        rx.center(
            rx.image(
            src="/marcianito.gif",
            width="50%",
            height="auto",
            cursor="pointer",
            ),
            
        ),
        
        justify_content="center",
        height="85vh",
    )