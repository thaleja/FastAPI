# Importar el método FastAPI
from fastapi import FastAPI,HTTPException

# Instalar la aplicación FastAPI
app = FastAPI()

# Definir las rutas o endPoints
# Home
@app.get("/")
async def home():
    return {"message": "Estamos en el home"}

# About

@app.get("/about")
async def about():
    return {"message": "Estamos en la página de acerca de"}

# Pedir dato en la ruta de empleado
@app.get("/empleado/{idemployee}")
async def employee(idemployee):
    if idemployee == "1":
        return {"perfil": "administrador"}
    else:
        return {"perfil": "usuario"}       
    
# Petición de varios datos en la ruta de product
@app.get("/product/{codprod}/{name}")
async def product(codprod, name):
    return {"product": str(codprod) + " " + name}
