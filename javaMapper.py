import os

import javaCommon as jCommon

import re






def extract_single_entity_attributes(class_string):
    # Enhanced to capture any amount of whitespace between types and variable names
    pattern = r'(@(ManyToOne|OneToOne)[\s\S]*?)(@JoinColumn[\s\S]*?)?(public|private|protected)?\s[A-Z]\w+'
    matches = re.findall(pattern, class_string)
    print('Matches : ', matches)
    attribute_names = [match[1].split(' ')[-1] for match in matches]
    return attribute_names


def extract_collection_entity_attributes(class_string):
    # Enhanced to capture any amount of whitespace between generic types and variable names
    pattern = r'@(OneToMany|ManyToMany).*?\s+List<\w+>\s+\w*;\s*(\w+)\s*;'
    matches = re.findall(pattern, class_string)
    attribute_names = [match[1] for match in matches]
    return attribute_names




def generate_equipment_mapper_class(equipment_entity_file):
    with open(equipment_entity_file, 'r') as file:
        entity_code = file.read()

    class_name = jCommon.get_class_name(entity_code)
    project_name = jCommon.get_project_name(entity_code)
    classSubEntityList = []
    classSubEntitiesSerieList = []

    mapper_class = generate_class_code(class_name, project_name, classSubEntityList, classSubEntitiesSerieList)
    write_to_file(mapper_class, class_name)

def get_class_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    return class_name

def generate_class_code(class_name, project, classSubEntityList = [], classSubEntitiesSerieList = []):
    package = f"package {project}.mappers;\n\n"

    imports = "import org.mapstruct.*;\n"
    imports += f"import {project}.helpers.CycleAvoidingMappingContext;\n\n"
    imports += f"import {project}.entities.{class_name}Entity;\n"
    imports += f"import {project}.dtos.{class_name}DTO;\n"
    imports += f"import {project}.models.{class_name};\n\n"
    class_definition = f"@Mapper(unmappedSourcePolicy = ReportingPolicy.WARN, unmappedTargetPolicy = ReportingPolicy.WARN,\n" \
                       f"\ttypeConversionPolicy = ReportingPolicy.IGNORE, componentModel = \"spring\")\n" \
                       f"@Named(\"{class_name}Mapper\")\n" \
                       f"public interface {class_name}Mapper {{\n\n" \
                       f"\t{class_name}DTO modelToDto({class_name} model);\n\n" \
                       f"\tList<{class_name}DTO> modelsToDtos(List<{class_name}> models);\n\n" \
                       f"\t{class_name} dtoToModel({class_name}DTO dto);\n\n" \
                       f"\tList<{class_name}> dtosToModels(List<{class_name}DTO> dtos);\n\n" \
                       f"\t{class_name}Entity modelToEntity({class_name} model);\n\n" \
                       f"\tList<{class_name}Entity> modelsToEntities(List<{class_name}> models);\n\n" \
                       f"\t{class_name} entityToModel({class_name}Entity entity);\n\n" \
                       f"\tList<{class_name}> entitiesToModel(List<{class_name}Entity> entities);\n\n" \
                       f"\t@BeanMapping(nullValuePropertyMappingStrategy = NullValuePropertyMappingStrategy.IGNORE)\n" \
                       f"\tvoid updateFromModel({class_name} model, @MappingTarget {class_name}Entity entity, @Context CycleAvoidingMappingContext cycleAvoidingMappingContext);\n\n" \
                       f"\tvoid updateFromDto({class_name}DTO dto, @MappingTarget {class_name} model, @Context CycleAvoidingMappingContext cycleAvoidingMappingContext);\n" \
                       f"\n" \
                       f"}}"


    class_code = package + imports + class_definition
    return class_code

def write_to_file(class_code, class_name):
    path = "./mappers"
    output_file = path + "/" + class_name + "Mapper.java"

    # Check whether the specified path exists or not

    if not os.path.exists(path):
        # Create a new directory because it does not exist
        os.makedirs(path)
    with open(output_file, 'w') as file:
        file.write(class_code)
    print(f"Java file '{output_file}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = 'tests/' + "EquipmentEntity.java"
#generate_equipment_mapper_class(equipment_entity_file)


# Read the content of the equipment_entity_file
with open(equipment_entity_file, 'r') as file:
    entity_code = file.read()
    print(entity_code)

# Test extract_single_entity_attributes
result_single = extract_single_entity_attributes(entity_code)
print("Result of extract_single_entity_attributes: ", result_single)

# Test extract_collection_entity_attributes
result_collection = extract_collection_entity_attributes(entity_code)
print("Result of extract_collection_entity_attributes: ", result_collection)
