# Fuel required to launch a given module is based on its mass. Specifically, to
# find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
#
# For example:
#
# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. To find it,
# individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.
#
# What is the sum of the fuel requirements for all of the modules on your spacecraft?
import math

masses = """146561
98430
131957
81605
70644
55060
93217
107158
110769
94650
141070
72381
100736
105705
99003
94057
110662
74429
55509
63492
102007
72627
95183
112072
122313
116884
125451
106093
140678
121751
149018
58459
138306
149688
82927
72676
95010
88439
51807
103175
107633
126439
128879
112054
52873
114493
77365
76768
60838
89692
66217
96060
100338
139063
126869
106490
128967
116312
56822
52422
124579
117120
106245
105255
66975
115340
145764
149427
64228
64237
67887
103345
134901
50226
126991
122314
140818
129687
149792
101148
73411
87078
121272
108804
96063
81155
62058
112684
134263
128454
99455
91689
141448
143892
103257
64352
90769
78307
111855
130153""".split('\n')


def solve(mass):
    return math.floor(int(mass) / 3) - 2


print((sum(map(solve, masses))))


def solve2(mass):
    if int(mass) <= 0:
        return 0
    fuell = max(0, math.floor(int(mass) / 3) - 2)
    res = fuell + solve2(fuell)
    return res


assert solve2(14) == 2
assert solve2(1969) == 966
assert solve2(100756) == 50346

print((sum(map(solve2, masses))))