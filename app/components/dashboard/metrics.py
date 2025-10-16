import reflex as rx
from app.states.state import DashboardState, Metric


def metric_card(metric: Metric) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(tag=metric["icon"], class_name="w-6 h-6 text-white"),
            class_name=f"p-3 rounded-lg {metric['color']} shadow-lg",
        ),
        rx.el.div(
            rx.el.p(metric["title"], class_name="text-sm text-gray-500 font-medium"),
            rx.el.p(metric["value"], class_name="text-2xl font-bold text-gray-800"),
            class_name="mt-2",
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 flex items-center gap-4",
    )


def metrics_grid() -> rx.Component:
    return rx.el.div(
        rx.foreach(DashboardState.metrics, metric_card),
        class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6",
    )