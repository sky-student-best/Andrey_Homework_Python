import allure

from calculator_page import CalculatorPage


@allure.title("Калькулятор считает 7 + 8 при задержке 45 секунд")
@allure.description(
    "Открываем калькулятор, выставляем задержку вычислений 45 секунд, "
    "складываем 7 и 8 и проверяем, что в поле результата появляется 15."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.BLOCKER)
def test_calculator_with_page_object(chrome_driver):
    """Проверка сложения на калькуляторе с медленным откликом."""
    page = CalculatorPage(chrome_driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку вычислений 45 секунд"):
        page.set_delay("45")

    with allure.step("Ввести выражение 7 + 8 и нажать равно"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Проверить, что результат равен 15"):
        result = page.get_result_text()
        assert result == "15", (
            f"Ожидался результат 15, но было: {result}"
        )
