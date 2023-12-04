import requests
import json

#headers
headers = {"Content-Type": "application/json", "Authorization": "Bearer"}
#data
first_name = "yourFirstName"
last_name = "yourLastName"
email = "email@example.com"
password = "Your Password"
phone = "yourPhoneNumber"
country_ID = "60e4482c7cb7d4bc4849c4d5"
business_ID = "businessid"

def verify_phone_number():
    OTP = input("Enter OTP that was sent to the above phone: ")
    url = "https://app.bosta.co/api/v2/users/business-admin/phone/confirm"
    payload = {"phone": phone, "token": OTP}
    request = requests.post(url, json=payload, headers=headers)
    response = request.json()
    if response["success"] == True:
        print("Your phone number is verified successfully")
    else:
        print("Your phone number verification failed")
        print(response["message"])
def create_account():
    url = "https://app.bosta.co/api/v2/users/business/admin"
    payload = (
        {
            "email": email,
            "password": password,
            "profile": {
                "firstName": first_name,
                "lastName": last_name,
                "phone": phone,
            },
            "heardAboutUsFrom": "Facebook",
            "monthlyShipmentVolume": "LITE",
            "countryId": country_ID,
        },
    )
    request = requests.post(
        url,
        json=payload,
        headers=headers,
    )
    response = request.json()
    if response["success"] == True:
        print("Registered Successfully")
        verify_phone_number()
    else:
        print("Registration Failed")
        print(response["message"])
def get_authorization_token():
    url = "https://app.bosta.co/api/v2/users/login"
    payload = {
        "email": email,
        "password": password,
    }
    request = requests.post(
        url, json=payload, headers=headers
    )
    response = request.json()
    if response["success"] == True:
        print("Authorization Is Done Successfully")
        return response["data"]
    else:
        print("Authorization Failed")
        print(response["message"])
def business_details():
    url = "https://app.bosta.co/api/v2/businesses"
    payload = {
        "name": "yourBusinessName",
        "salesChannel": "FACEBOOK_SELLER",
        "website": "yourStoreURL",
        "industry": "Electronics",
        "interestedInServices": ["Products Shipments"],
        "business_ID": "business id"
    }
    request = requests.post(url, json=payload, headers=headers)
    response = request.json()
    if response["success"] == True:
        print("Business Info Is Set Successfully")
        return response["data"]["_id"]
    else:
        print("Business Info Setting Failed")
        print(response["message"])
        return business_ID
def list_district():
    url = (
        "https://app.bosta.co/api/v2/cities/getAllDistricts?country_ID=" + country_ID + "&context=pickup"
    )
    request = requests.get(url, headers=headers)
    response = request.json()
    if response["success"] == True:
        print("Districts Are Retrieved Successfully")
        return response["data"][0]["_id"]
    else:
        print("Districts Retrieval Failed")
        print(response["message"])
def pickup_location():
    url = "https://app.bosta.co/api/v2/businesses/ " + business_id_retrieve
    district_ID = "zoJP71_5Ca1"
    payload = {
        "pickupAddress": [
            {
                "locationName": "yourLocationName",
                "districtId": district_ID,
                "firstLine": "Your address first line details",
                "buildingNumber": "1",
                "floor": "2",
                "apartment": "3",
                "secondLine": "Your address second line details like: landmarks",
            }
        ]
    }
    request = requests.put(url, json=payload, headers=headers)
    response = request.json()
    if response["success"] == True:
        print("Pickup Location Is Set Successfully")
    else:
        print("Pickup Location Setting Failed")
        print(response["message"])
def first_delivery():
    url = "http://app.bosta.co/api/v2/deliveries"
    payload = {
        "type": 25,
        "specs": {
            "packageType": "Parcel",
            "size": "LARGE",
            "packageDetails": {"itemsCount": 5, "description": "Description"},
        },
        "notes": "If you want to add anything",
        "cod": 250,
        "dropOffAddress": {
            "city": "Giza",
            "zone_ID": "zoneid",
            "district_ID": "zoJP71_5Ca1",
            "firstLine": "Haram st",
            "secondLine": "Arish st",
            "buildingNumber": "2",
            "floor": "3",
            "apartment": "9",
        },
        "pickupAddress": {
            "city": "Cairo",
            "zoneId": "zone",
            "districtId": "zoJP71_5Ca1",
            "firstLine": "fesal st",
            "secondLine": "opposite to carrefour",
            "buildingNumber": "5",
            "floor": "3",
            "apartment": "7",
        },
        "returnAddress": {
            "city": "cairo",
            "zoneId": "zone123",
            "districtId": "zoJP71_5Ca1",
            "firstLine": "Dokki",
            "secondLine": "Mossadak",
            "buildingNumber": "9",
            "floor": "5",
            "apartment": "14",
        },
        "business_Reference": business_id_retrieve,
        "receiver": {
            "first_name": "receiver first name",
            "last_name": "receiver last name",
            "phone": "0123456789",
            "email": "test@test.com",
        },
        "webhookUrl": "https://www.amazon.eg/",
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
def first_pickup():
    url = "http://app.bosta.co/api/v2/pickups"
    payload = {
        "scheduledDate": "2023-11-09",
        "business_ID": "2468aa",
        "scheduledTimeSlot": "13:00 to 16:00",
        "contactPerson": {
            "name": "person_name",
            "phone": "01122446789",
            "secPhone": "01225874391",
            "email": "person@gmail.com"
        },
        "notes": "any_note_you_want_to_add",
        "noOfPackages": "5",
        "packageType": "Normal",
         "repeatedData": {
            "repeatedType": "Daily",
            "days": ["Thursday"],
            "startDate": "2023-11-07",
             "endDate": "2023-11-14",
         }
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
print("Welcome to Bosta!")
print("Let's Start Registration")
verify_phone_number()
create_account()
print("Authorization Token")
login_data = get_authorization_token()
print(login_data)
business_id_retrieve=business_details()
print("Setting of your pickup location")
business_details()
pickup_location()
print("Your Account Is Ready")
first_delivery()
first_pickup()


