import requests


def download_file(link, filename):
    response = requests.get(link)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print('Downloaded', filename)
    else:
        print('Failed to download')


url = "https://raw.githubusercontent.com/daniil-vikulov/Hate-Speech-Detection/main/models/model_catboost"
filename = "model_catboost"

download_file(url, filename)
