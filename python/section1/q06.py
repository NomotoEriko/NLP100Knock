from q05 import make_ngram
string1 = "paraparaparadise"
string2 = "paragraph"
X = set(''.join(gram) for gram in make_ngram(sequence=string1))
Y = set(''.join(gram) for gram in make_ngram(sequence=string2))
uniXY = X.union(Y)
intXY = X.intersection(Y)
diffXY = X.difference(Y)
X_contains_se = X.__contains__('se')
Y_contains_se = Y.__contains__('se')

print('X:', X)
print('Y:', Y)
print('X ∪ Y:', uniXY)
print('X ∩ Y:', intXY)
print('X - Y:', diffXY)
print('X contains se:', X_contains_se)
print('Y contains se:', Y_contains_se)
