from calculadora import Calculadora

def test_add():
	calc = Calculadora()
	assert calc.add(2, 3) == 5

def test_sub():
	calc = Calculadora()
	assert calc.sub(5, 3) == 2