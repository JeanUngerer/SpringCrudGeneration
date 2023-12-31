def add_module_to_app_module(class_name):
    path = "./angularTestUI/src/app/"
    with open(path + 'app.module.ts', 'r') as file:
        module_code = file.readlines()

    # Find the line where the imports end
    import_end_index = None
    for i, line in enumerate(module_code):
        if 'import {' in line:
            import_end_index = i
        elif 'imports:' in line:
            break

    # Add the import statement for the component
    import_statement = f"import {{ {class_name}Module }} from './test/modules/{class_name.lower()}/{class_name.lower()}.module';\n"
    module_code.insert(import_end_index + 1, import_statement)

    # Find the line where the declarations end
    declarations_end_index = None
    for i, line in enumerate(module_code):
        if 'imports:' in line:
            declarations_end_index = i
            break

    # Add the component to the declarations
    declaration_statement = f"\t\t{class_name}Module,\n"
    module_code.insert(declarations_end_index + 1, declaration_statement)

    # Write the modified code back to the app.module.ts file
    with open(path + 'app.module.ts', 'w') as file:
        file.writelines(module_code)
    print(f"Added {class_name}DetailComponent to app.module.ts successfully!")


def add_component_to_app_routing_module(class_name):
    path = "./angularTestUI/src/app/"

    with open(path + 'app-routing.module.ts', 'r') as file:
        routing_module_code = file.readlines()

    # Find the line where the routes end
    routes_end_index = None
    for i, line in enumerate(routing_module_code):
        if ']' in line:
            routes_end_index = i
            break

    # Add the route for the component
    route_statement = f"\t{{ path: '{class_name.lower()}', loadChildren: () => import('./test/modules/{class_name.lower()}/{class_name.lower()}.module').then((m) => m.{class_name}Module), }},\n"
    routing_module_code.insert(routes_end_index - 2, route_statement)

    # Write the modified code back to the app-routing.module.ts file
    with open(path + 'app-routing.module.ts', 'w') as file:
        file.writelines(routing_module_code)
    print(f"Added {class_name} components route to app-routing.module.ts successfully!")


# Provide the class name for which the component was generated
class_name = "Equipment"

# Add the component to app.module.ts
#add_component_to_app_module(class_name)

# Add the route for the component to app-routing.module.ts
#add_component_to_app_routing_module(class_name)
