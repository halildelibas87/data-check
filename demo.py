def circle_area(radius):
    """Returns the area of the circle of given radius"""
    if radius < 0:
        return 0
    pi = 3.14
    return pi * (radius ** 2)
