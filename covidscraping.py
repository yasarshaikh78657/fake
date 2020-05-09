import requests
import bs4
import plyer
import time
import datetime


data = requests.get("https://www.mygov.in/covid-19")
bs = bs4.BeautifulSoup(data.text, 'html.parser')
active_case= bs.find("div" , class_="information_row").find("div" , class_="iblock active-case").find("span", class_="icount").get_text()
discharge= bs.find("div" , class_="information_row").find("div" , class_="iblock discharge").find("span", class_="icount").get_text()
death= bs.find("div" , class_="information_row").find("div" , class_="iblock death_case").find("span", class_="icount").get_text()
active_case = int(active_case)
discharge = int(discharge)
death = int(death)
confirm = active_case + discharge + death
print(confirm)
print(active_case)
print(discharge)
print(death)


