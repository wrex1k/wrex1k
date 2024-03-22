```java
public class Pyramid {
  int floors;
  char znak = '*';
  
  void classic() {
      for (int i = 0; i < floors; i++) {
        for (int j = 0; j < floors - i - 1; j++) {
            System.out.print(" ");
        }
        for (int j = 0; j < 2*i + 1; j++) {
            System.out.print(znak);
        }
      System.out.println();
    }
  }
  
  void reversed() {
    for (int i = floors - 1; i >= 0; i--) {
        for (int j = 0; j < floors - i - 1; j++) {
            System.out.print(" ");
        }
        for (int j = 0; j < 2*i + 1; j++) {
            System.out.print(znak);
        }
      System.out.println();
    }
  }
  
  void river() {
    for (int i = 0; i < floors; i++) {
        for (int j = 0; j < floors - i - 1; j++) {
            System.out.print(" ");
        }
        for (int j = 0; j < 2*i + 1; j++) {
            System.out.print(znak);
        }
      System.out.println();
    }
    for (int p = 0; p < floors*2 - 1; p++) {
        System.out.print('=');
    }
    System.out.println();
  }
  
}
```

<!--
**wrex1k/wrex1k** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
