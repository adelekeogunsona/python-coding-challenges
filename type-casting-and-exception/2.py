#!/usr/bin/python3

# Rates
usd_rates = {
    "EUR": 0.84,
    "JPY": 109.19,
    "GBP": 0.72,
    "AUD": 1.29,
    "CAD": 1.25,
    "CHF": 0.92,
    "CNY": 6.50
}

eur_rates = {
    "USD": 1.19,
    "JPY": 128.92,
    "GBP": 0.86,
    "AUD": 1.54,
    "CAD": 1.49,
    "CHF": 1.10,
    "CNY": 7.80
}

jpy_rates = {
    "USD": 0.0091,
    "EUR": 0.0078,
    "GBP": 0.0067,
    "AUD": 0.012,
    "CAD": 0.011,
    "CHF": 0.0083,
    "CNY": 0.059
}

gbp_rates = {
    "USD": 1.39,
    "EUR": 1.16,
    "JPY": 148.85,
    "AUD": 1.80,
    "CAD": 1.74,
    "CHF": 1.28,
    "CNY": 9.06
}

aud_rates = {
    "USD": 0.77,
    "EUR": 0.65,
    "JPY": 83.65,
    "GBP": 0.56,
    "CAD": 0.97,
    "CHF": 0.72,
    "CNY": 5.09
}

cad_rates = {
    "USD": 0.80,
    "EUR": 0.67,
    "JPY": 86.85,
    "GBP": 0.57,
    "AUD": 1.03,
    "CHF": 0.74,
    "CNY": 5.27
}

chf_rates = {
    "USD": 1.09,
    "EUR": 0.91,
    "JPY": 117.34,
    "GBP": 0.78,
    "AUD": 1.39,
    "CAD": 1.35,
    "CNY": 7.67
}

cny_rates = {
    "USD": 0.15,
    "EUR": 0.13,
    "JPY": 16.85,
    "GBP": 0.11,
    "AUD": 0.20,
    "CAD": 0.19,
    "CHF": 0.13
}

# Accepted Currencies
currencies = {
    'USD': 'usd_rates',
    'EUR': 'eur_rates',
    'JPY': 'jpy_rates',
    'GBP': 'gbp_rates',
    'AUD': 'aud_rates',
    'CAD': 'cad_rates',
    'CHF': 'chf_rates',
    'CNY': 'cny_rates'
}

# Getting correct input
while True:
    try:
        amount = float(input("Enter amount: "))
        if amount >= 0:
            break
        else:
            print("Invalid input. Please enter a valid amount.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

while True:
    try:
        original_cur = str(input("Enter original currency code: "))
        if original_cur in currencies:
            break
        else:
            print("Invalid currency code. Please enter a valid currency code")
    except ValueError:
        print("Invalid currency code. Please enter a valid currency code")

while True:
    try:
        desired_cur = str(input("Enter desired currency code: "))
        if desired_cur in currencies:
            break
        else:
            print("Invalid currency code. Please enter a valid currency code")
    except ValueError:
        print("Invalid currency code. Please enter a valid currency code")

target = globals()[currencies[original_cur]]
rate = target[desired_cur]
result = amount * rate

print("Result: {:0.2f} {}".format(result, desired_cur))
