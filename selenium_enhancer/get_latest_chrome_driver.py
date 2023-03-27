"""
This bash command will download the latest Chromedriver for Linux.
This script converts the concept to Python for this module.

LATEST_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && 
wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$LATEST_VERSION/chromedriver_linux64.zip && 
sudo unzip /tmp/chromedriver.zip chromedriver -d .;
"""
import os
import urllib.request
import zipfile


def main():
    version_url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = urllib.request.urlopen(version_url)
    version = response.read().decode('utf-8')
    download_url = (
        'https://chromedriver.storage.googleapis.com/'
        f'{version}/chromedriver_linux64.zip'
    )
    local_zip_file = '/tmp/chromedriver.zip'
    urllib.request.urlretrieve(download_url, local_zip_file)
    try:
        os.mkdir('drivers')
    except FileExistsError:
        pass
    with zipfile.ZipFile(local_zip_file, 'r') as zip_ref:
        zip_ref.extract('chromedriver', 'drivers')


if __name__ == "__main__":
    main()