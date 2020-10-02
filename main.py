
import requests as req 
import random

## Changes in the API Key are made to make sure that the App is able to send SMS properly

def otp_create():
	otp = random.randint(1999,9999)
	return otp

def send_otp(mobile_num):
	otp = otp_create()
	url = "https://www.fast2sms.com/dev/bulk"
	payload_part_1 = f"sender_id=IMPSMS&language=english&route=qt&numbers={mobile_num}"
	payload_part_2 = "&message=35860&variables={AA}&variables_values="
	payload_part_3 = f"{otp}"
	payload = payload_part_1 + payload_part_2 + payload_part_3
	headers = {
	'authorization': "FLAtMGWmvC5oeJ76GzD8OrxuFu1VDS662w9DY48Pl6CAtTKEVaYbsb3rZnLH",
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
	}
	response = req.request("POST", url, data=payload, headers=headers)
	return response, otp


while True:
	mobile_num = input("Enter Mobile Number (+91) : ")
	if len(mobile_num.replace(" ","")) == 10:
		response = send_otp(mobile_num)
		if response[0].status_code == 200:
			print("OTP Sent Successfully")
			while True:
				otp_ver = int(input("Enter the OTP Received : "))
				if otp_ver == response[1]:
					print("OTP Successfully Verified")
					break
				else:
					print("OTP not verifiable")
					continue
		else:
			print("OTP Failed to Send")
			break
		print()
	else:
		print("Invalid Mobile Number. It should be of 10 digits")
		print()




