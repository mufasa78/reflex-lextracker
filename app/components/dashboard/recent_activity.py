import reflex as rx
from app.states.state import DashboardState, Activity


def activity_item(activity: Activity) -> rx.Component:
    return rx.el.div(
        rx.el.img(
            src=f"https://api.dicebear.com/9.x/initials/svg?seed={activity['avatar_seed']}",
            class_name="w-10 h-10 rounded-full",
        ),
        rx.el.div(
            rx.el.p(
                rx.el.span(activity["user"], class_name="font-semibold text-gray-800"),
                f" {activity['action']} ",
                rx.el.span(
                    activity["details"], class_name="font-semibold text-orange-600"
                ),
                class_name="text-sm text-gray-600",
            ),
            rx.el.p(activity["timestamp"], class_name="text-xs text-gray-400"),
        ),
        class_name="flex items-start gap-4 p-3",
    )


def recent_activity_feed() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Recent Activity", class_name="text-lg font-semibold text-gray-800 mb-4"
        ),
        rx.el.div(
            rx.foreach(DashboardState.recent_activities, activity_item),
            class_name="flex flex-col divide-y divide-gray-200",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm",
    )