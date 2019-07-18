"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

For example, if the stair has 4 steps, there are 5 ways to climb to the top:
1) 1, 1, 1, 1
2) 1, 2, 1
3) 1, 1, 2
4) 2, 1, 1
5) 2, 2

The following class calculates the total ways to climb a stair with the specified number of steps.
It also counts the number of calculations performed which indicates the efficiency of the code.
Try if you can improve the performance of the code.
"""

class ClimbStairs:
    """
    Class constructor
    total_steps: how many steps in total in the stair
    """
    def __init__(self, total_steps=10): 
        self.total_steps = total_steps
        self.calculation_count = 0

    """
    This function calculates how many solutions are there to reach the top when I am currently at the ith 
    step i - the step I am currently at
    """
    def calc_solutions(self, i):
        # If the current step is already larger than total steps, there's 0 solution
        if i > self.total_steps:
            return 0

        # If the current step equals to the total steps, there is only one solution because I've reached 
        # the top
        if i == self.total_steps:
            return 1

        # If I am still in the middle of the stair, continue calculating
        self.calculation_count += 1

        # Call the current function recursively. 
        # The number of solutions at the ith step equals to the number of solutions at the (i+1)th step 
        # plus the number of solutions at the (i+2)th step
        return(self.calc_solutions(i+1) + self.calc_solutions(i+2))

    def get_calculation_count(self):
        return self.calculation_count

    def solve(self):
        #return self.calc_solutions(0)
        return self.calc_solutions2(self.total_steps)
    
    def calc_solutions2(self,i):
        act_l = [1,0]
        next_l = [1,1]
        if i == 1:
            return 1
        elif i == 2:
            return 2
        else:
            for i in range(i-2):
                self.calculation_count += 2
                new_l = [act_l[0]+next_l[0],act_l[1]+next_l[1]]
                act_l = next_l
                next_l = new_l
            self.calculation_count += 1
            return new_l[0]+new_l[1]

# In the optimization of this code I got the pattern in the secuence of the decision tree 
# for a stair with 30 steps the original recursively made 2178308 calculations.
# In the alternative implementation we get the same result with 57 calculations (2 sums in
# a for loop with 28 iterations and a final sum to return the result)

# A problem is that if we try to save all the posible ways with the new implementation it is
# not posible and I think that with the first we could do it.

total_steps = input("How many steps in the stair?")
new_challenge = ClimbStairs(int(total_steps))
print('Ways to climb to top: ' + str(new_challenge.solve()))
print('Total calculations performed: ' + str(new_challenge.get_calculation_count())) 