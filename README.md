# Amazon PrimeNow Slot Checker

## How It Works
    - Logs user in
    - Navigates to checkout
    - Goes back and forth until a slot is found
    - An annoying noise is made to notify user
    - IMPORTANT: When a slot is found you will need to click the slot and the pay button yourself

## Setup
`Install Chromedriver` https://chromedriver.chromium.org/ 

### Have the following noted down:
    - ChromeDriver file path
    - A ready-to-go Amazon PrimeNow Basket
    - Username/Password
    - Postcode

## Running Script
`pip3 install selenium`

### Slot Checker
`python3 amazon-slot-checker.py <ChromeDriver-FilePath> <Postcode> <Username> <Password>`
#### Example
`python3 amazon-slot-checker.py /Applications/chromedriver n412b myself@email.com mySecurePassword`

### Item Checker
`python3 ItemChecker/amazon-item-checker.py <ChromeDriver-FilePath> <Username> <Password> <Item-Url>`
#### Example
`python3 ItemChecker/amazon-item-checker.py /Applications/chromedriver myself@email.com mySecurePassword https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/`
