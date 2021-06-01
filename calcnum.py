class Big_Number:
    '''Classe para representar números com bases grandes com seus expoentes'''
    def __init__(self, base, expoente):
        self.base = base
        self.expoente = expoente


class System:
    '''Classe que comportará as operações'''
    def __init__(self, num_list, float_point = 4): #num_list comporta os itens que estarão no sistema; 4 é o floatpoint, por motivos pedagógicos de estar na questão
        self.num_list = num_list
        self.float_point = float_point

    def sum_op(self, sum_num_list = None):
        ''' você pode indicar quais itens quer interagir, adicionando uma lista ou tupla com o índice do item no parâmetro da função. Para fazer subtração, inverta manualmente o sinal do item na parametrizaçao do sistema '''
        if sum_num_list == None:
            sum_num_list = self.num_list
        else:
            
            temp_sum_num_list = sum_num_list
            sum_num_list = []
            for num in temp_sum_num_list:
                sum_num_list.append(self.num_list[num])    

        ''' Tentativa de replicar o funcionamento do algoritmo apresentado em sala:
        1: escolher o número com menor expoente entre as parcelas (Funcionando)
        e deslocar sua mantissa n vezes para a direita,
        de modo que n é a diferença absoluta entre o maior e o menor expoente
        '''
        lowest_exp = sum_num_list[0].expoente  # Inicializar o valor com o primeiro item do sistema
       
        biggest_exp = sum_num_list[0].expoente # Inicializar o valor com o primeiro item do sistema

        mantisse_sum = 0 # Inicializar o valor com 0

        for num in sum_num_list:
            if num.expoente < lowest_exp: lowest_exp = num.expoente
            if num.expoente > biggest_exp: biggest_exp = num.expoente

        print('Menor expoente: ',lowest_exp)
        print('Maior expoente: ',biggest_exp)

        # move_mantisse_to_right = biggest_exp - (lowest_exp)
        

        for num in sum_num_list:
            move_mantisse_to_right = biggest_exp - (num.expoente)
            while move_mantisse_to_right > 0: #isto é bom porque em teoria pula o expoente = aomaior expoente
                num.base /= 10
                move_mantisse_to_right -= 1
            mantisse_sum += num.base

        

                
        ''' 
        2: o Resultado deve possuir o maior expoente entre as parcelas, que está salvo em biggest_exp
        '''

        ''' 
        3: Executar a operação das mantissas e determinar o sinal do resultado
        '''

        print(mantisse_sum)

        ''' 
        4 e 5: Normalizar e verificar por under/over flow
        '''

System([Big_Number(0.7237,4) , Big_Number(-0.2145,-3), Big_Number(-0.2585,1)]).sum_op()


