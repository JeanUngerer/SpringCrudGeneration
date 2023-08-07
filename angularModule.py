import os


def create_angular_module(module_name, components):
    module_code = generate_module_code(module_name, components)

    path = "./angularTestUI/src/app/test/modules/" + module_name.lower() + "/"


    # Check whether the specified path exists or not

    if not os.path.exists(path):
        # Create a new directory because it does not exist
        os.makedirs(path)

    # Write the module code to a new .module.ts file
    module_file_name = path + f"{module_name.lower()}.module.ts"
    with open(module_file_name, 'w') as file:
        file.write(module_code)
    print(f"Angular module '{module_name}' created successfully!")

def generate_module_code(module_name, components):
    import_statements = ""
    component_declarations = ""

    for component in components:
        import_statements += f"import {{ {component} }} from './{component.lower()[0:-9]}/{component.lower()[0:-9]}.component';\n"
        component_declarations += f"\t\t{component},\n"

    import_statements += f"import {module_name}RoutingModule from './{module_name.lower()}-routing.module';"

    module_code = f"import {{ NgModule }} from '@angular/core';\n"
    module_code += f"import {{MatTableModule}} from '@angular/material/table';\n"
    module_code += import_statements + "\n"

    module_code += f"@NgModule({{\n"
    module_code += f"\tdeclarations: [\n"
    module_code += component_declarations
    module_code += "\t],\n"
    module_code += f"\timports: [\n"
    module_code += "MatTableModule,"
    module_code += f"{module_name}RoutingModule,"
    module_code += "\t]\n"
    module_code += f"\texports: [\n"
    module_code += "\t]\n"
    module_code += f"}})\n"
    module_code += f"export class {module_name}Module {{ }}\n"

    return module_code

# Provide the module name and list of component names

# Create the Angular module
# create_angular_module(module_name, components)
