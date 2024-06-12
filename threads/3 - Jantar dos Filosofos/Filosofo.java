public class Filosofo extends Thread {
    final static int TEMPO_MAXIMO = 100;
    Mesa mesa;
    int filosofo;

    public Filosofo(String nome, Mesa mesa, int filosofo) {
        super(nome);
        this.mesa = mesa;
        this.filosofo = filosofo;
    }

    public void run() {
        int acoesRealizadas = 0;
        while (acoesRealizadas < 10) { // 
            pensar();
            mesa.pegarHashis(filosofo);
            comer();
            mesa.devolverHashis(filosofo);
            acoesRealizadas++;
        }
    }

    public void pensar() {
        int tempo = (int) (Math.random() * TEMPO_MAXIMO);
        try {
            sleep(tempo);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void comer() {
        int tempo = (int) (Math.random() * TEMPO_MAXIMO);
        try {
            sleep(tempo);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
