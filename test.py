from main import Runner

#file = open('tupo_test.py', 'r')
#text = file.read()
#r = Runner(text, 'Python', 'mihailo', ['1', '3'], ['1 2 3 4 5', '5 4 3 15'])
#print(r.run_compile())

file = open('paskal.txt', 'r')
text = file.read()
r = Runner(text, 'PASCAL', 'mihailo', ['1', '3','41'], ['0 1', '1 2','6 10'], 'STRING')
print(r.run_compile())