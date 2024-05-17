import re
from playwright.sync_api import Page, expect


def test_signup(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/")
    page.get_by_role("link", name="Sign Up").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("Testsignup2")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("Ronaldogordo_123")
    page.get_by_label("Password confirmation:").click()
    page.get_by_label("Password confirmation:").fill("Ronaldogordo_123")
    page.get_by_role("button", name="Sign Up").click()
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("Testsignup2")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("Ronaldogordo_123")
    page.get_by_role("link", name="Log In").click()
