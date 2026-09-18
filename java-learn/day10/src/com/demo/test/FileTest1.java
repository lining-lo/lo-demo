package com.demo.test;

import java.io.File;
import java.util.Scanner;

public class FileTest1 {
    /*
        需求: 键盘录入一个文件夹路径，如果输入错误就给出提示，并继续录入，直到正确为止

        分析:
            1. 输入的路径有可能不存在
            2. 输入的路径有可能是文件路径

            封装为File对象
                调用 exists() 判断是否存在
                调用 isFile() 判断是否是文件

     */
    public static void main(String[] args) {

        File dir = getDir();
        System.out.println(dir);

    }

    public static File getDir() {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("请输入一个文件夹路径: ");
            String dir = sc.next();

            File file = new File(dir);

            if (!file.exists()) {
                System.out.println("您输入的文件夹路径不存在, 请检查!");
            } else if (file.isFile()) {
                System.out.println("您输入的是一个文件路径, 请重新输入文件夹路径: ");
            } else {
                return file;
            }
        }
    }
}
