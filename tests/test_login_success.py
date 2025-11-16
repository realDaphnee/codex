from playwright.sync_api import Page

def test_login_orangehrm_success(page: Page):
    # 1. Открыть страницу логина
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # 2. Ввести логин и пароль
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")

    # 3. Нажать кнопку логина
    page.locator("button[type='submit']").click()

    # Ждём, пока URL станет похож на /dashboard/
    page.wait_for_url("**/dashboard/**", timeout=10000)

    assert "dashboard" in page.url.lower()