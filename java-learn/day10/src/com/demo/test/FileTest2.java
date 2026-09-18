package com.demo.test;

import java.io.File;

public class FileTest2 {
    /*
        需求：键盘录入一个文件夹路径，找出这个文件夹下所有的 .java 文件

        public File[] listFiles()  获取当前目录下所有的  “一级文件对象”  返回 File 数组
     */
    public static void main(String[] args) {

        File dir = FileTest1.getDir();

        printJavaFile(dir);
    }

    private static void printJavaFile(File dir) {
        // 1. 获取当前文件夹下所有的文件和文件夹对象
        File[] files = dir.listFiles();
        // 2. 遍历数组, 获取每一个文件和文件夹对象
        for (File file : files) {
            // 3. 判断当前对象是否是文件, 并且是java文件
            if(file.isFile() && file.getName().endsWith(".java")){
                // 4. 打印在控制台
                System.out.println(file);
            }
        }
    }
}
