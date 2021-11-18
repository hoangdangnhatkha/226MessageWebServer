import requests
import json
urlGET = 'http://127.0.0.1:8000/hello/get/'
urlCREATE = 'http://127.0.0.1:8000/hello/create/'
urlIndex = 'http://127.0.0.1:8000/hello/'
GeneratedKey = 12345678

def sendData(key,message):
    payload = {'Key':key, 'Message':message}
    r = requests.post(urlCREATE,data = payload)
    return r.status_code

def getContent(key):
    return requests.get(urlGET + str(key) + "/")

response = requests.get(urlIndex)
if response.status_code == 200:
    print('Success!')
    while True: 
        print("Next Key: " + str(GeneratedKey) + "\n")
        keyContent = getContent(GeneratedKey)
        if (keyContent.text == ''):
            break
        GeneratedKey = GeneratedKey + 1
        print(keyContent.text)
    newMessage = input("Key is avaiable, enter new Message\n")
    sendData(GeneratedKey,newMessage)
elif response.status_code == 404:
    print('Not Found.')

    #data = response.content.decode('utf-8')
    #json = response.json()
    
    #for j in json:
    #    message = message + "Key: "
    #    message = message + str(j['Key']) + "\n"

    #print(message)
    #print(r.text)