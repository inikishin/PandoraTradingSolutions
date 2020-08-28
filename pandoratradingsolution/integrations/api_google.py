import requests

def search(q):
    url = 'https://www.googleapis.com/customsearch/v1'
    google_api_key = 'AIzaSyBr0q2xRokshSpTIDmngCAoal9Tcwrk_9Q'
    search_engine_id = '005580324007648051676:s-soh4gryq8'

    params = {'key': google_api_key,
              'cx': search_engine_id,
              'q': q
              }

    response = requests.get(url, params=params)
    results = response.json()

    return results
