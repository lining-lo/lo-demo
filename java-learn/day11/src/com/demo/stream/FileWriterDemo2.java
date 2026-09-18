package com.demo.stream;

import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;

public class FileWriterDemo2 {
    /*
        注意事项: 字符输出流写出数据, 需要调用flush或close方法, 数据才会写出

            flush() : 刷出数据, 刷出后可以继续写出
            close() : 关闭流释放资源, 顺便刷出数据, 关闭后不可以继续写出
     */
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("E:\\A.txt");

        fw.write("你好");
        fw.write("我好");

        fw.close();
    }
}
