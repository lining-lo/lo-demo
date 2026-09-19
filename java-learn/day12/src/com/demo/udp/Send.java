package com.demo.udp;

import java.net.*;

public class Send {
    public static void main(String[] args) throws Exception {
        // 1. 创建发送端的DatagramSocket对象 (发送端的驿站)
        // DatagramSocket socket = new DatagramSocket();  随机绑定端口
        DatagramSocket socket = new DatagramSocket(8888);

        // 2. 准备发送的数据
        String msg = "你好";
        byte[] bytes = msg.getBytes();

        // 3. 将数据打包
        DatagramPacket packet = new DatagramPacket(bytes, bytes.length,
                InetAddress.getByName("127.0.0.1"), 9999);

        // 4. 发送数据
        socket.send(packet);

        // 5. 释放资源
        socket.close();
    }
}
