```java
public class Pyramid {
    int floors;
    char symbol = '*';

    void classic() {
        for (int i = 0; i < floors; i++) {
            for (int j = 0; j < floors - i - 1; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * i + 1; j++) {
                System.out.print(symbol);
            }
            System.out.println();
        }
    }

    void reversed() {
        for (int i = floors - 1; i >= 0; i--) {
            for (int j = 0; j < floors - i - 1; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * i + 1; j++) {
                System.out.print(symbol);
            }
            System.out.println();
        }
    }

    void river() {
        for (int i = 0; i < floors; i++) {
            for (int j = 0; j < floors - i - 1; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < 2 * i + 1; j++) {
                System.out.print(symbol);
            }
            System.out.println();
        }
        for (int p = 0; p < floors * 2 - 1; p++) {
            System.out.print('=');
        }
        System.out.println();
    }
}
```
