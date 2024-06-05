from fastapi import FastAPI
from databases import Database
from app.config import DATABASE_URL, metadata, engine
from app.models import products
from app.schemas import Product

app = FastAPI()

database = Database(DATABASE_URL)


@app.on_event('startup')
async def startup():
    await database.connect()
    metadata.create_all(engine)


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get("/products/")
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.post("/products/")
async def create_products(product: Product):
    query = products.insert().values(
        name=product.name,
        price=product.price,
        amount=product.amount,
        description=product.description
    )
    last_record_id = await database.execute(query)
    return {
        "id": last_record_id,
        "name": product.name,
        "price": product.price,
        "amount": product.amount,
        "description": product.description
    }


@app.put("/products/{product_id}/")
async def update_products(product_id: int, product: Product):
    query = products.update().where(products.c.id == product_id).values(
        name=product.new_name,
        price=product.new_price,
        amount=product.new_amount,
        description=product.new_description,
    )

    result = await database.execute(query)

    return {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "amount": product.amount,
        "description": product.description
    }


@app.delete("/products/{product_id}/")
async def delete_products(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    result = await database.execute(query)

    return {"message": "Product deleted successfully"}