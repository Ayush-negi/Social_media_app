import time
from fastapi import FastAPI
import psycopg
from psycopg.rows import dict_row
from . import  models
from .database import engine
from .routers import post, user




# Automatically create tables on application startup.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()



while True:
    try:
        conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres',
        password='admin123', row_factory=dict_row)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break

    except Exception as error:
        print("Connection to database failed")
        print("Error:", error)
        time.sleep(2)

# In-memory storage for posts
my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite foods", "content": "I like pizza", "id": 2}
]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id: int):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

# Include the router objects for user and post endpoints
app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
