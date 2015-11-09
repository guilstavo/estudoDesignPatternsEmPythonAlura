from impostos import ISS, ICMS, ICPP, IKCV

class Imposto(object):

	def __init__(self, outro_imposto):
		self.__outro_imposto = outro_imposto

	def calcula(self, orcamento):
		pass

class Calculador_de_impostos(object):

	def realiza_calculo(self, orcamento, imposto):

		imposto_calculado = imposto.calcula(orcamento)

		print imposto_calculado


if __name__ == '__main__':

	from orcamento import Orcamento, Item

	calculador = Calculador_de_impostos()

	orcamento = Orcamento()
	orcamento.adiciona_item(Item('Item - 1', 50))
	orcamento.adiciona_item(Item('Item - 2', 200))
	orcamento.adiciona_item(Item('Item - 3', 250))

	print 'ISS e ICMS'
	calculador.realiza_calculo(orcamento, ISS())
	calculador.realiza_calculo(orcamento, ICMS())

	calculador.realiza_calculo(orcamento, ISS(ICMS()))	

	print 'ICPP e IKCV'
	calculador.realiza_calculo(orcamento, ICPP())
	calculador.realiza_calculo(orcamento, IKCV())

	calculador.realiza_calculo(orcamento, ICPP(IKCV()))