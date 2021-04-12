from file_reader import find_line, find_lines


class RVR(object):
    def __init__(self, file_path):
        self.file =  file_path

    def parsePage1(self):
        alarms = []

        line = find_line(self.file, "FS11 SYSTEM STATUS")
        if line:
            alarms.append(line[3])
        else:
            line = find_line(self.file, "FS11P SYSTEM STATUS")
            alarms.append(line[3])

        line = find_line(self.file, "Measurement unit")
        alarms.append(line[2])
        window_cont = find_lines(self.file, "window cont:")
        alarms.append(window_cont[0][2])
        alarms.append(window_cont[0][4])
        line = find_line(self.file, "DC saturation:")
        alarms.append(line[2])
        alarms.append(line[4])
        alarms.append(window_cont[1][2])
        alarms.append(window_cont[1][4])
        line = find_line(self.file, "intensity:")
        alarms.append(line[1])
        cont_compens = find_lines(self.file, "Contamination compensation:")
        alarms.append(cont_compens[0][2])
        line = find_line(self.file, "surface:")
        alarms.append(line[1])
        alarms.append(line[3])
        alarms.append(line[5])
        alarms.append(line[7])
        alarms.append(line[10])
        alarms.append(line[13])

        pos_12V = find_lines(self.file, "+12V")
        alarms.append(pos_12V[0][1])
        alarms.append(pos_12V[0][2].split(':')[1])
        alarms.append(pos_12V[0][4])
        alarms.append(pos_12V[0][6])
        line = find_line(self.file, "hood TX:")
        alarms.append(line[2].replace(',',''))
        alarms.append(line[5].replace(',',''))
        alarms.append(line[7].replace(',',''))
        line = find_line(self.file, "Interface unit:")
        alarms.append(line[2])

        line = find_line(self.file, "CPU:")
        alarms.append(line[1].replace(',',''))

        return alarms



    def parsePage2(self):
        alarms = []

        pos_12V = find_lines(self.file, "+12V")
        alarms.append(pos_12V[1][1])
        alarms.append(pos_12V[1][3])
        alarms.append(pos_12V[1][5])
        alarms.append(pos_12V[1][7])
        line = find_line(self.file, "Background luminance sensor:")
        alarms.append(line[3])

        window_cont = find_lines(self.file, "window cont:")
        cont_compens = find_lines(self.file, "contamination compensation:")

        alarms.append(window_cont[2][2])
        alarms.append(cont_compens[0][2])
        line = find_line(self.file, "backscatter:")
        alarms.append(line[1])

        lines = find_lines(self.file, "CPU:")
        alarms.append(lines[1][1])
        alarms.append(lines[1][3])
        line = find_line(self.file, "heater status: hood:")
        alarms.append(line[3].replace(',',''))
        alarms.append(line[5])
        line = find_line(self.file, "V5iso:")
        alarms.append(line[1])


        line = find_line(self.file, "VAISALA")
        if line:
            alarms.append(line[1])
            alarms.append(line[3])
            alarms.append(line[4])
            alarms.append(line[5].split(':')[1])
            alarms.append(line[8])
        else:
            for i in range(0,5):
                alarms.append('')

        line = find_line(self.file, "SIGNAL")
        if line:
            alarms.append(line[1])
            alarms.append(line[3])
            alarms.append(line[5])
        else:
            for i in range(0,4):
                alarms.append('')
        line = find_line(self.file, "REC. BACKSCATTER")
        if line:
            alarms.append(line[2])
            alarms.append(line[4])
        else:
            alarms.append('')
            alarms.append('')
        line = find_line(self.file, "TR. BACKSCATTER")
        if line:
            alarms.append(line[2])
            alarms.append(line[4])
        else:
            alarms.append('')
            alarms.append('')
        line = find_line(self.file, "LEDI")
        if line:
            alarms.append(line[1])
            alarms.append(line[3])
        else:
            alarms.append('')
            alarms.append('')
        line = find_line(self.file, "VBB")
        if line:
            alarms.append(line[1])
            alarms.append(line[3])
            alarms.append(line[5])
        else:
            alarms.append('')
            alarms.append('')
        line = find_line(self.file, "TS")
        if line:
            alarms.append(line[1])
            alarms.append(line[4])
        else:
            alarms.append('')
            alarms.append('')
       
        return alarms




    def parsePage3(self):
        alarms = []
        line = find_line(self.file, "TB")
        if line:
            alarms.append(line[1])
        else:
            alarms.append('')
        line = find_line(self.file, "TDRD")
        if line:
            alarms.append(f"{line[1]} {line[2]}")
            alarms.append(f"{line[4]} {line[5]}")
            alarms.append(line[7])
        else:
            alarms.append('')
            alarms.append('')
            alarms.append('')
        
        line = find_line(self.file, "HOOD HEATERS")
        if line:
            alarms.append(line[2])
        else:
            alarms.append('')
        
        alarms.append('')

        line = find_line(self.file, "vis sensor")
        if line:
            alarms.append(line[2])
        else:
            alarms.append('')
        line = find_line(self.file, "PWD:")
        if line:
            alarms.append(line[1])
        else:
            alarms.append('')
        line = find_line(self.file, "+12V out:")
        if line:
            alarms.append(line[2])
        else:
            alarms.append('')
        line = find_line(self.file, "PW option:")
        if line:
            alarms.append(line[2])
        else:
            alarms.append('---')
        return alarms

