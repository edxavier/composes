import os
import subprocess

def clear_special_chars(text):
    text = text.rstrip()
    text = text.replace('\x03','').replace('\x02','')
    text = text.rstrip('\n').rstrip('\r').strip()
    return text

def find_line(file_path, search_text):
    file1 = open(file_path, 'r')
    lines = file1.readlines()
    for line in lines:
        line = line.strip()
        line = " ".join(line.split())
        if line != '':
            if line.startswith(search_text):
                return line.split() 


def parsePage1(file_path):
    alarms = []
    #e = subprocess.run("awk '/^ Tmit/ {print $3,$5;exit}' ceilo.TXT", shell=True, stdout=subprocess.PIPE)
    #line1 = clear_special_chars(e.stdout.decode()).split(' ')
    line = find_line(file_path, "Tmit Shutoff")
    if line:
        alarms.append(line[2])
        alarms.append(line[4])
    line = find_line(file_path, "Receiver")
    if line:
        alarms.append(line[1])
        alarms.append(line[3])

    line = find_line(file_path, "Ext Memory")
    if line:
        alarms.append(line[2])
        alarms.append(line[6]) 
    line = find_line(file_path, "Rec Saturat")
    if line:
        alarms.append(line[2])
        alarms.append(line[5]) 

    line = find_line(file_path, "Engine")
    if line:
        alarms.append(line[1])


    line = find_line(file_path, "Oper Mode")
    if line:
        alarms.append(line[2])
        alarms.append(line[4]) 
    
    line = find_line(file_path, "Meas Mode")
    if line:
        alarms.append(line[2])
        alarms.append(line[4]) 

    line = find_line(file_path, "Power Save")
    if line:
        alarms.append(line[2])
        alarms.append(line[5]) 

    return alarms
