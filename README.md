README.md - Test Automation Framework

Test Automation Framework for Cart Functionality

This project implements automated tests for an e-commerce website using Selenium and the Python unittest framework. The primary test covers the workflow of adding an item to the cart, updating its quantity, and verifying the total price.

Design Patterns Used

Page Object Model (POM)

The framework follows the Page Object Model (POM) design pattern, which separates page-specific functionality from test logic. Each web page is represented by a corresponding class, encapsulating locators and actions.

Why POM?

	•	Maintainability: Changes in the UI (e.g., locators or element structures) are confined to page classes, making the tests easier to maintain.
	•	Readability: Test scripts focus on business logic, improving clarity.
	•	Reusability: Common page operations are reusable across multiple tests.

Test Workflow

	1.	Navigate to the shop page:
	•	Verify the shop title is displayed correctly.
	2.	Check cart status:
	•	Ensure the cart is initially empty.
	3.	Add an item to the cart:
	•	Add “Album” to the cart using the “Add to cart” button.
	4.	Navigate to the cart page:
	•	Click “View cart” to proceed to the cart page.
	5.	Update item quantity:
	•	Change the item quantity to 2 and click “Update Cart.”
	6.	Verify total price:
	•	Assert that the total price matches the expected value (30,00 €).

Code Overview

Page Classes

BasePage

The BasePage class serves as a parent for all page classes, providing utility methods such as:
	•	navigate_to(url): Opens a specified URL.
	•	wait_for_element(by, locator): Waits for an element to become visible.

ShopPage

Handles operations specific to the shop page:
	•	Verifies the shop title.
	•	Adds an item to the cart.
	•	Checks whether the cart is empty.

CartPage

Handles operations on the cart page:
	•	Updates the quantity of items.
	•	Waits for the total price to update.
	•	Verifies the total price.

Potential Challenges

1. Dynamic Elements

	•	Issue: Elements like total price or cart quantity may update asynchronously, leading to stale element errors.
	•	Solution: The framework uses explicit waits (WebDriverWait) to ensure elements are ready for interaction before proceeding.

2. Browser-Specific Behavior

	•	Issue: Different browsers may handle DOM updates at varying speeds.
	•	Solution: Tests are designed with sufficient timeout values and use generic selectors compatible across browsers.

3. Hardcoded Values

	•	Issue: The test workflow assumes fixed prices and items (e.g., 30,00 € for two items).
	•	Solution: For scalability, consider fetching dynamic data from the application or using parameterized tests.

Installation and Execution

Prerequisites

	1.	Python 3.9 or higher
	2.	Selenium WebDriver (compatible with your browser, e.g., ChromeDriver)
	3.	Required Python packages (install via requirements.txt):

pip install -r requirements.txt



Running Tests

Run the following command in the project root directory:

python -m unittest tests/test_cart_functionality.py

Future Improvements

	1.	Dynamic Data Handling:
	•	Use an external configuration (e.g., JSON) for test data like product IDs and expected prices.
	2.	Cross-Browser Testing:
	•	Integrate with tools like Selenium Grid or BrowserStack for testing on multiple browsers and platforms.
	3.	Scalability:
	•	Extend the framework with additional tests for other workflows (e.g., checkout, user registration).

Conclusion

The Page Object Model ensures that the framework is maintainable, readable, and reusable. Despite challenges with dynamic elements and hardcoded values, this approach provides a solid foundation for scalable test automation.