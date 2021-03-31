import java.util.Scanner;
import heap.heap;

class principal {
    public static void main(String Args[]) {
        boolean b = true;
        int entrada, prio;
        float value;
        Scanner scan = new Scanner(System.in);
        heap h = new heap();
        while (b) {
            System.out.printf("01)\tAdicionar elemento\n02)\tRemover elemento de maior prioridade\n03)\tBuscar elemento de maior prioridade\n04)\tAlterar prioridade\n05)\tImprimir heap\n06)\tSair\n");
            System.out.print("Insira a entrada desejada: ");
            entrada = Integer.parseInt(scan.nextLine());
            switch(entrada){
                case 1:
                    System.out.print("Insira a prioridade do elemento que deseja adicionar: ");
                    prio = Integer.parseInt(scan.nextLine());
                    System.out.print("Insira o valor do elemento que deseja adicionar: ");
                    value = Float.parseFloat(scan.nextLine());
                    h.add(value, prio);
                    break;

                case 2:
                    h.delete();
                    break;

                case 3:
                    System.out.printf("O elemento de maior prioridade possui valor %.2f\n", h.maior());
                    break;

                case 4:
                    System.out.print("Insira a prioridade do elemento que deseja mudar a prioridade: ");
                    prio = Integer.parseInt(scan.nextLine());
                    System.out.print("Insira a nova prioridade do elemento: ");
                    int newPrio = Integer.parseInt(scan.nextLine());
                    h.changePrio(prio, newPrio);
                    break;

                case 5:
                    h.print_heap();
                    break;

                case 6:
                    b = false;
                    break;

                default:
                    System.out.println("Opção não encontrada!");
                    break;
            }
        }
        scan.close();
    }
}