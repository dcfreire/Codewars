"""
Using the algorithm used to demonstrate converting an
n-state DFA -> n+2-state GNFA -> 2-state GNFA.
As explained in the Michael Sipser book: "Introduction to the Theory of Computation".
The general idea is to create a new initial and final state for the dfa, connect
with empty transitions, and removing state by state, repairing the machine on each
iteration as to compensate the state you removed.
It is a drag to do by hand, but using something like .dot files to graph each step
makes it easier.

div_7.dot:
--------------------
digraph G {
    rankdir=LR;
    node [shape = point ]; qi
    i[shape="circle"]
    0[shape="doublecircle"]
    1[shape="circle"]
    2[shape="circle"]
    3[shape="circle"]
    4[shape="circle"]
    5[shape="circle"]
    6[shape="circle"]
    qi -> i
    i -> 0 [label="0"]
    i -> 1 [label="1"]
    0 -> 0 [label="0"]
    0 -> 1 [label="1"]
    1 -> 2 [label="0"]
    1 -> 3 [label="1"]
    2 -> 4 [label="0"]
    2 -> 5 [label="1"]
    3 -> 0 [label="1"]
    3 -> 6 [label="0"]
    4 -> 2 [label="1"]
    4 -> 1 [label="0"]
    5 -> 3 [label="0"]
    5 -> 4 [label="1"]
    6 -> 6 [label="1"]
    6 -> 5 [label="0"]

}
"""
solution = '^(0|111|100((1|00)0)*011|(101|100((1|00)0)*(1|00)1)(1((1|00)0)*(1|00)1)*(01|1((1|00)0)*011)|(110|100((1|00)0)*010|(101|100((1|00)0)*(1|00)1)(1((1|00)0)*(1|00)1)*(00|1((1|00)0)*010))(1|0(1((1|00)0)*(1|00)1)*(00|1((1|00)0)*010))*0(1((1|00)0)*(1|00)1)*(01|1((1|00)0)*011))(0|111|100((1|00)0)*011|(101|100((1|00)0)*(1|00)1)(1((1|00)0)*(1|00)1)*(01|1((1|00)0)*011)|(110|100((1|00)0)*010|(101|100((1|00)0)*(1|00)1)(1((1|00)0)*(1|00)1)*(00|1((1|00)0)*010))(1|0(1((1|00)0)*(1|00)1)*(00|1((1|00)0)*010))*0(1((1|00)0)*(1|00)1)*(01|1((1|00)0)*011))*$'
