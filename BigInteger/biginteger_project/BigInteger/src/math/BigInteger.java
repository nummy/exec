package math;

/**
 * This class encapsulates a BigInteger, i.e. a positive or negative integer with 
 * any number of digits, which overcomes the computer storage length limitation of 
 * an integer.
 * 
 */
public class BigInteger {

	/**
	 * True if this is a negative integer
	 */
	boolean negative;
	
	/**
	 * Number of digits in this integer
	 */
	int numDigits;
	
	/**
	 * Reference to the first node of this integer's linked list representation
	 * NOTE: The linked list stores the Least Significant Digit in the FIRST node.
	 * For instance, the integer 235 would be stored as:
	 *    5 --> 3  --> 2
	 */
	DigitNode front;
	
	/**
	 * Initializes this integer to a positive number with zero digits, in other
	 * words this is the 0 (zero) valued integer.
	 */
	public BigInteger() {
		negative = false;
		numDigits = 0;
		front = null;
	}
	
	/**
	 * Parses an input integer string into a corresponding BigInteger instance.
	 * A correctly formatted integer would have an optional sign as the first 
	 * character (no sign means positive), and at least one digit character
	 * (including zero). 
	 * Examples of correct format, with corresponding values
	 *      Format     Value
	 *       +0            0
	 *       -0            0
	 *       +123        123
	 *       1023       1023
	 *       0012         12  
	 *       0             0
	 *       -123       -123
	 *       -001         -1
	 *       +000          0
	 *       
	 * 
	 * @param integer Integer string that is to be parsed
	 * @return BigInteger instance that stores the input integer
	 * @throws IllegalArgumentException If input is incorrectly formatted
	 */
	public static BigInteger parse(String integer) 
	throws IllegalArgumentException {
		// THE FOLLOWING LINE IS A PLACEHOLDER SO THE PROGRAM COMPILES
		// YOU WILL NEED TO CHANGE IT TO RETURN THE APPROPRIATE BigInteger
		BigInteger b = new BigInteger();
		if(integer.charAt(0)=='-') {
			b.negative = true;
		}else {
			b.negative = false;
		}
		while((integer.charAt(0)=='0' || integer.charAt(0) == '+' || integer.charAt(0) == '-' ) && integer.length() > 1) {
			integer = integer.substring(1,integer.length());
		}
		for(int i=0; i<integer.length(); i++) {
			if(!Character.isDigit(integer.charAt(i))) {
				throw new IllegalArgumentException();
			}
		}
		for(int i=0; i<integer.length(); i++) {
			int num = Integer.parseInt(String.valueOf(integer.charAt(i)));
			DigitNode node = new DigitNode(num, b.front);
			b.front = node;
		}
		b.numDigits = integer.length();
		return b;
	}
	
