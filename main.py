from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

with open("ministers1.json", "r", encoding="utf-8") as file:
    ministers_data = json.load(file)


@app.get("/")
async def root():
    return ministers_data


@app.get("/{item_name}")
async def read_item(item_name):
    # with open("ministers1.json", "r", encoding="utf-8") as file:
    #     ministers_data = json.load(file)
    # output_dict = [x for x in ministers_data if x["name"].lower() == item_name.lower()]

    if not output_dict:
        raise HTTPException(status_code=404, detail="Item not found")
    return ministers_data
