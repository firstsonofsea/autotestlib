from main import Runner

file = open('tupo_test.py', 'r')
text = file.read()
r = Runner(text, 'Python', 'mihailo', ['1', '3', '6'], ['1 2 3 4 5', '5 4 3 15', '5 3 2'], 'STRING', 'TEST')
print(r.run_compile())

file = open('paskal.txt', 'r')
text = file.read()
r = Runner(text, 'PASCAL', 'mihailo', ['1', '3','41'], ['0 1', '1 2','6 10'], 'STRING', 'ONLINE')
print(r.run_compile())

file = open('plpl.txt', 'r')
text = file.read()
r = Runner(text, 'C++', 'mihailo', ['3', '1','41'], ['5 3 4 9 0', '1 2 2 0', '6 10 12 3 0'], 'STRING', 'ONLINE')
print(r.run_compile())