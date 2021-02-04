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
        
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass