from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from interactor import Interactor
from pydantic import BaseModel

app = FastAPI()
interactor = Interactor("models")


class PredictionRequest(BaseModel):
    text: str
    model_name: str


result_int_to_str = {-1: "negative", 0: "neutral", 1: "positive"}


@app.post("/predict")
async def classify_text(request: PredictionRequest):
    result = result_int_to_str[int(interactor.predict(model_name=request.model_name, sentence=request.text)[0][0])]
    return {"result": result}

# Serve the static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("static/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)
