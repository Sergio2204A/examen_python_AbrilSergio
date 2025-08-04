import json
import os
 
class RestaurantManager:
    def __init__(self, data_file='data/data.json'):
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.data_file):
            with open (self.data_file, 'r' , encoding='uft-8') as f:
                return json.load(f)
            return {
                "ingredientes":[],
                "categorias": [],
                "chefs": [],
                "hamburguesas": []
            }
    def _save_data(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data,f, indent=4, ensure_ascii=False)

#---- funcionalidades CRUD 
    def create_item(self ,module, item):
        self.data[module].append(item.to_dict())
        self._save_data()
        print(f"{module.capitalize()} creado exitosamente ")

    def read_item(self, module):
        return self.data[module]
    
    def update_item(self, module, item_id, new_data):
        for i, item in enumerate(self.data[module]):
            if item.get('id') ==item_id:
                self.data[module][i].update(new_data)
                self._save_data()
                print(f"{module.capitalize()} actualizado correctamente")
                return True
            print(f"error : {module.capitalize()} con ID {item_id} no encontrado ")
            return False
    def delete_item(self, module, item_id):
        initial_len = len(self.data[module])
        self.data[module] = [item for item in self.data[module] if item.get('id') != item_id]
        if len (self.data[module]) < initial_len:
            self._save_data()
            print (f"{module.capitalize()} con ID {item_id} eliminado")
            return True
        print(f"error: {module.capitalize()} con ID {item_id} no encontrado")
        return False
    
    