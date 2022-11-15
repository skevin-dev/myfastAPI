from fastapi import FastAPI, Request
from datetime import datetime

storage = FastAPI(title='MY FASTAPI')

@storage.get('/mail')
def index():
    return "my name is kevin, this is my api for hackathon"

@storage.get('/today')
def today():
    return str(datetime.now())


@storage.get('/mynames')
def names(First_name:bool =False, last_name: bool =False,full_name_:bool=False):
    full_name =""
    if First_name:
        full_name += 'Shyaka'

    if last_name:
        full_name += ' Kevin'

    if full_name_:
        full_name += 'Shyaka kevin +'

    return full_name

if __name__ == "__main__":
    storage.run()