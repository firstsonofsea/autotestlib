from main import Runner

#file = open('tupo_test.py', 'r')
#text = file.read()
#r = Runner(text, 'Python', 'mihailo', ['1', '3'], ['1 2 3 4 5', '5 4 3 15'])
#print(r.run_compile())

file = open('plpl.txt', 'r')
text = file.read()
r = Runner(text, 'C++', 'mihailo', ['1', '3'], ['1 2 3 4 5 0', '5 4 3 15 0'])
print(r.run_cplusplus())