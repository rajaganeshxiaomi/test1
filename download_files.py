

import requests


url1 = 'https://raw.githubusercontent.com/rajaganeshxiaomi/test1/main/customer_data.csv'
url2 = 'https://raw.githubusercontent.com/rajaganeshxiaomi/test1/main/booking_data.csv'
url3 = 'https://raw.githubusercontent.com/rajaganeshxiaomi/test1/main/destination_data.csv'

filename1 = 'customer_data.csv'
filename2 = 'booking_data.csv'
filename3 = 'destination_data.csv'


def download_csv(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename} successfully.")
        else:
            print(f"Failed to download {filename}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading {filename}: {str(e)}")

download_csv(url1, filename1)
download_csv(url2, filename2)
download_csv(url3, filename3)







