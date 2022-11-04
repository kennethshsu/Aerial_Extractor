import os
import urllib.request

# Source: https://docs.google.com/spreadsheets/d/1bboTohF06r-fafrImTExAPqM9m6h2m2lgJyAkQuYVJI/edit#gid=1684411812
urls_file = "/Users/kennethhsu/Documents/GitHub/Aerial_Extractor/urls_file.txt"
download_dir = "/Users/kennethhsu/Documents/GitHub/Aerial_Extractor/downloads/"

download_count = 0

for url in open(urls_file):
    name = url.rsplit("/", 1)[-1][:-1]
    download_file_path = os.path.join(download_dir, name)
    print("Checking", download_file_path)

    if not os.path.isfile(download_file_path):
        urllib.request.urlretrieve(url.replace("https", "http"), download_file_path)

        download_count = download_count + 1
        print("Downloaded:", download_count)
    else:
        print("Skipping:", name)
