def generate_angular_service(equipment_entity_file):
    with open(equipment_entity_file, 'r') as file:
        entity_code = file.read()

    class_name = get_class_name(entity_code)
    interface_name = class_name + "DTO"

    service_code = generate_service_code(class_name, interface_name)
    write_to_file(service_code, class_name)

def get_class_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    return class_name

def generate_service_code(class_name, interface_name):
    service_code = f"import {interface_name} from './{interface_name}';\n"
    service_code += "import { Injectable } from '@angular/core';\n"
    service_code += "import { HttpClient } from '@angular/common/http';\n"
    service_code += "import { Observable } from 'rxjs';\n\n"

    service_code += "@Injectable({\n"
    service_code += "\tprovidedIn: 'root'\n"
    service_code += "})\n"
    service_code += f"export class {class_name}Service {{\n"
    service_code += "\tprivate baseUrl = '/api/equipment';\n\n"

    service_code += "\tconstructor(private http: HttpClient) { }\n\n"

    service_code += f"\tgetAll{class_name}(): Observable<{interface_name}[]> {{\n"
    service_code += f"\t\treturn this.http.get<{interface_name}[]>" + "(`${this.baseUrl}/equipments`);\n"
    service_code += "\t}\n\n"

    service_code += f"\tget{class_name}(id: number): Observable<{interface_name}> {{\n"
    service_code += f"\t\treturn this.http.get<{interface_name}>" + "(`${this.baseUrl}/${{id}}`);\n"
    service_code += "\t}\n\n"

    service_code += f"\tcreate{class_name}({class_name.lower()}: {interface_name}): Observable<{interface_name}> {{\n"
    service_code += f"\t\treturn this.http.put<{interface_name}>" + "(`${this.baseUrl}" + f"/create`, {class_name.lower()});\n"
    service_code += "\t}\n\n"

    service_code += f"\tupdate{class_name}({class_name.lower()}: {interface_name}): Observable<{interface_name}> {{\n"
    service_code += f"\t\treturn this.http.post<{interface_name}>" + "(`${this.baseUrl}/" + f"update`, {class_name.lower()});\n"
    service_code += "\t}\n\n"

    service_code += f"\tdelete{class_name}(id: number): Observable<any> {{\n"
    service_code += f"\t\treturn this.http.delete<any>" + "(`${this.baseUrl}/${{id}}`);\n"
    service_code += "\t}\n"
    service_code += "}\n"

    return service_code

def write_to_file(service_code, class_name):
    output_file = class_name + "Service.ts"
    with open(output_file, 'w') as file:
        file.write(service_code)
    print(f"Angular service file '{output_file}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = "tests/EquipmentEntity.java"
generate_angular_service(equipment_entity_file)
