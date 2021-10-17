import numpy as np

from sdia_python.lab2.utils import get_random_number_generator


# todo make a pass on the docstrings
class BoxWindow:
    """This class BoxWindow create a box with dimension [a1, b1] x ... x [an, bn."""

    def __init__(self, bounds):
        """Create the attribute bounds of the class BoxWindow.

        Args:
            bounds (list): list of the dimensions (for example in dimension2 [a1, b1] x [a2, b2])
        """
        self.bounds = np.atleast_2d(bounds)
        a, b = self.bounds[:, 0], self.bounds[:, 1]
        assert np.all(a <= b)

    def __str__(self):
        """BoxWindow: :math:`[a_1, b_1] \times [a_2, b_2] \times \cdots`

        Returns:
            str: the points of the box in each dimensions. (BoxWindow: [a1, b1] x [a2, b2] x ... )
        """

        b = "BoxWindow: "
        # ! use f-strings
        # * consider for a, b in self.bounds
        # for i in range(self.bounds.shape[0]):
        for a in self.bounds:
            b += f"{list(a)} x "
        return b[:-3]

    def shape(self):
        """This method enables to know the dimension of the box

        Returns:
            str : with the dimension of the box (n x 2)

        """
        return self.bounds.shape

    def indicator_function(self, point):
        """Check if the point is contained in the BoxWindow

        Point:
            Point (list) : list with the coordinates of the point to be tested

        Returns:
            bool : True if the point is contained in the box, False if not.
        """

        s = True
        for i, (a, b) in enumerate(self.bounds):
            if (self.bounds[i, 0] <= point[i]) and (point[i] <= self.bounds[i, 1]):
                s == True
            else:
                return False
        return s

    def __contains__(self, point):
        """Check if a point is contained in the BoxWindow or not

        Args:
            point (list): list with the coordinates of the point to be tested

        Returns:
            bool: It returns True if the point is contained in the box and False if not.
        """
        assert len(point) == self.shape()[0]
        a, b = self.bounds[:, 0], self.bounds[:, 1]
        return np.all(a <= point) and np.all(
            point <= b
        )  # Python exécute de façon lazy ce qu'on lui dit, si c'est faux pour a au début il s'arrête et renvoie directement faux.

        # np.all(np.logical_and(a <= point, point <=b))  en grande dimension cela est coûteux parce que l'on doit vérifier les deux conditions à chaque fois

    def dimension(self):
        """Enable to know the size of the space

        Returns:
            int: dimension of the space, also the dimension of the box.
        """
        return {self.bounds.shape[0]}

    def length(self):
        """This method return the length for each dimension of the BoxWindow.

        Returns:
            list : l[i] with the length of the BoxWindow in dimension i

        """
        l = []
        # for i in range(self.bounds.shape[0]):
        for a in self.bounds:
            l += list(np.diff(a))
        return l

    # tested
    def volume(self):
        """It returns the volume of the BoxWindow, if dimension is greater (or equal) than 3, otherwise, it returns the area in dimension 2, the length in dimension 1.

        Returns:
            str : the volume of the BoxWindow.

        """
        x1 = self.bounds[:, 0]
        x2 = self.bounds[:, 1]
        return np.prod(np.diff(self.bounds[:]))

    def indicator_function_several(self, args):
        """Check if the several points are contained in the BoxWindow or not.

        Args:
            args (list): list of the points to be tested

        Returns:

            list : list of booleans, with True if the point is contained in the BoxWindow, False if not
        """
        a = []
        for b in args:
            a = a + [self.indicator_function(b)]
        return a

    def rand(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): It is the number of points we want to create. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        points = []
        for i in range(n):
            point = []
            for (a, b) in self.bounds:
                point.append(rng.uniform(a, b))
            points.append(point)
        return points

    def center(self):
        """Returns the center of the BoxWindow

        Returns:
            list: coordonnates of the center.
        """

        return list(np.mean(self.bounds, axis=1))


# todo implement, document and test the class
class UnitBoxWindow(BoxWindow):
    def __init__(self, center):
        """Create a box that is centered in a point.

        Args:
            center (list, optional): Center is a list with the coordonnates of the center. Defaults to None.
        """

        bounds = np.add.outer(center, [-0.5, 0.5])
        super(UnitBoxWindow, self).__init__(bounds)
