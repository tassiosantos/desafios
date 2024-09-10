# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora de todos os dias de um ano, faça um programa, na linguagem que desejar, que calcule e retorne:

# - O menor valor de faturamento ocorrido em um dia do ano;
# - O maior valor de faturamento ocorrido em um dia do ano;
# - Número de dias no ano em que o valor de faturamento diário foi superior à média anual.

# a) Considerar o vetor já carregado com as informações de valor de faturamento.

# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média.

# c) Utilize o algoritmo mais veloz que puder definir.



class Faturamento:
    
    def _media_(self):
        validos = 0
        soma = 0
        for i, valor in enumerate(self.vetor_faturamento):
            if valor > 0 :
                soma = soma + valor
                validos = validos + 1
                media = soma/validos if validos > 0 else 0
        print(f"media: {media}")
        return soma/validos if validos > 0 else 0
    
    def calcular_menor_valor(self):
        min = None
        for i, valor in enumerate(self.vetor_faturamento):
            if i == 0:
                min = valor
            
            if valor < min:
                min = valor
           
        return min
    
    
    def calcular_maior_valor(self):
        max = None
        for i, valor in enumerate(self.vetor_faturamento):
            if i == 0:
                max = valor
                
            if valor > max:
                max = valor
        return max
    
        
    def dias_faturamento_maior_media(self):
        media = self._media_()
        dias = 0
        for i in self.vetor_faturamento:
            if i > media:
                dias = dias + 1
            
        return dias
        
        
   
    
    def __init__(self, vetor_faturamento):
        self.vetor_faturamento = vetor_faturamento
        
        print(f"Maior faturamento: {self.calcular_maior_valor()}")
        print(f"Menor faturamento: {self.calcular_menor_valor()}")
        print(f"Dias com faturamento acima da média: {self.dias_faturamento_maior_media()}")
        
        



faturamentos = [1000, 2000, 3000, 0, 500, 2500, 5000, 5000]


faturamento_teste = Faturamento(faturamentos)