import reflex as rx
import reflex_enterprise as rxe
from app.states.state import DashboardState
from app.components.sidebar import sidebar
from app.components.dashboard.header import dashboard_header
from app.components.dashboard.metrics import metrics_grid
from app.components.dashboard.case_status_chart import case_status_chart
from app.components.dashboard.upcoming_events import upcoming_events_widget
from app.components.dashboard.recent_activity import recent_activity_feed
from app.pages.cases_page import cases_page


def index() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            dashboard_header(),
            rx.el.main(
                metrics_grid(),
                rx.el.div(case_status_chart(), class_name="mt-6"),
                rx.el.div(
                    upcoming_events_widget(),
                    recent_activity_feed(),
                    class_name="mt-6 grid grid-cols-1 lg:grid-cols-2 gap-6",
                ),
                class_name="p-6",
            ),
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


app = rxe.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)
app.add_page(cases_page, route="/cases")