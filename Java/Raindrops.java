class RaindropConverter {

    String convert(int number) {
      String I="Pling";      
      String A="Plang";
      String O="Plong";

      if (number % 3 == 0 && number % 5 == 0 && number % 7 == 0) {
          return I+A+O;
      } else if (number % 3 == 0 && number % 5 == 0) {
          return I+A;
      } else if (number % 3 == 0 && number % 7 == 0) {
          return I+O;
      } else if (number % 5 == 0 && number % 7 == 0) {
          return A+O;
      } else if (number % 3 == 0) {
          return I;
      } else if (number % 5 == 0) {
        return A;
      } else if (number % 7 == 0) {
        return O;
      } else {
          return Integer.toString(number);
      }  
    }  
}