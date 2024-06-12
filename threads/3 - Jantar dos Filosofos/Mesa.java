public class Mesa {
    boolean[] hashis = new boolean[5];

    public Mesa() {
        for (int i = 0; i < 5; i++) {
            hashis[i] = true;
        }
    }

    public synchronized void pegarHashis(int filosofo) {
        while (!hashis[filosofo] || !hashis[(filosofo + 1) % 5]) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        hashis[filosofo] = false;
        hashis[(filosofo + 1) % 5] = false;
        System.out.println("Filósofo " + filosofo + " está comendo.");
        printEstadoHashis();
    }

    public synchronized void devolverHashis(int filosofo) {
        hashis[filosofo] = true;
        hashis[(filosofo + 1) % 5] = true;
        System.out.println("Filósofo " + filosofo + " está meditando.");
        printEstadoHashis();
        notifyAll();
    }

    public void printEstadoHashis() {
        String status = "";
        for (int i = 0; i < 5; i++) {
            status += hashis[i] ? "LIVRE " : "OCUPADO ";
        }
        System.out.println("Estado dos hashis: " + status);
    }
}
