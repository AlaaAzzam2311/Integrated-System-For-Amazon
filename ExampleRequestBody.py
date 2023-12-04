import requests
url = "http://app.bosta.co/api/v2/deliveries"
payload = {
    "type": 25,
    "specs": {
        "packageType": "Parcel",
        "size": "LARGE",
        "packageDetails": {"itemsCount": 5, "description": "Description"},
    },
    "notes": "Start Note",
    "cod": 250,
    "dropOffAddress": {
        "city": "Giza",
        "zoneId": "123abc",
        "districtId": "zoJP71_5Ca1",
        "firstLine": "Haram st",
        "secondLine": "Abuzed Market",
        "buildingNumber": "2",
        "floor": "3",
        "apartment": "9",
    },
    "pickupAddress": {
        "city": "Giza",
        "zoneId": "123abc",
        "districtId": "zoJP71_5Ca1",
        "firstLine": "Haram st",
        "secondLine": "Abuzed Market",
        "buildingNumber": "2",
        "floor": "3",
        "apartment": "9",
    },
    "returnAddress": {
        "city": "Giza",
        "zoneId": "123abc",
        "districtId": "zoJP71_5Ca1",
        "firstLine": "Haram st",
        "secondLine": "Abuzed Market",
        "buildingNumber": "2",
        "floor": "3",
        "apartment": "9",
    },
    "businessReference": "2468157",
    "receiver": {
        "firstName": "Alaa",
        "lastName": "Ahmed",
        "phone": "01234567891",
        "email": "alaaahmed@gmail.com",
    },
    "webhookUrl": "https://www.amazon.eg/",
}
headers = {"Content-Type": "application/json", "Authorization": "Bearer API Key"}
response = requests.request("POST", url, json=payload, headers=headers)
print(response.text)