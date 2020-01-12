## Implementation
The conversion from convetional(infix) notation to postfix is done by an implemetation of [Dijkstra's shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm). See: [infix.py](/infix.py).

Evaluation of postfix expression is done by an implementation of the postfix evaluation algorithm as explained [here](https://en.wikipedia.org/wiki/Reverse_Polish_notation). See: [posfix.py](/postfix.py).

## Background and Advantages
In postfix notation, the operators follow their operands; for instance, to add 3 and 4, one would write 3 4 + rather than 3 + 4. If there are multiple operations, operators are given immediately after their second operands; so the expression written 3 − 4 + 5 in conventional notation would be written 3 4 − 5 + in postfix notation: 4 is first subtracted from 3, then 5 is added to it. 

An advantage of postfix notation is that it removes the need for parentheses that are required by infix notation. While 3 − 4 × 5 can also be written 3 − (4 × 5), that means something quite different from (3 − 4) × 5. In postfix notation, the former could be written 3 4 5 × −, which unambiguously means 3 (4 5 ×) − which reduces to 3 20 − (which can further be reduced to -17); the latter could be written 3 4 − 5 × (or 5 3 4 − ×, if keeping similar formatting), which unambiguously means (3 4 −) 5 ×. 

In comparison testing of postflix notation with algebraic notation, postfix notation has been found to lead to faster calculations, for two reasons. The first reason is that postfix notation calculators do not need expressions to be parenthesized, so fewer operations need to be entered to perform typical calculations. Additionally, users of postfix notation calculators made fewer mistakes than for other types of calculators.Later research clarified that the increased speed from reverse postfix notation may be attributed to the smaller number of keystrokes needed to enter this notation, rather than to a smaller cognitive load on its users. However, anecdotal evidence suggests that postfix notation is more difficult for users to learn than algebraic notation. [Source](https://en.wikipedia.org/wiki/Reverse_Polish_notation)


