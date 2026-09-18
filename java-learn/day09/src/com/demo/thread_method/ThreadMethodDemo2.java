package com.demo.thread_method;

public class ThreadMethodDemo2 {
    /*
        线程优先级的方法:

            public setPriority(int newPriority) : 设置线程优先级
            public final int getPriority() : 获取线程优先级
     */
    public static void main(String[] args) {
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 1; i <= 200; i++) {
                    System.out.println(Thread.currentThread().getName() + "--- 线程任务执行" + i);
                }
            }
        }, "线程A: ");

        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 1; i <= 200; i++) {
                    System.out.println(Thread.currentThread().getName() + "--- 线程任务执行" + i);
                }
            }
        }, "线程B: ");

        t1.setPriority(1);
        t2.setPriority(10);

        // System.out.println(t1.getPriority());
        // System.out.println(t2.getPriority());

        t1.start();
        t2.start();
    }
}
