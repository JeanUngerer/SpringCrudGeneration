def generate_equipment_service_class(equipment_entity_file):
    with open(equipment_entity_file, 'r') as file:
        entity_code = file.read()

    class_name = get_class_name(entity_code)
    project_name = get_project_name(entity_code)

    service_class = generate_class_code(class_name, project_name)
    write_to_file(service_class, class_name)


def get_class_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    class_name = class_name[:-6]
    return class_name


def get_project_name(entity_code):
    package_start_index = entity_code.index("package") + len("package")
    package_end_index = entity_code.index(".entities")
    project_name = entity_code[package_start_index:package_end_index].strip()
    return project_name


def generate_class_code(class_name, project):
    name_lower = class_name[0].lower() + class_name[1:-1]
    package = f"package {project}.services;\n\n"
    imports = f"import {project}.DTOs.{class_name}DTO;\n"
    imports += f"import {project}.exception.ExceptionHandler;\n"
    imports += f"import {project}.helpers.CycleAvoidingMappingContext;\n"
    imports += f"import {project}.mappers.{class_name}Mapper;\n"
    imports += f"import {project}.models.{class_name};\n"
    imports += f"import {project}.repositories.{class_name}Repository;\n"
    imports += f"import lombok.AccessLevel;\n"
    imports += f"import lombok.RequiredArgsConstructor;\n"
    imports += f"import lombok.experimental.FieldDefaults;\n"
    imports += f"import lombok.extern.log4j.Log4j2;\n"
    imports += f"import org.springframework.stereotype.Service;\n"
    imports += f"import org.springframework.transaction.annotation.Transactional;\n"
    imports += f"import java.util.ArrayList;\n"
    imports += f"import java.util.List;\n\n"

    class_definition = f"@Service\n"
    class_definition += f"@RequiredArgsConstructor\n"
    class_definition += f"@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)\n"
    class_definition += f"@Log4j2\n"
    class_definition += f"@Transactional\n"
    class_definition += f"public class {class_name}Service {{\n\n"
    class_definition += f"\t{class_name}Repository {name_lower}Repository;\n\n"
    class_definition += f"\t{class_name}Mapper {name_lower}Mapper;\n\n"
    class_definition += f"\tpublic List<{class_name}> findAll{class_name}() {{\n"
    class_definition += f"\t\ttry {{\n"
    class_definition += f"\t\t\tlog.info(\"findAll{class_name}\");\n"
    class_definition += f"\t\t\tList<{class_name}> {name_lower}List = new ArrayList<{class_name}>();\n"
    class_definition += f"\t\t\t{name_lower}Repository.findAll().forEach(ct -> {name_lower}List.add({name_lower}Mapper.entityToModel(ct)));\n"
    class_definition += f"\t\t\treturn {name_lower}List;\n"
    class_definition += f"\t\t}} catch (Exception e) {{\n"
    class_definition += f"\t\t\tlog.error(\"We could not find all {name_lower}: \" + e.getMessage());\n"
    class_definition += f"\t\t\tthrow new ExceptionHandler(\"We could not find your {name_lower}s\");\n"
    class_definition += f"\t\t}}\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\tpublic {class_name} find{class_name}ById(Long id) {{\n"
    class_definition += f"\t\ttry {{\n"
    class_definition += f"\t\t\tlog.info(\"find{class_name}ById - id: \" + id.toString());\n"
    class_definition += f"\t\t\t{class_name} {name_lower} = {name_lower}Mapper.entityToModel({name_lower}Repository.findById(id).orElseThrow(()\n"
    class_definition += f"\t\t\t\t-> new ExceptionHandler(\"We didn't find your {name_lower}\")));\n"
    class_definition += f"\t\t\treturn {name_lower};\n"
    class_definition += f"\t\t}} catch (Exception e) {{\n"
    class_definition += f"\t\t\tlog.error(\"We could not find all {name_lower}: \" + e.getMessage());\n"
    class_definition += f"\t\t\tthrow new ExceptionHandler(\"We could not find your {name_lower}\");\n"
    class_definition += f"\t\t}}\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\tpublic {class_name} create{class_name}({class_name}DTO dto) {{\n"
    class_definition += f"\t\ttry {{\n"
    class_definition += f"\t\t\tlog.info(\"create{class_name}\");\n"
    class_definition += f"\t\t\t{class_name} {name_lower} = {name_lower}Mapper.dtoToModel(dto);\n"
    class_definition += f"\t\t\t{name_lower}Repository.save({name_lower}Mapper.modelToEntity({name_lower}));\n"
    class_definition += f"\t\t\treturn {name_lower};\n"
    class_definition += f"\t\t}} catch (Exception e) {{\n"
    class_definition += f"\t\t\tlog.error(\"Couldn't {name_lower} user: \" + e.getMessage());\n"
    class_definition += f"\t\t\tthrow new ExceptionHandler(\"We could not create your {name_lower}\");\n"
    class_definition += f"\t\t}}\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\tpublic {class_name} update{class_name}({class_name}DTO dto) {{\n"
    class_definition += f"\t\ttry {{\n"
    class_definition += f"\t\t\tlog.info(\"update{class_name} - id: \" + dto.getId().toString());\n"
    class_definition += f"\t\t\t{class_name} {name_lower} = {name_lower}Mapper.entityToModel({name_lower}Repository.findById(dto.getId()).orElseThrow(()\n"
    class_definition += f"\t\t\t\t-> new ExceptionHandler(\"We could not find your {name_lower}\")));\n"
    class_definition += f"\t\t\t{name_lower}Mapper.updateFromDto(dto, {name_lower}, new CycleAvoidingMappingContext());\n"
    class_definition += f"\t\t\t{name_lower}Repository.save({name_lower}Mapper.modelToEntity({name_lower}));\n"
    class_definition += f"\t\t\treturn {name_lower};\n"
    class_definition += f"\t\t}} catch (Exception e) {{\n"
    class_definition += f"\t\t\tlog.error(\"Couldn't update user: \" + e.getMessage());\n"
    class_definition += f"\t\t\tthrow new ExceptionHandler(\"We could not update your {name_lower}\");\n"
    class_definition += f"\t\t}}\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\tpublic String delete{class_name}(Long id) {{\n"
    class_definition += f"\t\ttry {{\n"
    class_definition += f"\t\t\tlog.info(\"delete{class_name} - id: \" + id.toString());\n"
    class_definition += f"\t\t\t{class_name} {name_lower} = {name_lower}Mapper.entityToModel({name_lower}Repository.findById(id).orElseThrow(()\n"
    class_definition += f"\t\t\t\t-> new ExceptionHandler(\"We could not find your {name_lower}\")));\n"
    class_definition += f"\t\t\t{name_lower}Repository.delete({name_lower}Mapper.modelToEntity({name_lower}));\n"
    class_definition += f"\t\t\treturn \"{class_name} deleted\";\n"
    class_definition += f"\t\t}} catch (Exception e) {{\n"
    class_definition += f"\t\t\tlog.error(\"Couldn't delete {name_lower}: \" + e.getMessage());\n"
    class_definition += f"\t\t\tthrow new ExceptionHandler(\"We could not delete your {name_lower}\");\n"
    class_definition += f"\t\t}}\n"
    class_definition += f"\t}}\n"
    class_definition += f"}}\n"

    class_code = package + imports + class_definition
    return class_code

def write_to_file(class_code, class_name):
    output_file = class_name + "Service.java"
    with open(output_file, 'w') as file:
        file.write(class_code)
    print(f"Java file '{output_file}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = "tests/UserEntity.java"
#generate_equipment_service_class(equipment_entity_file)
