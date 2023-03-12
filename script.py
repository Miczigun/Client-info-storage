#script makes dumpdata
from random import randint
import json

city = []
with open('spis.txt',encoding="utf-8") as f:
    for line in f:
        city.append(line)

province = ['Śląskie','Łódzkie','Małopolskie','Lubuskie','Wielkopolskie','Opolskie']

adres = []
with open('adres.txt',encoding="utf8") as f1:
    for line1 in f1:
        adres.append(line1)

name = []
with open('optyk.txt',encoding="utf-8") as f2:
    for line2 in f2:
        name.append(line2)


data = []
for item in range(200):
    data.append( {
        'model': 'klient.klient',
        'pk': item,
        'fields':
            {
            'nazwa': name[randint(0,len(name)-1)],
            'nip': randint(1000000000,9999999999),
            'adres': adres[randint(0,len(adres)-1)],
            'miejscowosc': city[randint(0,len(city)-1)],
            'wojewodztwo': province[randint(0, len(province) - 1)],
            'telefon': randint(500000000,800000000),
            'grupa': randint(2,3) #account user id( admin has id=1)
            }
    }
    )


with open("dane.json",'w') as f:
    json.dump(data,f,indent=2)