import reflex as rx
import reflex_enterprise as rxe
from app.components.sidebar import sidebar
from app.states.state import DashboardState
from app.components.cases.cases_header import cases_header
from app.components.cases.kanban_board import kanban_board


def cases_page() -> rx.Component:
    return rxe.dnd.provider(
        rx.el.div(
            sidebar(),
            rx.el.div(
                cases_header(),
                rx.el.main(kanban_board(), class_name="p-6"),
                class_name="lg:pl-64 flex-1 flex flex-col transition-all duration-300",
            ),
            rx.cond(
                DashboardState.sidebar_open,
                rx.el.div(
                    on_click=DashboardState.toggle_sidebar,
                    class_name="fixed inset-0 bg-black/30 z-40 lg:hidden",
                ),
                None,
            ),
            class_name="min-h-screen bg-gray-50 font-['Lora']",
        )
    )