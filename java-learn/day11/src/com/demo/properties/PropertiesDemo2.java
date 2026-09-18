package com.demo.properties;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Properties;

public class PropertiesDemo2 {
    /*
        Properties 和 IO 有关的方法

            void load(InputStream inStream)     从输入字节流读取属性列表（键和元素对）
            void load(Reader reader)            从输入字符流读取属性列表（键和元素对）
            void store(OutputStream out, String comments)   将集合的键值对写出到文件(字节流)
            void store(Writer writer, String comments)      将集合的键值对写出到文件(字符流)
     */
    public static void main(String[] args) throws IOException {
        Properties prop = new Properties();
        prop.setProperty("name", "zhangsan");
        prop.setProperty("age", "25");

        FileWriter fos = new FileWriter("day11\\test.properties");

        prop.store(fos,null);

        fos.close();
    }

    private static void method() throws IOException {
        Properties prop = new Properties();

        FileInputStream fis = new FileInputStream("day11\\config.properties");

        prop.load(fis);

        fis.close();

        System.out.println(prop);
    }
}
