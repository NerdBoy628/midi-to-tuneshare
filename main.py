# CONVERT MIDI FILE TO TUNESHARE CODE
# `multiplier` is the accuracy of the song, 
# you may have to play around with the value to get desired results.
# `tempo_changes` determines if it tries to approximate tempo changes.
# It ignores every track in `disabled_tracks`

path = 'enter path here'
multiplier = 8
tempo_changes = False
disabled_tracks = []

inst_table = "00001144ffgfiif42227997734543444544544kk7777765h77dbebd7888a87jkaaaa88d9dbdcccddkjcb4cbkgdkcd49bfdf3edd44464fa79f6hllllllcll9llll"
drum_table = [18,24,25,25,18,17,20,21,11,11,12,10,17,10,23,15,23,24,23,13,22,22,13,22,14,13,13,16,14,19,13,26,14,20,20,17,22,23,10,10,27,27,15,15,16,16,25,25,18,20,22,27,27,16,21,24,14,16,17,11,11]

import os
try:
    from mido import MidiFile, second2tick
    import pyperclip
except:
    os.system('pip3 install mido')
    os.system('pip3 install pyperclip')
    from mido import MidiFile, second2tick
    import pyperclip
os.system('clear')

def sec2tick(x):
    return(second2tick(x,mid.ticks_per_beat,60000000/bpm)/mid.ticks_per_beat)

mid = MidiFile(path)
firstbpm = 0
for msg in mid:
    if msg.type == 'set_tempo':
        firstbpm = round(60000000 / msg.tempo)
        bpm = firstbpm
        break
channels = [0]*16
volumes = [127]*16
note_on_times = {}
data = []
code = str(int(firstbpm*multiplier/4))+"!"
clock = 0.0
tempo_change_count = 0
for msg in mid:
    clock += sec2tick(msg.time)*firstbpm/bpm
    if msg.type == 'program_change':
        channels[msg.channel] = 128 if msg.channel == 9 else msg.program
    elif msg.type == 'note_on' and 24 <= msg.note <= 113 and msg.velocity > 0 and msg.channel not in disabled_tracks:
            data.append([msg.note-14,channels[msg.channel],1,msg.velocity*volumes[msg.channel]/127,clock])
            note_on_times[(msg.channel, msg.note)] = [clock,len(data)]
    elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
        if (msg.channel, msg.note) in note_on_times:
            data[note_on_times[(msg.channel, msg.note)][1]-1][2] = clock - note_on_times[(msg.channel, msg.note)][0]
            del note_on_times[(msg.channel, msg.note)]
    elif msg.type == 'tempo':
        if not tempo_changes:
            bpm = round(60000000 / msg.tempo)
            tempo_change_count += 1
    elif msg.type == 'control_change':
        if msg.control == 7:
            volumes[msg.channel] = msg.value
print("Tempo changes: "+str(tempo_change_count))

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
