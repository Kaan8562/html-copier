import requests
from bs4 import BeautifulSoup

url = input("Html içeriğini kaydetmek istediğiniz sitenin linkini giriniz: ")
dosya_ismi = input("Dosya ismi ne olsun, giriniz: ")

r = requests.get(url)
html_icerigi = BeautifulSoup(r.content)
print(html_icerigi.prettify())

dosya = open(dosya_ismi + ".html", "a+")
dosya.write(str(html_icerigi))
dosya.close()
print("Html içeriği kaydedildi.")
