import re
from playwright.sync_api import Page, expect


def test_3deleteOneReservation(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/")
    page.get_by_role("link", name="Go to available cinemas").click()
    page.get_by_role("button", name="Espai Funàtic").click()
    page.get_by_role("link", name="The Fate of the Furious").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("geiade")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("geiadegeiade")
    page.get_by_role("button", name="Log In").click()
    page.get_by_label("Select Showtime:").click()
    page.get_by_label("Select Showtime:").select_option("18:00")
    page.get_by_label("Select tickets:").click()
    page.get_by_label("Select tickets:").fill("2")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm Reservation").click()
    page.get_by_role("link", name="Back", exact=True).click()
    page.get_by_role("link", name="Back").click()
    page.get_by_role("link", name="Go to my reservations").click()
    page.get_by_role("link", name="Delete").nth(4).click()
    page.get_by_role("link", name="Log Out").click()
