package com.demo.thread;

public class ThreadDemo2 {
    /*
        开启线程的第一种方式 - 继承Thread类

        1. 编写一个类继承Thread类
        2. 重写run方法
        3. 将线程任务代码写在run方法中
        4. 创建线程对象
        5. 调用start方法开启线程

        注意事项: 调用start方法的时候, 会自动调用run方法.

                    - 只有是调用了start()方法, 才是开启了新的线程.
     */
    public static void main(String[] args) {
        // 4. 创建线程对象
        MyThread mt = new MyThread();
        // 5. 调用start方法开启线程
        mt.start();

        for (int i = 1; i <= 500; i++) {
            System.out.println("main线程执行任务" + i);
        }
    }
}

// 1. 编写一个类继承Thread类
class MyThread extends Thread {
    // 2. 重写run方法
    @Override
    public void run() {
        // 3. 将线程任务代码写在run方法中
        for (int i = 1; i <= 500; i++) {
            System.out.println("线程任务执行了" + i);
        }
    }
}
