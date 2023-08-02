from fastapi import FastAPI
import uvicorn

from plugs.IRS.IRS import reco_intent
from plugs.cus_ner import NER

app = FastAPI()

@app.get("/")
async def index():
    return '<-- this is fury IRS NER node -->'

@app.get("/api/irs")
async def irs_point(text:str):
    reply = await reco_intent(text)
    return {"reply":reply}

@app.get("/api/ner")
async def ner_point(text:str,tag:str):
    reply = await NER(text,tag)
    return {"reply":{"ner":reply}}

@app.get("/api/irs-ner")
async def irs_ner_point(text:str):
    irs = await reco_intent(text)
    if irs['ner'] == True:
        ner = await NER(text,irs['ner-tag'])
        reply = {"text":text,"ner":ner,"irs":irs['irs']}
    else:
        reply = {"reply":text,"irs":irs['irs']}
    return reply

@app.get("/status")
async def status_check():
    return {"status":"online"}

if __name__ == "__main__":
    # uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run("app:app")