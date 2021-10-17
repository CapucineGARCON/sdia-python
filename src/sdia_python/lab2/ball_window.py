import numpy as np


# todo implement, document and test the class
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
            string : a sentence with the area of the ballimport sdia_python.lab
        """
        return f"The area is {round(4 * np.pi * self.radius **2, 2)}"
