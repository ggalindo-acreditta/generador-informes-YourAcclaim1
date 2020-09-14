import csv
import requests

num_accept_badges = 0
num_pendin_badges = 0
num_reject_badges = 0

r = requests.get('https://api.youracclaim.com/v1/organizations/b64843be-4a6c-4188-871e-16f0d822d7b8/high_volume_issued_badge_search', auth=('iYLBMep7N13lFmisbGNHvfesk5ibNKgNxqxT', ''))

status_code = r.status_code
resp_json = r.json()

data1 = resp_json["data"]
longitud_resp_data1 = len(data1)

for i in range(0,longitud_resp_data1):
    badge1 = data1[i]
    if badge1["state"] == "accepted":
        num_accept_badges += 1
    if badge1["state"] == "pending":
        num_pendin_badges += 1
    if badge1["state"] == "pending":
        num_reject_badges += 1
    
