import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for key, value in kwargs.items():
            i = 0
            while i < value:
                self.contents.append(key)
                i += 1
                
    def draw(self, num_balls) -> list:
        i = 0
        drawn_balls = []
            
        if len(self.contents) <= num_balls:
            return self.contents
                
        while i < num_balls:
            random_ball = random.choice(self.contents)
            self.contents.remove(random_ball) 
            drawn_balls.append(random_ball)
            i += 1
        

        return drawn_balls
            
        
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> float:
    i = 0
    while i < 5:
        hat_copy = copy.deepcopy(hat)
        print(hat_copy.draw(4))
        i += 1