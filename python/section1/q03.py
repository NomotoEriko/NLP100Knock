string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
strlist = [len(s.strip(',.')) for s in string.split(' ')]
print(strlist)
