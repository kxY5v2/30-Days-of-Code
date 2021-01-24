'''
Objective:
    Today, we're learning about Interfaces. Check out the Tutorial 
    tab for learning materials and an instructional video! 

Task:
    The AdvancedArithmetic interface and the method declaration for
    the abstract divisorSum(n) method are provided for you in the editor
    below.
    Complete the implementation of Calculator class, which implements the
    AdvancedArithmetic interface. The implementation for the divisorSum(n)
    method must return the sum of all divisors of n.

Input Format:
    A single line containing an integer, n.

Constraints:
    1 <= n <= 1000

Output Format:
    You are not responsible for printing anything to stdout. The locked 
    template code in the editor below will call your code and print the 
    necessary output.    

Sample Input:
    6
Sample Output:
    I implemented: AdvancedArithmetic
    12

Explanation:
    The integer 6 is evenly divisible by 1, 2, 3, and 6. our divisorSum 
    method should return the sum of these numbers, which is 1 + 2 + 3 + 6 = 12.
    The solution class then prints I implemented: AdvancedArithmetic on the first
    line, followed by the sum returned by divisorSum (which is 12)
    on the second line.
'''

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        self.n = n
        divisors = []
        for i in range(n+1):
            if i != 0:
                if n % i == 0:
                    divisors.append(i)
                else:
                    pass
            else:
                pass
        sumD = 0
        for div in divisors:
            sumD += div
        return sumD


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)