def generate_equipment_mapper_class(equipment_entity_file):
    with open(equipment_entity_file, 'r') as file:
        entity_code = file.read()

    class_name = get_class_name(entity_code)

    mapper_class = generate_class_code(class_name)
    write_to_file(mapper_class, class_name)

def get_class_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    return class_name

def generate_class_code(class_name):
    imports = "import org.mapstruct.*;\n\n"
    class_definition = f"@Mapper(unmappedSourcePolicy = ReportingPolicy.WARN, unmappedTargetPolicy = ReportingPolicy.WARN,\n" \
                       f"\ttypeConversionPolicy = ReportingPolicy.IGNORE, componentModel = \"spring\")\n" \
                       f"public interface {class_name}Mapper {{\n\n" \
                       f"\t{class_name}DTO modelToDto({class_name} model);\n\n" \
                       f"\tList<{class_name}DTO> modelsToDtos(List<{class_name}> model);\n\n" \
                       f"\t{class_name} dtoToModel({class_name}DTO dto);\n\n" \
                       f"\tList<{class_name}> dtosToModels(List<{class_name}DTO> dtos);\n\n" \
                       f"\t{class_name}Entity modelToEntity({class_name} model);\n\n" \
                       f"\tList<{class_name}Entity> modelsToEntities(List<{class_name}> models);\n\n" \
                       f"\t{class_name} entityToModel({class_name}Entity entity);\n\n" \
                       f"\tList<{class_name}> entitiesToModel(List<{class_name}Entity> entities);\n\n" \
                       f"\t@BeanMapping(nullValuePropertyMappingStrategy = NullValuePropertyMappingStrategy.IGNORE)\n" \
                       f"\tvoid updateFromModel({class_name} model, @MappingTarget {class_name}Entity entity, @Context CycleAvoidingMappingContext cycleAvoidingMappingContext);\n\n" \
                       f"\tvoid updateFromDto({class_name}DTO dto, @MappingTarget {class_name} model, @Context CycleAvoidingMappingContext cycleAvoidingMappingContext);\n" \
                       f"}}"

    class_code = imports + class_definition
    return class_code

def write_to_file(class_code, class_name):
    output_file = class_name + "Mapper.java"
    with open(output_file, 'w') as file:
        file.write(class_code)
    print(f"Java file '{output_file}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = "EquipmentEntity.java"
#generate_equipment_mapper_class(equipment_entity_file)
