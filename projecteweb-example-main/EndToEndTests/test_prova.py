import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.locator("body").click()
    page.goto("http://127.0.0.1:8000/")
    page.get_by_role("link", name="Go to available cinemas").click()
    page.get_by_role("button", name="JCA Cinemes alpicat").click()
    page.get_by_role("link", name="Jurassic Park Poster").click()
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("geiadegeiade")
    page.get_by_role("button", name="Log In").click()
    page.get_by_label("Select Showtime:").select_option("20")
    page.get_by_label("Select tickets:").click()
    page.get_by_label("Select tickets:").click(click_count=3)
    page.get_by_label("Select tickets:").fill("2")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm Reservation").click()
    page.get_by_role("link", name="Back", exact=True).click()
    page.get_by_role("link", name="Back").click()
    page.get_by_role("link", name="Go to my reservations").click()
    page.get_by_role("link", name="Edit").nth(1).click()
    page.get_by_label("Num tickets:").click()
    page.get_by_label("Num tickets:").fill("5")
    page.get_by_role("button", name="Save changes").click()
    page.get_by_role("link", name="Delete").first.click()
    page.get_by_role("link", name="Back").click()
