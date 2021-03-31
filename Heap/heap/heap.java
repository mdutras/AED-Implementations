package heap;

public class heap {
    class element{
        float value;
        int prio;
        element next;

        void def_value(float value, int prio){
            this.value = value;
            this.prio = prio;
        }
    }
    element start;

    void up(int k, element n){
        element node = new element();
        node.def_value(n.value, n.prio);
        while(true){
            element parent = this.start;
            k = (int) Math.floor(k/2);
            for(int i = 0; i < k - 1; i++){
                parent = parent.next;
            }
            n.prio = parent.prio;
            n.value = parent.value;
            n = parent;
            if(node.prio >= parent.prio && k == 1){
                break;
            }
        }
        n.prio = node.prio;
        n.value = node.value;
    }

    public float maior(){
        return this.start.value;
    }

    void down(int k, element n){
        element node = new element();
        node.def_value(n.value, n.prio);
        while(true){
            element right = start;
            element left = start;
            for(int i = 0; i < 2*k && left.next != null; i++){
                if(i < 2*k - 1){
                    left = left.next;
                }
                right = right.next;
            }
            if(right.prio > left.prio){
                n.def_value(right.value, right.prio);
                n = right;
                k = 2*k;
            }else{
                n.def_value(left.value, left.prio);
                n = left;
                k = 2*k + 1;
            }
            if(right.next == null || (node.prio >= left.prio && node.prio >= right.prio)){
                break;
            }
        }
        n.def_value(node.value, node.prio);
    }

    public void add(float value, int prio){
        element novo = new element();
        novo.def_value(value, prio);
        if(start == null){
            start = novo;
        }else{
            element aux = this.start;
            int i = 1;
            while(aux.next != null){
                i+= 1;
                aux = aux.next;
            }
            aux.next = novo;
            up(i+1, novo);
            System.out.printf("i = %d\n", i);
        }
    }

    public void delete(){
        element aux = this.start.next;
        this.start.next = null;
        this.start = aux;
        down(1, this.start);
    }

    public void changePrio(int oldPrio, int newPrio){
        element aux = this.start;
        int i = 1;
        while(aux.next != null && aux.prio != oldPrio){
            i+= 1;
            aux = aux.next;
        }
        if(aux.prio == oldPrio){
            aux.prio = newPrio;
            if(oldPrio > newPrio){
                down(i, aux);
            }else if(oldPrio < newPrio){
                up(i+1, aux);
            }else{
                System.out.println("A nova prioridade é mesma que a prioridade antiga.\n");
            }
        }else{
            System.out.println("Não há elemento com a prioridade dada.");
        }
    }

    public void print_heap(){
        if(start != null){
            element aux = start;
            System.out.print("[");
            while(aux.next != null){
                System.out.printf("%.1f, ", aux.value);
                aux = aux.next;
            }
            System.out.printf("%.1f]\n", aux.value);
        }else{
            System.out.println("Lista vazia!");
        }
    }
}
