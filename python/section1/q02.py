string1 = 'パトカー'
string2 = 'タクシー'
string12 = ''.join(s1+s2 for s1, s2 in zip(string1, string2))
print(string12)
