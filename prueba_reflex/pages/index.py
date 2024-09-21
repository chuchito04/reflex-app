import reflex as rx
from prueba_reflex.database.models import get_all_data
from prueba_reflex.components.Footer import Footer

@rx.page(
    title="Inicio",
)
def index() -> rx.Component:
    datos = get_all_data()
    
    table_rows = [
        rx.table.row(
            rx.table.row_header_cell(dato.localidad),  
            rx.table.cell(dato.clave_inegi),           
            rx.table.cell(f"{dato.id_estado}-{dato.id_municipio}"),  
        )
        for dato in datos
    ]
    
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.text("MYSQL + REFLEX",
                font_weight="bold",
                font_size="3rem",
                align="center",
            ),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Localidad"),
                        rx.table.column_header_cell("Clave INEGI"),
                        rx.table.column_header_cell("Estado-Municipio"),
                    ),
                ),
                rx.table.body(*table_rows),  
                width="100%",
            ),
        
            rx.alert_dialog.root(
                rx.alert_dialog.trigger(
                    rx.button("Marcianito 😎", variant="solid", color_scheme="green", cursor = "pointer",),
                ),
                rx.alert_dialog.content(
                    rx.alert_dialog.title("Marcianito 100% Real No Fake"),
                    rx.alert_dialog.description(
                        "grande el marcianito",
                        size="2",
                        text_align="center",
                        margin_bottom="10px",
                    ),
                    rx.center(
                        rx.image(
                            src="/marcianito.gif",
                            width="30vw",
                            height="50vh",
                            cursor="pointer",
                        ),
                    ),
                    rx.flex(
                        rx.alert_dialog.cancel(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                                cursor = "pointer",
                            ),
                        ),
                        rx.alert_dialog.action(
                            rx.button(
                                "Ok",
                                color_scheme="red",
                                variant="solid",
                                cursor = "pointer",
                            ),
                        ),
                        spacing="3",
                        margin_top="16px",
                        justify="end",
                    ),
                    style={"max_width": 1000},
                ),
            ),
            display="flex",
            align_items="center",
            justify_content="center",
            margin_top="20vh",
        ),
        Footer(),
        height="100vh",
        ##background_image="url(/dark.webp)",
    )