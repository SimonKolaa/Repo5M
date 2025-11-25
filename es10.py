import requests
import json

user_id = 1
url_utente = f"https://jsonplaceholder.typicode.com/users/{user_id}"

try:
    response = requests.get(url_utente)

    response.raise_for_status()

    dati_utente = response.json()

    print("--- Dati Utente Ricevuti ---")
    print(json.dumps(dati_utente, indent=4))

    print("\n--- Informazioni Specifiche ---")
    print(f"Nome: {dati_utente['name']}")
    print(f"Email: {dati_utente['email']}")
    print(f"Città: {dati_utente['address']['city']}")

except requests.exceptions.HTTPError as err:
    print(f"Errore HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Errore durante la richiesta: {err}")

url_posts = "https://jsonplaceholder.typicode.com/posts"

nuovo_post = {
    'title': 'Il Mio Nuovo Post',
    'body': 'Questo è il contenuto del mio primo post creato tramite API!',
    'userId': 1
}

try:
    response = requests.post(url_posts, json=nuovo_post)

    response.raise_for_status()

    post_creato = response.json()

    print("\n--- Risposta dal Server ---")
    print(f"Status Code: {response.status_code} (Created!)")
    print(json.dumps(post_creato, indent=4))
    print(f"\nIl nostro post è stato creato con ID: {post_creato['id']}")

except requests.exceptions.RequestException as err:
    print(f"Errore durante la richiesta: {err}")