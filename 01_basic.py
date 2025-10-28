from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_api():
    return {"Hello": "World!!"}

@app.get("/greeting")
def greeting_api():
    return "Hello World!!"

# placement of this api matters
@app.get("/item/my_item")
def get_item():
    return {"itemid": "current user item"}

@app.get("/item/{item_id}")
def get_item(item_id):
    return {"itemid": item_id}

@app.get("/int_item/{item_id}")
def get_int_item(item_id: int):
    return {"itemid": item_id}

# same way, do not use the below pattern, the first one would be given preference

@app.get("/users")
async def read_users():
    return ["Rick", "first"]


@app.get("/users")
async def read_users2():
    return ["Bean", "second"]