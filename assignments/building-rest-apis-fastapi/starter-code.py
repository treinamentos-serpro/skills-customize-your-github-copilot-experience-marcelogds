from fastapi import FastAPI

app = FastAPI(title="Task API")

items = [
    {"id": 1, "name": "Learn FastAPI", "done": False},
    {"id": 2, "name": "Build a sample API", "done": True},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add a GET route to list all items
# TODO: Add a GET route to fetch one item by its id
# TODO: Add a POST route to create a new item
# TODO: Add a PUT or PATCH route to update an item
