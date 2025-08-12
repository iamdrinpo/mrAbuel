# **BUBBLE SORT**

This Python program accepts a list of numbers, letters, or words from the user and sorts them into two categories:

* **Numbers** are sorted in ascending or descending numeric order.
* **Words** are sorted based on their length (shortest to longest, or longest to shortest).

---

## **How It Works**

1. **User Input**

   * The program first asks you to enter **any combination** of numbers, letters, or words separated by spaces.
   * Then, it asks you to choose the sorting order:

     * `asc` → Sort in ascending order.
     * `desc` → Sort in descending order.

2. **Separation of Data**

   * The program checks each input item:

     * If it’s made only of digits (e.g., `42`), it’s treated as a number and added to the `nums` list.
     * Otherwise, it’s treated as a word or letter and added to the `words` list.

3. **Sorting**

   * Numbers are sorted using Python’s `.sort()` method.
   * Words are sorted using `.sort(key=len)`, which sorts them by **length** instead of alphabetical order.

4. **Output**

   * The program displays the sorted numbers followed by the sorted words.

---

## **Example Usage**

### **Example 1 — Ascending Order**

```
Enter numbers, letters, or words: 5 apple 3 banana 10 cat
(asc/desc): asc
Sorted: [3, 5, 10, 'cat', 'apple', 'banana']
```

**Explanation:**

* Numbers sorted: `[3, 5, 10]` (ascending)
* Words sorted by length: `['cat', 'apple', 'banana']` (shortest to longest)

---

### **Example 2 — Descending Order**

```
Enter numbers, letters, or words: 5 apple 3 banana 10 cat
(asc/desc): desc
Sorted: [10, 5, 3, 'banana', 'apple', 'cat']
```

**Explanation:**

* Numbers sorted: `[10, 5, 3]` (descending)
* Words sorted by length: `['banana', 'apple', 'cat']` (longest to shortest)

---

## **Code**

```python
items = input("Enter numbers, letters, or words: ").split()
order = input("(asc/desc): ").lower()

nums = []
words = []

for i in items:
    if i.isdigit():
        nums.append(int(i))
    else:
        words.append(i)

# Sort numbers
nums.sort(reverse=(order == "desc"))

# Sort words by length
words.sort(key=len, reverse=(order == "desc"))

print("Sorted:", nums + words)
```

---

## **Features**

* Accepts mixed input (numbers and words) in a single line.
* Flexible sorting order: ascending (`asc`) or descending (`desc`).
* Numbers sorted numerically.
* Words sorted by length instead of alphabetical order.
* Efficient and concise using Python’s built-in `.sort()`.

---

## **Requirements**

* Python **3.6+** installed on your system.
* A code editor or IDE (e.g., VS Code, PyCharm, Sublime Text) or simply the Python IDLE.
* No external libraries required — uses only Python built-ins.
* Basic understanding of how to run Python scripts from terminal/command prompt.



