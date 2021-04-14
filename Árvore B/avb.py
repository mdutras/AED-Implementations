class elemento:
    valor = None
    ponteiro = None
    
    def __init__(self, valor):
        self.valor = valor

class pagina:
    content  = []
    limit = 0
    entrada = None
    def __init__(self, ordem):
        self.limit = 2*ordem

    def isFull(self):
        if len(self.content) > self.limit:
            return True
        else:
            return False

class avB:
    altura = 0
    start = None
    def __init__(self, ordem):
        self.ordem = ordem
        self.start = pagina(ordem)
    
    def isEmpty(self):
        if(self.start.content == []):
            return True
        else:
            return False

    def busca(self, value):
        found = False
        aux = self.start
        ant = aux
        if(not self.isEmpty()):
            ind_valor = 0;
            while(aux != None):
                if(aux.content[ind_valor].valor < value):
                    ind_valor += 1
                elif(aux.content[ind_valor].valor > value):
                    if ind_valor == 0:
                        ant = aux
                        aux = aux.content[ind_valor].entrada
                    else:
                        aux = aux.content[ind_valor - 1].ponteiro
                        ind_valor = 0
                else:
                    found = True
                if aux !=  None and ind_valor >= len(aux.content):
                    ant = aux
                    aux = aux.content[ind_valor - 1].ponteiro
        return found, ant, aux

    def cisao(self, pag, pag_ant):
        meio = int((len(pag.content)-1)/2)
        a = pag.content[0:meio]
        b = pag.content[meio+1:len(pag.content)]
        novo_elem = elemento(pag.content[meio].valor)
        if pag == self.start:
            nova_pag_esq = pagina(self.ordem)
            nova_pag_esq.content = a[:]
            nova_pag_dir = pagina(self.ordem)
            nova_pag_dir.content = b[:]
            pag.entrada = nova_pag_esq
            novo_elem.ponteiro = nova_pag_dir
            pag.content = [novo_elem]
        else:
            nova_pag = pagina(self.ordem)
            nova_pag.content = a[:]
            pag.content = b[:]
            novo.ponteiro = nova_pag
            while(i < len(ant.content) and ant.content[i].valor < value):
                i += 1
            pag_ant.content.insert(i, novo)

    def search(self, alvo):
        aux = self.start
        ant = aux
        i = 0
        while aux != alvo:
            if aux.content[i].valor < value:
                i += 1
            else:
                if i == 0:
                    ant = aux
                    aux = aux.content[ind_valor].entrada
                else:
                    ant = aux
                    aux = aux.content[i].ponteiro
                    i = 0
            if i > len(aux.content):
                ant = aux
                aux = aux.content[ind_valor - 1].ponteiro
                i = 0
        return aux, ant

    def add(self, value):
        [found, ant, aux] = self.busca(value)
        if(found):
            print("Elemento já pertence à árvore.\n")
        else:
            novo = elemento(value)
            if self.isEmpty():
                self.start.content.append(novo)
            else:
                i = 0
                while(i < len(ant.content) and ant.content[i].valor < value):
                    i += 1
                ant.content.insert(i, novo)
                while(ant.isFull()):
                    [aux, ant] = self.search(ant)
                    self.cisao(aux, ant)


