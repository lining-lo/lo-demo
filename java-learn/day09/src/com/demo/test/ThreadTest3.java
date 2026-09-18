package com.demo.test;

import java.util.concurrent.locks.ReentrantLock;

public class ThreadTest3 {
    /*
        使用 Lock 锁, 我们可以更清晰的看到哪里加了锁，哪里释放了锁
        Lock 是接口, 无法直接创建对象, 需要创建 ReentrantLock
     */
    public static void main(String[] args) {
        TicketTask3 task = new TicketTask3();

        Thread t1 = new Thread(task, "窗口A");
        Thread t2 = new Thread(task, "窗口B");

        t1.start();
        t2.start();
    }
}

class TicketTask3 implements Runnable {

    int tickets = 1000;
    ReentrantLock lock = new ReentrantLock();

    @Override
    public void run() {
        while (true) {
            try {
                lock.lock();
                if (tickets == 0) {
                    break;
                }
                System.out.println(Thread.currentThread().getName() + "卖出了第" + tickets + "号票");
                tickets--;
            } finally {
                lock.unlock();
            }
        }

    }

}