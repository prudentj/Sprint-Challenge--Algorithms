#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) time complexity
``` n*n*n/n*n= n
    This can be simplified to 
    a=0
    while(a<n ):
        a=a+n
    The while loop will run n times
```

b) O(n^c)
```
    The first for loop guarantees that the loop will run
    n times. The while guarantees that it will run n/2 times
    for each n of the above. It is slightly less than O(n^2)
    probably O(n^1.5) or O (n*sqrt(n))
```

c)O(n)
```
    The recursive loop will go for n levels since it will
    decrease by 1 to approach zero. This means it will be
    at least n complexity. It will then finish up each
    function call. I think this simplifies to n complexity

```

## Exercise II
The n time solution would be to throw an egg off the first floor, it doesn't break move to the second floor ect.

I set lower boundry as the floor and upper as the top floor.

The better way is to go to the n/2 floor, see if it doesn't break, if it does I go half way between my current and my upper (I eliminate half the building as potential spots, from now on). I set my previous current as my lower.

If it doesn't I go half way between my current and my lower. I set my previous current as my lower. I repeat until I have one floor left. If the egg breaks I say it was the floor below the one I was on. If not I say it is my current floor. 

