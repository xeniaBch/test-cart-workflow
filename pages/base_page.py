from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Base class for all page objects.
    Provides common functionality such as navigation and element waiting.
    """

    def __init__(self, driver):
        """
        Initialize the BasePage with a WebDriver instance.
        :param driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, url):
        """
        Navigate to a specified URL.
        :param url: URL to navigate to
        """
        self.driver.get(url)

    def wait_for_element(self, by, locator):
        """
        Wait for an element to become visible on the page.
        :param by: Locator strategy (e.g., By.ID, By.CSS_SELECTOR)
        :param locator: The locator string
        :return: WebElement once it becomes visible
        """
        return self.wait.until(EC.visibility_of_element_located((by, locator)))