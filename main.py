from fastapi import FastAPI
import os
import uvicorn

app =FastAPI()

@app.get('/')
def home():
    return ("Hi this home page ")

@app.get('/')
def homeget():
    return ("Hi this home page  2")

if __name__=='__main__':
    port=int(os.getenv("PORT",8080))
    import uvicorn
    uvicorn.run(app, host = '0.0.0.0', port =port)