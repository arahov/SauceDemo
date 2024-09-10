
# Swag Labs Automatin tests using Python-pytest Selenium

Testing Swag Labs demo website for trainging perposes 



## Dependencies

1- Make sure python is installed in your system 
2- nstall Selenium webdrive

```bash
  pip install selenium
```
3- install pytest

```bash
  pip install pytest
```
4- install -html report
```bash
 pip install pytest-html
```
5- install allure
```bash
brew install allure
```
```bash
pip install allure-pytest
```

Run Tests with Allure Reporting Enabled
```bash
pytest --alluredir=allure-results
```

to generate allure report html after running your tests
```bash
    Allure serve AllureReport
```

## Installation Dependencies and Test Execution

## Dependencies

1- Make sure python is installed in your system 
2- nstall Selenium webdrive

```bash
  pip install selenium
```
3- install pytest

```bash
  pip install pytest
```
4- install -html report
```bash
 pip install pytest-html
```
5- install allure
```bash
brew install allure
```
```bash
pip install allure-pytest
```

Run Tests with Allure Reporting Enabled
```bash
pytest --alluredir=AllureReport
```

to generate allure report html after running your tests
```bash
Allure serve AllureReport
```

## Running the test 
```bash
project folder path pytest
```
to run specific test example
```bash
pytest tests/test_checkout_overview.py
pytest tests/test_checkout_overview.py:test_checkout_overview
```

# Test Cases

## Login_test

### test_valid_credentials
- Navigate  to https://www.saucedemo.com
- Enter correct credentials and press login button
- Verify user is directed to inventory (products) page
### test_invalid_credentials
- Navigate  to https://www.saucedemo.com
- Enter invalid credentials
- Assert error message
### test_no_username
- Navigate  to https://www.saucedemo.com
- Enter only password
- Assert error message
### test_no_password
- Navigate  to https://www.saucedemo.com
- Enter only username
- Assert error message

## inventory_test
### Test_inventory_add_items_to_cart
- Navigate  to https://www.saucedemo.com
- Enter correct credentials and press login button
- Verify user is directed to inventory (products) page
- Filter by lower to higher
- add the lowes 2 items to the cart
- Assert number of items are 2 
- Click on your cart
- Assert page navigates to your cart page
### Test_inventory_add_remove_items_cart
- Navigate  to https://www.saucedemo.com
- Enter correct credentials and press login button
- Verify user is directed to inventory (products) page
- Filter by lower to higher
- add the lowes 2 items to the cart
- Remove 1 item from cart
- Assert number of items in cart should be 1

## Test_cart
### test_checkout
- Navigate  to https://www.saucedemo.com
- Enter correct credentials and press login button
- Verify user is directed to inventory (products) page
- Filter by lower to higher
- add the lowes 2 items to the cart
- click on the cart button
- Click on checkout button 
- Assert page redirects to “your Information” page
	

### Test_continue_shopping
- Navigate  to https://www.saucedemo.com
- Enter correct credentials and press login button
- Verify user is directed to inventory (products) page
- Filter by lower to higher
- add the lowes 2 items to the cart
- click on the cart button
- Click back to shopping button
- Assert page is navigated to “products” 

## test_checkout_informaiton
### test_your_valid_information
- fill checkout-information (name, Lastname, postal-code)
- click continue 
- assert page should navigate to "checkout Overview" page

### test_your_information_empty
- leave all field empty 
- click on continue button
- assert error message "name is missing" 

### test_your_information_no_lastname
- leave last name field empty
- click in continue 
- assert error message "no last name "

### test_your_information_no_postalcode
- leave postal_code field empty 
- click continue
- assert error message "no postal code "

## Test_checkout_overview
### test_checkout_information_overview
- verify card ID SauceCard #31337
- verify delivery address = Free Pony Express Delivery!
- verify Total items price = sum of item prices in the cart
- verify total price with tax = total items price * 1.08
- click finish button 
- assert page redirects to complete page

## test_checkout_complete
### test_go_back_home
- click on finish
- verify page redirects to Homepage 



