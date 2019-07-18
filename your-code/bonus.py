class ClimbStairs:

    def __init__(self, total_steps=10): 
        self.total_steps = total_steps
        self.calculation_count = 0

    def calc_solutions(self, i):
        if i == 0 or i == 1:
            return 1
        else:
            cont = [x for x in range(i+1)]
            cont[0] = 1 
            cont[1] = 1
        for x in range(2, i+1):
            cont[x] = cont[x-1] + cont[x-2]
            self.calculation_count += 1
        return cont[i]
    
    def get_calculation_count(self):
        return self.calculation_count

    def solve(self):
        return self.calc_solutions(0)

total_steps = input("How many steps in the stair?")
new_challenge = ClimbStairs(int(total_steps))
print('Ways to climb to top: ' + str(new_challenge.calc_solutions(int(total_steps))))
print('Total calculations performed: ' + str(new_challenge.get_calculation_count()))


