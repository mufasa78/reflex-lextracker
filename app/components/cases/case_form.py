import reflex as rx
from app.states.case_state import CaseState


def case_form() -> rx.Component:
    return rx.radix.primitives.dialog.root(
        rx.radix.primitives.dialog.trigger(
            rx.el.button(
                rx.icon(tag="plus", class_name="mr-2 h-4 w-4"),
                "New Case",
                on_click=CaseState.toggle_modal,
                class_name="flex items-center bg-orange-500 text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-orange-600 transition-colors shadow-sm hover:shadow-md",
            )
        ),
        rx.radix.primitives.dialog.content(
            rx.el.form(
                rx.radix.primitives.dialog.title(
                    "Add New Case", class_name="font-bold text-lg mb-4"
                ),
                rx.el.div(
                    rx.el.label("Case Number", class_name="text-sm font-medium"),
                    rx.el.input(
                        name="case_number",
                        placeholder="e.g., HCC/E001/2024",
                        class_name="w-full p-2 border rounded-md mt-1",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label("Client Name", class_name="text-sm font-medium"),
                    rx.el.input(
                        name="client_name",
                        placeholder="e.g., KCB Bank Kenya",
                        class_name="w-full p-2 border rounded-md mt-1",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label("Court", class_name="text-sm font-medium"),
                    rx.el.select(
                        rx.foreach(
                            CaseState.courts,
                            lambda court: rx.el.option(court, value=court),
                        ),
                        name="court",
                        class_name="w-full p-2 border rounded-md mt-1",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label("Assigned Lawyer", class_name="text-sm font-medium"),
                    rx.el.select(
                        rx.foreach(
                            CaseState.lawyers,
                            lambda lawyer: rx.el.option(lawyer, value=lawyer),
                        ),
                        name="assigned_lawyer",
                        class_name="w-full p-2 border rounded-md mt-1",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label("Priority", class_name="text-sm font-medium"),
                    rx.el.select(
                        rx.el.option("High", value="High"),
                        rx.el.option("Medium", value="Medium"),
                        rx.el.option("Low", value="Low"),
                        name="priority",
                        default_value="Medium",
                        class_name="w-full p-2 border rounded-md mt-1",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label("Next Date", class_name="text-sm font-medium"),
                    rx.el.input(
                        type="date",
                        name="next_date",
                        class_name="w-full p-2 border rounded-md mt-1",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancel",
                        type="button",
                        on_click=CaseState.toggle_modal,
                        class_name="px-4 py-2 bg-gray-200 rounded-md",
                    ),
                    rx.el.button(
                        "Add Case",
                        type="submit",
                        class_name="px-4 py-2 bg-orange-500 text-white rounded-md",
                    ),
                    class_name="flex justify-end gap-4 mt-6",
                ),
                on_submit=CaseState.add_case,
                reset_on_submit=True,
            ),
            style={"max_width": "500px"},
        ),
        open=CaseState.is_modal_open,
        on_open_change=CaseState.set_is_modal_open,
    )