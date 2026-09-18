package com.demo.stream;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileOutputStreamDemo1 {
    /*
      字节流写出数据

          构造方法:
                  1. public FileOutputStream(String name) : 输出流关联文件, 文件路径以字符串形式给出
                     public FileOutputStream(String name, boolean append) : 参数2为追加写入的开关

                  2. public FileOutputStream(File file) : 输出流关联文件, 文件路径以File对象形式给出
                     public FileOutputStream(File file, boolean append) : 参数2为追加写入的开关

          成员方法:
                  public void write(int i) : 写出一个字节
                  public void write(byte[] b) : 写出一个字节数组
                  public void write(byte[] b, int off, int len) : 写出字节数组的一部分

          细节:
                  输出流关联文件, 文件如果不存在: 会自动创建出来
                                  如果文件存在: 会清空现有的内容, 然后再进行写入操作
   */
    public static void main(String[] args) throws IOException {
        // 1. 创建字节输出流对象关联文件
        FileOutputStream fos = new FileOutputStream("E:\\A.txt", true);

        // 2. 写出数据
        byte[] bys = {97, 98, 99};

        fos.write(bys,0,2);

        fos.write("你好".getBytes());
    }
}


