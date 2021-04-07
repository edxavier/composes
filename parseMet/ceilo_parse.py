import os
import subprocess

def clear_special_chars(text):
    text = text.rstrip()
    text = text.replace('\x03','').replace('\x02','')
    text = text.rstrip('\n').rstrip('\r').strip()
    return text

def parse():
    ceilo = {}
    e = subprocess.run("awk '/^ Tmit/ {print $3,$5;exit}' ceilo.TXT", shell=True, stdout=subprocess.PIPE)
    line1 = clear_special_chars(e.stdout.decode()).split(' ')
    return line1
    
parse()