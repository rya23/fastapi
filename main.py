from fastapi import FastAPI
import json

app = FastAPI()

with open("ministers1.json", "r", encoding="utf-8") as file:
    ministers_data = json.load(file)


@app.get("/")
async def root():
    return ministers_data


@app.get("/{item_name}")
async def read_item(item_name):
    output_dict = [x for x in ministers_data if x["name"] == item_name]
    return output_dict
