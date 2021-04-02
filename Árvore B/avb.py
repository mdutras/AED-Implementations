class elemento:
    valor = None
    ponteiro = None

class pagina:
    left = None
    right = None
    content  = []
    limit = 0
    def __init__(self, ordem):
        self.limit = 2*ordem

    def isFull(self):
        if self.content.lenght == self.limit:
            return True
        else:
            return False

class avB:
    altura = 0

    def __init__(self, ordem):
        self.ordem = ordem
        start = pagina(ordem/2)
    
    def isEmpty(self):
        if(start.content = []):
            return True
        else:
            return False

    def busca(self, value):
        found = False
        if(not self.isEmpty()):
            ind_valor = 0;
            ind_pagina = 0;
            aux = start
            found = False
            while(aux != None):
                if(aux.content[ind_valor].valor < value):
                    ind_valor += 1
                elif(aux.content[ind_valor] > value):
                    if ind_valor == 0:
                        aux = aux.left
                    else:
                        aux = aux.content[ind_valor].ponteiro
                        ind_valor = 0
                    ind_pagina += 1
                else:
                    found = True
                    aux = None
                if ind_valor > aux.content.length:
                    aux = aux.right
                    ind_pagina += 1
        return found

    def add(self, value):
        pass