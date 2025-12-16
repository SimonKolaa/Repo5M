import requests

base_url = "https://jsonplaceholder.typicode.com"

# Recupera tutti i post pubblicati dall'utente con ID = 1
response = requests.get(f"{base_url}/posts?userId=1")
if response.status_code == 200:
    posts = response.json()
    print("--- Post dell'utente 1 ---")
    for post in posts:
        print(f"ID Post: {post['id']}, Titolo: {post['title']}")
else:
    print(f"Errore nel recupero dei post: {response.status_code}")
    exit(1)

# Recupera i commenti per il primo post
if posts:
    first_post_id = posts[0]['id']
    comments_response = requests.get(f"{base_url}/posts/{first_post_id}/comments")
    if comments_response.status_code == 200:
        comments = comments_response.json()
        print("\n--- Commenti per il primo post ---")
        for comment in comments:
            print(f"- {comment['name']}: {comment['body']}")
    else:
        print(f"Errore nel recupero dei commenti: {comments_response.status_code}")
        exit(1)
else:
    print("Nessun post trovato.")
    exit(1)

# Crea un nuovo commento per il primo post
new_comment = {
    "postId": first_post_id,
    "name": "Nuovo Commentatore",
    "email": "nuovo@example.com",
    "body": "Questo è un commento aggiunto tramite API!"
}

post_response = requests.post(f"{base_url}/comments", json=new_comment)
if post_response.status_code == 201:
    print("\n--- Nuovo Commento Creato ---")
    import json
    print(json.dumps(post_response.json(), indent=4))
else:
    print(f"Errore nella creazione del commento: {post_response.status_code}")