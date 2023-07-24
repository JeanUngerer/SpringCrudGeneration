import re

def generate_typescript_interface(equipment_entity_file):
    with open(equipment_entity_file, 'r') as file:
        entity_code = file.read()

    interface_name = get_interface_name(entity_code)
    interface_properties = get_interface_properties(entity_code)

    interface_model = generate_interface_model(interface_name, interface_properties)
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
    print(properties)

    data = [('Long', 'id'), ('String', 'name'), ('String', 'type'), ('String', 'effects'),
            ('List<SpecialRuleEntity>', 'specialRules')]

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

    print(properties)

    return properties

def generate_interface_model(interface_name, interface_properties):
    interface_model = f"export interface {interface_name} {{\n"
    for prop_type, prop_name in interface_properties:
        interface_model += f"\t{prop_name}: {prop_type};\n"
    interface_model += "}\n"
    return interface_model

def write_to_file(interface_model, interface_name):
    output_file = interface_name + ".ts"
    with open(output_file, 'w') as file:
        file.write(interface_model)
    print(f"TypeScript interface file '{output_file}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = "tests/EquipmentEntity.java"
generate_typescript_interface(equipment_entity_file)
