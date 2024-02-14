import os
import javaCommon as jCommon


def generate_class(entity_file):
    with open(entity_file, 'r') as file:
        entity_code = file.read()

    class_name = jCommon.get_class_name(entity_code)
    project_name = jCommon.get_project_name(entity_code)
    fields = get_fields(entity_code)

    equipment_class = generate_class_code(class_name, fields, project_name)
    write_to_file(equipment_class, class_name)

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

def generate_class_code(class_name, fields, project):
    package = f"package {project}.services;\n\n"
    imports = "import java.time.LocalDateTime;\n"
    imports += "import java.util.List;\n\n"
    imports += f"import lombok.AccessLevel;\n"
    imports += f"import lombok.Getter;\n"
    imports += f"import lombok.Setter;\n"
    imports += f"import lombok.NoArgsConstructor;\n"
    imports += f"import lombok.AllArgsConstructor;\n"
    imports += f"import lombok.Experimental.FieldDefaults;\n"
    imports += f"\n"
    class_definition = f"@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = false)\n"
    class_definition += f"@Getter\n"
    class_definition += f"@Setter\n"
    class_definition += f"@NoArgsConstructor\n"
    class_definition += f"@AllArgsConstructor\n"
    class_definition += f"public class {class_name} {{\n\n"
    fields_definition = "\n".join([field for field in fields if '@' not in field]).replace('Entity', '') + "\n\n"
    class_code = package + imports + class_definition + fields_definition + "}"
    return class_code

def write_to_file(class_code, class_name):
    path = "./models"
    output_file = path + "/" + class_name + ".java"

    # Check whether the specified path exists or not

    if not os.path.exists(path):
        # Create a new directory because it does not exist
        os.makedirs(path)
    with open(output_file, 'w') as file:
        file.write(class_code)
    print(f"Java file '{output_file}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = "notInTests/EquipmentEntity.java"
#generate_equipment_class(equipment_entity_file)
