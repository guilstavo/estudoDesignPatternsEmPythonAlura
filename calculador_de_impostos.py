from impostos import calcula_ISS, calcula_ICMS

class Calculador_de_impostos(object):

	def realiza_calculo(self, orcamento, imposto):

		imposto_calculado = imposto(orcamento)

		print imposto_calculado


if __name__ == '__main__':

	from orcamento import Orcamento

	calculador = Calculador_de_impostos()

	orcamento = Orcamento(500)

	calculador.realiza_calculo(orcamento, calcula_ISS)
	calculador.realiza_calculo(orcamento, calcula_ICMS)
	