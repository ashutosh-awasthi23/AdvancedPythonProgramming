fruits={'Apple','Mango','Litchi','Kiwi'}
vegetables={'Mango','Beans','Cabbage','Kiwi'}
grains={'Mango','Wheat','Rice'}

print(f"The interesection of three is {grains.intersection(fruits.intersection(vegetables))}")
print(f"The union of three is {grains.union(fruits.union(vegetables))}")
print(f"The symmetric difference among three sets is {(fruits.symmetric_difference(vegetables))-grains}")
print(f"The items unique to fruits are {(fruits-vegetables)-grains}")
print(f"The items unique to vegetables are {(vegetables-fruits)-grains}")
print(f"The items unique to grains are {(grains-fruits)-vegetables}")