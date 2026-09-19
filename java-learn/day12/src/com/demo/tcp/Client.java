package com.demo.tcp;

import java.io.*;
import java.net.Socket;

public class Client {
    public static void main(String[] args) throws IOException {
        // 使用File对象, 封装要上传的文件
        File src = new File("D:\\2.jpg");

        // 1. 创建客户端的站点指定服务端的ip和端口
        Socket socket = new Socket("localhost", 8899);

        // 2. 客户端通过socket获取传输数据的输入输出流
        InputStream is = socket.getInputStream();
        OutputStream os = socket.getOutputStream();

        // 3. 客户端创建本地的流对象, 读取要上传的文件
        FileInputStream fis = new FileInputStream(src);
        byte[] bys = new byte[1024];
        int len;
        while((len = fis.read(bys)) != -1){
            // 重点: 将读取到的字节, 通过网络流对象, 写出给服务端
            os.write(bys, 0, len);
        }
        // 客户端给服务端结束的标记
        socket.shutdownOutput();
        fis.close();

        // 4. 读取服务端发送回来的消息  (上传成功)
        byte[] data = new byte[1024];
        int dataLength = is.read(data);
        String msg = new String(data, 0, dataLength);

        System.out.println("读取到服务的消息为:" + msg);

        // 5. 关闭流, 释放资源
        is.close();
        os.close();
        socket.close();

    }
}
