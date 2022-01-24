class Generator:
    def indent(str):
        return f"\t{str}"
    def endline():
        return "\n"
    def create_function(func_name, param_list):
        definition=f"def {func_name}"
