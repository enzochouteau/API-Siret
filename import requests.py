import requests


def get_api_data(api_url):
    try:
        # Effectuer une requête GET à l'API
        response = requests.get(api_url)

        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            # Convertir la réponse JSON en objet Python
            data = response.json()
            return data
        else:
            # Afficher un message d'erreur si la requête a échoué
            print(f"Erreur de requête : {response.status_code}")
            return None
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None


api_url = "https://api.societe.com/api/v1"
api_data = get_api_data(api_url)

if api_data:
    print("Données récupérées avec succès:")
    print(api_data)
else:
    print("Impossible de récupérer les données de l'API.")