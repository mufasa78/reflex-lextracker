import reflex as rx
from app.states.case_state import CaseState
from app.components.cases.case_form import case_form


def cases_header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.h1(
                "Case Management",
                class_name="text-2xl font-bold text-gray-800 font-['Lora']",
            ),
            class_name="flex items-center gap-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.input(
                    placeholder="Search by case number or client...",
                    on_change=CaseState.set_search_query,
                    class_name="bg-gray-100 border-none rounded-lg pl-10 pr-4 py-2 text-sm w-full focus:ring-2 focus:ring-orange-500",
                ),
                rx.icon(
                    tag="search",
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400",
                ),
                class_name="relative hidden md:block w-64",
            ),
            case_form(),
            rx.el.button(
                rx.icon(tag="filter", class_name="h-5 w-5"),
                class_name="p-2 rounded-lg hover:bg-gray-200 text-gray-600",
            ),
            class_name="flex items-center gap-4",
        ),
        class_name="flex items-center justify-between p-4 bg-white/80 backdrop-blur-sm sticky top-0 z-10 border-b border-gray-200",
    )