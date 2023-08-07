import re
import os

def generate_typescript_interface(interface_name, primitive_properties, non_primitive_properties):

    interface_properties = primitive_properties
    if len(non_primitive_properties) != 0:
        interface_properties += non_primitive_properties
    interface_model = generate_interface_model(interface_name, interface_properties, non_primitive_properties)
    write_to_file(interface_model, interface_name)

def get_interface_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    interface_name = class_name[:-6]
    return interface_name

def get_interface_properties(entity_code):
    properties = re.findall(r"@Column\(.+\)\s+(\w+)\s+(\w+);", entity_code)
    properties += re.findall(r"@JoinColumn\(.+\)\s+(\w+)\s+(\w+);", entity_code)
    properties += re.findall(r"@JoinColumn\(.+\)\s+(\w+<[^>]+>)\s+(\w+);", entity_code)

    replacements = {
        'Long': 'number',
        'int': 'number',
        'double': 'number',
        'String': 'string',
        'Entity': ''
    }

    for i in range(len(properties)):
        properties_type, var_name = properties[i]

        # Replace properties type
        for old_type, new_type in replacements.items():
            properties_type = properties_type.replace(old_type, new_type)

        # Replace List<*>
        if 'List<' in properties_type and '>' in properties_type:
            properties_type = properties_type.replace('List<', '').replace('>', '[]')

        properties[i] = (properties_type, var_name)


    return properties

def generate_interface_model(interface_name, interface_properties, non_primitive_properties):
    interface_model = f''
    for prop_type, prop_name in non_primitive_properties:
        prop_type = prop_type.translate({ord(i): None for i in '[]'})
        print(prop_type)
        interface_model += "import {" + f"{prop_type}" + "}" + f" from './{prop_type}.model';\n"
    interface_model += f"\n"
    interface_model += f"export interface {interface_name} {{\n"

    for prop_type, prop_name in interface_properties:
        interface_model += f"\t{prop_name}: {prop_type};\n"
    interface_model += "}\n"
    return interface_model

def write_to_file(interface_model, interface_name):
    path = "./angularTestUI/src/app/test/models"

    output_file = path + "/" + interface_name  + ".model.ts"


    # Check whether the specified path exists or not

    if not os.path.exists(path):
        # Create a new directory because it does not exist
        os.makedirs(path)

    with open(output_file, 'w') as file:
        file.write(interface_model)

# Provide the path to the EquipmentEntity class file
## equipment_entity_file = "tests/EquipmentEntity.java"
## generate_typescript_interface(equipment_entity_file)
