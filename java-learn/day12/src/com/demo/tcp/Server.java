package com.demo.tcp;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) throws IOException {
        // 1. 创建ServerSocket对象
        ServerSocket server = new ServerSocket(8899);
        System.out.println("服务端开启, 等待客户端连接...");
        // 2. 响应客户端发送的请求
        Socket socket = server.accept();
        System.out.println("响应成功!");

        // 3. 服务端通过socket获取传输数据的输入输出流
        InputStream is = socket.getInputStream();
        OutputStream os = socket.getOutputStream();

        // 本地字节输出流
        FileOutputStream fos = new FileOutputStream("E:\\result.jpg");

        // 4. 读取客户端发送过来的文件 (图片的字节)
        byte[] bys = new byte[1024];
        int len;
        while ((len = is.read(bys)) != -1) {
            fos.write(bys, 0, len);
        }
        fos.close();

        // 5. 写出上传成功的消息给客户端
        os.write("上传成功".getBytes());

        // 6. 关闭流, 释放资源
        is.close();
        os.close();
        socket.close();
    }
}
