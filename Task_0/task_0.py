import random

rl = random.sample(range(-100, 100), 30)
print("\n", rl)

print("\nМаксимальний елемент списку: ", max(rl))
print("Порядковий номер: ", rl.index(max(rl)))
print("\n")

newlist = [i for i in rl if (i % 2) == 1]
if len(newlist) == 0:
    print("Не знайдено")
print(sorted(newlist, reverse=True))
print("\n")