import requests
import time
safemoonWallet = "https://api.safemoon.net/wallet/"
safemoonPrice = "https://api.safemoon.net/price"
address = "0x2053B622b9D195ab845f010C82016CE060518486"
arrBalance = []
arrPrice = []
reflections = []


while True:
    arrBalance.append(float(requests.get(safemoonWallet+address).json()['balance']))
    arrPrice.append(float(requests.get(safemoonPrice).json()['price']))
    #print(requests.get(safemoonWallet+address).json()['balance'])
    #print(arrBalance)
    time.sleep(5)

def getCurrentPrice():
    price = float(requests.get(safemoonPrice).json()['price'])

def getTotalReflectionPrice():
    reflections[-1] * getCurrentPrice()

def getReflections(): 
    if len(arrBalance) > 2:
        x = 0
        while x < len(arrBalance):
            if x+1 >= len(arrBalance) : 
                break
            first = arrBalance[x+1]
            second = arrBalance[x]
            sumofBalance = float(second-first)
            reflections.append(sumofBalance)
            x += 1
