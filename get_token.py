
import requests
import json


def main():
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=V9g5iyFNUspWQHypfyC2hQER&client_secret=kzKXqtwDkoQwvIFRHfzyYCaBlxc801Vz"
    
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.json())
    

if __name__ == '__main__':
    main()
