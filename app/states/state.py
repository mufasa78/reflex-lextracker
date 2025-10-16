import reflex as rx
from typing import TypedDict, Literal
import datetime


class Metric(TypedDict):
    title: str
    value: str
    icon: str
    color: str


class CaseStatusData(TypedDict):
    name: str
    Active: int
    Pending: int
    Closed: int


class UpcomingEvent(TypedDict):
    case_name: str
    event_type: str
    date: str
    time: str
    court: str


class Activity(TypedDict):
    user: str
    action: str
    details: str
    timestamp: str
    avatar_seed: str


class DashboardState(rx.State):
    sidebar_open: bool = False
    metrics: list[Metric] = [
        {
            "title": "Total Cases",
            "value": "128",
            "icon": "briefcase",
            "color": "bg-orange-500",
        },
        {
            "title": "Upcoming Events",
            "value": "12",
            "icon": "calendar",
            "color": "bg-blue-500",
        },
        {
            "title": "Documents",
            "value": "5,432",
            "icon": "file-text",
            "color": "bg-green-500",
        },
        {
            "title": "Billable Hours",
            "value": "452",
            "icon": "clock",
            "color": "bg-purple-500",
        },
    ]
    case_status_data: list[CaseStatusData] = [
        {"name": "Jan", "Active": 40, "Pending": 24, "Closed": 10},
        {"name": "Feb", "Active": 30, "Pending": 13, "Closed": 22},
        {"name": "Mar", "Active": 20, "Pending": 58, "Closed": 19},
        {"name": "Apr", "Active": 27, "Pending": 39, "Closed": 20},
        {"name": "May", "Active": 18, "Pending": 48, "Closed": 28},
        {"name": "Jun", "Active": 23, "Pending": 38, "Closed": 25},
    ]
    upcoming_events: list[UpcomingEvent] = [
        {
            "case_name": "KPLC vs. Omondi",
            "event_type": "Hearing",
            "date": "2024-07-28",
            "time": "10:00 AM",
            "court": "High Court, Milimani",
        },
        {
            "case_name": "Safaricom vs. Chepkoech",
            "event_type": "Mention",
            "date": "2024-07-29",
            "time": "09:30 AM",
            "court": "Magistrate's Court, Kiambu",
        },
        {
            "case_name": "In re Estate of Mwangi",
            "event_type": "Filing Deadline",
            "date": "2024-08-01",
            "time": "05:00 PM",
            "court": "Family Division",
        },
        {
            "case_name": "Republic vs. Wafula",
            "event_type": "Hearing",
            "date": "2024-08-05",
            "time": "02:00 PM",
            "court": "Court of Appeal",
        },
    ]
    recent_activities: list[Activity] = [
        {
            "user": "Jane Kamau",
            "action": "added a document to",
            "details": "KPLC vs. Omondi",
            "timestamp": "2 hours ago",
            "avatar_seed": "Jane",
        },
        {
            "user": "John Otieno",
            "action": "updated status of",
            "details": "Safaricom vs. Chepkoech to 'Pending'",
            "timestamp": "5 hours ago",
            "avatar_seed": "John",
        },
        {
            "user": "Admin",
            "action": "generated a report for",
            "details": "Q2 Billings",
            "timestamp": "1 day ago",
            "avatar_seed": "Admin",
        },
        {
            "user": "Alice Wanjiru",
            "action": "scheduled a new hearing for",
            "details": "In re Estate of Mwangi",
            "timestamp": "2 days ago",
            "avatar_seed": "Alice",
        },
    ]

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open