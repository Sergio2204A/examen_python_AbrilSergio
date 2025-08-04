class Ingredient :
    def __init__(self, ingredient_id, name, description, price, stock):
        self.id = ingredient_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.name,
            "description": self.description,
            "precio": self.price,
            "stock" : self.stock
        }