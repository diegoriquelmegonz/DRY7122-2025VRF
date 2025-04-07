import yaml


with open("eva1.yaml", "r") as archivo:
    archivo_yaml = archivo.read()


parseoyaml = yaml.safe_load(archivo_yaml)


print("ID Usuario:", parseoyaml.get("id_usuario"))
print("Token de Seguridad:", parseoyaml.get("token_seguridad"))
print("Fecha de Creación:", parseoyaml.get("fecha_creacion"))
print("Estado:", parseoyaml.get("estado"))
