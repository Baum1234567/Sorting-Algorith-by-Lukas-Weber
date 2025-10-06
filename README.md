# Sorting Algorithm Visualizer

A Python program that visualizes various sorting algorithms using **Pygame**.  
You can choose the number of elements and the sorting algorithm to see how it works step by step.

---

## How to Run

```bash
python sortingAlgorithm.py <number_of_elements> <sorting_type>

```
 - <number_of_elements>: Number of elements to sort (e.g., 100, 500)
 - <sorting_type>: Choose the sorting algorithm by number (see table below)

---

# Sorting Algorithms
1. Bubble Sort – Compares adjacent elements and swaps them if needed, causing the largest elements to "bubble" to the end. Simple but inefficient for large lists. ✓

2. Selection Sort – Finds the smallest element in the unsorted portion and places it at the current position. Performs minimal swaps but still O(n²) time complexity. ✓

3. Insertion Sort – Inserts each element into its correct position within the sorted portion of the list. Efficient for small or nearly sorted datasets.

4. Merge Sort – Recursively divides the list into halves, sorts them, and merges the sorted halves. Stable and O(n log n) time complexity.

5. Quick Sort – Picks a pivot, partitions the list into elements smaller and larger than the pivot, and recursively sorts each partition. Fast in practice but worst-case O(n²).

6. Heap Sort – Builds a heap from the list and repeatedly extracts the largest element, placing it in its final position. Efficient and in-place sorting.

7. Counting Sort – Counts the occurrences of each value and directly constructs the sorted list. Works best for integers with a small range.

8. Shell Sort – Sorts the list using progressively smaller gaps between elements, finishing with a standard insertion sort. Improves insertion sort for larger lists.

9. Tim Sort – Hybrid of merge sort and insertion sort, optimized for real-world datasets with partially ordered sequences. Stable and very efficient in practice.

10. Radix Sort – Sorts numbers digit by digit, starting from the least significant digit. Works well for integers or fixed-length strings.

11. Stalin Sort – Removes any element that is out of order, keeping only the non-decreasing subsequence. Mostly a joke algorithm but produces a sorted sequence instantly. ✓

---

Example

Copy code
```bash
python sortingAlgorithm.py 500 4
```
This runs the visualizer with 500 elements using Merge Sort.

---

# Requirements
 - Python 3.6 or higher
 - Pygame library (pip install pygame)

---

# Notes
The visualizer shows one step per frame for each algorithm, allowing you to see how elements move and get sorted.

Adjust the window size and number of elements to experiment with performance and visual effects.

Some algorithms, like Bubble Sort and Cocktail Shaker Sort, move elements gradually and look visually similar.

Faster algorithms like Merge Sort, Quick Sort, or Tim Sort may appear smoother and sort large lists more efficiently.
