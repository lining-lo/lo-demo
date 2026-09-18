package com.demo.thread_method;

public class ThreadNameDemo1 {
    /*
        线程设置名字和获取名字

        Thread类的方法:

            public String getName() : 获取线程名字
            public void setName() : 设置线程名字
            public static Thread currentThread() : 获取当前线程的对象

     */
    public static void main(String[] args) {
        MyThread mt1 = new MyThread("线程A: ");
        MyThread mt2 = new MyThread("线程B: ");

        // mt1.setName("线程A: ");
        // mt2.setName("线程B: ");

        mt1.start();
        mt2.start();
    }
}

class MyThread extends Thread {

    public MyThread() {
    }

    public MyThread(String name) {
        super(name);
    }

    @Override
    public void run() {
        for (int i = 1; i <= 200; i++) {
            System.out.println(super.getName() + "线程任务执行了" + i);
        }
    }
}