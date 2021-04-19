class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs
  def bark(self):
    print("woof!")

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
print(felix.color)
print(felix.bark())


#INHERITANCE
class Animal:
  def __init__(self,name,color):
    self.name=name
    self.color=color
class Dog(Animal):
  def bark(self):
    print("woof!")
class Cat(Animal):
  def purr(self):
    print("mew")

browny = Dog("pinky","pink")
print(browny.color)


class Wolf:
  def __init__(self,name,color):
    self.name=name
    self.color=color
  def bark(self):
    print("wuff!")
class Dog(Wolf):
  def bark(self):
    print("woof!")
husky = Dog("thomas","white")
husky.bark()






class A:
  def spam(self):
    print(1)
class B(A):
  def spam(self):
    print(2)
class C(B):
  def spam(self):
    print(3)
    super().spam()
C().spam()



#MAGIC METHODS AND OPERATOR OVERLOADING
class vector:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def __add__(self, other):
    return vector(self.x+other.x,self.y+other.y)

first = vector(3,5)
second = vector(8,2)
result = first + second
print(result.y)
print(result.x)



class ABC:
  def __init__(self,const):
    self.const=const
  def __truediv__(self, other):
    line = "="*len(other.const)
    return "\n".join([self.const,line,other.const])

first = ABC('hello')
second = ABC('world')
result=first/second
print(result)



# DATA HIDING
class spam:
  __egg = 7
  _spam = 10
  def print_egg(self):
    print(self.__egg)

first=spam()
print(first._spam__egg)
print(first._spam)
first.print_egg()


# Methods of objects we've looked at so far are called by an instance of a class,
# which is then passed to the self parameter of the method.
# Class methods are different - they are called by a class,
# which is passed to the cls parameter of the method.
# A common use of these are factory methods, which instantiate an instance of a class,
# using different parameters than those usually passed to the class constructor.
# Class methods are marked with a classmethod decorator.

class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
  def calculate_area(self):
    return self.width * self.height
  @classmethod
  def Square(cls,height):
    return cls(height,height)

first = Rectangle.Square(5)
print(first.calculate_area())




