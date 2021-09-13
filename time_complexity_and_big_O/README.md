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
