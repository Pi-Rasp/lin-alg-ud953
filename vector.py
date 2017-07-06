import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    
    def add(self, v):
        try :
            if self.dimension != v.dimension:
                raise ValueError
            c = [None for x in range(v.dimension)]
            for i in range((v.dimension)):
                c[i] = self.coordinates[i] + v.coordinates[i]
            return Vector(c)
        except ValueError:
            raise ValueError("Length of both vectors must be same")
    
    
    def sub(self, v):
        try :
            if self.dimension != v.dimension:
                raise ValueError
            c = [None for x in range(v.dimension)]
            for i in range((v.dimension)):
                c[i] = self.coordinates[i] - v.coordinates[i]
            return Vector(c)
        except ValueError:
            raise ValueError("Length of both vectors must be same")
    
    
    def scalMult(self, scal):
        try:
            if not scal:
                raise ValueError
            c = [None for x in range(self.dimension)]
            for i in range((self.dimension)):
                c[i] = scal * self.coordinates[i]
            return Vector(c)
        except ValueError:
            raise ValueError("Scalar cannot be empty")
            
    
    def magnitude(self):
        sum=0
        for i in self.coordinates:
            sum = sum + i*i
        return math.sqrt(sum)
    
    
    def normalization(self):
        try:
            if self.magnitude() == 0:
                raise ZeroDivisionError
            return self.scalMult((1/self.magnitude()))
        except ZeroDivisionError:
            raise ZeroDivisionError("Can't Normalize with Zero Vector")
    
    
    def dotProduct(self,v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    
    
    def angle(self,v):
        try:
            if self.magnitude() * v.magnitude()==0:
                raise ZeroDivisionError
            return math.acos(self.normalization().dotProduct(v.normalization())) # Return in Radians
        except ZeroDivisionError:
            raise ZeroDivisionError("Can't find angle with Zero Vector")
            
    
    def checkOrthogonal(self,v,tolerance=1e-10):
        return math.fabs(self.dotProduct(v))<tolerance
    
    
    def checkParallel(self,v,tolerance=1e-10):
        return math.fabs(self.magnitude())<tolerance or math.fabs(v.magnitude())<tolerance \
                or self.angle(v)==0 or self.angle(v)==math.pi
            
            
vector1 = Vector([-2.328,-7.284,-1.214])
vector2 = Vector([0,0,0])
print((vector1.checkParallel(vector2)))