# —— CONVERT MIDI FILE TO TUNESHARE CODE ——
# This version has a bug where rounding errors cause beats to be split incorrctly,
# sometimes skipping beats and sometimes adding extras.
# I don't know how to fix this yet. Please help 😩

path = 'enter path here'
multiplier = 16

inst_table = "00001144ffgfiif42227997734543444544544kk7777765h77dbebd7888a87jkaaaa88d9dbdcccddkjcb4cbkgdkcd49bfdf3edd44464fa79f6hllllllcll9llll"
drum_table = [18,24,25,25,18,17,20,21,11,11,12,10,17,10,23,15,23,24,23,13,22,22,13,22,14,13,13,16,14,19,13,26,14,20,20,17,22,23,10,10,27,27,15,15,16,16,25,25,18,20,22,27,27,16,21,24,14,16,17,11,11]

from mido import MidiFile
import os, pyperclip, time
os.system('clear')

mid = MidiFile(path)
channels = [0]*16
note_on_times = {}
data = []
code = str(int(mid.ticks_per_beat*multiplier/32))+"!"
clock = 0
errors = 0
for msg in mid:
    clock += msg.time
    if msg.type == 'program_change':
        channels[msg.channel] = 128 if msg.channel == 9 else msg.program
    elif msg.type == 'note_on' and 10 <= msg.note <= 99:
            data.append([msg.note-14,channels[msg.channel],1,msg.velocity,clock])
            note_on_times[(msg.channel, msg.note)] = [clock,len(data)]
    elif msg.type == 'note_off':
        if (msg.channel, msg.note) in note_on_times:
            data[note_on_times[(msg.channel, msg.note)][1]-1][2] = clock - note_on_times[(msg.channel, msg.note)][0]
            del note_on_times[(msg.channel, msg.note)]
        else:
            errors += 1
clock = 0
for i in data:
    i[2] = round(i[2]*multiplier)
    i[4] = round(i[4]*multiplier)
    if inst_table[i[1]] == "l":
        if i[1] == 128:
            i[0] = drum_table[i[0]-74]
        else:
            i[0] = [19,23,22,23,14,15,14,16,14,13,10][[115,116,117,118,119,120,122,123,125,126,127].index(i[1])]
    while clock < i[4]:
        code += "!"
        clock += 1
    code += str(i[0]) + inst_table[i[1]] + "00123456789abcdefghijklmno"[min(i[2],25)] + "0123456789abcdefghijklmnopqrstuvwxyz"[round(i[3]/127*35)]
    
pyperclip.copy(code)
print("Copied!")
