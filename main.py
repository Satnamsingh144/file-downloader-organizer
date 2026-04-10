import requests
import os
from urllib.parse import urlparse

def download_file(url, folder="downloads"):
    try:
        os.makedirs(folder, exist_ok=True)

        file_name = url.split("/")[-1] or "file"
        local_path = os.path.join(folder, file_name)

        response = requests.get(url)
        response.raise_for_status()

        with open(local_path, "wb") as f:
            f.write(response.content)

        print(f"✅ Downloaded: {file_name}")

    except Exception as e:
        print(f"❌ Failed to download {url} | Error: {e}")


def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in ["http", "https"] and parsed.netloc != ""


def main():
    urls = input("Enterr URLs (comma separated): ").split(",")

    valid_urls = []
    invalid_urls = []

    for url in urls:
        url = url.strip()

        if not is_valid_url(url):
            invalid_urls.append(url)
            continue

        valid_urls.append(url)
        download_file(url)

    print("\nInvalid URLs:")
    for bad_url in invalid_urls:
        print(f"❌ {bad_url}")

    print(f"\nValid: {len(valid_urls)} | Invalid: {len(invalid_urls)}")


if __name__ == "__main__":
    main()