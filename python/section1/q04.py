string = "Hi He Lied Because Boron Could Not Oxidize Fluorine." \
         " New Nations Might Also Sign Peace Security Clause. Arthur King Can."
strdict = {k+1: v[0] if k+1 in (1, 5, 6, 7, 8, 9, 15, 16, 19) else v[:2] for k, v in enumerate(string.split(' '))}
print(strdict)
