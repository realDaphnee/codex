from playwright.sync_api import Page

def test_login_wrong_password(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # ВЕРНЫЙ логин, НЕВЕРНЫЙ пароль
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("wrongpass")
    page.locator("button[type='submit']").click()

    # Ждём появления сообщения об ошибке
    error_message = page.locator("p.oxd-text.oxd-text--p.oxd-alert-content-text")
    error_message.wait_for(timeout=5000)

    # Проверяем текст
    text = error_message.inner_text()
    assert "Invalid credentials" in text
    page.wait_for_timeout(5000)