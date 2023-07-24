def generate_angular_component(equipment_entity_file):
    with open(equipment_entity_file, 'r') as file:
        entity_code = file.read()

    class_name = get_class_name(entity_code)
    interface_name = class_name + "DTO"

    component_code = generate_component_code(class_name, interface_name)
    template_code = generate_template_code(class_name)
    stylesheet_code = generate_stylesheet_code()

    write_to_file(component_code, class_name)
    write_to_file(template_code, f"{class_name.lower()}.component.html")
    write_to_file(stylesheet_code, f"{class_name.lower()}.component.scss")

def get_class_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    return class_name

def generate_component_code(class_name, interface_name):
    component_code = f"import {{ Component, OnInit }} from '@angular/core';\n"
    component_code += f"import {{ Router }} from '@angular/router';\n"
    component_code += f"import {{ {class_name}Service }} from './{class_name}Service';\n"
    component_code += f"import {{ {interface_name} }} from './{interface_name}';\n\n"

    component_code += "@Component({\n"
    component_code += f"\tselector: '{class_name.lower()}-list',\n"
    component_code += f"\ttemplateUrl: '{class_name.lower()}.component.html',\n"
    component_code += f"\tstyleUrls: ['{class_name.lower()}.component.scss']\n"
    component_code += "})\n"
    component_code += f"export class {class_name}ListComponent implements OnInit {{\n"
    component_code += f"\t{class_name.lower()}List: {interface_name}[];\n\n"

    component_code += f"\tconstructor(private {class_name.lower()}Service: {class_name}Service, private router: Router) {{ }}\n\n"

    component_code += "\tngOnInit() {\n"
    component_code += f"\t\tthis.get{class_name}List();\n"
    component_code += "\t}\n\n"

    component_code += f"\tget{class_name}List() {{\n"
    component_code += f"\t\tthis.{class_name.lower()}Service.getAll{class_name}().subscribe(data => {{\n"
    component_code += f"\t\t\tthis.{class_name.lower()}List = data;\n"
    component_code += "\t\t}});\n"
    component_code += "\t}\n\n"

    component_code += f"\tonRowClick(id: number) {{\n"
    component_code += f"\t\tthis.router.navigate(['{class_name.lower()}', id]);\n"
    component_code += "\t}\n"
    component_code += "}\n"

    return component_code

def generate_template_code(class_name):
    template_code = f"<table mat-table [dataSource]=\"{class_name.lower()}List\">\n"
    template_code += f"\t<ng-container matColumnDef=\"name\">\n"
    template_code += "\t\t<th mat-header-cell *matHeaderCellDef>Name</th>\n"
    template_code += "\t\t<td mat-cell *matCellDef=\"let element\">{{element.name}}</td>\n"
    template_code += "\t</ng-container>\n\n"

    template_code += f"\t<ng-container matColumnDef=\"type\">\n"
    template_code += "\t\t<th mat-header-cell *matHeaderCellDef>Type</th>\n"
    template_code += "\t\t<td mat-cell *matCellDef=\"let element\">{{element.type}}</td>\n"
    template_code += "\t</ng-container>\n\n"

    template_code += f"\t<ng-container matColumnDef=\"effects\">\n"
    template_code += "\t\t<th mat-header-cell *matHeaderCellDef>Effects</th>\n"
    template_code += "\t\t<td mat-cell *matCellDef=\"let element\">{{element.effects}}</td>\n"
    template_code += "\t</ng-container>\n\n"

    template_code += f"\t<tr mat-header-row *matHeaderRowDef=\"['name', 'type', 'effects']\"></tr>\n"
    template_code += f"\t<tr mat-row *matRowDef=\"let row; columns: ['name', 'type', 'effects']; click: onRowClick\"></tr>\n"
    template_code += "</table>\n"

    return template_code

def generate_stylesheet_code():
    stylesheet_code = ":host {\n"
    stylesheet_code += "\tdisplay: block;\n"
    stylesheet_code += "}\n\n"

    stylesheet_code += "table {\n"
    stylesheet_code += "\twidth: 100%;\n"
    stylesheet_code += "}\n\n"

    stylesheet_code += "th.mat-header-cell, td.mat-cell {\n"
    stylesheet_code += "\ttext-align: left;\n"
    stylesheet_code += "}\n"

    return stylesheet_code

def write_to_file(content, file_name):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File '{file_name}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = "EquipmentEntity.java"
generate_angular_component(equipment_entity_file)
