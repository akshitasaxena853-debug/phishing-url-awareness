# Phishing URL Awareness Checker

## 1. Project Overview

The Phishing URL Awareness Checker is a beginner-friendly Python project that examines URL text for common warning signs associated with potentially suspicious links.

It is an educational tool designed to help users become more aware of URL-based risks. It does not determine with certainty whether a URL is safe or malicious.

## 2. Features

The checker identifies six warning signs:

- The URL contains an `@` symbol.
- The URL is longer than 100 characters.
- The hostname resembles an IPv4 address.
- The hostname contains five or more labels.
- The hostname contains the `xn--` punycode marker.
- The URL uses HTTP instead of HTTPS.

Additional features include:

- Inspection of multiple URLs in one session.
- Handling of empty input.
- Basic malformed-URL handling.
- A quit option using `q`.
- A warning when no listed indicators are detected.

## 3. Requirements

- Python 3.10 or higher.
- VS Code or another code editor.
- A terminal to execute the program.

The program uses Python's built-in `re` and `urllib.parse` modules. No additional Python packages are required.

## 4. Project Structure

```text
phishing-url-awareness/
├── phishing_checker.py
├── README.md
├── requirements.txt
├── tests/
│   └── test_samples.md
└── screenshots/
    ├── sample_run.png
    └── test_results.png
```

## 5. How to Run

Open a terminal in the project directory and execute:

```bash
python3 phishing_checker.py
```

Enter a URL when prompted. The checker displays any detected warning signs and then asks for another URL.

Enter `q` to exit.

## 6. Testing

The program was tested using the five sample URLs provided in the project workbook. The expected warning signs were detected in each test.

Additional tests covered empty input, malformed input, and the quit option.

See `tests/test_samples.md` for the test record.

## 7. Limitations

- The checker uses simple rules rather than a comprehensive phishing-detection model.
- A URL without the listed warning signs may still be malicious.
- HTTP usage or a punycode marker alone does not prove malicious intent.
- The program does not visit websites, follow redirects, or check domain reputation.
- Its IPv4-style hostname check is a basic pattern check, not complete IP-address validation.

## 8. Ethical Use

This project is intended for educational awareness and defensive learning. It analyses URL text locally and does not open submitted URLs or send network requests.

## 9. Author

Prepared as an educational cybersecurity project for the EWB internship workbook.
