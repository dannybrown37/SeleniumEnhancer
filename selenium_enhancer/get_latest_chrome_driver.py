"""
This bash command will download the latest Chromedriver for Linux.
This script converts the concept to Python for this module.

LATEST_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && 
wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$LATEST_VERSION/chromedriver_linux64.zip && 
sudo unzip /tmp/chromedriver.zip chromedriver -d .;
"""
import platform
import urllib.request
import zipfile
from pathlib import Path


def main():
    is_windows = platform.system() == 'Windows'
    system_type = 'win32' if is_windows else 'linux64'

    version_url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = urllib.request.urlopen(version_url)
    version = response.read().decode('utf-8')
    download_url = (
        'https://chromedriver.storage.googleapis.com/'
        f'{version}/chromedriver_{system_type}.zip'
    )
    print("Downloading:", download_url)
    local_zip_file = ('C:\\Temp\\' if is_windows else '/tmp/') 
    local_zip_file += 'chromedriver.zip'
    if is_windows:
        temp_path = Path('C:/Temp')
        temp_path.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(download_url, local_zip_file)
    drivers_path = Path('selenium_enhancer/drivers')
    drivers_path.mkdir(exist_ok=True)
    with zipfile.ZipFile(local_zip_file, 'r') as zip_ref:
        driver_name = 'chromedriver.exe' if is_windows else 'chromedriver'
        zip_ref.extract(driver_name, drivers_path)


if __name__ == "__main__":
    main()