public class KeywordsAndExpressions {
    public static void main(String[] args) {
        // A mile is equal to 1.609344 kilometers
        double kilometers = (100 * 1.609344);
        
        int highScore = 50;

        if (highScore > 25) {
            highScore  = 1000 + highScore;
        }

        int health = 100;

        if ((health < 25) && (highScore > 1000)) {
            highScore = highScore - 1000;
        }

        int myVariable = 50;

        myVariable++;
        myVariable--;

        System.out.println("This is a test");

        System.out.println("This is" +
                " another" +
                " still more.");

        int anotherVariable = 50; 
        myVariable--; 
        System.out.println("This is another one");

        boolean gameOver = true;
        int score = 5000;
        int levelCompleted = 5;
        int bonus = 100;

        if (score == 5000) {
            System.out.println("Your score was 5000");
        }

        
    }
}
