import os
import random

import requests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, Response

app = FastAPI()

if (
    not os.path.exists("data")
    and os.environ.get("KAGGLE_ENABLE")
    and os.environ.get("KAGGLE_USERNAME")
    and os.environ.get("KAGGLE_KEY")
):
    import kaggle

    kaggle.api.dataset_download_files(
        "tornikeonoprishvili/pepe-memes-dataaset", unzip=True
    )

default_image_response = requests.get(
    "https://upload.wikimedia.org/wikipedia/en/6/63/Feels_good_man.jpg",
    timeout=100,
)


@app.get("/")
async def return_pepe():
    if not os.path.exists("data"):
        return Response(default_image_response.content, media_type="image/jpeg")
    random_image = random.choice(os.listdir("data"))
    image_path = os.path.join("data", random_image)
    return FileResponse(image_path)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
