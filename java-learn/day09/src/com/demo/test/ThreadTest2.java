package com.demo.test;

public class ThreadTest2 {
    /*
        同步方法: 在方法的返回值类型前面加入 synchronized 关键字

        方法分为静态和非静态
        静态方法的锁对象是字节码对象，非静态方法的锁对象是 this
     */
    public static void main(String[] args) {
        TicketTask2 task = new TicketTask2();

        Thread t1 = new Thread(task, "窗口A");
        Thread t2 = new Thread(task, "窗口B");

        t1.start();
        t2.start();
    }
}

class TicketTask2 implements Runnable {

    static int tickets = 1000;

    @Override
    public void run() {
        while (true) {

            String name = Thread.currentThread().getName();

            if ("窗口A".equals(name)) {
                if (method()) {
                    break;
                }
            } else if ("窗口B".equals(name)) {
                synchronized (TicketTask2.class) {
                    if (tickets == 0) {
                        break;
                    }
                    System.out.println(Thread.currentThread().getName() + "卖出了第" + tickets + "号票");
                    tickets--;
                }
            }


        }
    }

    private static synchronized boolean method() {
        if (tickets == 0) {
            return true;
        }
        System.out.println(Thread.currentThread().getName() + "卖出了第" + tickets + "号票");
        tickets--;
        return false;
    }
}