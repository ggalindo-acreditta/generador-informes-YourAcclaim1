import csv
import requests

num_accept_badges = 0
num_pendin_badges = 0
num_reject_badges = 0
next_page = True
req_url = 'https://api.youracclaim.com/v1/organizations/b64843be-4a6c-4188-871e-16f0d822d7b8/high_volume_issued_badge_search'
acclaim_token = 'iYLBMep7N13lFmisbGNHvfesk5ibNKgNxqxT'

print(" Conectando con la organización")

while next_page:
    r = requests.get(req_url, auth=(acclaim_token, ''))

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
        if badge1["state"] == "rejected":
            num_reject_badges += 1

    metada1 = resp_json["metadata"]
    if metada1["next_page_url"] is None:
        next_page = False
    else:
        req_url = metada1["next_page_url"]


print("Se calculó el informe de Unirversidad Rosario")
    
