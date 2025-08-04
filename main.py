from services.restaurant_manager import RestaurantManager
from services.report_generator import ReportGenerator
from models.categoria import Categoria
from models.ingrediente import Ingredient
from models.chef import Chef
from models.hamburguesas import hamburguer

if __name__ == "__main__":
    manager = RestaurantManager
    manager.create_item("ingredientes", Ingredient(1,"Pan","Pan brioche", 2.5, 500))
    manager.create_item("ingredientes", Ingredient(2,"carne de res", "Carne Angus", 8.0, 350))
    manager.create_item("ingredientes", Ingredient(3,"Queso cheddar", "Queso americano", 3.0, 450))
    manager.create_item("ingredientes", Ingredient(4,"Lechuga", "Lechuga romana", 1.5, 6))
    manager.create_item("ingredientes", Ingredient(5,"pan integral", "pan integral artesanal", 3.5, 200))

    manager.create_item("categorias",Categoria(1, "Clasica", "Hamburguesas tradicionales"))
    manager.create_item("categorias",Categoria(1, "Vegetariana", "Hamburguesas sin carne"))
    manager.create_item("categorias",Categoria(1, "Gourmet", "Hamburguesas premium"))

    manager.create_item("chefs", Chef(1, "chef A", "carnes"))
    manager.create_item("chefs", Chef(1, "chef B", "carnes"))

    manager.create_item("hamburguesas", hamburguer(1, "Clasica", "Clasica",["Pan", "Carne de res", "queso cheddar"],12.0, "chef A"))
    manager.create_item("hamburguesas", hamburguer(2, "Vaggie Burguer", "vegetariana",["Pan integral", "Lechuga"],10.0, "chef A"))
    manager.create_item("hamburguesas", hamburguer(3, "Hamburguesa Gourmet", "Gourmet",["Pan Brioche", "Carne de Res", "Queso","Bacon"],18.0, "chef B"))
    print("Datos iniciales creados y guardados")

def mostrar_menu():
    print("------Menu de gestion-------      ")
    print("1 Crear datos iniciales           ")
    print("2 ver todos los ingredientes      ")
    print("3 ver todas las hamburguesas      ")
    print("4 Generar todos los reportes      ")
    print("5 Salir                           ")
    return input("elige una opcion del 1-5 : ")

if __name__ == "__main__":
    manager = RestaurantManager()
    report_generator = ReportGenerator(manager)

    while True:
        opcion = mostrar_menu()
         
        if opcion == "1":
            crear_datos_iniciales(manager)
        elif opcion == "2":
            ingredientes = manager.read_item("hamburguesas")
            print("----listado de ingredientes-----")
            for h in ingredientes:
                