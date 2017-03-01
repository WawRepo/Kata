from unittest import TestCase

from parse_molecule import parse_molecule, full_molecule_count

class TestParse_molecule(TestCase):
    def equals_atomically(self, obj1, obj2):
        if len(obj1) != len(obj2):
            return False
        for k in obj1:
            if obj1[k] != obj2[k]:
                return False
        return True

    def test_add_one_to_molecule(self):
        self.assertEquals(full_molecule_count("K4[ON(SO3)2]2"), "K4[O1N1(S1O3)2]2")

    def test_add_one_to_molecule(self):
        self.assertEquals(full_molecule_count("MgO2"), "Mg1O2")

    def test_watter(self):
        self.assertTrue(self.equals_atomically(parse_molecule("H2O"), {'H': 2, 'O': 1}), "Should parse water")

    def test_magnesium_hydroxide(self):
        self.assertTrue(self.equals_atomically(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O': 2, 'H': 2}),
                "Should parse magnesium hydroxide: Mg(OH)2")

    def test_Fremy_salt(self):
        self.assertTrue(self.equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {'K': 4, 'O': 14, 'N': 2, 'S': 4}),
                "Should parse Fremy's salt: K4[ON(SO3)2]2")


