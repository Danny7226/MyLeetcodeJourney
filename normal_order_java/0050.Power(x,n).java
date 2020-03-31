class Solution {
    // n might be -2147483648(-2^31);
    // double range from (-2^31 ~ 2^31-1)
    public double myPow(double x, int n) {
        if (x==1) return 1;
        if (n<0) {
            x = 1/x;
            n = -n;
        }
        double res = 1;
        while (n!=0){
            if (n<0) n = -n;
            if (n % 2 == 1){
                res *= x;
                n -= 1;
            }else{
                x *= x;
                n >>= 1;
            }
        }
        return res;
    }
}