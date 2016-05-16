#!/usr/bin/python3
import subprocess
import sys

model = sys.argv[1]
question = sys.argv[2]

cmd = 'th sample.lua {} -gpuid -1 -temperature 0.2 -length 1000 -primetext "{}" -seed `rand`'.format(model, question)
#print(cmd)
proc = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
text = proc.stdout.read().decode("UTF-8")

end_str = "--------------------------"
text = text[text.find(end_str) + len(end_str)+2:]

if text.startswith(question):
    text = text[len(question):]

text = text.replace("\n", " ")

print(text)
