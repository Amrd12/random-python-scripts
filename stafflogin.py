import requests
import time
import argparse

url = r"http://10.18.15.254:8002/index.php?zone=staff"

def login(number):
    url = "http://10.18.15.254:8002/index.php?zone=staff"
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://10.18.15.254:8002',
        'Referer': 'http://10.18.15.254:8002/index.php?zone=staff&redirurl=http%3A%2F%2Fedge-http.microsoft.com%2Fcaptiveportal%2Fgenerate_204',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }

    data = {
        'auth_user': f'enguccd{number}',  # Ensure the username format is correct
        'auth_pass': 'asd@2021',
        'redirurl': 'http://edge-http.microsoft.com/captiveportal/generate_204',
        'zone': 'staff',
        'accept': 'Login'
    }

    try:
        response = requests.post(url, headers=headers, data=data, verify=False)
        print(f"Login response status: {response.status_code}")
        if response.status_code == 200:
            print("Login successful!")
        else:
            print(f"Login failed with status code: {response.status_code}")
            print("Response text:", response.text)  # Print response content for more debugging info
    except requests.RequestException as e:
        print(f"An error occurred during login: {e}")

def check():
    try:
        req = requests.get(url, verify=False)
        if req.status_code == 200:
            return req.text.startswith("You are connected")
        else:
            print(f"Check failed with status code: {req.status_code}")
            return False
    except requests.RequestException as e:
        print(f"An error occurred during check: {e}")
        return False

def main(number , sec):
    while True:
        if not check():
            print("Not connected. Attempting to login...")
            login(number)
            continue
        else:
            print("Already connected.")
        # Sleep for ~1 hour before checking again
        time.sleep(sec)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Login Script")
    parser.add_argument('--n', required=True, help="user name number")
    parser.add_argument('--s', required=False, help="sec between 2 checks", default= 3)
    args = parser.parse_args()
    main(args.n , args.s)
