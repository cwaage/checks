# glocal

## Prerequisites
None

## Problem
The below code takes input from the user, and passes it through to a function that is supposed to increase its value by 5. However, it looks like despite the function, <code>add_5</code>, seemingly adding 5 to the value of <code>x</code> -- the value of x doesn't change! Run the code once or twice to see what happens, and update the code in <code>add_5</code> and <code>main</code> to correctly update the value of x.

## Distribution Code
```c

#include <cs50.h>
#include <stdio.h>

// TODO: function prototype to fix
void add_5(int x);

int main(void)
{
    // input from user
    printf("Enter some integer value: ");
    int x = get_int();
    printf("the value of x before adding 5 is %d\n", x);
    // TODO: fix this so that the value of x is updated
    add_5(x);
    printf("the value of x after adding 5 is %d\n", x);
}

// TODO: function definition to fix
void add_5(int x)
{
    x = x + 5;
}
```
