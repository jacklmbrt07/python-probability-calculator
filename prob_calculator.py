import copy
import random
# Consider using the modules imported above.

class Hat:
    # initialize Hat, adds each ball into contents.
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    
    # draws balls out of hat, and then removes it from the contents. 
    def draw(self, num_balls) -> list:
        drawn_balls = []
            
        # error handling, just returns the contents if more balls to draw than exist in the hat.
        if len(self.contents) <= num_balls:
            return self.contents
                
        # removes the randomly chosen ball from the hat and adds it to a new list.
        for i in range(num_balls):
            random_ball = random.choice(self.contents)
            self.contents.remove(random_ball) 
            drawn_balls.append(random_ball)

        return drawn_balls
            
        
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> float:
    expected_list = []
    M = 0
    N = num_experiments
    
    # converts the expected_balls dictionary into a list
    for key, value in expected_balls.items():
        for i in range(value):
            expected_list.append(key)
    
    # if x balls are drawn from a hat, and it matches the expected_list, considered a success, and M is incremented.
    for i in range(N):
        hat_copy = copy.deepcopy(hat)
        draw_list = hat_copy.draw(num_balls_drawn)
        m = 0
        for ball in expected_list:
            if ball in draw_list:
                draw_list.remove(ball) # chosen ball must removed in case of multiple expected balls.(such as 2 blues)
                m += 1
            if m == len(expected_list): 
                M += 1
            
    # M = number of successful tests, N = total number of tests. Probaility is M / N. Probability becomes more accurate with increasing N. 
    return M / N
        