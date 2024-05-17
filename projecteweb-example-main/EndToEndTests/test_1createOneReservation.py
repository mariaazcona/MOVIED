import re
from playwright.sync_api import Page, expect


def test_1createOneReservation(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/")
    page.get_by_role("link", name="Go to available cinemas").click()
    page.get_by_role("button", name="JCA Cinemes alpicat").click()
    page.get_by_role("link", name="Jurassic Park").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("geiade")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("geiadegeiade")
    page.get_by_role("button", name="Log In").click()
    page.get_by_label("Select Showtime:").click()
    page.get_by_label("Select Showtime:").select_option("18:00")
    page.get_by_label("Select tickets:").click()
    page.get_by_label("Select tickets:").fill("3")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm Reservation").click()
    page.get_by_role("link", name="Log Out").click()