from re import I
points=0

print("hello player! this is a quiz:")
zettel=input("how old do mammoth trees get?:\n")
if zettel =="2200":
    points=points+3 
    print("right")
else:
    print("wrong")


print("you got ", points, "out of three points.")