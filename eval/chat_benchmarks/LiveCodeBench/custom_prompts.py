SOLVER_F = """
## Task: Your task is to implement code that solves the following programming problem: {subproblem}.

### Task description: Break down your solution into these steps:
1. First understand what the problem is asking for
2. Plan out the key components needed
3. Write clean, well-documented code with an entry function named `f`

### Program format:
- Wrap your Python code in ```python``` tags.
- Name the entry function `f` (e.g., `def f(...): ...`), you can have nested definitions inside `f`
- Ensure the function returns a value
- Include at least one input parameter
- Make the function deterministic
- Make the snippet require state tracking across multiple data transformations, ensuring the task requires long multi step reasoning
- AVOID THE FOLLOWING:
* Random functions or variables
* Date/time operations
* I/O operations (reading files, network requests)
* Printing or logging
* Any external state
- Ensure execution completes within 10 seconds on a modern CPU
- All imports and class definitions should be at the very top of the code snippet
- Use imports if it makes it easier to solve the problem
- The snippet should end with a return statement from the main function `f`, anything after will be removed
- For example:
```python
def f(arg1: str, arg2: int):
    # code logic here
    return result
```

Do NOT use if __name__ == "__main__" in your code. You must name your entry function `f`!
Include comments explaining your approach. Remember to wrap your final code block in ```python and ``` tags.
You are only given 4096 tokens total, be brief and make sure to have a complete code block before you finish."""

SOLVER_STDIN = """
## Task: Your task is to implement code that solves the following programming problem: {subproblem}.

### Task description: Break down your solution into these steps:
1. First understand what the problem is asking for
2. Plan out the key components needed
3. Write clean, well-documented code

### Program format:
- Wrap your Python code in ```python``` tags.
- Must accept input from stdin
- Ensure your code prints a value to stdout
- Include at least one input parameter
- Make the function deterministic
- Make the snippet require state tracking across multiple data transformations, ensuring the task requires long multi step reasoning
- AVOID THE FOLLOWING:
* Random functions or variables
* Date/time operations
* I/O operations (reading files, network requests)
* Printing or logging
* Any external state
- Ensure execution completes within 10 seconds on a modern CPU
- All imports and class definitions should be at the very top of the code snippet
- Use imports if it makes it easier to solve the problem
- The snippet should end with a print statement to stdout, only print the final result
- Do not print any example cases you make up yourself
- For example:
```python
t = input()
# code logic here
print(result)
```

Do NOT use if __name__ == "__main__" in your code.
Include comments explaining your approach. Remember to wrap your final code block in ```python and ``` tags.
You are only given 4096 tokens total, be brief and make sure to have a complete code block before you finish."""