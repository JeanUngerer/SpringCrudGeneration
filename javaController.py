def generate_equipment_controller_class(equipment_entity_file):
    with open(equipment_entity_file, 'r') as file:
        entity_code = file.read()

    class_name = get_class_name(entity_code)

    controller_class = generate_class_code(class_name)
    write_to_file(controller_class, class_name)

def get_class_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    return class_name

def generate_class_code(class_name):
    imports = "import com.oldhammer.fantasylistbuilder.DTOs.EquipmentDTO;\n"
    imports += "import com.oldhammer.fantasylistbuilder.auth.service.TokenService;\n"
    imports += "import com.oldhammer.fantasylistbuilder.mappers.EquipmentMapper;\n"
    imports += "import com.oldhammer.fantasylistbuilder.services.EquipmentService;\n"
    imports += "import lombok.AccessLevel;\n"
    imports += "import lombok.AllArgsConstructor;\n"
    imports += "import lombok.experimental.FieldDefaults;\n"
    imports += "import lombok.extern.slf4j.Slf4j;\n"
    imports += "import org.springframework.beans.factory.annotation.Autowired;\n"
    imports += "import org.springframework.http.ResponseEntity;\n"
    imports += "import org.springframework.security.access.prepost.PreAuthorize;\n"
    imports += "import org.springframework.web.bind.annotation.*;\n\n"
    imports += "import java.util.List;\n\n"

    class_definition = f"@RestController\n"
    class_definition += f"@AllArgsConstructor\n"
    class_definition += f"@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)\n"
    class_definition += f"@Slf4j\n"
    class_definition += f"@RequestMapping(\"equipment\")\n"
    class_definition += f"public class {class_name}Controller {{\n\n"
    class_definition += f"\t@Autowired\n"
    class_definition += f"\tEquipmentService equipmentService;\n\n"
    class_definition += f"\t@Autowired\n"
    class_definition += f"\tTokenService tokenService;\n\n"
    class_definition += f"\tprivate EquipmentMapper equipmentMapper;\n\n"
    class_definition += f"\t@PreAuthorize(\"hasAuthority('SCOPE_ROLE_ADMIN')\")\n"
    class_definition += f"\t@GetMapping(\"/equipments\")\n"
    class_definition += f"\tpublic ResponseEntity<List<EquipmentDTO>> getEquipments() {{\n"
    class_definition += f"\t\treturn ResponseEntity.ok(equipmentMapper.modelsToDtos(equipmentService.findAllEquipment()));\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\t@PreAuthorize(\"hasAuthority('SCOPE_ROLE_ADMIN')\")\n"
    class_definition += f"\t@GetMapping(\"/{class_name.lower()}Id\")\n"
    class_definition += f"\tpublic ResponseEntity<EquipmentDTO> get{class_name}ById(@PathVariable(\"id\") Long id) {{\n"
    class_definition += f"\t\treturn ResponseEntity.ok(equipmentMapper.modelToDto(equipmentService.findEquipmentById(id)));\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\t@PreAuthorize(\"hasAuthority('SCOPE_ROLE_ADMIN')\")\n"
    class_definition += f"\t@PutMapping(\"/create\")\n"
    class_definition += f"\tpublic ResponseEntity<EquipmentDTO> create(@RequestBody EquipmentDTO {class_name.lower()}Dto) {{\n"
    class_definition += f"\t\treturn ResponseEntity.ok(equipmentMapper.modelToDto(equipmentService.createEquipment({class_name.lower()}Dto)));\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\t@PreAuthorize(\"hasAuthority('SCOPE_ROLE_ADMIN')\")\n"
    class_definition += f"\t@PostMapping(\"/update\")\n"
    class_definition += f"\tpublic ResponseEntity<EquipmentDTO> update(@RequestBody EquipmentDTO {class_name.lower()}Dto) {{\n"
    class_definition += f"\t\treturn ResponseEntity.ok(equipmentMapper.modelToDto(equipmentService.updateEquipment({class_name.lower()}Dto)));\n"
    class_definition += f"\t}}\n\n"
    class_definition += f"\t@PreAuthorize(\"hasAuthority('SCOPE_ROLE_ADMIN')\")\n"
    class_definition += f"\t@DeleteMapping(\"/{class_name.lower()}Id\")\n"
    class_definition += f"\tpublic ResponseEntity<String> delete(@PathVariable(\"id\") Long id) {{\n"
    class_definition += f"\t\treturn ResponseEntity.ok(equipmentService.deleteEquipment(id));\n"
    class_definition += f"\t}}\n"
    class_definition += f"}}\n"

    class_code = imports + class_definition
    return class_code

def write_to_file(class_code, class_name):
    output_file = class_name + "Controller.java"
    with open(output_file, 'w') as file:
        file.write(class_code)
    print(f"Java file '{output_file}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = "EquipmentEntity.java"
#generate_equipment_controller_class(equipment_entity_file)
