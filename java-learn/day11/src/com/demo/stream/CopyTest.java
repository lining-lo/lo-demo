package com.demo.stream;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class CopyTest {
    /*
        将 D:\嘿嘿.jpg，拷贝到 E:\ 根目录下
     */
    public static void main(String[] args) {
        try ( // 创建输入流对象读取文件
              FileInputStream fis = new FileInputStream("D:\\嘿嘿.jpg");
              // 创建输出流对象关联数据目的x
              FileOutputStream fos = new FileOutputStream("E:\\copy.jpg");) {
            // 读写操作
            int len;
            byte[] bys = new byte[1024];
            while ((len = fis.read(bys)) != -1) {
                fos.write(bys, 0, len);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
