import reflex as rx
from app.states.state import DashboardState


def dashboard_header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.button(
                rx.icon(tag="menu", class_name="h-6 w-6 text-gray-600"),
                on_click=DashboardState.toggle_sidebar,
                class_name="lg:hidden p-2 rounded-md hover:bg-gray-200",
            ),
            rx.el.h1(
                "Dashboard", class_name="text-2xl font-bold text-gray-800 font-['Lora']"
            ),
            class_name="flex items-center gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.input(
                    placeholder="Search cases, documents...",
                    class_name="bg-gray-100 border-none rounded-lg pl-10 pr-4 py-2 text-sm w-full focus:ring-2 focus:ring-orange-500",
                ),
                rx.icon(
                    tag="search",
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400",
                ),
                class_name="relative hidden md:block",
            ),
            rx.el.button(
                rx.icon(tag="plus", class_name="mr-2 h-4 w-4"),
                "New Case",
                class_name="hidden sm:flex items-center bg-orange-500 text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-orange-600 transition-colors shadow-sm hover:shadow-md",
            ),
            rx.el.button(
                rx.icon(tag="bell", class_name="h-5 w-5"),
                class_name="p-2 rounded-full hover:bg-gray-200 text-gray-600",
            ),
            class_name="flex items-center gap-4",
        ),
        class_name="flex items-center justify-between p-4 bg-white/80 backdrop-blur-sm sticky top-0 z-10 border-b border-gray-200",
    )