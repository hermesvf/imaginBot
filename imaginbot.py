from flask import Flask
import numpy as np
import random
import json

app = Flask(__name__)

users = ['hermes','marc','alex']
companies = ['Zara','McDonalds','imaginBank']


promotions_elements = {
    'Barcelona': {
        'Cinema': [
            ('Blade Runner',
             'http://sm.ign.com/ign_latam/movie/b/blade-runn/blade-runner-2049_u4ch.jpg',
             'Blade Runner 2049​ es una película neo-noir y de ciencia ficción estadounidense dirigida por Denis Villeneuve, estrenada en 2017 y escrita por Hampton Fancher y Michael Green.'),

            ('Kingsman II: The Golden Circle', 'https://pics.filmaffinity.com/kingsman_the_golden_circle-211353775-large.jpg',
             'Kingsman: El círculo dorado es una película de comedia de espías y acción de 2017 coproducida y dirigida por Matthew Vaughn y escrita por Vaughn y Jane Goldman.'),

            ('IT',
             'http://t3.gstatic.com/images?q=tbn:ANd9GcQLrPN9F6ZG74wznVu2Gk1XgEw87RIXI6i7VFmcxrmp-7q3Hrcf',
             'It es una película de 2017 basada en la novela de Stephen King de 1986 con el mismo nombre. Producido por New Line Cinema, KatzSmith Productions, Lin Pictures y Vertigo Entertainment, y distribuido por Warner Bros.'),

            ('Annabelle',
             'http://t3.gstatic.com/images?q=tbn:ANd9GcQFy7y7uWomJe_z5_R2aBTUNOGZj9TpbL4dNyV-KxCgqbI-_RiP',
             'Annabelle: Creation es una película de terror sobrenatural estadounidense de 2017 dirigida por David F. Sandberg y escrita por Gary Dauberman. Es una precuela de Annabelle de 2014 y la cuarta entrega de la franquicia de The Conjuring.'),

            ('The Snowman',
             'http://t0.gstatic.com/images?q=tbn:ANd9GcR7S69onWXf7b4AB2xCLTzlUHs5JaLxKefmMK6XDGtLz1-O12zr',
             'Cuando el líder (Fassbender) de un equipo de detectives comienza a investigar un caso de desaparición durante la primera nevada del invierno, temerá el regreso de un astuto asesino serial. ')
        ],
        'Restaurants': [
            ('El Bar de la FIB', 'https://igx.4sqi.net/img/general/200x200/qxR1yeKt8m33giZHPH1_Pn4fxiC8fPtom9EdKaeFgvQ.jpg',
             'El mítico bar de la facultad de Informática de Barcelona. En él encontrarás desde platos combinados hasta los bocadillos más variados'),
            ('Timesburg Sant Pau', 'http://2.bp.blogspot.com/-BrwsaiZxEvQ/VU-lWJ-Ok_I/AAAAAAAABQU/f3F-6dAiZGU/s1600/20150509_224017.jpg',
             'ngredientes de primera calidad, un ambiente de barrio cercano y ponerle pasión a todo lo que hacemos. Esta fórmula junto a la implantación de procesos pioneros en la elaboración de nuestros productos como el sello de nuestro pan, han convertido a Timesburg en todo un referente entre los amantes de las hamburguesas.'),
            ('La Esquinica,','http://laesquinica.com/wp-content/uploads/2015/10/004_luces.jpg','Tapeo y raciones de toda la vida en reconocido y clásico bar de azulejos decorado con aperos de campo.'),
            ('Tasca i Vins','https://u.tfstatic.com/restaurant_photos/682/47682/169/612/tasca-i-vins-diputacio-vista-interior-cb98d.jpg','El restaurante Tasca i Vins de la calle Diputació de Barcelona es uno de cuatro hermanos mellizos repartidos por distintos puntos carismáticos de la ciudad.')
        ],
        'Theatre': [
            ('Monólogo Berto Romero','https://www.atrapalo.com/common/photo/event/4/8/0/8906/458277/si_372_0.jpg','Llega a los escenarios de Barcelona el nuevo espectáculo de Berto Romero. Divertido a más no poder, no te dejará indiferente.'),
            ('Cabaret','https://www.atrapalo.com/common/photo/event/4/8/0/4226/442601/si_372_0.jpg', 'El mítico y ya conocido espectáculo de baile llega a Barcelona con un aire renovado y alguna que otra sorpresa. ¡No te lo puedes perder!')
        ],
        'Sport': [
            ('Barcelona - Manchester City', 'http://www.fcbarcelonanoticias.com/img2/2016/08/entradas-barcelona-manchester-city-196355.png', 'Disfruta en el Camp Nou de este emocionante partido de la Champions League'),
            ('Montmelo Formula 1', 'https://okdiario.com/img/2016/05/MONTMELO.jpg','La emoción de vivir de cerca la Fórmula 1, ahora al alcance de tu mano. No lo dejes escapar y compra ya tu entrada.')
        ]
    }
}

