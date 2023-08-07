import os


def create_routing_module(module_name, components):
    routing_module_code = generate_routing_module_code(module_name, components)
    path = "./angularTestUI/src/app/test/modules/" + module_name.lower() + "/"

    #path = "./aRoutingModuleOutput/"


    # Check whether the specified path exists or not

    if not os.path.exists(path):
        # Create a new directory because it does not exist
        os.makedirs(path)

    # Write the routing module code to a new -routing.module.ts file
    routing_module_file_name = path + f"{module_name.lower()}-routing.module.ts"
    with open(routing_module_file_name, 'w') as file:
        file.write(routing_module_code)
    print(f"Angular routing module '{module_name}RoutingModule' created successfully!")

def generate_routing_module_code(module_name, components):
    route_statements = ""


    route_statements += f"\t{{ path: 'list', component: {module_name}ListComponent }},\n"
    route_statements += f"\t{{ path: 'detail/:id', component: {module_name}DetailComponent }},\n"
    route_statements += f"\t{{ path: 'create', component: {module_name}CreateComponent }},\n"

    routing_module_code = f"import {{ NgModule }} from '@angular/core';\n"
    routing_module_code += f"import {{ RouterModule, Routes }} from '@angular/router';\n\n"


    routing_module_code += f"import {{ {module_name}Module }} from './{module_name.lower()}.module';\n\n"
    routing_module_code += f"import {{ {module_name}ListComponent }} from './{module_name.lower()}list/{module_name}list.component';\n"
    routing_module_code += f"import {{ {module_name}DetailComponent }} from './{module_name.lower()}detail/{module_name}detail.component';\n"
    routing_module_code += f"import {{ {module_name}CreateComponent }} from './{module_name.lower()}create/{module_name}create.component';\n"

    routing_module_code += f"const routes: Routes = [\n"
    routing_module_code += route_statements
    routing_module_code += f"];\n\n"

    routing_module_code += f"@NgModule({{\n"
    routing_module_code += f"\timports: [RouterModule.forChild(routes), {module_name}Module],\n"
    routing_module_code += f"\texports: [RouterModule]\n"
    routing_module_code += f"}})\n"
    routing_module_code += f"export class {module_name}RoutingModule {{ }}\n"

    return routing_module_code

# Provide the module name and list of component names
module_name = "Equipment"
components = ["EquipmentDetailComponent", "EquipmentCreateComponent"]

# Create the Angular routing module
# create_routing_module(module_name, components)
