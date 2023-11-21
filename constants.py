"""the constants"""

EMPTY = (-1,-1)
START = (-2,-2)

CORRIDOR22 = (2,2)
CORRIDOR32 = (3,2)
CORRIDOR42 = (4,2)
CORRIDOR23 = (2,3)
CORRIDOR43 = (4,3)
CORRIDOR24 = (2,4)
CORRIDOR44 = (4,4)
CORRIDOR25 = (2,5)
CORRIDOR45 = (4,5)

LUNCHROOM13 = (1,3)
LAB54 = (5,4)
ENGINES14 = (1,4)
ENGINES54 = (5,4)
PLANT26 = (2,6)
WATERGEN46 = (4,6)
BEDROOM = (3,1)

MAIN_HTML = \
"""
<!DOCTYPE html>
<html>
<head>
<title>Space Snack</title>
<style>
* {
    font-family: Roboto;
    background-color: black;
    color: white;
}
.page {
    position: absolute;
    top: -500em;
    transition: top 1s;
}
.page:target {
    top: 0em;
}
</style>
</head>
<body>
[[CODE]]
</body>
</html>
"""