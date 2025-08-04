from services.restaurant_manager import RestaurantManager
from services.report_generator import ReportGenerator
from models.ingredientes import Ingredient
from models.categoria import Categoria
from models.chef import Chef
from models.hamburguesas import hamburguer

def crear_datos_iniciales(manager):
    """Función para crear datos de ejemplo en el sistema."""
    print("\nCreando datos iniciales...")
    
    # Creación de Ingredientes
    manager.create_item("ingredientes", Ingredient(1, "Pan", "Pan brioche", 2.5, 500))
    manager.create_item("ingredientes", Ingredient(2, "Carne de Res", "Carne Angus", 8.0, 350))
    manager.create_item("ingredientes", Ingredient(3, "Queso cheddar", "Queso americano", 3.0, 450))
    manager.create_item("ingredientes", Ingredient(4, "Lechuga", "Lechuga romana", 1.5, 6))
    manager.create_item("ingredientes", Ingredient(5, "Pan Integral", "Pan integral artesanal", 3.5, 200))

    # Creación de Categorías
    manager.create_item("categorias", Categoria(1, "Clásica", "Hamburguesas tradicionales"))
    manager.create_item("categorias", Categoria(2, "Vegetariana", "Hamburguesas sin carne"))
    manager.create_item("categorias", Categoria(3, "Gourmet", "Hamburguesas premium"))

    # Creación de Chefs
    manager.create_item("chefs", Chef(1, "Chef A", "Carnes"))
    manager.create_item("chefs", Chef(2, "Chef B", "Carnes"))

    # Creación de Hamburguesas
    manager.create_item("hamburguesas", hamburguesas(1, "Clásica", "Clásica", ["Pan", "Carne de Res", "Queso cheddar"], 12.0, "Chef A"))
    manager.create_item("hamburguesas", hamburguesas(2, "Veggie Burger", "Vegetariana", ["Pan Integral", "Lechuga"], 10.0, "Chef A"))
    manager.create_item("hamburguesas", hamburguesas(3, "Hamburguesa Gourmet", "Gourmet", ["Pan Brioche", "Carne de Res", "Queso", "Bacon"], 18.0, "Chef B"))
    
    print("Datos iniciales creados y guardados.")

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Menú de Gestión del Restaurante ---")
    print("1. Crear datos iniciales")
    print("2. Ver todos los ingredientes")
    print("3. Ver todas las hamburguesas")
    print("4. Generar todos los reportes")
    print("5. Salir")
    return input("Elige una opción: ")

if __name__ == "__main__":
    manager = RestaurantManager()
    report_generator = ReportGenerator(manager)

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            crear_datos_iniciales(manager)
        elif opcion == "2":
            ingredientes = manager.read_items("ingredientes")
            print("\n--- Listado de Ingredientes ---")
            for ing in ingredientes:
                print(f"ID: {ing['id']}, Nombre: {ing['nombre']}, Precio: ${ing['precio']}, Stock: {ing['stock']}")
        elif opcion == "3":
            hamburguesas = manager.read_items("hamburguesas")
            print("\n--- Listado de Hamburguesas ---")
            for h in hamburguesas:
                print(f"ID: {h['id']}, Nombre: {h['nombre']}, Categoría: {h['categoria']}, Precio: ${h['precio']}")
        elif opcion == "4":
            report_generator.generate_reports()
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta pronto! ")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")