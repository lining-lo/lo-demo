package com.demo.error;

public class OOMTest {
    public static void main(String[] args) {
        int[] arr = new int[Integer.MAX_VALUE];
    }
}
