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
    component_code = f"import {{ Component }} from '@angular/core';\n"
    component_code += f"import {{ FormBuilder, FormGroup, Validators }} from '@angular/forms';\n"
    component_code += f"import {{ {class_name}Service }} from './{class_name}Service';\n"
    component_code += f"import {{ {interface_name} }} from './{interface_name}';\n\n"

    component_code += "@Component({\n"
    component_code += f"\tselector: '{class_name.lower()}-create',\n"
    component_code += f"\ttemplateUrl: '{class_name.lower()}.component.html',\n"
    component_code += f"\tstyleUrls: ['{class_name.lower()}.component.scss']\n"
    component_code += "})\n"
    component_code += f"export class {class_name}CreateComponent {{\n"
    component_code += f"\t{class_name.lower()}Form: FormGroup;\n\n"
    component_code += f"\tconstructor(private formBuilder: FormBuilder, private {class_name.lower()}Service: {class_name}Service) {{\n"
    component_code += f"\t\tthis.initForm();\n"
    component_code += "\t}\n\n"

    component_code += "\tinitForm() {\n"
    component_code += f"\t\tthis.{class_name.lower()}Form = this.formBuilder.group({{\n"
    component_code += f"\t\t\tname: ['', Validators.required],\n"
    component_code += f"\t\t\ttype: ['', Validators.required],\n"
    component_code += f"\t\t\teffects: ['', Validators.required]\n"
    component_code += "\t\t}});\n"
    component_code += "\t}\n\n"

    component_code += f"\tget name() {{ return this.{class_name.lower()}Form.get('name'); }}\n\n"
    component_code += f"\tget type() {{ return this.{class_name.lower()}Form.get('type'); }}\n\n"
    component_code += f"\tget effects() {{ return this.{class_name.lower()}Form.get('effects'); }}\n\n"

    component_code += f"\tonSubmit() {{\n"
    component_code += f"\t\tif (this.{class_name.lower()}Form.invalid) {{\n"
    component_code += "\t\t\treturn;\n"
    component_code += "\t\t}\n\n"
    component_code += f"\t\tconst {class_name.lower()}: {interface_name} = {{\n"
    component_code += f"\t\t\tid: null,\n"
    component_code += f"\t\t\tname: this.name.value,\n"
    component_code += f"\t\t\ttype: this.type.value,\n"
    component_code += f"\t\t\teffects: this.effects.value,\n"
    component_code += "\t\t};\n\n"
    component_code += f"\t\tthis.{class_name.lower()}Service.create{class_name}({class_name.lower()}).subscribe(created{class_name} => {{\n"
    component_code += "\t\t\tconsole.log('EquipmentEntity created successfully:', createdEquipment);\n"
    component_code += "\t\t\t// Add further logic as needed\n"
    component_code += "\t\t}});\n"
    component_code += "\t}\n"
    component_code += "}\n"

    return component_code

def generate_template_code(class_name):
    template_code = f"<form [formGroup]=\"{class_name.lower()}Form\" (ngSubmit)=\"onSubmit()\">\n"
    template_code += f"\t<mat-form-field>\n"
    template_code += f"\t\t<input matInput placeholder=\"Name\" formControlName=\"name\">\n"
    template_code += f"\t\t<mat-error *ngIf=\"name.invalid\">Name is required</mat-error>\n"
    template_code += "\t</mat-form-field>\n\n"

    template_code += f"\t<mat-form-field>\n"
    template_code += f"\t\t<input matInput placeholder=\"Type\" formControlName=\"type\">\n"
    template_code += f"\t\t<mat-error *ngIf=\"type.invalid\">Type is required</mat-error>\n"
    template_code += "\t</mat-form-field>\n\n"

    template_code += f"\t<mat-form-field>\n"
    template_code += f"\t\t<input matInput placeholder=\"Effects\" formControlName=\"effects\">\n"
    template_code += f"\t\t<mat-error *ngIf=\"effects.invalid\">Effects is required</mat-error>\n"
    template_code += "\t</mat-form-field>\n\n"

    template_code += "\t<button mat-raised-button color=\"primary\" type=\"submit\">Create</button>\n"
    template_code += "</form>\n"

    return template_code

def generate_stylesheet_code():
    return ""  # Empty SCSS stylesheet for now

def write_to_file(content, file_name):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File '{file_name}' generated successfully!")

# Provide the path to the EquipmentEntity class file
equipment_entity_file = "EquipmentEntity.java"
generate_angular_component(equipment_entity_file)
