/**
* @Description Elementary practise of java
* @Author L.John
* @Version 1.0.0
* @Date 2020-10-04 13:56:56
*/

public class prac0{
    public static void main(String[] args){
        // 1.Hello World!
        System.out.println("Hello World!");
        // 2.Value types
        char c = 'a';//单引号只用于单个字符
        System.out.println(c);
        // 3.Reference types
        String str = "Hello" + " World!";
        System.out.println(str);//双引号可用于多个字符
        // 4.operation
        System.out.println(7 / 2.0);
        int i1 = 10, i2 = 20;
        int i = i1++;//先对i赋值，i1再+1
        System.out.println(+i);
        System.out.println(+i1);
        i = ++i1;//先对i1+1，再对i赋值
        System.out.println(+i);
        System.out.println(+i1);
        i = i2--;
        System.out.println(+i);
        System.out.println(+i2);
        i = --i2;
        System.out.println(+i);
        System.out.println(+i2);
        // 5.assignment operation
        short s = 5;
        s += 3;//+=可用于隐式强制变换数据类型
        s = (short) (s + 1);
        System.out.println(s);
        // 6.Bitwise operation
        short s0 = -128;
        System.out.println(s0>>1);//二进制变量值左边第一位为符号位，用于判断值位数右移后左边补0还是1
        // 7.Operation rank
        System.out.println(1 + 6 % 4 * 2 + 1);//相同优先级从代码左侧往右顺序运算；不同优先级，优先级高的先运算
        // 8.Structure
        int i3 = 3;
        if (i3 == 1){
            System.out.println("1");
        }else if (i3 == 2){
            System.out.println("2");
        }else {
            System.out.println("3");
        }

        int i4 = 1;
        switch (i4){
            case 1:
                System.out.println("a");
                break;
            case 2:
                System.out.println("b");
                break;
            default:
                System.out.println("0");
                break;
        }
        // 9.Loop structure
        for (int i5 = 0; i5 < 5; i5++){
            System.out.println("Hello World!");
        }

        int i6 = 1;
        while (i6 <= 5){
            System.out.println(i6);
            i6++;
        }

        int m = 1;
        do{
            System.out.println(m);
            m++;
        }while(m <= 5);

        for (int i7 = 0; i7 < 2; i7++){//建议外层循环次数小于内层循环次数
            for (int j = 0; j < 5; j++){

            }
        }

        for (int i8 = 2; i8 <= 100; i8++){// 找出2-100内质数
            int k = 0;
            for (int j = 2; j < i; j++){
                if (i % j == 0){
                    k++;
                }
            }
            if (k == 0){
                System.out.println(i);
            }
        }
        // 10.Special structure
        // break终止当前所在循环；continue跳过一次当前所在循环，不执行该次循环内的后面代码；return结束整个方法
        // 11.Array
        int[] i9 = {1,2,3};// int[] i = new int[4];数字类型元素默认值为0，对象类型元素默认值为null
        int b[] = {1,2,3};// int[] i = new int[]{1,2};
        System.out.println(i9[1]);
        System.out.println(b.length);
        int[][] arr = new int[2][];//二维数组，必须定义第一维长度，第二维长度对应的每个一维数组可分别初始化
        arr[0] = new int[]{1,2,3,4};
        arr[1] = new int[]{1,2,3};
        int[][] arr0 = new int[][]{
            {1,2,3,4},
            {1,2,3}
        };
        //特殊写法，同时定义一维数组x，二维数组y
        int[] x,y[] = new int[2][2];
        x = new int[]{1,2};
        y[0] = new int[]{1,2,3};
        // 12.Array sort
        // 冒泡排序
        int[] arr1 = new int[]{4,7,3,1};
        int temp = 0;
        for (int i10 = 0; i10 < arr1.length - 1; i10++) {//外层循环是循环轮次，其次数为数组长度-1
            for (int j = 0 ; j < arr1.length - 1 -i10; j++) {//每轮循环进行相邻数字对比排序，循环次数为数组长度-1-对应的外层循环轮次
                if (arr1[j] > arr1[j + 1]) {
                    temp = arr1[j];
                    arr1[j] = arr1[j + 1];
                    arr1[j + 1] = temp;
                }
            }
        }
        for (int i11 = 0; i11 < arr1.length; i11++) {
            System.out.println(arr1[i11]);
        }
    }
}

