import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **ar):
        self.contents = []
        for k, v in ar.items():
            for i in range(v):
                self.contents.append(k)
    
    def draw(self,amount):
        listt = []

        if amount >= len(self.contents):
            return self.contents

        for i in range(amount):
            list_r = random.choice(self.contents)
            listt.append(list_r)
            self.contents.pop(self.contents.index(list_r))
            
        return listt
       
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    results = 0

    for i in range(num_experiments):
        my_hat = copy.deepcopy(hat)

        my_balls = my_hat.draw(num_balls_drawn)
    
        my_balls_dict = {ball: my_balls.count(ball) for ball in set(my_balls)}

        result = True
        for v, v in expected_balls.items():
            if key not in my_balls_dict or my_balls_dict[v] < expected_balls[v]:
                result = False
                break

        if result:
            results += 1

    return results/num_experiments
