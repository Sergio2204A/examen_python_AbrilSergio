class Chef:
    def __init__(self, Chef_id, name, specialization):
        self.id = Chef_id
        self.name = name 
        self.specilization = specialization

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.name,
            "especialidad": self.specilization
        }