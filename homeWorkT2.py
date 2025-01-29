# Implement python script that calculate visible color of star based on its
# temperature. The colors can be blue, white, yellow, orange and red.
# Input of the script should be dictionary where key is name of the star
# and value is a temperature. Output of the script should be colors
# separated by newlines that has at least one star in it spectrum and star
# names separated by comma. Script should has at least two functions:
# one for calculating values and one for printing it.

starsDict = {3000:"red",
             25000:"blue",
             10000:"white",
             4000:"orange",
             6000:"yellow"}


def task2(name, temerature:int):
    print(f"{name}, {starsDict.get(temerature)}")


task2("Sun",6000)
task2("vega",10000)
#incorrect solution, only one function, but more useful

def t2v2 (name, temerature:int):
    match temerature:
        case 3000:
            return f"{name},red"
        case 4000:
            return f"{name},orange"
        case 6000:
            return  f"{name},yellow"
        case 10000:
            return f"{name},white"
        case 25000:
            return f"{name},blue"
def task2_v2(name, temperature:int):
    print(t2v2(name,temperature))
task2_v2("sun",6000)
#correct solution, but only for python 3.11+


