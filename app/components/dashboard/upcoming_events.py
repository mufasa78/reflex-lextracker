import reflex as rx
from app.states.state import DashboardState, UpcomingEvent


def event_item(event: UpcomingEvent) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.cond(
                event["event_type"] == "Hearing",
                rx.icon(tag="gavel", class_name="w-5 h-5 text-red-500"),
                rx.cond(
                    event["event_type"] == "Mention",
                    rx.icon(tag="file-check", class_name="w-5 h-5 text-blue-500"),
                    rx.icon(tag="calendar-clock", class_name="w-5 h-5 text-yellow-500"),
                ),
            ),
            class_name="p-3 bg-gray-100 rounded-lg",
        ),
        rx.el.div(
            rx.el.p(
                event["case_name"], class_name="font-semibold text-gray-800 text-sm"
            ),
            rx.el.p(
                f"{event['event_type']} at {event['court']}",
                class_name="text-xs text-gray-500",
            ),
        ),
        rx.el.div(
            rx.el.p(
                event["date"],
                class_name="font-medium text-gray-700 text-sm whitespace-nowrap",
            ),
            rx.el.p(event["time"], class_name="text-xs text-gray-500"),
            class_name="text-right ml-auto",
        ),
        class_name="flex items-center gap-4 p-3 hover:bg-gray-50 rounded-lg transition-colors",
    )


def upcoming_events_widget() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Upcoming Events", class_name="text-lg font-semibold text-gray-800 mb-4"
        ),
        rx.el.div(
            rx.foreach(DashboardState.upcoming_events, event_item),
            class_name="flex flex-col gap-2",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
    )