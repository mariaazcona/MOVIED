import re
from playwright.sync_api import Page, expect


def test_login(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/")
    page.get_by_role("link", name="Log In").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("geiade")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("geiadegeiade")
    page.get_by_role("button", name="Log In").click()
