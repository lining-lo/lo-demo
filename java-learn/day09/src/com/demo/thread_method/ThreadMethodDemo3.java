package com.demo.thread_method;

public class ThreadMethodDemo3 {
    /*
        public final void setDaemon(boolean on) : 设置为守护线程
     */
    public static void main(String[] args) {
        Thread t1 = new Thread(new Runnable(){
            @Override
            public void run() {
                for(int i = 1; i <= 20; i++){
                    System.out.println(Thread.currentThread().getName() + "--- 任务执行了" + i);
                }
            }
        }, "线程A");

        Thread t2 = new Thread(new Runnable(){
            @Override
            public void run() {
                for(int i = 1; i <= 200; i++){
                    System.out.println(Thread.currentThread().getName() + "--- 任务执行了" + i);
                }
            }
        }, "线程B");

        t2.setDaemon(true);

        t1.start();
        t2.start();
    }
}
