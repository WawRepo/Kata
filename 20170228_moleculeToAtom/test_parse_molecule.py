from unittest import TestCase

from parse_molecule import *

class TestParse_molecule(TestCase):
    def equals_atomically(self, obj1, obj2):
        if len(obj1) != len(obj2):
            return False
        for k in obj1:
            if obj1[k] != obj2[k]:
                return False
        return True

    def test_add_one_to_molecule(self):
        self.assertEquals(full_molecule_count("(MgO2)"), "(Mg1O2)1")
        self.assertEquals(full_molecule_count("MgO2"), "Mg1O2")
        self.assertEquals(full_molecule_count("K4[ON(SO3)2]2"), "K4[O1N1(S1O3)2]2")


    def test_watter(self):
        self.assertTrue(self.equals_atomically(parse_molecule("H2O"), {'H': 2, 'O': 1}), "Should parse water")


    def test_reduce_parenhesis(self):
        self.assertEquals(reduce_parenhesis("(S1O3)2"), "S2O6")
        self.assertEquals(reduce_parenhesis("K4[O1N1(S1O3)2]2"), "K4O2N2S4O12")


    def test_identify_brackets(self):
        self.assertEquals(identify_brackets("(S1O3)2(S1O3)2"), [(0, 5),(7, 12)])
        self.assertEquals(identify_brackets("(S1O3)2"), [(0,5)])
        self.assertEquals(identify_brackets("K4[O1N1(S1O3)2]2"), [(7,12),(2,14)])
        self.assertEquals(identify_brackets("K4[O1N1S2O6]2"), [(2, 11)])


    def test_reduce_parenhesis_for_bracket(self):
        self.assertEquals(reduce_parenhesis_for_bracket("(S1O3)2",[(0,5)]), "S2O6")
        self.assertEquals(reduce_parenhesis_for_bracket("K4[O1N1(S1O3)2]2", [(7, 12)]), "K4[O1N1S2O6]2")
        self.assertEquals(reduce_parenhesis_for_bracket("K4[O1N1S2O6]2", [(2, 11)]), "K4O2N2S4O12")

    def test_magnesium_hydroxide(self):
        self.assertTrue(self.equals_atomically(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O': 2, 'H': 2}),
                "Should parse magnesium hydroxide: Mg(OH)2")

    def test_Fremy_salt(self):
        self.assertTrue(self.equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {'K': 4, 'O': 14, 'N': 2, 'S': 4}),
                "Should parse Fremy's salt: K4[ON(SO3)2]2")


    def test_particles(self):
        print parse_molecule("{[Co(NH3)4(OH)2]3Co}(SO4)3")
        self.assertTrue(self.equals_atomically(parse_molecule("Pd[P(C6H5)3]4"), {'Pd': 1, 'P': 4, 'C': 72, 'H': 60}),
                        "=")
        print parse_molecule("As2{Be4C5[BCo3(CO2)3]2}4Cu5")
        print parse_molecule("{[Co(NH3)4(OH)2]3Co}(SO4)3")



