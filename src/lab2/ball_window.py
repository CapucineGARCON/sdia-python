import numpy as np


# todo implement, document and test the class
class BallWindow:
    def __init__(self, center, radius):
        """

        Args:
            center (array): a point with two coordinates.
            radius (int):
        """
        self.center = np.array(center)
        self.radius = radius

    def __contains__(self, point):
        """This function checks if a points is in the ball or not
        Args:
            point ([type]): [description]
        """
        all((i - j) < self.radius for i, j in point, self.center)
