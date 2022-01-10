import time
import requests
safemoonWallet = "https://api.safemoon.net/wallet/"
safemoonPrice = "https://api.safemoon.net/price"
address = "0x2053B622b9D195ab845f010C82016CE060518486"
arrBalance = []
x = 0
while x != 6:
    while True: 
        arrBalance.append(float(requests.get(safemoonWallet+address).json()['balance']))
        time.sleep(5)
        x += 1
        break
    saveFile = open('C:/Users/Aman/Desktop/SafeMoon Tracker/balanceTracked.txt', 'w')
    saveFile.write(str(arrBalance))
    saveFile.close()
