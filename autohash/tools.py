from operator import attrgetter, methodcaller


def create_getters_list(attributes=None, methods=None):
    getters_list = []
    if attributes is not None:
        getters_list.extend(map(attrgetter, attributes))
    if methods is not None:
        getters_list.extend(map(methodcaller, methods))
    return getters_list


def is_build_in_method(obj, name):
    result = getattr(obj, name, None)
    if result is None:
        return False
    return isinstance(result, build_in_methods_types)


class _C(object):
    pass
build_in_methods_types = (type(_C.__eq__), type(_C.__hash__))
del _C
