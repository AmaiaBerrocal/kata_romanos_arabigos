import unittest
from romanos import romano_a_arabigo
from arabigos import arabigo_a_romano


class RomanNumberTest(unittest.TestCase):

    def test_symbols_romans(self):
        self.assertEqual(romano_a_arabigo('I'), 1)
        self.assertEqual(romano_a_arabigo('V'), 5)
        self.assertEqual(romano_a_arabigo('X'), 10)
        self.assertEqual(romano_a_arabigo('L'), 50)
        self.assertEqual(romano_a_arabigo('C'), 100)
        self.assertEqual(romano_a_arabigo('D'), 500)
        self.assertEqual(romano_a_arabigo('M'), 1000)
        self.assertEqual(romano_a_arabigo('A'), 0)
        
    def test_numeros_crecientes(self):
        self.assertEqual(romano_a_arabigo('XVI'), 16)
        self.assertEqual(romano_a_arabigo('III'), 3)

    def test_control_repeticiones(self):
        self.assertEqual(romano_a_arabigo('IIII'), 0)
        self.assertEqual(romano_a_arabigo('LXXIII'), 73)
        self.assertEqual(romano_a_arabigo('VV'), 0)
       

    def test_numeros_decrecientes(self):
        self.assertEqual(romano_a_arabigo('IX'), 9)
        self.assertEqual(romano_a_arabigo('CMXCIX'), 999)
        
    def test_restas_no_admiten_repeticiones(self):   
        self.assertEqual(romano_a_arabigo('MIIX'), 0)

    def test_las_restas_no_admiten_derivados_del_5(self):
        self.assertEqual(romano_a_arabigo('VC'), 0)
        
    def test_restas_no_admiten_mas_de_un_orden(self):
        self.assertEqual(romano_a_arabigo('IC'), 0)
        self.assertEqual(romano_a_arabigo('IL'), 0)
        self.assertEqual(romano_a_arabigo('IV'), 4)
        self.assertEqual(romano_a_arabigo('XL'), 40)
        self.assertEqual(romano_a_arabigo('XC'), 90)
        self.assertEqual(romano_a_arabigo('CD'), 400)
        self.assertEqual(romano_a_arabigo('CM'), 900)

    def numeros_mayores_de_3999(self):
        self.assertEqual(romano_a_arabigo('(IV)'), 4000)
        self.assertEqual(romano_a_arabigo('(VI)'), 6000)
        self.assertEqual(romano_a_arabigo('(VII)CMXXIII'), 7923)
        self.assertEqual(romano_a_arabigo('((VII))(DLIII)DCXXXVII'), 7553637)


class ArabicNumberTest(unittest.TestCase):
    
    def test_unidades(self):
        self.assertEqual(arabigo_a_romano(1), 'I')
        self.assertEqual(arabigo_a_romano(2), 'II')
        self.assertEqual(arabigo_a_romano(4), 'IV')

    def test_arabic_a_roman(self):
        self.assertEqual(arabigo_a_romano(1597), 'MDXCVII')
        self.assertEqual(arabigo_a_romano(2123), 'MMCXXIII')
        self.assertEqual(arabigo_a_romano(2444), 'MMCDXLIV')
        self.assertEqual(arabigo_a_romano(3555), 'MMMDLV')
        self.assertEqual(arabigo_a_romano(1678), 'MDCLXXVIII')
        self.assertEqual(arabigo_a_romano(2999), 'MMCMXCIX')

    def test_mas_3999(self):
        self.assertEqual(arabigo_a_romano(4000), '(IV)')
        self.assertEqual(arabigo_a_romano(6000), '(VI)')
        self.assertEqual(arabigo_a_romano(5025), '(V)XXV')
        self.assertEqual(arabigo_a_romano(7923), '(VII)CMXXIII')
        self.assertEqual(arabigo_a_romano(7553637), '(VII)(DLIII)DCXXXVII')

        

if __name__ == '__main__':
    unittest.main()
