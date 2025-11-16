from playwright.sync_api import Page

def test_login_orangehrm_wrong_password(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("wrongpass")
    page.locator("button[type='submit']").click()

    page.wait_for_timeout(3000)

      # Пока что просто проверяем, что не попали на dashboard
    assert "dashboard" not in page.url.lower()