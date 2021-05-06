import requests



apikey = 'fb69039d'
def get_omdb_movie(title: str):
    response = requests.get(f'http://www.omdbapi.com/?apikey=fb69039d&t={title}')
    #print(pesquisa)
    return response.status_code, response.json()

if __name__ == '__main__':
    status, resp = get_omdb_movie('Hacksaw Ridge')
    print(f'status: {status} \n'
          f'Response: {resp}')
