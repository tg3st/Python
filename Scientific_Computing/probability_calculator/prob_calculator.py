import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            return self.contents
        self.balls = []
        for i in range(num_balls_drawn):
          pick = random.choice(self.contents)
          self.balls.append(pick)
          self.contents.remove(pick)
        
        return self.balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    theo_result = []
    for k,v in expected_balls.items():
        for i in range(v):
            theo_result.append(k)
    print(theo_result)
    m=0
    for n in range(num_experiments):
        dchat = copy.deepcopy(hat)
        balls_drawn = dchat.draw(num_balls_drawn)
        print(balls_drawn)
        print(theo_result)
        for ball in theo_result:
          if ball in balls_drawn:
            balls_drawn.remove(ball)
            match = True
          else:
            match = False
            break
        
        if match == True:
          m +=1
          print("match")

    return m/num_experiments
