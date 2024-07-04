from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"massage":"Hello Word"}

@app.get('/hello')
def read_hello():
    return{"message":'Hello','123':123}

@app.get('/item/{id}')
def read_item(id:int):
    return {"item":id}
