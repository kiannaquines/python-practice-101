import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

items = [random.randint(1, 200) for _ in range(100)]

fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(items)), items, align="edge")

def bubble_sort_visualization():
    n = len(items)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:  # Swap elements
                items[j], items[j + 1] = items[j + 1], items[j]
            yield items

def update(frame):
    for rect, val in zip(bar_rects, frame):
        rect.set_height(val)
    return bar_rects

ani = animation.FuncAnimation(fig, update, frames=bubble_sort_visualization(), interval=100, repeat=False)
plt.show()
