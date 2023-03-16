# Python Coding Challenges

## Type Casting and Exceptions

### Challenge 1

Write a Python function that takes in a list of strings representing integers and returns the sum of those integers as an integer. If any of the strings in the list cannot be converted to an integer, return None.

Function signature: def sum_strings(numbers: List[str]) -> Optional[int]:

```
Test case 1:

Input: ['1', '2', '3']
Expected output: 6

Test case 2:

Input: ['2', '4', '6', '8']
Expected output: 20

Test case 3:

Input: ['1', '2', '3', 'four']
Expected output: None

Test case 4 (edge case):

Input: ['0', '-1', '123', '456', '789', '1000', '9999']
Expected output: 12366
```

## Challenge 2

Currency Converter

Create a Python program that converts an amount in one currency to another currency. The program should take in the following inputs from the user:
- The amount to be converted (as a float)
- The currency code of the original currency (as a string)
- The currency code of the desired currency (as a string)

The program should then convert the amount from the original currency to the desired currency and print out the result.

The program should be able to handle the following errors:
- If the user inputs an invalid amount (e.g. a non-numeric value or a negative value), the program should print an error message and ask the user to input the amount again.
- If the user inputs an invalid currency code (e.g. a code that is not in the list of supported currencies), the program should print an error message and ask the user to input the currency code again.

The program should support the following currencies:
- USD (US Dollar)
- EUR (Euro)
- JPY (Japanese Yen)
- GBP (British Pound)
- AUD (Australian Dollar)
- CAD (Canadian Dollar)
- CHF (Swiss Franc)
- CNY (Chinese Yuan Renminbi)

The exchange rates for the currencies can be hardcoded into the program. Here are the exchange rates as of the knowledge cutoff date:

```
usd_rates = {"EUR": 0.84, "JPY": 109.19, "GBP": 0.72, "AUD": 1.29, "CAD": 1.25, "CHF": 0.92, "CNY": 6.50}
eur_rates = {"USD": 1.19, "JPY": 128.92, "GBP": 0.86, "AUD": 1.54, "CAD": 1.49, "CHF": 1.10, "CNY": 7.80}
jpy_rates = {"USD": 0.0091, "EUR": 0.0078, "GBP": 0.0067, "AUD": 0.012, "CAD": 0.011, "CHF": 0.0083, "CNY": 0.059}
gbp_rates = {"USD": 1.39, "EUR": 1.16, "JPY": 148.85, "AUD": 1.80, "CAD": 1.74, "CHF": 1.28, "CNY": 9.06}
aud_rates = {"USD": 0.77, "EUR": 0.65, "JPY": 83.65, "GBP": 0.56, "CAD": 0.97, "CHF": 0.72, "CNY": 5.09}
cad_rates = {"USD": 0.80, "EUR": 0.67, "JPY": 86.85, "GBP": 0.57, "AUD": 1.03, "CHF": 0.74, "CNY": 5.27}
chf_rates = {"USD": 1.09, "EUR": 0.91, "JPY": 117.34, "GBP": 0.78, "AUD": 1.39, "CAD": 1.35, "CNY": 7.67}
cny_rates = {"USD": 0.15, "EUR": 0.13, "JPY": 16.85, "GBP": 0.11, "AUD": 0.20, "CAD": 0.19, "CHF": 0.13}
```

Example input/output:

```
Enter amount: 100
Enter original currency code: USD
Enter desired currency code: EUR
Result: 84.0 EUR
```

```
Enter amount: abc
Invalid input. Please enter a valid amount.
Enter amount: -50
Invalid input. Please enter a valid amount.
Enter amount: 50
Enter original currency code: ABC
Invalid currency code. Please enter a valid currency code.
Enter original currency code: USD
Enter desired currency code: XYZ
Invalid currency code. Please enter a valid currency code.
Enter desired currency code: EUR
Result: 42.0 EUR
```