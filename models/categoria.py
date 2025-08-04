class Categoria:
    def __init__(self, Categoria_id, name, description):
        self.id = Categoria_id
        self.name = name 
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.name,
            "descripcion": self.description,
        }