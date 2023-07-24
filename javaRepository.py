def generate_equipment_repository_class(equipment_entity_file):
    with open(equipment_entity_file, 'r') as file:
        entity_code = file.read()

    class_name = get_class_name(entity_code)

    repository_class = generate_class_code(class_name)
    write_to_file(repository_class, class_name)

def get_class_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    return class_name

def generate_class_code(class_name):
    imports = "import org.springframework.data.jpa.repository.JpaRepository;\n"
    entity_import = f"import com.oldhammer.fantasylistbuilder.entities.{class_name}Entity;\n\n"
    class_definition = f"public interface {class_name}Repository extends JpaRepository<{class_name}Entity, Long> {{\n}}"
    class_code = imports + entity_import + class_definition
    return class_code

def write_to_file(class_code, class_name):
    output_file = class_name + "Repository.java"
    with open(output_file, 'w') as file:
        file.write(class_code)
    print(f"Java file '{output_file}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = "EquipmentEntity.java"
generate_equipment_repository_class(equipment_entity_file)
