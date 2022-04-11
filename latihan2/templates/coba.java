
package pbo_m04_5210411178;

import java.util.Scanner;

public class SOAL01_PBO_M04_5210411178 {
    public static void main(String[] args){
        int menu;
        int[] array = {55, 31, 92, 36, 73};

        do {
            System.out.println("1. Tampilkan data");
            System.out.println("2. Memangkatkan setiap data");
            System.out.println("3. Mecari dua bilangan");
            System.out.println("4. Keluar Program");

            Scanner input = new Scanner(System.in);
            System.out.print("masukan nilai: ");
            menu = input.nextInt();

            switch(menu){
                case 1:
                    System.out.println("--- Tampilkan data ---");
                    for (int x = 0; x < array.length; x++){
                        System.out.println(array[x]);
                    }
                    System.out.println("----------------");
                    break;

                case 2:
                    System.out.println("--- Pangkatkan ---");
                    for (int x = 0; x < array.length; x++){
                        System.out.println(array[x] * array[x]);
                    }
                    System.out.println("----------------");
                    break;

                case 3:
                    System.out.println("--- Mencari dua bilangan ---");

                    Scanner bil = new Scanner(System.in);
                    System.out.print("bil pertama: ");
                    int bil_1 = bil.nextInt();
                    System.out.print("bil kedua: ");
                    int bil_2 = bil.nextInt();

                    for (int x = 0; x < array.length; x++){
                        for (int i = 0; i < array.length; i++){
                            if (bil_1 == array[x] && bil_2 == array[i]){
                                System.out.println(bil_1 + " dan " + bil_2 + " ditemukan! ");
                                break;
                            }else{
                                System.out.println(bil_1 + " dan " + bil_2 + " tidak ditemukan! "); 
                                break;           
                            }
                        }
                    }
                    System.out.println("----------------");
                    break;

                case 4:
                    System.out.println("--- keluar program ---");
                    break;

                default:
                    System.out.println("tidak ada di menu");
                    break;
            }input.close();
        } while(true);
    } 
}
