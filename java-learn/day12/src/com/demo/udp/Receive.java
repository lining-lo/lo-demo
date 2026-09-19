package com.demo.udp;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class Receive {
    public static void main(String[] args) throws IOException {
        // 1. 创建接收端的DatagramSocket对象 (接收端的驿站)
        DatagramSocket socket = new DatagramSocket(9999);

        // 2. 准备接收端的包裹对象
        DatagramPacket packet = new DatagramPacket(new byte[1024], 1024);

        // 3. 接受数据
        System.out.println(1);
        socket.receive(packet);
        System.out.println(2);

        // 4. 拆包裹
        byte[] data = packet.getData();
        String msg = new String(data, 0, packet.getLength());
        String ip = packet.getAddress().getHostAddress();
        System.out.println("接收到" + ip + "发送的数据为:" + msg);

        // 5. 释放资源
        socket.close();
    }
}