	/**
	 * Adds an integer to this integer, and returns the result in a NEW BigInteger object. 
	 * DOES NOT MODIFY this integer.
	 * NOTE that either or both of the integers involved could be negative.
	 * (Which means this method can effectively subtract as well.)
	 * 
	 * @param other Other integer to be added to this integer
	 * @return Result integer
	 */
	public BigInteger add(BigInteger other) {
		// THE FOLLOWING LINE IS A PLACEHOLDER SO THE PROGRAM COMPILES
		// YOU WILL NEED TO CHANGE IT TO RETURN THE APPROPRIATE BigInteger
		BigInteger res = new BigInteger();
		if(this.negative == other.negative) {
			int len1 = this.numDigits;
			int len2 = other.numDigits;
			int len = 0;
			if(len1<len2) {
				len = len2;
			}else {
				len = len1;
			}
			res.negative = this.negative;
			int num1 = 0;
			int num2 = 0;
			int sum = 0;
			int carry = 0;
			int count = 0;
			DigitNode node1 = this.front;
			DigitNode node2 = other.front;
			while(count<len) {
				if(node1 == null) {
					num1 = 0;
				}else {
					num1 = node1.digit;
				}
				if(node2 == null) {
					num2 = 0;
				}else{
					num2 = node2.digit;
				}
				sum = num1+ num2 + carry;
				if(sum>=10) {
					carry = 1;
					sum = sum -10;
				}else {
					carry = 0;
				}
				DigitNode n = new DigitNode(sum, null);
				DigitNode p = res.front;
				if(p == null) {
					p = n;
					res.front = n;
				}else {
					while(p.next != null) {
						p = p.next;
					}
					p.next = n;
				}
				if(node1!=null) {
					node1 = node1.next;
				}
				if(node2!=null) {
					node2 = node2.next;
				}
				count++;
			}
			if(carry>0) {
				DigitNode n = new DigitNode(1, null);
				DigitNode p = res.front;
				if(p == null) {
					p = n;
					res.front = n;
				}else {
					while(p.next != null) {
						p = p.next;
					}
					p.next = n;
				}
				res.numDigits = len + 1;
			}else {
				res.numDigits = len;
			}
		}else {
			// get the bigger one
			BigInteger bigNum = null;
			BigInteger smallNum = null;
			int last1 = 0;
			int last2 = 0;
			if(this.numDigits > other.numDigits) {
				bigNum = this;
				smallNum = other;
			}else if (this.numDigits < other.numDigits) {
				bigNum = other;
				smallNum = this;
			}else {
				DigitNode p = this.front;
				if(p == null) {
					last1 = 0;
				}else {
					while(p.next != null) {
						p = p.next;
					}
					last1 = p.digit;
				}
				p = other.front;
				if(p == null) {
					last2 = 0;
				}else {
					while(p.next != null) {
						p = p.next;
					}
					last2 = p.digit;
				}
				if(last1>last2) {
					bigNum = this;
					smallNum = other;
				}else {
					bigNum = other;
					smallNum = this;
				}
			}
			res.negative = bigNum.negative;
			int num1 = 0;
			int num2 = 0;
			int sub = 0;
			int carry = 0;
			int count = 0;
			int len = bigNum.numDigits;
			DigitNode node1 = bigNum.front;
			DigitNode node2 = smallNum.front;
			while(count<len) {
				if(node1 == null) {
					num1 = 0;
				}else {
					num1 = node1.digit;
				}
				if(node2 == null) {
					num2 = 0;
				}else{
					num2 = node2.digit;
				}
				if(num1+carry < num2) {
					num1 = num1+ carry +10;
					carry = -1;
				}else {
					num1 = num1 + carry;
					carry = 0;
				}
				sub = num1-num2;
				//System.out.println("sub:" + sub+ " carry:" + carry);
				DigitNode n = new DigitNode(sub, null);
				DigitNode p = res.front;
				if(p == null) {
					p = n;
					res.front = n;
				}else {
					while(p.next != null) {
						p = p.next;
					}
					p.next = n;
				}
				count++;
				if(node1!=null) {
					node1 = node1.next;
				}
				if(node2!=null) {
					node2 = node2.next;
				}
			}
		}
		return res;
	}
	
	/**
	 * Returns the BigInteger obtained by multiplying the given BigInteger
	 * with this BigInteger - DOES NOT MODIFY this BigInteger
	 * 
	 * @param other BigInteger to be multiplied
	 * @return A new BigInteger which is the product of this BigInteger and other.
	 */
	public BigInteger multiply(BigInteger other) {
		// THE FOLLOWING LINE IS A PLACEHOLDER SO THE PROGRAM COMPILES
		// YOU WILL NEED TO CHANGE IT TO RETURN THE APPROPRIATE BigInteger
		BigInteger res = new BigInteger();
		res.front = new DigitNode(0, null);
		res.numDigits = 1;
		if(this.negative == other.negative) {
			res.negative = false;
		}else {
			res.negative = true;
		}
		if(this.numDigits == 1 && this.front.digit ==0) {
			return res;
		}
		if(other.numDigits==1 && other.front.digit==0) {
			return res;
		}
		DigitNode node1 = this.front;
		BigInteger temp = null;
		int count =0;
		other.negative = false;
		while(node1!=null) {
			temp = new BigInteger();
			int digit = node1.digit;
			for(int i=0; i<digit; i++) {
				temp = temp.add(other);
			}
			for(int i=0; i<count; i++) {
				DigitNode node = new DigitNode(0, temp.front);
				temp.front = node;
				temp.numDigits=temp.numDigits +1;
			}
			//System.out.println("#2 res:" + res);
			count++;
			res = res.add(temp);
			node1 = node1.next;
		}
		return res;
	}
	
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString() {
		if (front == null) {
			return "0";
		}
		String retval = front.digit + "";
		for (DigitNode curr = front.next; curr != null; curr = curr.next) {
				retval = curr.digit + retval;
		}
		
		if (negative) {
			retval = '-' + retval;
		}
		
		return retval;
	}
	public static void main(String[] args) {
//		System.out.println(BigInteger.parse("+0"));
//		System.out.println(BigInteger.parse("+123"));
//		System.out.println(BigInteger.parse("1023"));
//		System.out.println(BigInteger.parse("0012"));
//		System.out.println(BigInteger.parse("0"));
//		System.out.println(BigInteger.parse("-123"));
//		System.out.println(BigInteger.parse("-001"));
//		System.out.println(BigInteger.parse("+000"));
		BigInteger num1 = BigInteger.parse("-12");
		BigInteger num2 = BigInteger.parse("-34");
		System.out.println(num1.multiply(num2));
	}
}
