import reflex as rx
from app.states.state import DashboardState


def sidebar_link(text: str, icon: str, url: str) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(tag=icon, class_name="w-5 h-5"),
            rx.el.span(text),
            class_name="flex items-center gap-3 px-3 py-2 text-gray-700 rounded-lg hover:bg-gray-200 transition-colors duration-200",
        ),
        href=url,
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("scale", class_name="w-8 h-8 text-orange-500"),
                    rx.el.h1(
                        "LexTrack",
                        class_name="text-2xl font-bold text-gray-800 font-['Lora']",
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.el.button(
                    rx.icon(tag="x", class_name="w-6 h-6"),
                    on_click=DashboardState.toggle_sidebar,
                    class_name="lg:hidden p-1 rounded-md hover:bg-gray-200",
                ),
                class_name="flex items-center justify-between p-4 border-b border-gray-200",
            ),
            rx.el.nav(
                sidebar_link("Dashboard", "layout-dashboard", "/"),
                sidebar_link("Cases", "briefcase", "/cases"),
                sidebar_link("Calendar", "calendar-days", "#"),
                sidebar_link("Documents", "file-text", "#"),
                sidebar_link("Time Tracking", "clock", "#"),
                sidebar_link("Reports", "bar-chart-3", "#"),
                class_name="flex flex-col gap-1 p-4",
            ),
            class_name="flex-grow",
        ),
        rx.el.div(
            sidebar_link("Settings", "settings", "#"),
            rx.el.div(
                rx.el.div(
                    rx.el.img(
                        src=f"https://api.dicebear.com/9.x/initials/svg?seed=Advocate",
                        class_name="w-10 h-10 rounded-full",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Advocate", class_name="font-semibold text-sm text-gray-800"
                        ),
                        rx.el.p(
                            "advocate@lextrack.co.ke",
                            class_name="text-xs text-gray-500",
                        ),
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.icon(tag="fold_vertical", class_name="text-gray-500"),
                class_name="flex items-center justify-between p-4 border-t border-gray-200",
            ),
            class_name="flex flex-col gap-1 p-4",
        ),
        class_name=rx.cond(
            DashboardState.sidebar_open,
            "fixed inset-y-0 left-0 z-50 w-64 bg-gray-100 border-r border-gray-200 flex flex-col transition-transform transform translate-x-0 ease-out duration-300",
            "fixed inset-y-0 left-0 z-50 w-64 bg-gray-100 border-r border-gray-200 flex flex-col transition-transform transform -translate-x-full lg:translate-x-0 ease-in duration-300",
        ),
    )