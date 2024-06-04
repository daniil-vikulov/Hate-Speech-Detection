import argparse
import os

import requests


def download_file(link, filename):
    """
    Downloads file from the link and saves it at a specific path. Note that existing file with the same name will be overwritten.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    response = requests.get(link)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print('Downloaded', filename)
    else:
        print('Failed to download')


def main(model_type):
    base_link = "https://raw.githubusercontent.com/daniil-vikulov/Hate-Speech-Detection/main/models/"

    if model_type == "all":
        model_types = ["catboost", "logisticregression", "randomforest", "vectorizer"]
    else:
        model_types = [model_type]

    for mt in model_types:
        link = f"{base_link}model_{mt}"
        fn = f"models/model_{mt}"
        download_file(link, fn)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download model")
    parser.add_argument("model_type", choices=['catboost', 'randomforest', 'logisticregression', "vectorizer", 'all'],
                        help="Specify model name to pull")

    args = parser.parse_args()

    main(args.model_type)
