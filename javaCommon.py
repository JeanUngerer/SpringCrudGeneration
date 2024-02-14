def get_class_name(entity_code):
    class_start_index = entity_code.index("class") + len("class")
    class_end_index = entity_code.index("{")
    class_name = entity_code[class_start_index:class_end_index].strip()
    class_name = class_name[:-6]
    return class_name


def get_project_name(entity_code):
    package_start_index = entity_code.index("package") + len("package")
    package_end_index = entity_code.index(".entities")
    project_name = entity_code[package_start_index:package_end_index].strip()
    return project_name