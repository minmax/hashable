from unittest import TestCase
from autohash import hashable


class NotHashable(object):
    def __init__(self, attr):
        self.attr = attr

    def get_attr(self):
        return self.attr


class TestHashable(TestCase):
    def test_hash_with_attr(self):
        @hashable(attributes=['attr'])
        class Hashable(NotHashable):
            pass
        self.validate_hash(Hashable)

    def test_hash_with_method(self):
        @hashable(methods=['get_attr'])
        class Hashable(NotHashable):
            pass
        self.validate_hash(Hashable)

    def validate_hash(self, cls):
        self.assertEquals(cls(1), cls(1))
        self.assertEquals(hash(cls(1)), hash(cls(1)))
        self.assertIsNotNone(hash(cls(1)))



class TestOOPSCompatibility(TestCase):
    identifier = 789

    def test_self_defined_methods_not_overridden(self):
        @hashable(attributes='attr')
        class SelfHashedCLS(object):
            attr = 1
            def __hash__(self):
                return TestOOPSCompatibility.identifier

        self.assertEqual(self.identifier, hash(SelfHashedCLS()))
