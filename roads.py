"""
Heathrow to London:
problem from 'Learn you Haskell for great good' implemented in Python
http://learnyouahaskell.com/functionally-solving-problems#heathrow-to-london

-> A -> A  ->A
   |C   |C  |C
-> B -> B  ->B
"""

A = 'A'
B = 'B'
C = 'C'

sumA = 0
sumB = 0

pathA = []
pathB = []


def follow_paths(section):
    global sumA, sumB, pathA, pathB
    pathA_in_loop = pathA[:]
    pathB_in_loop = pathB[:]
    sumA_in_loop = sumA
    sumB_in_loop = sumB
    a, b, c = section

    "to A"
    toA = sumA + a
    toAthroughC = sumB + b + c

    "to B"
    toB = sumB + b
    toBthroughC = sumA + a + c

    if toA < toAthroughC:
        pathA_in_loop.append((A, a))
        sumA_in_loop = sumA + a
    else:
        path = pathB[:]
        path.extend([(B, b), (C, c)])
        pathA_in_loop = path
        sumA_in_loop = sumB + b + c

    if toB < toBthroughC:
        pathB_in_loop.append((B, b))
        sumB_in_loop = sumB + b
    else:
        path = pathA[:]
        path.extend([(C, c), (A, a)])
        pathB_in_loop = path
        sumB_in_loop = sumA + a + c

    pathA = pathA_in_loop
    pathB = pathB_in_loop
    sumA = sumA_in_loop
    sumB = sumB_in_loop


def roads_to(sections):
    for section in sections:
        follow_paths(section)
    print('Path A: {}'.format(pathA))
    print('Path B: {}'.format(pathB))
    print('Shorter path is {} ->> {} km'.format('A'
                                                if sumA < sumB else 'B', sumA
                                                if sumA < sumB else sumB))

# Example data from 'Learn you Haskell for great good'
# sections = [(50, 10, 30), (5, 90, 20), (40, 2, 25), (10, 8, 0)]
# roads_to(sections)
