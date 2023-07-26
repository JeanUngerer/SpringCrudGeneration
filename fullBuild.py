import os

import angularModel as aModel
import angularService as aService
import angularList as aList


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
    aModel.generate_typescript_interface(infos.name, infos.primitiveAttributes, infos.nonPrimitiveAttributes)
    aService.generate_angular_service(infos.name, infos.entity_code)
    aList.generate_angular_component(infos.name, infos.entity_code)