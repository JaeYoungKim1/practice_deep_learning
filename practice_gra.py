for i in enumerate([1,2,3,5,10]):
    print(i)

for i in range(10):
    print(i)
    if i >= 5:
        break
    elif i < 3:
        print("hi")
        continue

a = [1050, 150, 20, -30, -50]


for i in a:
    print(a.index(-30))

print(i)


x = [4, 2, 3, 1]
y = ["hello", "there"]

if ("hello") in y:
    print("hello가 있어요")

x = {
    0: "Jae",
    1: "Hello",
    "age": 20
}
print(x.keys())

# fruit enumeration
f = ["사과", "사과", "딸기"]
dic = {}
for i in f:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
print(dic)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self, to_name):
        print(to_name + "아" + " 내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + " 살이야")

jaeyoung = person("jaeyoung", 27)
jaeyoung.introduce("구웩")

class police(person):
    def arrest(self, to_arrest):
        print("넌 체포됐다," + to_arrest)
wonny = police("워니",20)
wonny.arrest("wonny")
wonny.introduce("구웩")

k = [5,3,6]
for i in k:
    print(i)

from animal import *

d = dog_cry()
d.hi()
c = cat_cry()
c.hi()

