from .equals_builder import EqualsBuilder
from .hash_code_builder import HashCodeBuilder
from .tools import is_build_in_method


__all__ = [
    'hashable',
    'equality_comparable',
]


def hashable(cls=None, attributes=None, methods=None):
    def decorator(cls):
        cls = equality_comparable(cls, attributes, methods)
        if is_build_in_method(cls, '__hash__'):
            cls.__hash__ = HashCodeBuilder.auto_generate(attributes, methods)
        return cls
    return decorator if cls is None else decorator(cls)


def equality_comparable(cls=None, attributes=None, methods=None):
    def decorator(cls):
        if is_build_in_method(cls, '__eq__'):
            cls.__eq__ = EqualsBuilder.auto_generate(attributes, methods)

        if is_build_in_method(cls, '__ne__'):
            cls.__ne__ = EqualsBuilder.auto_ne_from_eq()
        return cls
    return decorator if cls is None else decorator(cls)
