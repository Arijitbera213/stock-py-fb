import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import numpy as np
start= datetime.datetime(2017,1,1)
end= datetime.datetime(2021,5,17)
tesla=web.DataReader("TSLA",'yahoo',start,end)
ford=web.DataReader("F",'yahoo',start,end)
gm=web.DataReader("GM",'yahoo',start,end)
tesla.to_csv('TeslaStock_up.csv')
ford.to_csv('FordStock_up.csv')
gm.to_csv('GMStock_up.csv')
tesla['Open'].plot(label='TSLA Open price',figsize=(15,6))
gm['Open'].plot(label='GM Open price')
ford['Open'].plot(label='F Open price')
plt.title(' Stock Prices of cars companys')
plt.ylabel('Stock Price')
plt.legend()
plt.savefig("graphopenprice.jpg")
from firebase_admin import credentials, initialize_app, storage,firestore
# Init firebase with your credentials
cred = credentials.Certificate(r"serviceAccountKey.json")
initialize_app(cred, {'storageBucket': 'stock-data-fc41e.appspot.com'})
fileName = r"graphopenprice.jpg"
bucket = storage.bucket()
blob = bucket.blob("graphopenprice_test")
blob.upload_from_filename(fileName)
# Opt : if you want to make public access from the URL
blob.make_public()
print("your file url", blob.public_url)
db = firestore.client()
doc_ref = db.collection(u'stock').document(u'data')
doc_ref.set({
     u'img-link': blob.public_url,
})
tesla['Volume'].plot(label="Tesla",figsize=(10,7))
ford['Volume'].plot(label="Ford")
gm['Volume'].plot(label="Tesla")
plt.legend()
plt.savefig("volume_traded.jpg")
from firebase_admin import credentials, initialize_app, storage
# Put your local file path 
fileName = r"volume_traded.jpg"
bucket = storage.bucket()
blob = bucket.blob("graphopenprice")
blob.upload_from_filename(fileName)

# Opt : if you want to make public access from the URL
blob.make_public()

print("your file url", blob.public_url)

print('test case 1.0.2')
print(f"Hello\nWorld!")
print("test line 3")
