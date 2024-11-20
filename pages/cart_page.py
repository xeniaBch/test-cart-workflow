from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class CartPage(BasePage):
    """
    Page object class for the cart page.
    Encapsulates locators and actions specific to the cart page.
    """

    # Locators
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input.input-text.qty.text")
    UPDATE_CART_BUTTON = (By.NAME, "update_cart")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".order-total > td")

    def set_item_quantity_and_update(self, quantity):
        """
        Update the quantity of an item in the cart and refresh the cart total.
        :param quantity: The new quantity to set
        """
        # Update the item quantity
        input_field = self.wait_for_element(*self.QUANTITY_INPUT)
        input_field.click()
        input_field.clear()
        input_field.send_keys(quantity)

        # Click the "Update Cart" button
        update_button = self.wait_for_element(*self.UPDATE_CART_BUTTON)
        old_total_price = self.wait_for_element(*self.TOTAL_PRICE).text.strip()
        update_button.click()

        # Wait for the total price to update
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*self.TOTAL_PRICE).text.strip() != old_total_price,
            message="The total price did not update."
        )

    def verify_total_price(self, expected_price):
        """
        Verify that the total price matches the expected value.
        :param expected_price: The expected total price
        """
        total_price = self.wait_for_element(*self.TOTAL_PRICE).text.strip()
        assert total_price == expected_price, f"Expected total price to be '{expected_price}', but got '{total_price}'"