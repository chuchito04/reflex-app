import reflex as rx

def Footer() -> rx.Component:
    return rx.vstack(
        

        rx.hstack(
            rx.text("By @chuchito04"),
            rx.text("2024"),
            rx.text("v0.1"),
            justify="center",
            color="gray", 
        ),
        rx.logo(),
        margin_top="30vh",
        align_items="center",  
    )
