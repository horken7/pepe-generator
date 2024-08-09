import os
import random
from zipfile import ZipFile

import requests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, Response

app = FastAPI()

if (
    os.environ.get("KAGGLE_ENABLE")
    and os.environ.get("KAGGLE_USERNAME")
    and os.environ.get("KAGGLE_KEY")
):
    # URL for the dataset download
    URL = (
        "https://www.kaggle.com/api/v1/datasets/download/tornikeonoprishvili/"
        "pepe-memes-dataaset?datasetVersionNumber=1"
    )

    # Destination folder
    DEST_FOLDER = "data"

    # Path to save the downloaded file
    zip_path = os.path.join(DEST_FOLDER, "pepe-memes-dataset.zip")

    # Download the dataset
    response = requests.get(
        URL,
        auth=(os.environ.get("KAGGLE_USERNAME"), os.environ.get("KAGGLE_KEY")),
        timeout=100,
    )
    response.raise_for_status()  # Check if the request was successful

    # Save the downloaded zip file
    with open(zip_path, "wb") as file:
        file.write(response.content)

    print(f"Downloaded dataset to {zip_path}")

    # Unzip the file
    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(DEST_FOLDER)

    print(f"Extracted files to {DEST_FOLDER}")


default_image_response = requests.get(
    "https://upload.wikimedia.org/wikipedia/en/6/63/Feels_good_man.jpg",
    timeout=100,
)


@app.get("/")
async def return_pepe():
    if not os.environ.get("KAGGLE_ENABLE"):
        return Response(default_image_response.content, media_type="image/jpeg")
    random_image = random.choice(
        [f for f in os.listdir("data/data") if not f.endswith(".txt")]
    )
    image_path = os.path.join("data/data", random_image)
    return FileResponse(image_path)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
