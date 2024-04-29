import os

import angularModel as aModel
import angularService as aService
import angularList as aList
import angularModule as aModule
import angularRoutingModule as aRoutingModule
import angularAddToModules as aAddToModules
import javaService as jService
import javaMapper as jMapper
import javaDTO as jDTO
import javaModel as jModel
import javaController as jController
import javaRepository as jRepository



class ClassInfo:
    name = ""
    primitiveAttributes = []
    nonPrimitiveAttributes = []
    entity_code = ""

    def __init__(self, name, primitiveAttributes, nonPrimitiveAttributes, entity_code):
        self.name = name
        self.primitiveAttributes = primitiveAttributes
        self.nonPrimitiveAttributes = nonPrimitiveAttributes
        self.entity_code = entity_code

    def __str__(self):
        return f"{self.name}({self.primitiveAttributes}), ({self.nonPrimitiveAttributes}), \n({self.entity_code})"


listOfEntities = []

entityDirectory = './tests'

for root, dirs, files in os.walk(entityDirectory):
    for name in files:

        with open(entityDirectory + '/' + name, 'r') as file:
            entity_code = file.read()
        interface_name = aModel.get_interface_name(entity_code)
        properties = aModel.get_interface_properties(entity_code)
        interface_properties = []
        interface_non_primitive = []

        for prop in properties:
            if prop[0][0].isupper():
                interface_non_primitive.append(prop)
            else:
                interface_properties.append(prop)

        fileInfo = ClassInfo(interface_name, interface_properties, interface_non_primitive, entity_code)
        listOfEntities.append(fileInfo)

for infos in listOfEntities:
    #aModel.generate_typescript_interface(infos.name, infos.primitiveAttributes, infos.nonPrimitiveAttributes)
    #aService.generate_angular_service(infos.name, infos.entity_code)

    components = [infos.name + "ListComponent", infos.name + "DetailComponent", infos.name + "CreateComponent"]
    #aModule.create_angular_module(infos.name, components)

    #aRoutingModule.create_routing_module(infos.name, components)
    #aAddToModules.add_component_to_app_routing_module(infos.name)
    #aAddToModules.add_module_to_app_module(infos.name)

    path = 'tests/' + infos.name + 'Entity.java'
    #jService.generate_equipment_service_class(path)

    jMapper.generate_equipment_mapper_class(path)
    jDTO.generate_equipment_dto_class(path)
    #jModel.generate_class(path)
    #jController.generate_equipment_controller_class(path)
    #jRepository.generate_equipment_repository_class(path)



    aList.generate_angular_component(infos.name, infos.entity_code)