catalogs = {
    'zara': [
        ('Black T-Shirt','https://s3-eu-west-1.amazonaws.com/micoletstatic/item_images/fb1/b1e/ad7/9b1/d8e/eea/231082/standard/camiseta-negra-basica-manga-corta.JPG?1470303502'),
        ('Blue jeans','https://s-media-cache-ak0.pinimg.com/originals/8d/fb/38/8dfb3860ee73183250ecb72da66984c4.jpg'),
        ('Casual shoes','https://s-media-cache-ak0.pinimg.com/originals/c3/ab/af/c3abaf3b5a1a253d1f31502413fadafe.jpg'),
        ('Modern shirt', 'https://s-media-cache-ak0.pinimg.com/236x/1c/fe/0f/1cfe0f2a51a552039ac479a78fff6478.jpg'),
        ('Leather jacket','https://cdn.fashiola.es/L435452564/gebeana-camisa.jpg'),
        ('Sport bag','https://s-media-cache-ak0.pinimg.com/236x/fb/15/d7/fb15d75b9bb35181a3bd58e61c5809a1--zara-bags-bowling-bags.jpg'),
        ('Party shoes','http://www.colectivocomun.co/images/category_5/Nuevos%20productos%20en%20l%C3%ADnea%20Mujer%20Zapatos%20Zara%20Bot%C3%ADn%20granate%20Todas.jpg')
            ],
    "mcdonald's": [
        ('Big Mac', 'https://www.mcdonalds.es/sites/default/files/styles/mcdo_small_306x134/public/produits/306x134_bm.png'),
        ('Grand Big Mac', 'https://www.mcdonalds.es/sites/default/files/styles/mcdo_small_306x134/public/produits/306x134_gbm_0.png'),
        ('Grand McExtreme','https://www.mcdonalds.es/sites/default/files/styles/mcdo_small_306x134/public/produits/306x134.png'),
        ('CBO','https://www.mcdonalds.es/sites/default/files/styles/mcdo_small_306x134/public/produits/306x134_cbo.png'),
        ('McWrap','https://www.mcdonalds.es/sites/default/files/styles/mcdo_small_306x134/public/produits/306x134_mcwrapbaconyqueso.png'),
        ('McNuggets','https://www.mcdonalds.es/sites/default/files/styles/mcdo_small_306x134/public/produits/306x134_hm_mcnuggets_0.png'),
        ('French Fries','https://www.mcdonalds.es/sites/default/files/styles/mcdo_small_306x134/public/produits/7-patatas-fritas-medianas-frontal.png'),
        ('Deluxe Fries','https://www.mcdonalds.es/sites/default/files/styles/mcdo_small_306x134/public/produits/patatasdeluxe_0.png'),
        ('Salad','https://www.mcdonalds.es/sites/default/files/styles/mcdo_small_306x134/public/produits/ensaladadelahuerta306_134_0.png')
    ]
}




def genItems(param):
    lista = []
    for item in promotions_elements['Barcelona'][param]:
        lista.append(
                    {
                        "optionInfo" : {
                            "key"     : item[0].upper(),
                            "synonyms": []
                        },
                        "title"      : item[0],
                        "description": item[2],
                        "image"      : {
                            "url": item[1]
                        }
                    }
        )
    return lista


def getPromos(type):


    promos = {
                "type"    : "carousel_card",
                "platform": "google",
                "id"      : "4a857630-8667-466f-887f-7f3bd26ab3dd",
                "items"   : genItems(type)
            }
    return promos







