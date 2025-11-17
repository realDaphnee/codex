from playwright.sync_api import Page  # импорт типа Page — объект вкладки/страницы браузера

def login_as_admin(page: Page):  # отдельная функция: логин как админ
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # открываем страницу логина

    page.locator("input[name='username']").fill("Admin")      # находим поле username по атрибуту name и вводим Admin
    page.locator("input[name='password']").fill("admin123")   # находим поле password и вводим admin123
    page.locator("button[type='submit']").click()             # находим кнопку с type='submit' и кликаем по ней

    page.wait_for_url("**/dashboard/**", timeout=10000)       # ждём, пока URL станет похож на .../dashboard/ (до 10 сек)


def test_dashboard_shows_quick_launch(page: Page):  # сам тест: после логина проверяем блок Quick Launch
    login_as_admin(page)  # переиспользуем общий шаг логина
    
    # создаём локатор: ищем <p> с классами oxd-text и oxd-text--p
    quick_launch = page.locator("p.oxd-text.oxd-text--p").filter(has_text="Quick Launch")  # фильтруем по тексту внутри: должен быть "Quick Launch"

    quick_launch.wait_for(timeout=5000)   # ждём появления этого элемента (до 5 секунд)

    assert quick_launch.is_visible()      # проверяем, что элемент виден на странице

    # Ждём
    page.wait_for_timeout(5000)