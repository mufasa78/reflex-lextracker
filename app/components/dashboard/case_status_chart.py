import reflex as rx
from app.states.state import DashboardState


def case_status_chart() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Case Status Overview",
            class_name="text-lg font-semibold text-gray-800 mb-4 px-6 pt-4",
        ),
        rx.recharts.area_chart(
            rx.recharts.cartesian_grid(
                stroke_dasharray="3 3", class_name="stroke-gray-200"
            ),
            rx.recharts.x_axis(data_key="name", class_name="text-xs text-gray-500"),
            rx.recharts.y_axis(class_name="text-xs text-gray-500"),
            rx.recharts.tooltip(
                content_style={
                    "background": "#FFFFFF",
                    "border": "1px solid #E5E7EB",
                    "borderRadius": "0.5rem",
                },
                label_style={"color": "#1F2937", "fontWeight": "bold"},
            ),
            rx.recharts.legend(wrapper_style={"paddingTop": "20px"}),
            rx.recharts.area(
                type="monotone",
                data_key="Active",
                stroke="#f97316",
                fill="#fb923c",
                fill_opacity=0.3,
            ),
            rx.recharts.area(
                type="monotone",
                data_key="Pending",
                stroke="#3b82f6",
                fill="#60a5fa",
                fill_opacity=0.3,
            ),
            rx.recharts.area(
                type="monotone",
                data_key="Closed",
                stroke="#22c55e",
                fill="#4ade80",
                fill_opacity=0.3,
            ),
            data=DashboardState.case_status_data,
            height=300,
            margin={"top": 5, "right": 30, "left": 0, "bottom": 5},
        ),
        class_name="bg-white rounded-xl border border-gray-200 shadow-sm",
    )