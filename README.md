# 487 Nigerian Bank Codes 🇳🇬

This project provides a comprehensive and structured list of bank codes in Nigeria, including commercial banks, microfinance banks, merchant banks, and payment service providers. The data is organized in a developer-friendly JSON format, making it easy to integrate into applications that require bank code validation, dropdowns, or lookups.

## Use Case

Developers can use this repository as a reliable source for Nigerian bank codes when building financial, fintech, or payment-related solutions.

## Contents

- `bank_codes.json`: Contains the full list of Nigerian bank codes with their corresponding bank names and labels.

```json
{
    "<institution_code>": {
        "bank_name": "<bank_name>",
        "label": "<label>"
    }
}
```

`<institution_code>`: The institution code of the bank. This is a unique identifier for each bank. Assigned by NIBSS. Identifies the bank as a whole. Used in APIs, BVN, eNaira, NIBSS, Paystack/Flutterwave, CBN reporting.

`<bank_name>`: The name of the bank.
`<label>`: The label of the bank, useful in case you want the bank name as an identifier say in an enum or something


## How to Use

Simply import or reference the `bank_codes.json` file in your project to access up-to-date Nigerian bank codes in a structured format.

## Contribution

Feel free to contribute by submitting pull requests for updates or corrections to the bank codes.

eg. adding bank logos
```json
{
    "<institution_code>": {
        "bank_name": "<bank_name>",
        "label": "<label>",
        "logo": "<logo_uri>"
    }
}
```
