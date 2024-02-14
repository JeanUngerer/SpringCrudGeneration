import os

import javaCommon as jCommon

def generate_equipment_controller_class(equipment_entity_file):
    with open(equipment_entity_file, 'r') as file:
        entity_code = file.read()

    class_name = jCommon.get_class_name(entity_code)
    class_project = jCommon.get_project_name(entity_code)

    controller_class = generate_class_code(class_name, class_project)
    write_to_file(controller_class, class_name)

def get_class_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    return class_name

def generate_class_code(class_name, project):
    package = f"package {project}.controllers;\n\n"
    imports = f"import {project}.dtos.{class_name}DTO;\n"
    imports += f"import {project}.mappers.{class_name}Mapper;\n"
    imports += f"import {project}.services.{class_name}Service;\n"
    imports += f"import lombok.AccessLevel;\n"
    imports += f"import lombok.AllArgsConstructor;\n"
    imports += f"import lombok.experimental.FieldDefaults;\n"
    imports += f"import lombok.extern.slf4j.Slf4j;\n"
    imports += f"import org.springframework.beans.factory.annotation.Autowired;\n"
    imports += f"import org.springframework.http.ResponseEntity;\n"
    imports += f"import org.springframework.security.access.prepost.PreAuthorize;\n"
    imports += f"import org.springframework.web.bind.annotation.*;\n\n"
    imports += f"import java.util.List;\n\n"

    class_definition = f"@RestController\n"
    class_definition += f"@AllArgsConstructor\n"
    class_definition += f"@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)\n"
    class_definition += f"@Slf4j\n"
    class_definition += f"@RequestMapping(\"{class_name.lower()}\")\n"
    class_definition += f"public class {class_name}Controller {{\n\n"
    class_definition += f"\t@Autowired\n"
    class_definition += f"\t{class_name}Service {class_name.lower()}Service;\n\n"
    class_definition += f"\tprivate {class_name}Mapper {class_name.lower()}Mapper;\n\n"
    class_definition += f"\t@PreAuthorize(\"hasAuthority('SCOPE_ROLE_ADMIN')\")\n"
    class_definition += f"\t@GetMapping(\"/{class_name.lower()}s\")\n"
    class_definition += f"\tpublic ResponseEntity<List<{class_name}DTO>> get{class_name}s() {{\n"
    class_definition += f"\t\treturn ResponseEntity.ok({class_name.lower()}Mapper.modelsToDtos({class_name.lower()}Service.findAll{class_name}()));\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\t@PreAuthorize(\"hasAuthority('SCOPE_ROLE_ADMIN')\")\n"
    class_definition += "\t@GetMapping(\"/{id}\")\n"
    class_definition += f"\tpublic ResponseEntity<{class_name}DTO> get{class_name}ById(@PathVariable(\"id\") Long id) {{\n"
    class_definition += f"\t\treturn ResponseEntity.ok({class_name.lower()}Mapper.modelToDto({class_name.lower()}Service.find{class_name}ById(id)));\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\t@PreAuthorize(\"hasAuthority('SCOPE_ROLE_ADMIN')\")\n"
    class_definition += f"\t@PostMapping(\"/create\")\n"
    class_definition += f"\tpublic ResponseEntity<{class_name}DTO> create(@RequestBody {class_name}DTO {class_name.lower()}Dto) {{\n"
    class_definition += f"\t\treturn ResponseEntity.ok({class_name.lower()}Mapper.modelToDto({class_name.lower()}Service.create{class_name}({class_name.lower()}Dto)));\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\t@PreAuthorize(\"hasAuthority('SCOPE_ROLE_ADMIN')\")\n"
    class_definition += f"\t@PutMapping(\"/update\")\n"
    class_definition += f"\tpublic ResponseEntity<{class_name}DTO> update(@RequestBody {class_name}DTO {class_name.lower()}Dto) {{\n"
    class_definition += f"\t\treturn ResponseEntity.ok({class_name.lower()}Mapper.modelToDto({class_name.lower()}Service.update{class_name}({class_name.lower()}Dto)));\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\t@PreAuthorize(\"hasAuthority('SCOPE_ROLE_ADMIN')\")\n"
    class_definition += "\t@DeleteMapping(\"/{id}\")\n"
    class_definition += f"\tpublic ResponseEntity<String> delete(@PathVariable(\"id\") Long id) {{\n"
    class_definition += f"\t\treturn ResponseEntity.ok({class_name.lower()}Service.delete{class_name}(id));\n"
    class_definition += f"\t}}\n"
    class_definition += f"}}\n"

    class_code = package + imports + class_definition
    return class_code

def write_to_file(class_code, class_name):
    path = "./controllers"
    output_file = path + "/" + class_name + "Controller.java"

    # Check whether the specified path exists or not

    if not os.path.exists(path):
        # Create a new directory because it does not exist
        os.makedirs(path)
    with open(output_file, 'w') as file:
        file.write(class_code)
    print(f"Java file '{output_file}' generated successfully!")

# Provide the path to the {class_name}Entity class file
equipment_entity_file = "{class_name}Entity.java"
#generate_{class_name.lower()}_controller_class({class_name.lower()}_entity_file)
