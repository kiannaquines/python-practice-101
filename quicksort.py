import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

items = [random.randint(1, 500) for _ in range(500)]
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        yield arr[:]

        yield from quicksort(arr, low, pivot_index - 1)
        yield from quicksort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


fig, ax = plt.subplots()
bar_rects = ax.bar(range(len(items)), items, align="edge")
ax.set_xlim(0, len(items))
ax.set_ylim(0, max(items) * 1.1)
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)


def update(arr):
    for rect, val in zip(bar_rects, arr):
        rect.set_height(val)
    text.set_text(f"Sorting...")
    return bar_rects


sort_generator = quicksort(items, 0, len(items) - 1)

ani = animation.FuncAnimation(fig, update, frames=sort_generator, interval=50, repeat=False)
plt.show()
