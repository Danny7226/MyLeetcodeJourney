// 507
class Solution {
    // o(√N)
    public boolean checkPerfectNumber(int num) {
        if (num <= 0) return false;
        int sum = 0;
        double square = Math.pow(num, 0.5);
        if (num/square == square) sum += square;
        for (int div = 1; div < square; div++){
            if (num % div == 0){
                sum += num/div + div;
            if (sum > 2 * num){
                break;
            }
            }
        }
        return sum == 2 * num;
    }
}    