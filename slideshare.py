import requests
import urllib.request
r = requests.get("https://www.slideshare.net/bgasecurity/beyaz-apkal-hacker-ceh-eitimi-blm-4-5-6")
data = r.content
data=data.decode("utf-8")
liste=list(data.split('data-full='))
url=[]
kelime=""
slayt=1
sayi=0
link=[]
for i in liste:
    yeni_liste = list(i.split("\n"))
    url.append(yeni_liste[0])
url.remove(url[0])
for i in url :
    a=i.split('"')
    link.append(a[1])
url.clear()
for k in link:
    a = k.split(':')
    url.append(a[1])
for i in url:
    isim=str(slayt)+".jpg"
    urllib.request.urlretrieve("http:"+i,isim)
    print(str(slayt) +". slayt indirildi\n")
    slayt += 1