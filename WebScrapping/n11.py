# N11 sayfasından cep telefonlarının bilgilerinin çekilmesi
# source: https://www.youtube.com/watch?v=CxaT-jqp3Is

import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?pg=1"
r = requests.get(url)
#r.status_code
#r.content
soup = BeautifulSoup(r.content, "lxml")
urunler = soup.find_all("li", attrs={"class":"column"})

urun_sayisi = 0
for urun in urunler:
    urunAdi = urun.a.get("title")
    urunLink = urun.a.get("href")

    try:
        urun_r = requests.get(urunLink)
        #print(urun_r.status_code) #200 geliyorsa başarılı
    except Exception:
        print("Ürün detayı alınamadı")

    urun_soup = BeautifulSoup(urun_r.content) # ürüne ait sayfa odağa alındı
    
    ozellikler = urun_soup.find_all("div", attrs={"class":"unf-p-detail"})
    #print(ozellikler)

    for ozellik in ozellikler:
      urun_sayisi +=1
      print("-"*12 + str(urun_sayisi))
      print(ozellik.find("h1", attrs={"class": "proName"}).text.strip())
      print(ozellik.find("ins").text)
print("-"*24 )   
print("Toplam ürün sayısı: " + str(urun_sayisi))
