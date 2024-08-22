import sys
import pprint


def introspection_info(obj):
    result = {
        'type': type(obj),
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],

        'get_size': sys.getsizeof(obj)

    }
    return result


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = MyClass(1, 2)
print(introspection_info(obj))



