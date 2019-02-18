import requests
import json

# ##############################################################################
# CATEGORIES
categories = [
    {'name': 'Junior',
     'code': 'JUN',
     'initials': 'J',
     'gender': 'M',
     'reference': ''},
    {'name': 'Senior',
     'code': 'SEN',
     'initials': 'S',
     'gender': 'M',
     'reference': ''},
]
for cat in categories:
    r = requests.post('http://127.0.0.1:8000/categories',
                      data=json.dumps(cat),
                      headers={'content-type': 'application/json'})

r = requests.get('http://127.0.0.1:8000/categories',)
print("Code: %s\nText: %s" % (r.status_code, r.text))


# ##############################################################################
# COUNTRIES
countries = [
    {'name': 'Brazil',
     'code': 'BR',
     'initials': 'B',
     'reference': 'BRA001'},
    {'name': 'United States of America',
     'code': 'USA',
     'initials': 'EEUU',
     'reference': 'USA001'},
]
for country in countries:
    r = requests.post('http://127.0.0.1:8000/countries',
                      data=json.dumps(country),
                      headers={'content-type': 'application/json'})

r = requests.get('http://127.0.0.1:8000/countries',)
print("Code: %s\nText: %s" % (r.status_code, r.text))


# ##############################################################################
# DISCIPLINES
disciplines = [
    {'name': 'Hockey Inline',
     'code': 'HI',
     'web': 'https://hockey-inline.wrg2019.com/',
     'reference': 'HI-001'},
    {'name': 'Inline Freestyle',
     'code': 'IF',
     'web': 'https://inline-freestyle.wrg2019.com/',
     'reference': 'IF-001'},
]
for discipline in disciplines:
    r = requests.post('http://127.0.0.1:8000/disciplines',
                      data=json.dumps(discipline),
                      headers={'content-type': 'application/json'})

r = requests.get('http://127.0.0.1:8000/disciplines',)
print("Code: %s\nText: %s" % (r.status_code, r.text))


# ##############################################################################
# LOCATIONS
locations = [
    {'name': 'Palau Sant Jordi',
     'address': 'Passeig Olimpic',
     'postal_code': '08038',
     'city': 'Barcelona',
     'country': 'Spain',
     'gps': '43.0317522,-7.5922429',
     'reference': 'PSJ-001'},
    {'name': 'Santa Coloma de Gramanet',
     'address': 'Carrer del Peru',
     'postal_code': '08052',
     'city': 'Barcelona',
     'country': 'Spain',
     'gps': '41.4534932,2.2051065',
     'reference': 'SCG-001'},
]
for location in locations:
    r = requests.post('http://127.0.0.1:8000/locations',
                      data=json.dumps(location),
                      headers={'content-type': 'application/json'})

r = requests.get('http://127.0.0.1:8000/locations',)
print("Code: %s\nText: %s" % (r.status_code, r.text))


# ##############################################################################
# REFEREES
referees = [
    {'name': 'Pier Luiggi',
     'surname': 'Colina',
     'birthdate': '1972-01-01T12:12:12Z',
     'bio': 'Biography of Pier Luiggi Colina',
     'photo': 'path/to/uploads/photos/pierluiggi-md5.jpg',
     'gender': 'M'},
    {'name': 'Manuel Enrique',
     'surname': 'Mejuto Gonzalez',
     'birthdate': '1974-11-21T14:15:27Z',
     'bio': 'Biography of Mejuto Gonzalez',
     'photo': 'path/to/uploads/photos/mejutogonzalez-md5.jpg',
     'gender': 'M'},
]
for referee in referees:
    r = requests.post('http://127.0.0.1:8000/referees',
                      data=json.dumps(referee),
                      headers={'content-type': 'application/json'})

r = requests.get('http://127.0.0.1:8000/referees',)
print("Code: %s\nText: %s" % (r.status_code, r.text))


# ##############################################################################
# ROUNDS
rounds = [
    {'name': 'Quarters Finals',
     'order': 1},
    {'name': 'Semifinals',
     'order': 2},
    {'name': 'Final',
     'order': 3},
]
for round in rounds:
    r = requests.post('http://127.0.0.1:8000/rounds',
                      data=json.dumps(round),
                      headers={'content-type': 'application/json'})

r = requests.get('http://127.0.0.1:8000/rounds',)
print("Code: %s\nText: %s" % (r.status_code, r.text))


# ##############################################################################
# SESSIONS
sessions = [
    {'name': 'Short Program Junior Women',
     'code': 'SPJW',
     'reference': 'SPJW-001',
     'date': '2018-07-03',
     'time': '18:30:00'},
    {'name': 'Short Program Senior Men',
     'code': 'SPSM',
     'reference': 'SPSM-001',
     'date': '2018-07-03',
     'time': '19:30:00'},
]
for session in sessions:
    r = requests.post('http://127.0.0.1:8000/sessions',
                      data=json.dumps(session),
                      headers={'content-type': 'application/json'})

r = requests.get('http://127.0.0.1:8000/sessions',)
print("Code: %s\nText: %s" % (r.status_code, r.text))


# ##############################################################################
# TEAM
teams = [
    {'name': 'Brazil Inline Roller',
     'bio': 'Biography of Brazil Inline Roller',
     'photo': 'path/to/uploads/photos/bra-inline-roller-md5.jpg'},
    {'name': 'USA hockey-inline',
     'bio': 'Biography of USA hockey-inline',
     'photo': 'path/to/uploads/photos/usa-hockey-inline-md5.jpg'},
]
for team in teams:
    r = requests.post('http://127.0.0.1:8000/teams',
                      data=json.dumps(team),
                      headers={'content-type': 'application/json'})

r = requests.get('http://127.0.0.1:8000/teams',)
print("Code: %s\nText: %s" % (r.status_code, r.text))


# ##############################################################################
# ATHLETES
athletes = [
    {'name': 'Mery',
     'surname': 'Poppins',
     'birthdate': '2001-01-01T12:12:12Z',
     'bio': "This is the Merys biography",
     'photo': 'path/to/uploads/photos/-merypoppins-md5.jpg',
     'weight': 60,
     'height': 160,
     'gender': 'W',
     'country_id': 1,
     'reference': 'REF001'},
    {'name': 'Felipe Juan Froilan',
     'surname': 'De todos los Santos Marichalar y Borbon',
     'birthdate': '2001-01-01T12:12:12Z',
     'bio': "This is the Felipe Juan Froilan biography",
     'photo': 'path/to/uploads/photos/froilan-md5.jpg',
     'weight': 75,
     'height': 182,
     'gender': 'M',
     'country_id': 2,
     'reference': 'REF002'},
]
for athlete in athletes:
    r = requests.post('http://127.0.0.1:8000/athletes',
                      data=json.dumps(athlete),
                      headers={'content-type': 'application/json'})

r = requests.get('http://127.0.0.1:8000/athletes',)
print("Code: %s\nText: %s" % (r.status_code, r.text))
