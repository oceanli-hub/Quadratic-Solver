import math

def solveQuadratic(a: float, b: float, c: float) -> str:
    """
        This function takes the coefficients of a 
        quadratic equation as its three parameters.
        It returns a string that states its roots as
        described in the specification.
    """

    discriminant = b**2 - 4*a*c

    if (discriminant<0):
        output = "No real roots"
    elif(discriminant==0):
        root = -b/(2*a)
        output = "The root is {:.2f}".format(root)
    elif(discriminant>0):
        r1 = (-b + math.sqrt(discriminant))/(2*a)
        r2 = (-b - math.sqrt(discriminant))/(2*a)
        output = "The roots are {:.2f} and {:.2f}".format(r1,r2)

    return (output)

if __name__ == "__main__":

    Tests = [(1, 2, 3), (1, 2, 1), (1, 3, 1), (1.5, -8, -0.2)] 
    expectedOutput = ["No real roots", 
                      "The root is -1.00",  
                      "The roots are -0.38 and -2.62",
                      "The roots are 5.36 and -0.02"]
    for i in range(len(Tests)):
        print(f"Test {i} : a={Tests[i][0]}, b={Tests[i][1]} c={Tests[i][2]}")
        result = solveQuadratic(a=Tests[i][0], b=Tests[i][1], c=Tests[i][2])
        print(result)
        assert(result == expectedOutput[i])