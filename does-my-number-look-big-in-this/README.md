[Does my number look big in this?](https://www.codewars.com/kata/5287e858c6b5a9678200083c)

A [Narcissistic Number](https://en.wikipedia.org/wiki/Narcissistic_number) is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits):
```
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
```

and 1634 (4 digits):
```
    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
```

__The Challenge:__
Your code must return __true or false__ depending upon whether the given number is a Narcissistic number in base 10.