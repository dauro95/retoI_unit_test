import unittest
from Geometria_.model.Geometria import Geometria

class testGeometria(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.g= Geometria(2.00, 3.10, 4.00)
       
    @classmethod
    def tearDownClass(self) -> None:
        print("tearDowClass")
    
    def setUp(self) -> None:
        print("setup")
        
    
    def tearDown(self) -> None:
        print("tearDow OK")
    
    def test_areaCuadrado(self):
        self.g.set_figuraName(1)
        figura= self.g.figuraName
        result=self.g.switch(1)
        self.assertEquals(result,4,"Mal")
        self.assertEquals(figura,"Cuadrado")
        print("test areaCuadrado() OK")

    def test_areaCirculo(self):
        self.g.set_figuraName(2)
        figura= self.g.figuraName
        result=self.g.switch(2)
        self.assertEquals(result,12.5664,"Mal")
        self.assertEquals(figura,"Circulo")
        print("test areaCirculo() OK")

    def test_Triangulo(self):
        self.g.set_figuraName(3)
        figura= self.g.figuraName
        result=self.g.switch(3)
        self.assertEquals(result,3.1,"Mal")
        self.assertEquals(figura,"Triangulo")
        print("test areaCirculo() OK")
    
    def test_Rectangulo(self):
        self.g.set_figuraName(4)
        figura= self.g.figuraName
        result=self.g.switch(4)
        self.assertEquals(result,6.2,"Mal")
        self.assertEquals(figura,"Rectangulo")
        print("test areaCirculo() OK")

    def test_Pentagono(self):
        self.g.set_figuraName(5)
        figura= self.g.figuraName
        result=self.g.switch(5)
        self.assertEquals(result,3.1,"Mal")
        self.assertEquals(figura,"Pentagono")
        print("test areaCirculo() OK")

    def test_Rombo(self):
        self.g.set_figuraName(6)
        figura= self.g.figuraName
        result=self.g.switch(6)
        self.assertEquals(result,3.1,"Mal")
        self.assertEquals(figura,"Rombo")
        print("test areaCirculo() OK")
    
    def test_Romboide(self):
        self.g.set_figuraName(7)
        figura= self.g.figuraName
        result=self.g.switch(7)
        self.assertEquals(result,6.2,"Mal")
        self.assertEquals(figura,"Romboide")
        print("test areaCirculo() OK")
    
    def test_Trapecio(self):
        self.g.set_figuraName(8)
        figura= self.g.figuraName
        result=self.g.switch(8)
        self.assertEquals(result,10.2,"Mal")
        self.assertEquals(figura,"Trapecio")
        print("test areaCirculo() OK")
        