// https://stackoverflow.com/questions/4582277/biginteger-powbiginteger
// https://docs.oracle.com/javase/7/docs/api/java/math/BigInteger.html#modPow(java.math.BigInteger,%20java.math.BigInteger)

import java.math.BigInteger;

public class BigIntegerCalculator {
    public static void main(String args[]) {
        BigInteger C = new BigInteger("455254144570149659309053721142936464401700360179699485409768697057718862"); 
        BigInteger d = new BigInteger("298082873119252710460625055681222869281660460407961156878212145977719009"); 
        BigInteger N = new BigInteger("501281908486219621910086584233925309600136539640088201223414043112175611");
        System.out.println("M = " + C.modPow(d, N));
    }
}
