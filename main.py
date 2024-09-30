from flask import Flask
import random
import requests

app = Flask(__name__)

facts_list=["Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
            "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
            "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время."]
def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['link']
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
def get_dogs_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@app.route("/")
def hello_world():
    return f'<p><a href="/random_fact">Посмотреть случайный факт!</a></p>'+'<p><a href="/random_animal">Посмотреть случайное фото!</a></p>'
@app.route("/random_animal")
def animals():
    fun=[get_fox_image_url(),get_duck_image_url(),get_dogs_image_url()]
   
    return f'<p><a href="{random.choice(fun)}">Что изображено?</a></p>'
@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'
app.run(debug=True)
