import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        self.contents_copy = []
        for key, value in kwargs.items():
            i = 0
            while i < value:
                self.contents.append(key)
                self.contents_copy.append(key)
                i += 1
                
    def draw(self, num_balls) -> list:
        i = 0
        drawn_balls = []
            
        while i < num_balls:
            if len(self.contents) == 0:
                self.contents = self.contents_copy
            random_ball = random.choice(self.contents)
            self.contents.remove(random_ball) 
            drawn_balls.append(random_ball)
            i += 1
        
        return drawn_balls
            
        
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass