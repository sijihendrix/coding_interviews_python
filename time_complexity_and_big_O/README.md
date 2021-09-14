# Time Complexity:

Time it takes for a function to run

### Example input: given list = [4,7,2]

```python
def total(given_list):
    x = 0
    for item in given_list:
        x += item
    return x
```

The time the function takes increases as the lenght of the input increases.

```python

def total(given_list):
     x = 0
     return(x)
```

The above function will always run the same amount of time because its input has no effect on the run time

### Pros

- a convenient way to get a rough idea about efficiency

### cons

- Difficult to assess more complicated functions
- Awkward way to describe efficiency as we have to use specific terminologies for diff complexities like
  - constant
  - linear
  - quadratic
  - exponential

# Big O Notation

It is a way of indicating how complex a function is and how much time it takes to run your function.

A covenient way to express the time complexity of a function

Let's say the time taken for the first function total is t = an + b = 0(n), with n representing the variation in the the input the function takes and would be the O(n)

Let's say the time taken for the second function total is t = 20ms so the O(n) is 1

### Example 3: array_2d = [[4,5],[6,7]]

```python

def total(given_list):
    for row in given_list:
        for item in row:
            x += item
    return x
```

t = a(n\*\*2) + c. This is a quadratic time complexity. In this case it will be a O(n\*\*2)

Time complexity and BigO only define the time it takes to run your function as the input size grows

### Interview question, 2d array and time complexity: You're given a 2d array which is square shaped, which means the number of rows == cols. This array has a special property that each row and each column is sorted. If you look at the columns from top to bottom,the intergers increase or stay the same; if you look at each row from left the right, the integers always increase or stay the same. write a funciton: count_negatives(array) that returns the number of negative numbers in it. First find a O(n\*\*2) then find a O(n) solution

Clarifying questions:
Is the 2d array always square shaped?
ans: yes

What about 0?
ans: 0 is not counted as a negative number
