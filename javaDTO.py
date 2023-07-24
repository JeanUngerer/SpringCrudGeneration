def generate_equipment_dto_class(equipment_entity_file):
    with open(equipment_entity_file, 'r') as file:
        entity_code = file.read()

    class_name = get_class_name(entity_code)
    fields = get_fields(entity_code)

    equipment_dto_class = generate_class_code(class_name, fields)
    write_to_file(equipment_dto_class, class_name)

def get_class_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    return class_name

def get_fields(entity_code):
    fields_start_index = entity_code.index("{") + 1
    fields_end_index = entity_code.index("}")
    fields_code = entity_code[fields_start_index:fields_end_index]
    fields = fields_code.split("\n")
    fields = [field.strip() for field in fields if field.strip()]
    return fields

def generate_class_code(class_name, fields):
    imports = "import java.util.List;\n\n"
    class_definition = f"public class {class_name}DTO {{\n\n"
    fields_definition = "\n".join(fields) + "\n\n"
    class_code = imports + class_definition + fields_definition + "}"
    return class_code

def write_to_file(class_code, class_name):
    output_file = class_name + "DTO.java"
    with open(output_file, 'w') as file:
        file.write(class_code)
    print(f"Java file '{output_file}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = "tests/EquipmentEntity.java"
generate_equipment_dto_class(equipment_entity_file)
