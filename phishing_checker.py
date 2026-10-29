
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    raw_url = raw_url.strip()

    if not raw_url:
        return ["No URL was entered."]

    # Add a scheme if the user did not provide one.
    if "://" not in raw_url:
        raw_url = "http://" + raw_url

    try:
        parsed = urlparse(raw_url)
        hostname = parsed.hostname or ""
    except ValueError:
        return ["Malformed URL. Please check the input."]

    warnings = []

    # Check 1: @ symbol
    if "@" in raw_url:
        warnings.append("URL contains an @ symbol.")

    # Check 2: URL length
    if len(raw_url) > 100:
        warnings.append("URL is longer than 100 characters.")

    # Check 3: IP-address-style hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", hostname):
        warnings.append("Hostname looks like an IPv4 address.")

    # Check 4: Five or more hostname labels
    if len(hostname.split(".")) >= 5:
        warnings.append("Hostname has five or more labels.")

    # Check 5: Punycode marker
    if "xn--" in hostname.lower():
        warnings.append("Hostname contains a punycode marker.")

    # Check 6: HTTP instead of HTTPS
    if parsed.scheme.lower() == "http":
        warnings.append("URL uses HTTP instead of HTTPS.")

    return warnings


def main():
    print("=== Phishing URL Awareness Checker ===")
    print("Warnings are indicators, not proof of malicious activity.")

    while True:
        raw_url = input(
            "\nEnter a URL to inspect (or q to quit): "
        )

        if raw_url.strip().lower() == "q":
            print("Exiting the checker. Goodbye!")
            break

        warnings = inspect_url(raw_url)

        if not warnings:
            print("\nNo listed warning signs detected.")
            print("This does not guarantee that the URL is safe.")

        elif warnings == ["No URL was entered."]:
            print(warnings[0])

        else:
            print("\nWarning signs detected:")
            for warning in warnings:
                print("- " + warning)


if __name__ == "__main__":
    main()
