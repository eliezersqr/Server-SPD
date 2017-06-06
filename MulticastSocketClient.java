import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class MulticastSocketClient {
    
    final static String INET_ADDR = "224.0.0.3";
    final static int PORT = 8888;

    public static void main(String[] args) throws UnknownHostException {
     
        InetAddress address = InetAddress.getByName(INET_ADDR);
       
        byte[] buf = new byte[1024];
        
        System.out.println("Escolha um canal de 1 a 10 ou ENTER para ouvir todos os canais: ");
        @SuppressWarnings("resource")
		Scanner reader = new Scanner(System.in); 
        int n = reader.nextInt();
        
        if (n >= 1 && n <= 10){
        	
        	System.out.println("\n - Ouvindo Canal " + n + " - \n");
        	
	        try (MulticastSocket clientSocket = new MulticastSocket(PORT)){
	        	
	            clientSocket.joinGroup(address);
	     
	            while (true) {

	                DatagramPacket msgPacket = new DatagramPacket(buf, buf.length);
	                clientSocket.receive(msgPacket);
	
	                String msg = new String(buf, 0, buf.length);
	                
	                // Aqui manipular a string para verificar o canal desejado
	                
	                System.out.println("Mensagem Recebida: " + msg);
	            }
	        } catch (IOException ex) {
	            ex.printStackTrace();
	        }  
        	
        }else {
        	
        	System.out.println("\n - Ouvindo todos os canais - \n");
        	
	        try (MulticastSocket clientSocket = new MulticastSocket(PORT)){
	        	
	            clientSocket.joinGroup(address);
	     
	            while (true) {

	                DatagramPacket msgPacket = new DatagramPacket(buf, buf.length);
	                clientSocket.receive(msgPacket);
	
	                String msg = new String(buf, 0, buf.length);
	                
	                // Aqui fazer a manipulação da String recebida
	                
	                System.out.println("Mensagem Recebida: " + msg);
	            }
	        } catch (IOException ex) {
	            ex.printStackTrace();
	        }        	
        	
        }
        

    }
}
