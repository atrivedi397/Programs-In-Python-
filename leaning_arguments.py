from time import time
t = time()
my = [(x, x*x) for x in range(1, 10)]
print(f'list comprehension took : {time()-t}')

t2 = time()
my2 = list((x, x*x) for x in range(1, 10))
print(f"generator took : {time()-t2}")

t3 = time()
my3 = list(map(lambda x: (x, x**2), range(1, 10)))
print(f"map took : {time()-t3}")

my4 = list()
t4 = time()
for i in range(1, 10):
    my4.append((i, i**2))

print(f"for loop took : {time()-t3}", end="\n")

print(my, "\n", my2, "\n", my3, "\n", my4)
print(my == my2 == my3 == my4)


class Hello:
    @staticmethod
    def game():
        pass


cd = Hello()
name = Hello.game
print(type(cd))
print(type(Hello))
print(isinstance(name(), Hello))