bank_accounts = {
    'hermes' : 1000,
    'marc' : 1000,
    'alex' : 1000
}

entidades_cobradoras = ['Escuela Música', 'Eroski', 'UPC', 'Restaurante FLOR', 'Gimnasio', 'Parking', 'Bar Fib', 'JEDI']
entidades_pagadoras = ['Antonio', 'Nomina', 'Trabajo', 'Retribución', 'Maria', 'Juan', 'Regalo cumpleaños', 'JEDI']

quantities = list(np.random.normal(0,100,50))

movements = {}

def generateRandomMovements():
    for i in bank_accounts.keys():
        list = []
        for q in quantities:
            if q > 0:
                list.append((q,random.choice(entidades_pagadoras)))
            else:
                list.append((q, random.choice(entidades_cobradoras)))
            movements[i] = list


def catalogItems(company):
    company = company.lower()
    list_items = []
    for item in catalogs[company]:
        list_items.append(
                {
                    "optionInfo": {
                        "key"     : item[0].upper(),
                        "synonyms": []
                    },
                    "title"     : item[0],
                    "image"     : {
                        "url": item[1]
                    }
                }
        )
    return list_items



@app.route('/products/<company>')
def products_company(company):
    if company in ['McDonalds','mcdonalds',"McDonald's","mcdonald's"]:
        company = "mcdonald's"
    messages = [
        {
            "type": "simple_response",
            "platform": "google",
            "id": "1ab6abf0-442e-4a84-9d7b-5a9ebd2312ff",
            "textToSpeech":"Here are the products from {}".format(company)
        },
        {
        "type"        : "list_card",
        "platform"    : "google",
        "id"          : "1ab6abf0-442e-4a84-9d7b-5a9ebd2312ff",
        "title": "Catalog of {0}".format(company),
        "items" : catalogItems(company)
        },
        {
            "type"  : 0,
            "id"    : "8e5ac865-75c7-48fa-be75-3d74cfcf83a3",
            "speech": ""
        }
    ]

    response = {
        "speech"  : "",
        "messages": messages
    }
    return json.dumps(response)

@app.route('/')
def hello_world():
    return 'Hello World!'


def notValid():
    pass


@app.route('/send/<from_user>/<to_user>/<amount>')
def send_money(from_user,to_user,amount):
    from_user = from_user.lower()
    to_user = to_user.lower()
    amount = eval(amount)

    try:
        b_from = bank_accounts[from_user]
        b_to = bank_accounts[to_user]
    except:
        return notValid()

    if b_from < amount:
        return "Not Enough Money"
    else:
        bank_accounts[from_user] -= amount
        bank_accounts[to_user] += amount
        return "Done"

@app.route('/promotions/<type>/<city>')
def promotions(type,city):
    city = 'Barcelona'
    if type in ['restaurant', 'Restaurant', 'Food', 'food', 'restaurants', 'Restaurants', 'Eating', 'eating', 'eat', 'Eat']:
        type = 'Restaurants'
    elif type in ['Cinema', 'cinema', 'movies', 'Movies']:
        type = 'Cinema'
    elif type in ['Theatre', 'theatre', 'spectacles', 'Spectacles']:
        type = 'Theatre'
    elif type in ['Sports', 'sports', 'Sport', 'sport']:
        type = 'Sport'
    elif type in ['clothing', 'Clothing', 'clothes', 'Clothes']:
        type = 'Clothing'

    messages = [{
        "type"        : "simple_response",
        "platform"    : "google",
        "id"          : "1ab6abf0-442e-4a84-9d7b-5a9ebd2312ff",
        "textToSpeech": "Here are some promotions we've found for you"
    },
        getPromos(type)
    ]

    response = {
        "speech"  : "",
        "messages": messages
    }
    return json.dumps(response)


@app.route('/<user>/movements')
def movements_user(user):
    return str(movements['Marc'])

@app.route('/<user>/balance')
def balance(user):
    user = 'Marc' #HARCODEITO FUERTE
    user = user.lower()
    try:
        balance = bank_accounts[user]
    except:
        return "Unknown user"
    return str(balance)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
