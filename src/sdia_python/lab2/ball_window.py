import numpy as np


class BallWindow:
    """Create a ball with a center and a radius
    """

    def __init__(self, center, radius):
        """Initialize the center and the radius of the ball

        Args:
            center (array): a point with two coordinates.
            radius (int):
        """

        self.center = np.array(center)
        self.radius = radius

    # tested
    def __str__(self):
        """Give a description of the ball

        Returns:
            string: description with radius and center.
        """
        return f"A ball with center= {self.center} and radius= {self.radius}"

    def dimension(self):
        """Give the dimension of the space

        Returns:
            int : It is an integer that gives the dimension.
        """
        return len(self.center)

    # tested
    def __contains__(self, point):
        """Check if a point is in the ball or not

        Args:
            point (list): coordinates of the point
        """
        p = np.array(point)
        assert len(p) == len(self.center)
        return np.linalg.norm(p - self.center) <= self.radius

    # tested
    def volume(self):
        """Calculate the volume of the ball.

        Returns:
            str: a sentence with the volume of the ball.
        """
        return f"The volume is {round((4/3) * self.radius **3 * np.pi, 2)}"

    # tested
    def area(self):
        """Calculate the area/ the curved surface of the ball.

        Returns:
            string : a sentence with the area of the ball
        """
        return f"The area is {round(4 * np.pi * self.radius **2, 2)}"

    def indicator_function(self, args):
        """Check if the points are contained in the Ball, it returns True if the point is in the Ball, and False if not.

        Args:
            args (list): list of the points' coordonnates to be tested

        Returns:
            list: list of booleans.
        """
        a = []
        for b in args:
            a = a + [self.__contains__(b)]
        return a


class UnitBallWindow(BallWindow):
    def __init__(self, center):
        """Create a unit Ball, a Ball with a radius of 1.

        Args:
            center (list): list with the coordonnates of the center of the ball.
        """
        super(UnitBallWindow, self).__init__(center, 1)
