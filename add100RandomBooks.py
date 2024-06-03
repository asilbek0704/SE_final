#!/usr/bin/env python3

import requests
import json
from faker import Faker

APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def getBooks():
    r = requests.get(
            f"{APIHOST}/api/v1/books",
    )
    if r.status_code == 200:
        return r.json()

def deleteBook(bookID, apiKey):
    r = requests.delete(
            f"{APIHOST}/api/v1/books/{bookID}",
            headers = {
                "X-API-Key": apiKey
            }
    )
    if r.status_code == 200:
        print(f"Book with ID {bookID} is successfully deleted")

# Get the Auth Token Key
apiKey = getAuthToken()

# Get all books to know the amount
books = getBooks()

for index in range(0, 5):
    bookInfo = books[index]
    bookID = bookInfo["id"]

    deleteBook(bookID, apiKey)
    
for index in range(-5, 0):
    bookInfo = books[index]
    bookID = bookInfo["id"]

    deleteBook(bookID, apiKey)
