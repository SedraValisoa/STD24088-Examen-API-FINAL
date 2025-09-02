from fastapi import FastAPI

app = FastAPI(title="Examen API Final", description="",version="1.0.0")

@app.get("/ping")
def read_root():
    return {"message":"pong"}
