import reflex as rx
import reflex_enterprise as rxe
from app.states.case_state import CaseState, Case, CaseStatus


def case_card(case: rx.Var[Case]) -> rx.Component:
    """Renders a draggable card for a single case."""
    return rxe.dnd.draggable(
        rx.el.div(
            rx.el.h3(case["case_number"], class_name="font-bold text-sm text-gray-800"),
            rx.el.p(case["client_name"], class_name="text-xs text-gray-600 mt-1"),
            rx.el.div(
                rx.el.div(
                    rx.icon("user", class_name="w-3 h-3"),
                    rx.el.p(case["assigned_lawyer"], class_name="text-xs"),
                    class_name="flex items-center gap-1 text-gray-500",
                ),
                rx.el.div(
                    rx.el.span(
                        case["priority"],
                        class_name=rx.match(
                            case["priority"],
                            (
                                "High",
                                "text-xs font-medium px-2 py-0.5 rounded-full bg-red-100 text-red-700",
                            ),
                            (
                                "Medium",
                                "text-xs font-medium px-2 py-0.5 rounded-full bg-yellow-100 text-yellow-700",
                            ),
                            (
                                "Low",
                                "text-xs font-medium px-2 py-0.5 rounded-full bg-green-100 text-green-700",
                            ),
                            "text-xs font-medium px-2 py-0.5 rounded-full bg-gray-100 text-gray-700",
                        ),
                    )
                ),
                class_name="flex justify-between items-center mt-3",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon("calendar", class_name="w-3 h-3"),
                    rx.el.p(case["next_date"], class_name="text-xs"),
                    class_name="flex items-center gap-1 text-gray-500",
                ),
                rx.el.p(
                    "Updated ", case["last_updated"], class_name="text-xs text-gray-400"
                ),
                class_name="flex justify-between items-center mt-2",
            ),
            class_name="bg-white p-4 rounded-lg border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-0.5 transition-all cursor-grab active:cursor-grabbing",
        ),
        item={"id": case["id"]},
        type="case",
    )


def kanban_column(
    title: CaseStatus, cases: rx.Var[list[Case]], count: rx.Var[int]
) -> rx.Component:
    """Renders a column in the Kanban board for a given case status."""
    drop_params = rxe.dnd.DropTarget.collected_params
    return rxe.dnd.drop_target(
        rx.el.div(
            rx.el.div(
                rx.el.h2(title, class_name="font-semibold text-gray-700"),
                rx.el.span(
                    count,
                    class_name="text-sm text-gray-500 bg-gray-200 px-2 py-1 rounded-md font-mono",
                ),
                class_name="flex justify-between items-center px-4 py-2 border-b border-gray-200",
            ),
            rx.el.div(rx.foreach(cases, case_card), class_name="p-2 space-y-2 h-full"),
            class_name=rx.cond(
                drop_params.is_over & drop_params.can_drop,
                "bg-orange-50 border-orange-200 rounded-lg border transition-colors",
                "bg-gray-50/50 rounded-lg border border-transparent transition-colors",
            ),
            min_height="300px",
        ),
        accept=["case"],
        on_drop=lambda item: CaseState.handle_drop(item, title),
    )


def kanban_board() -> rx.Component:
    return rx.el.div(
        kanban_column(
            title="Active",
            cases=CaseState.active_cases,
            count=CaseState.active_cases_count,
        ),
        kanban_column(
            title="Pending",
            cases=CaseState.pending_cases,
            count=CaseState.pending_cases_count,
        ),
        kanban_column(
            title="Closed",
            cases=CaseState.closed_cases,
            count=CaseState.closed_cases_count,
        ),
        class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6",
    )