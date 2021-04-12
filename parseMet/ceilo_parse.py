from file_reader import find_line, find_lines

def clear_special_chars(text):
    text = text.rstrip()
    text = text.replace('\x03','').replace('\x02','')
    text = text.rstrip('\n').rstrip('\r').strip()
    return text


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

    line = find_line(file_path, "Pulse Len")
    if line:
        alarms.append(line[2])
        alarms.append(line[4]) 

    line = find_line(file_path, "Inlaser")
    if line:
        alarms.append(line[1])
        alarms.append(line[3]) 

    line = find_line(file_path, "Pulse Cnt")
    if line:
        alarms.append(line[2])
        alarms.append(f"{line[5]} {line[6]}") 

    line = find_line(file_path, "Pulse Frq")
    if line:
        alarms.append(f"{line[2]} {line[3]}")

    line = find_line(file_path, "Window Cnd")
    if line:
        alarms.append(line[2])
        alarms.append(line[5]) 
    
    line = find_line(file_path, "Backg Rad")
    if line:
        alarms.append(line[3])
        alarms.append(line[2]) 

    #26,27
    line = find_line(file_path, "Tilt Angle")
    if line:
        alarms.append(line[2])
        alarms.append(line[4]) 


    line = find_line(file_path, "Internal:")
    if line:
        alarms.append(line[1])
        alarms.append(line[3]) 

    line = find_line(file_path, "DC Power:")
    if line:
        alarms.append(line[2])
        alarms.append(line[4]) 

    line = find_line(file_path, "Laser:")
    if line:
        alarms.append(line[1])
        alarms.append(line[3]) 


    return alarms


def parsePage2(file_path):
    alarms = []

    line = find_line(file_path, "Internal heater:")
    if line:
        alarms.append(f"{line[2]}{line[3]}")

    line = find_line(file_path, "Blower:")
    if line:
        alarms.append(f"{line[1]}{line[2]}")
    
    line = find_line(file_path, "Blower heater:")
    if line:
        alarms.append(line[2])

    line = find_line(file_path, "Batt Use:")
    if line:
        alarms.append(line[2])
    
    line = find_line(file_path, "System Status:")
    if line:
        alarms.append(line[2])

    line = find_line(file_path, "Suspect Module:")
    if line:
        alarms.append(line[2])
    
    #6
    line = find_line(file_path, "Tmit Shut ")
    if line:
        alarms.append(line[2])
    line = find_line(file_path, "Tmit Fail ")
    if line:
        alarms.append(line[2])
    lines = find_lines(file_path, "Receiver ")
    if lines.__len__()>1:
        alarms.append(lines[1][1])
    line = find_line(file_path, "Voltage ")
    if line:
        alarms.append(line[1])
    line = find_line(file_path, "Mem Fail ")
    if line:
        alarms.append(line[2])

    line = find_line(file_path, "Light Obst ")
    if line:
        alarms.append(line[2])
    
    line = find_line(file_path, "Receiv Sat")
    if line:
        alarms.append(line[2])
    line = find_line(file_path, "Coax Fail")
    if line:
        alarms.append(line[2])

    lines = find_lines(file_path, "Engine")
    if lines.__len__()>1:
        alarms.append(lines[1][1])

    #15
    line = find_line(file_path, "Win Contam")
    if line:
        alarms.append(line[2])        
    line = find_line(file_path, "Batt Low")
    if line:
        alarms.append(line[2]) 
    
    line = find_line(file_path, "Transm Exp ")
    if line:
        alarms.append(line[2])
    line = find_line(file_path, "Humid High")
    if line:
        alarms.append(line[2])
    lines = find_lines(file_path, "Blower ")
    if line:
        alarms.append(lines[1][1])
    line = find_line(file_path, "Humid Sens")
    if line:
        alarms.append(line[2])
    line = find_line(file_path, "Inheater")
    if line:
        alarms.append(line[1])
    line = find_line(file_path, "High Rad")
    if line:
        alarms.append(line[2])
    
    lines = find_lines(file_path, "Engine")
    if lines.__len__()>1:
        alarms.append(lines[2][1])

    line = find_line(file_path, "Batt Fail")
    if line:
        alarms.append(line[2])
    line = find_line(file_path, "Laser Mon ")
    if line:
        alarms.append(line[2])
    line = find_line(file_path, "Rec Fail ")
    if line:
        alarms.append(line[2])
    line = find_line(file_path, "Tilt Angle ")
    if line:
        alarms.append(line[2])

    return alarms


