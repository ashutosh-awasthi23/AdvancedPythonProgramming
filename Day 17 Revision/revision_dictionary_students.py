def dict_color(d):
    print(f"OG Dict: {d}")
    print(f"Total number of students in the list: {len(d)}")
    d['Lisa'] = "Violet"
    print(f"Changed Lisa's favorite color from 'Yellow' to 'Violet': {d}")
    d.pop('Jenny')
    print(f"Removed 'Jenny': {d}")
    s = {x: d[x] for x in sorted(d)}
    print("Sorted Dictionary: ", s)
    pass


d = {'Vinod': 'Purple', 'Aaryan': 'Blue', 'Lisa': 'Yellow', 'Jenny': 'Pink'}
dict_color(d)
