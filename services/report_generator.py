class ReportGenerator:
    def _init_(self, manager):
        self.manager = manager
        self.data = manager.data

    def generate_reports(self):
        print("--- Generando Reportes ---")

        low_stock_ingredientes = [ing for ing in self.data["ingredientes"] if ing["stock"] < 400]
        print("\na. Ingredientes con stock < 400:")
        print([ing["nombre"] for ing in low_stock_ingredientes])
        
        hamburguesas_veg = [h for h in self.data["hamburguesas"] if h["categoria"] == "Vegetariana"]
        print("\nb. Hamburguesas de la categoría 'Vegetariana':")
        print([h["nombre"] for h in hamburguesas_veg])
        
        chefs_carnes = [c for c in self.data["chefs"] if c["especialidad"] == "Carnes"]
        print("\nc. Chefs especializados en 'Carnes':")
        print([c["nombre"] for c in chefs_carnes])

        for h in self.data["hamburguesas"]:
            h["precio"] += 1.5
        self.manager._save_data()
        print("\nd. Precio de todas las hamburguesas aumentado en $1.5.")

        hamburguesas_chef_b = [h for h in self.data["hamburguesas"] if h["chef"] == "Chef B"]
        print("\ne. Hamburguesas preparadas por 'Chef B':")
        print([h["nombre"] for h in hamburguesas_chef_b])

        print("\nf. Nombre y descripción de todas las categorías:")
        for cat in self.data["categorias"]:
            print(f" - {cat['nombre']}: {cat['descripcion']}")

        stock_seis = [ing for ing in self.data["ingredientes"] if ing["stock"] == 6]
        print("\ng. Ingredientes con stock de 6:")
        print([ing["nombre"] for ing in stock_seis])
        
        for h in self.data["hamburguesas"]:
            if h["nombre"] == "Clásica":
                h["precio"] *= 1.15
        self.manager._save_data()
        print("\nh. Precio de la hamburguesa 'Clásica' aumentado en 15%.")

        # --- Consultas Complejas ---

        # i. Hamburguesas con "Pan Integral"
        hamburguesas_pan_integral = [h for h in self.data["hamburguesas"] if "Pan Integral" in h["ingredientes"]]
        print("\ni. Hamburguesas con 'Pan Integral':")
        print([h["nombre"] for h in hamburguesas_pan_integral])

        # j. Contar hamburguesas en "Gourmet" o "Cocina Internacional"
        conteo_categorias = sum(1 for h in self.data["hamburguesas"] if h["categoria"] in ["Gourmet", "Cocina Internacional"])
        print(f"\nj. Total de hamburguesas en 'Gourmet' o 'Cocina Internacional': {conteo_categorias}")

        # k. Ingrediente más caro
        ingrediente_mas_caro = max(self.data["ingredientes"], key=lambda x: x["precio"])
        print(f"\nk. Ingrediente más caro: {ingrediente_mas_caro['nombre']} (Precio: {ingrediente_mas_caro['precio']})")

        # l. Hamburguesas sin "Queso cheddar"
        hamburguesas_sin_queso = [h for h in self.data["hamburguesas"] if "Queso cheddar" not in h["ingredientes"]]
        print("\nl. Hamburguesas sin 'Queso cheddar':")
        print([h["nombre"] for h in hamburguesas_sin_queso])

        # m. Incrementar stock de "Pan" en 100
        for ing in self.data["ingredientes"]:
            if ing["nombre"] == "Pan":
                ing["stock"] += 100
        self.manager._save_data()
        print("\nm. Stock de 'Pan' incrementado en 100 unidades.")

        # n. Eliminar hamburguesas con menos de 3 ingredientes
        self.manager.data["hamburguesas"] = [h for h in self.data["hamburguesas"] if len(h["ingredientes"]) >= 3]
        self.manager._save_data()
        print("\nn. Hamburguesas con menos de 3 ingredientes eliminadas.")

        # o. Asignar especialidad a "Chef B"
        for chef in self.data["chefs"]:
            if chef["nombre"] == "Chef B":
                chef["especialidad"] = "Cocina Asiática"
        self.manager._save_data()
        print("\no. Especialidad de 'Chef B' actualizada a 'Cocina Asiática'.")

        # p. Listar hamburguesas por precio ascendente
        hamburguesas_ordenadas = sorted(self.data["hamburguesas"], key=lambda x: x["precio"])
        print("\np. Hamburguesas listadas por precio ascendente:")
        for h in hamburguesas_ordenadas:
            print(f" - {h['nombre']}: ${h['precio']}")

        # q. Ingredientes con precio entre $2 y $5
        ingredientes_rango = [ing for ing in self.data["ingredientes"] if 2 <= ing["precio"] <= 5]
        print("\nq. Ingredientes con precio entre $2 y $5:")
        print([ing["nombre"] for ing in ingredientes_rango])

        # r. Actualizar descripción de "Pan"
        for ing in self.data["ingredientes"]:
            if ing["nombre"] == "Pan":
                ing["descripcion"] = "Pan fresco y crujiente"
        self.manager._save_data()
        print("\nr. Descripción de 'Pan' actualizada.")

        # s. Hamburguesa más cara de un chef especializado en "Carnes"
        chefs_carnes = [c['nombre'] for c in self.data["chefs"] if c['especialidad'] == "Carnes"]
        hamburguesas_chef_carnes = [h for h in self.data["hamburguesas"] if h['chef'] in chefs_carnes]
        if hamburguesas_chef_carnes:
            hamburguesa_mas_cara = max(hamburguesas_chef_carnes, key=lambda x: x["precio"])
            print(f"\ns. Hamburguesa más cara de un chef de 'Carnes': {hamburguesa_mas_cara['nombre']} (Precio: ${hamburguesa_mas_cara['precio']})")
        else:
            print("\ns. No se encontraron hamburguesas de chefs especializados en 'Carnes'.")
            
        # t. Ingredientes con su conteo en hamburguesas
        ingrediente_conteo = {}
        for h in self.data["hamburguesas"]:
            for ing_nombre in h["ingredientes"]:
                ingrediente_conteo[ing_nombre] = ingrediente_conteo.get(ing_nombre, 0) + 1
        print("\nt. Conteo de ingredientes en hamburguesas:")
        for ing, count in ingrediente_conteo.items():
            print(f" - {ing}: {count}")