def parsePage3(file_path):
    alarms = []
    line = find_line(file_path, "Window Contam")
    if line:
        alarms.append(line[2])
        alarms.append(line[5])
    line = find_line(file_path, "Transm Expire")
    if line:
        alarms.append(line[2])
        alarms.append(line[5])
    
    lines = find_lines(file_path, "Blower ")
    if lines.__len__()>1:
        alarms.append(lines[2][1])
        alarms.append(lines[2][4])

    line = find_line(file_path, "Int Heater ")
    if line:
        alarms.append(line[2])
        #alarms.append(line[5])

    lines = find_lines(file_path, "Engine")
    if lines.__len__()>1:
        alarms.append(lines[4][1])
        alarms.append(lines[4][3])

    line = find_line(file_path, "Laser Monitor")
    if line:
        alarms.append(line[2])
        alarms.append(line[4])
    
    lines = find_lines(file_path, "Tilt Angle ")
    if lines.__len__()>1:
        alarms.append(lines[1][2])

    lines = find_lines(file_path, "System Status")
    if lines.__len__()>1:
        alarms.append(lines[1][2])
    lines = find_lines(file_path, "Suspect Module")
    if lines.__len__()>1:
        if lines[1].__len__()>3:
            alarms.append(f"{lines[1][2]}{lines[1][3]}")
        else:
            alarms.append(lines[1][2])

    line = find_line(file_path, "Angle Corr")
    if line:
        alarms.append(line[2])
    line = find_line(file_path, "Sky Cond")
    if line:
        alarms.append(line[2])

    line = find_line(file_path, "Scale")
    if line:
        alarms.append(line[1])
    line = find_line(file_path, "Noise")
    if line:
        alarms.append(line[2])
    line = find_line(file_path, "Ceiling")
    if line:
        alarms.append(line[1])

    line = find_line(file_path, "Reporting")
    if line:
        alarms.append(line[1])
    else:
        alarms.append('--')

    line = find_line(file_path, "Timeout")
    if line:
        alarms.append(line[1])

    lines = find_lines(file_path, "Window Cnd")
    if lines.__len__()>1:
        alarms.append(lines[1][2])
        alarms.append(lines[1][5])
    lines = find_lines(file_path, "Backg Rad")
    if lines.__len__()>1:
        alarms.append(lines[1][2])
        alarms.append(lines[1][3])
    lines = find_lines(file_path, "Tilt Angle:")
    if lines.__len__()>1:
        alarms.append(lines[1][2])
        alarms.append(lines[1][4])
    line = find_line(file_path, "Angle A")
    if line:
        alarms.append(line[2])
        alarms.append(line[5])

    return alarms

def parsePage4(file_path):
    alarms = []

    line = find_line(file_path, "+12V")
    if line:
        alarms.append(line[1])
        alarms.append(line[3])

    line = find_line(file_path, "+13VR")
    if line:
        alarms.append(line[1])
        alarms.append(line[3])
    line = find_line(file_path, "BAT ")
    if line:
        alarms.append(line[1])
        alarms.append(line[3])
    line = find_line(file_path, "+5VA ")
    if line:
        alarms.append(line[1])
        alarms.append(line[3])
    line = find_line(file_path, "-5VR")
    if line:
        alarms.append(line[1])
        alarms.append(line[3])

    line = find_line(file_path, "+2.5V")
    if line:
        alarms.append(line[1])
        alarms.append(line[3])
    
    line = find_line(file_path, "RHVD")
    if line:
        alarms.append(line[1])
        alarms.append(line[3])
    line = find_line(file_path, "-10V")
    if line:
        alarms.append(line[1])
        alarms.append(line[3])
    line = find_line(file_path, "+12VF")
    if line:
        alarms.append(line[1])
        alarms.append(line[3])
    else:
        line = find_line(file_path, "+3.3A")
        if line:
            alarms.append('---')
            alarms.append(line[1])
    
    line = find_line(file_path, "+3.3C")
    if line:
        alarms.append(line[1])
    else:
        alarms.append('---')

    line = find_line(file_path, "5V Isolat")
    if line:
        alarms.append(line[3])
        alarms.append(line[6])
    line = find_line(file_path, "Over Curr")
    if line:
        alarms.append(line[3])
        alarms.append(line[7])
    
    return alarms