from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import json

app = FastAPI()

with open("ministers1.json", "r", encoding="utf-8") as file:
    ministers_data = json.load(file)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return ministers_data


@app.get("/{item_name}")
async def read_item(item_name):

    # output_dict = [x for x in ministers_data if x["name"].lower() == item_name.lower()]
    output_dict = []
    for x in ministers_data:
        if x["name"].lower() == item_name.lower():
            output_dict.append(x)
    if not output_dict:
        raise HTTPException(status_code=404, detail="Item not found")
    return JSONResponse(content=output_dict)
