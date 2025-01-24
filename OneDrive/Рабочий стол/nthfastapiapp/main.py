from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def controller():
    return "Hello computer"
