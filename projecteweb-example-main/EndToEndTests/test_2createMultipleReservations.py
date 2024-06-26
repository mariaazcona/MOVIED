import re
from playwright.sync_api import Page, expect


def test_2createMultipleReservations(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/")
    page.get_by_role("link", name="Go to available cinemas").click()
    page.get_by_role("button", name="Cinemes Lauren").click()
    page.get_by_role("link", name="Ferris Bueller's Day Off").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("geiade")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("geiadegeiade")
    page.get_by_role("button", name="Log In").click()
    page.get_by_label("Select Showtime:").click()
    page.get_by_label("Select Showtime:").select_option("20:00")
    page.get_by_label("Select tickets:").click()
    page.get_by_label("Select tickets:").fill("2")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm Reservation").click()
    page.get_by_role("link", name="The Matrix").click()
    page.get_by_label("Select Showtime:").click()
    page.get_by_label("Select Showtime:").select_option("20:00")
    page.get_by_label("Select tickets:").click()
    page.get_by_label("Select tickets:").fill("6")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm Reservation").click()
    page.get_by_role("link", name="Ocean's Eleven").click()
    page.get_by_label("Select Showtime:").click()
    page.get_by_label("Select Showtime:").select_option("22:00")
    page.get_by_label("Select tickets:").click()
    page.get_by_label("Select tickets:").fill("1")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm Reservation").click()
    page.get_by_role("link", name="Log Out").click()
