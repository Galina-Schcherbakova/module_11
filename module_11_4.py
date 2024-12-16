import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    obj_module = obj.__module__

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info


class SampleClass:
    def __init__(self, name):
        self.name = name
        self.value = 42

    def greet(self):
        return f"Hello, {self.name}!"

    def add(self, x):
        return self.value + x


sample_object = SampleClass("Alice")

object_info = introspection_info(sample_object)
print(object_info)
