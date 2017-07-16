import os


def read_file(file_name):
    with open('stories' + os.sep + file_name, 'rb') as f:
        lines = [l for l in f.readlines() if len(l) != 2]
        story = ' '.join(lines)
    return story

data = read_file('thw.txt')

test = 'tester.rtf'
out_file = open(test,'w')
out_file.write("""{\\rtf1 This is \\b Bold  \\b0\line\ }""")
out_file.close() #thanks to the comment below