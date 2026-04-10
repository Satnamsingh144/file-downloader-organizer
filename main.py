import requests
import os
from urllib.parse import urlparse
import threading

def download_file(url, folder="downloads"):
    try:
        os.makedirs(folder, exist_ok=True)

        file_name = url.split("/")[-1] or "file"
        local_path = os.path.join(folder, file_name)
        i=1
        name,ext = os.path.splitext(file_name)
        while os.path.exists(local_path):
            file_name=f"{name}({i}){ext}"
            local_path=os.path.join(folder,file_name)
            i +=1
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
    urls = input("Enter URLs (comma separated): ").split(",")
    
    valid_urls = []
    invalid_urls = []
    threads=[]
    for url in urls:
        url = url.strip()

        if not is_valid_url(url):
            invalid_urls.append(url)
            continue
        
        valid_urls.append(url)
        t=threading.Thread(target=download_file,args=(url,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()    

    print("\nInvalid URLs:")
    for bad_url in invalid_urls:
        print(f"❌ {bad_url}")

    print(f"\nValid: {len(valid_urls)} | Invalid: {len(invalid_urls)}")


if __name__ == "__main__":
    main()