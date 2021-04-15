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
            while(aux != None and not found):
                if(aux.content[ind_valor].valor < value):
                    ind_valor += 1
                elif(aux.content[ind_valor].valor > value):
                    if ind_valor == 0:
                        ant = aux
                        aux = aux.content[ind_valor].entrada
                    else:
                        ant = aux
                        aux = aux.content[ind_valor - 1].ponteiro
                        ind_valor = 0
                else:
                    found = True
                if aux !=  None and ind_valor >= len(aux.content):
                    ant = aux
                    aux = aux.content[ind_valor - 1].ponteiro
                    ind_valor = 0
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
            self.altura += 1
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
            if aux.content[i].valor < alvo.content[0].valor:
                i += 1
            else:
                if i == 0:
                    ant = aux
                    aux = aux.content[ind_valor].entrada
                else:
                    ant = aux
                    aux = aux.content[i].ponteiro
                    i = 0
            if i >= len(aux.content):
                ant = aux
                aux = aux.content[ind_valor - 1].ponteiro
                i = 0
        return ant, aux

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

    def remove(self, value):
        [found, ant, aux] = self.busca(value)
        if(not found):
            print("O elemento não pertence à essa árvore")
        else:
            i = 0
            while(i < len(aux.content) - 1 and aux.content[i].valor != value):
                i += 1
            if(aux.entrada != None):
                anchor = aux
                u = i
                ant = aux
                aux = aux.content[i].ponteiro
                while(aux.entrada == None):
                    ant = aux
                    aux = aux.entrada
                i = 0
                anchor.content[u].valor = aux.content[i].valor
            aux.content.pop(i)
            while(len(aux.content) < self.ordem):
                i = 0
                while(i < len(ant.content) - 1 and ant.content[i].ponteiro != aux):
                    i += 1
                if(i == 0):
                    j = 0
                    elems = ant.entrada.content + aux.content
                else:
                    j =  i - 1
                    elems = ant.content[j].ponteiro.content + aux.content
                k = 0
                while(k < len(elems) - 1 and elems[k].valor < ant.content[i].valor):
                    k += 1
                elems.insert(k, ant.content[i])
                elems[k].ponteiro = aux.entrada
                if(len(elems) >= 2*self.ordem and ant != self.start):
                    # redistribuicao
                    meio = int(len(elems)/2)
                    a = elems[0:meio]
                    b = elems[meio+1:len(elems)]
                    ant.content[i].valor = elems
                    if(i == 0):
                        ant.entrada = a
                        ant.content[i].ponteiro = b
                    else:
                        ant.content[j].ponteiro = a
                        ant.content[i].ponteiro = b
                else:
                    # concatenacao()
                    if(ant == self.start):
                        ant.entrada = ant.entrada.entrada if i==0 else ant.content[j].ponteiro.entrada
                        ant.content = elems
                        self.altura -= 1
                    else:
                        ant.content.pop(i)
                        if(i == 0):
                            ant.entrada = elems
                        else:
                            ant.content[j].ponteiro = elems
                [ant, aux] = self.search(ant)

    def print_tree(self):
        heap = []
        for i in range(self.altura + 1):
            heap.append([])
        self.count_tree(self.start, heap, 0)
        i = 0
        for h in heap:
            print(f"{i}: ", end="")
            for k in h:
                print(k, end=" ")
            print()
            i+=1

    def count_tree(self, page, heap, altura):
        if page != None:
            novo = []
            for i in page.content:
                novo.append(i.valor)
            heap[altura].append(novo)
            self.count_tree(page.entrada, heap, altura + 1)
            for i in page.content:
                self.count_tree(i.ponteiro, heap, altura + 1)