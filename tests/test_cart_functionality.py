import unittest
from selenium import webdriver
from pages.shop_page import ShopPage
from pages.cart_page import CartPage


class TestCartFunctionality(unittest.TestCase):
    """
    Test suite for verifying cart functionality in an e-commerce shop.
    Covers the workflow of adding an item to the cart, updating quantity, and checking the total price.
    """

    def setUp(self):
        """
        Setup method to initialize the WebDriver and browser configuration.
        Runs before each test.
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://autoprojekt.simplytest.de/"

    def tearDown(self):
        """
        Teardown method to quit the WebDriver after each test.
        Runs after each test.
        """
        self.driver.quit()

    def test_cart_workflow(self):
        """
        Test case for the complete cart workflow:
        1. Navigate to the shop page.
        2. Verify the page title.
        3. Check if the cart is initially empty.
        4. Add the "Album" item to the cart.
        5. Navigate to the cart page.
        6. Update the item quantity to 2.
        7. Verify that the total price matches the expected value.
        """
        # Initialize page objects
        shop_page = ShopPage(self.driver)
        cart_page = CartPage(self.driver)

        # Step 1: Open the shop page
        shop_page.navigate_to(self.base_url)

        # Step 2: Verify the shop title
        shop_page.verify_shop_title()

        # Step 3: Verify the cart is initially empty
        shop_page.verify_cart_is_empty()

        # Step 4: Add "Album" to the cart
        shop_page.add_album_to_cart()

        # Step 5: Navigate to the cart page
        shop_page.click_view_cart()

        # Step 6: Update the item quantity to 2
        cart_page.set_item_quantity_and_update("2")

        # Step 7: Verify the total price
        cart_page.verify_total_price("30,00 €")


if __name__ == "__main__":
    unittest.main()