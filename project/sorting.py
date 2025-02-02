import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def visualize(ax, data, colorArray):
    ax.bar(range(len(data)), data, color=colorArray)
    for i, val in enumerate(data):
        ax.text(i, val + 0.1, str(val), ha='center', va='bottom')
    ax.set_xticks([])  # Remove x-axis ticks
    ax.set_yticks([])  # Remove y-axis ticks

def visualize_step(ax, data, current_index, comparing_index):
    ax.clear()  # Clear only the bars, not the labels
    colorArray = ['blue' if x == current_index or x == comparing_index else 'grey' for x in range(len(data))]
    visualize(ax, data, colorArray)

def bubble_sort(data, steps):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append((data[:], j, j + 1))
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                steps.append((data[:], j, j + 1))

def selection_sort(data, steps):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps.append((data[:], min_idx, j))
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        steps.append((data[:], i, min_idx))

def insertion_sort(data, steps):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            steps.append((data[:], j, j + 1))
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        steps.append((data[:], j + 1, i))

def merge_sort(data, steps):
    def merge_sort_recursive(data, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_recursive(data, left, mid)
            merge_sort_recursive(data, mid + 1, right)
            merge(data, left, mid, right)

    def merge(data, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        L = data[left:mid + 1]
        R = data[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < n1 and j < n2:
            steps.append((data[:], left + i, mid + 1 + j))
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1
        while i < n1:
            steps.append((data[:], left + i, k))
            data[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            steps.append((data[:], mid + 1 + j, k))
            data[k] = R[j]
            j += 1
            k += 1

    merge_sort_recursive(data, 0, len(data) - 1)

def quick_sort(data, steps):
    def quick_sort_recursive(data, low, high):
        if low < high:
            pi = partition(data, low, high)
            quick_sort_recursive(data, low, pi - 1)
            quick_sort_recursive(data, pi + 1, high)

    def partition(data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            steps.append((data[:], j, high))
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                steps.append((data[:], i, j))
        data[i + 1], data[high] = data[high], data[i + 1]
        steps.append((data[:], i + 1, high))
        return i + 1

    quick_sort_recursive(data, 0, len(data) - 1)

if __name__ == "__main__":
    data = [8, 3, 1, 7, 1, 10, 2, 12, 4, 15, 5]  # Example list

    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    fig, axes = plt.subplots(1, len(sorting_algorithms), figsize=(20, 5))
    fig.tight_layout(pad=5.0)

    steps_dict = {name: [] for name in sorting_algorithms.keys()}

    for name, sort_func in sorting_algorithms.items():
        sort_func(data.copy(), steps_dict[name])

    def update(frame):
        for ax, (name, steps) in zip(axes, steps_dict.items()):
            if frame < len(steps):
                data, current_index, comparing_index = steps[frame]
                visualize_step(ax, data, current_index, comparing_index)
            else:
                ax.clear()
                visualize(ax, steps[-1][0], ['grey'] * len(steps[-1][0]))
                ax.set_title(name)

    ani = FuncAnimation(fig, update, frames=max(len(steps) for steps in steps_dict.values()) + 1, repeat=False)
    plt.subplots_adjust(bottom=0.2)  # Adjust the bottom to make space for x-labels
    plt.show()