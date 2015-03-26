from .tools import create_getters_list, get_super_not_buildin_method_or_none


__all__ = ['HashCodeBuilder']


class HashCodeBuilder(object):
    @classmethod
    def auto_generate(cls, hashable_cls, attributes=None, methods=None):
        getters_list = create_getters_list(attributes, methods)

        super_method = get_super_not_buildin_method_or_none(hashable_cls, '__hash__')

        def __hash__(self):
            hash_code_builder = cls()
            if super_method is not None:
                hash_code_builder.append_super(super_method(self))
            for getter in getters_list:
                value = getter(self)
                hash_code_builder.append(value)
            return hash_code_builder.get_hash_code()
        return __hash__

    def __init__(self, initial_non_zero_odd_number=17, multiplier_non_zero_odd_number=37):
        assert initial_non_zero_odd_number != 0 and initial_non_zero_odd_number % 2 != 0
        assert multiplier_non_zero_odd_number != 0 and multiplier_non_zero_odd_number % 2 != 0

        self._total = initial_non_zero_odd_number
        self._constant = multiplier_non_zero_odd_number

    def append_super(self, super_hash_code):
        self._total = self._total * self._constant + super_hash_code
        return self

    def append(self, obj):
        if obj is None:
            self._total = self._total * self._constant
        else:
            self._total = self._total * self._constant + hash(obj)
        return self

    def __hash__(self):
        return self._total

    def get_hash_code(self):
        return self._total
