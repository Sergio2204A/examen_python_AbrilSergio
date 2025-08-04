class hamburguer:
    def __init__(self, hamburguesa_id, name, categoria, ingredientes, precio, chef):
        self.id = hamburguesa_id
        self.name = name
        self.categoria = categoria
        self.ingredientes = ingredientes
        self.precio = precio
        self.chef = chef

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.name,
            "categoria": self.categoria,
            "ingredientes": self.ingredientes,
            "precio": self.precio,
            "chef" : self.chef
        }