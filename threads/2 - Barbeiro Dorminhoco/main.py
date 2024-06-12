// Barbearia.java
import java.util.LinkedList;
import java.util.Queue;

public class Barbearia {
    private final int numeroDeCadeiras;
    private final Queue<Cliente> filaDeEspera;

    public Barbearia(int numeroDeCadeiras) {
        this.numeroDeCadeiras = numeroDeCadeiras;
        this.filaDeEspera = new LinkedList<>();
    }

    public synchronized void entrarNaBarbearia(Cliente cliente) {
        if (filaDeEspera.size() == numeroDeCadeiras) {
            System.out.println(cliente.getNome() + " saiu porque não havia cadeiras disponíveis.");
        } else {
            filaDeEspera.add(cliente);
            System.out.println(cliente.getNome() + " sentou-se para esperar.");
            notifyAll(); // Notifica o barbeiro que há um cliente esperando
        }
    }

    public synchronized Cliente obterProximoCliente() {
        while (filaDeEspera.isEmpty()) {
            try {
                System.out.println("Barbeiro está dormindo...");
                wait(); // Barbeiro dorme enquanto não há clientes
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        return filaDeEspera.poll();
    }
}

// Cliente.java
public class Cliente implements Runnable {
    private final String nome;
    private final Barbearia barbearia;

    public Cliente(String nome, Barbearia barbearia) {
        this.nome = nome;
        this.barbearia = barbearia;
    }

    public String getNome() {
        return nome;
    }

    @Override
    public void run() {
        System.out.println(nome + " entrou na barbearia.");
        barbearia.entrarNaBarbearia(this);
    }
}

// Barbeiro.java
public class Barbeiro implements Runnable {
    private final Barbearia barbearia;

    public Barbeiro(Barbearia barbearia) {
        this.barbearia = barbearia;
    }

    @Override
    public void run() {
        while (true) {
            Cliente cliente = barbearia.obterProximoCliente();
            if (cliente != null) {
                System.out.println("Barbeiro está cortando o cabelo de " + cliente.getNome());
                try {
                    Thread.sleep(3000); // Simula o tempo de cortar o cabelo
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                System.out.println("Barbeiro terminou de cortar o cabelo de " + cliente.getNome());
            }
        }
    }
}

// Main.java
public class Main {
    public static void main(String[] args) {
        Barbearia barbearia = new Barbearia(3); // Barbearia com 3 cadeiras
        Thread barbeiroThread = new Thread(new Barbeiro(barbearia));
        barbeiroThread.start();

        // Criando e iniciando threads de clientes
        for (int i = 1; i <= 10; i++) {
            Cliente cliente = new Cliente("Cliente " + i, barbearia);
            Thread clienteThread = new Thread(cliente);
            clienteThread.start();
            try {
                Thread.sleep(1000); // Intervalo entre a chegada dos clientes
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}
