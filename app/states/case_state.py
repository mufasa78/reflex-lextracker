import reflex as rx
from typing import TypedDict, Literal
import datetime

CaseStatus = Literal["Active", "Pending", "Closed"]


class Case(TypedDict):
    id: int
    case_number: str
    client_name: str
    court: str
    assigned_lawyer: str
    status: CaseStatus
    next_date: str
    priority: Literal["High", "Medium", "Low"]
    last_updated: str


class CaseState(rx.State):
    cases: list[Case] = [
        {
            "id": 1,
            "case_number": "HCC/E001/2024",
            "client_name": "KCB Bank Kenya",
            "court": "High Court - Commercial",
            "assigned_lawyer": "John Otieno",
            "status": "Active",
            "next_date": "2024-08-15",
            "priority": "High",
            "last_updated": "2 days ago",
        },
        {
            "id": 2,
            "case_number": "CMC/E002/2024",
            "client_name": "Jane Doe",
            "court": "Magistrates Court - Milimani",
            "assigned_lawyer": "Alice Wanjiru",
            "status": "Active",
            "next_date": "2024-08-20",
            "priority": "Medium",
            "last_updated": "5 hours ago",
        },
        {
            "id": 3,
            "case_number": "CAC/E003/2024",
            "client_name": "Safaricom PLC",
            "court": "Court of Appeal",
            "assigned_lawyer": "John Otieno",
            "status": "Pending",
            "next_date": "2024-09-01",
            "priority": "High",
            "last_updated": "1 day ago",
        },
        {
            "id": 4,
            "case_number": "ELC/E004/2024",
            "client_name": "Peter Kimani",
            "court": "Environment and Land Court",
            "assigned_lawyer": "Emily Koech",
            "status": "Pending",
            "next_date": "2024-08-25",
            "priority": "Low",
            "last_updated": "1 week ago",
        },
        {
            "id": 5,
            "case_number": "JRC/E005/2023",
            "client_name": "Republic",
            "court": "Supreme Court",
            "assigned_lawyer": "Lead Counsel",
            "status": "Closed",
            "next_date": "N/A",
            "priority": "Medium",
            "last_updated": "2 months ago",
        },
    ]
    search_query: str = ""
    is_modal_open: bool = False
    courts: list[str] = [
        "Supreme Court",
        "Court of Appeal",
        "High Court - Milimani",
        "High Court - Commercial",
        "High Court - Family Division",
        "Environment and Land Court",
        "Employment and Labour Relations Court",
        "Magistrates Court - Milimani",
        "Magistrates Court - Kiambu",
        "Kadhis' Court",
    ]
    lawyers: list[str] = ["John Otieno", "Alice Wanjiru", "Emily Koech", "Lead Counsel"]

    @rx.var
    def filtered_cases(self) -> list[Case]:
        if not self.search_query:
            return self.cases
        return [
            case
            for case in self.cases
            if self.search_query.lower() in case["case_number"].lower()
            or self.search_query.lower() in case["client_name"].lower()
        ]

    @rx.var
    def active_cases(self) -> list[Case]:
        return [case for case in self.filtered_cases if case["status"] == "Active"]

    @rx.var
    def pending_cases(self) -> list[Case]:
        return [case for case in self.filtered_cases if case["status"] == "Pending"]

    @rx.var
    def closed_cases(self) -> list[Case]:
        return [case for case in self.filtered_cases if case["status"] == "Closed"]

    @rx.var
    def active_cases_count(self) -> int:
        return len(self.active_cases)

    @rx.var
    def pending_cases_count(self) -> int:
        return len(self.pending_cases)

    @rx.var
    def closed_cases_count(self) -> int:
        return len(self.closed_cases)

    @rx.event
    def handle_drop(self, item: dict, new_status: CaseStatus):
        case_id = int(item["id"])
        for i, case in enumerate(self.cases):
            if case["id"] == case_id:
                self.cases[i]["status"] = new_status
                self.cases[i]["last_updated"] = "Just now"
                break

    @rx.event
    def toggle_modal(self):
        self.is_modal_open = not self.is_modal_open

    @rx.event
    def add_case(self, form_data: dict):
        new_case = Case(
            id=len(self.cases) + 1,
            case_number=form_data["case_number"],
            client_name=form_data["client_name"],
            court=form_data["court"],
            assigned_lawyer=form_data["assigned_lawyer"],
            status="Active",
            next_date=form_data["next_date"],
            priority=form_data["priority"],
            last_updated="Just now",
        )
        self.cases.append(new_case)
        self.is_modal_open = False
        return rx.toast("Case added successfully!")