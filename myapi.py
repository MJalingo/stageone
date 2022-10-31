from fastapi import FastAPI

app = FastAPI()

student = {
    1:{
        "name": "Mohammed ",
        "age": 18,
        "class":"year 12" 
        
    }
}

@app.get("/")
def index():
    return  { "slackUsername": "mohammed jalingo nuruddeen", "backend": True, "age": 60, "bio":"python backend developer" }
    