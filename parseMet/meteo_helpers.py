
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot
from reportlab.pdfgen.canvas import Canvas

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from ceilo_parse import parsePage1, parsePage2, parsePage3, parsePage4
from rvr_parser import RVR
import traceback


class WorkerSignals(QObject):
    """
    Defines the signals available from a running worker thread.
    """
    error = pyqtSignal(str)
    file_saved_as = pyqtSignal(str, str)


class Generator(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handle worker thread setup, signals
    and wrap-up.

    :param data: The data to add to the PDF for generating.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            out_file_name = 'result_cab' + str(self.data['cab']) + '_semana' + str(self.data['week']) + '.pdf'
            outfile = self.data.get("selected_folder", "") + '/' +out_file_name
            #template = PdfReader("parseMet\ceilo_template.pdf", decompress=False)
            template = PdfReader("parseMet/ceilo_template.pdf", decompress=False)
            canvas = Canvas(outfile, pagesize='A4')

            names = self.data['name']
            form_date = self.data['date']
            cab = self.data['cab']
            week = self.data['week']

            column_1 = 180
            cab_offset = 77
            column_offset = 145
            column_2 = (column_offset + column_1)-5 # 310
            column_3 = (column_offset + column_2)-10 #450

            top_l = 679
            l_offset = 14

            # create page objects
            pages = template.pages[0: 4]
            pages = [pagexobj(page) for page in pages]
            pages_count = 1
            column = column_1
            if week == 2:
                column = column_2
            elif week == 3:
                column = column_3

            cab_pos = column
            if cab == 28:
                cab_pos = column + cab_offset

    
            for page in pages:
                #canvas.setPageSize((page.BBox[2], page.BBox[3]))
                if self.data['preview']:
                    canvas.doForm(makerl(canvas, page))
                canvas.setFont("Helvetica", 9)
                #data = parse()
                top_l = 680
                canvas.drawString(column, top_l, names)
                canvas.drawString(column, top_l-l_offset, form_date)

                if pages_count == 1:
                    res = parsePage1(self.data['selected_file'])
                    top_l = 598    
                    canvas.drawString(cab_pos, top_l, res[0])
                    for i in range(0,9):
                        canvas.drawString(cab_pos,  top_l, res[i])
                        top_l = top_l-l_offset
                    
                    top_l = top_l-l_offset    
                    for i in range(9,15):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l = top_l-l_offset
                    top_l = (top_l-l_offset)+3
                    for i in range(15,22):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l = top_l-l_offset
                    
                    top_l = (top_l-l_offset)+2
                    for i in range(22,28):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l = top_l-l_offset

                    top_l = (top_l-l_offset)+2
                    for i in range(28,34):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l = top_l-l_offset
                
                if pages_count == 2:
                    res2 = parsePage2(self.data['selected_file'])
                    top_l = 605
                    canvas.drawString(cab_pos,  top_l, res2[0])
                    top_l = 585
                    canvas.drawString(cab_pos,  top_l, res2[1])
                    top_l = 566
                    canvas.drawString(cab_pos,  top_l, res2[2])
                    top_l = top_l-l_offset
                    canvas.drawString(cab_pos,  top_l, res2[3])
                    top_l = (top_l-l_offset * 2 ) - 4
                    canvas.drawString(cab_pos,  top_l, res2[4])
                    top_l = (top_l-l_offset * 2 ) + 3 
                    canvas.drawString(cab_pos,  top_l, res2[5])

                    top_l = (top_l-l_offset * 2 ) - 12
                    
                    for i in range(6,15):
                        canvas.drawString(cab_pos,  top_l, res2[i])
                        top_l = top_l-l_offset
                    
                    top_l = (top_l-l_offset)+2
                    for i in range(15,28):
                        canvas.drawString(cab_pos,  top_l, res2[i])
                        top_l = top_l-l_offset
                    top_l = (top_l-l_offset * 2 ) 
                    for i in range(0,5):
                        canvas.drawString(cab_pos,  top_l, res[i])
                        top_l = top_l-l_offset
                
                if pages_count == 3:
                    top_l = 622
                    res3 = parsePage3(self.data['selected_file'])
                    for i in range(5,9):
                        canvas.drawString(cab_pos,  top_l, res[i])
                        top_l = top_l-l_offset
                    top_l = (top_l-l_offset)-1 
                    for i in range(0,14):
                        canvas.drawString(cab_pos,  top_l, res3[i])
                        top_l = top_l-l_offset
                        if i == 5:
                            top_l -=4
                        if i == 12:
                            top_l -=8
                    top_l = (top_l-l_offset) - 3
                    canvas.drawString(cab_pos,  top_l, res3[14])
                    top_l = top_l-l_offset
                    canvas.drawString(cab_pos,  top_l, res3[15])
                    top_l = (top_l-l_offset * 2 ) - 2
                    canvas.drawString(cab_pos,  top_l, res3[16])
                    top_l = top_l-l_offset 
                    canvas.drawString(cab_pos,  top_l, res3[17])
                    top_l = (top_l-l_offset * 2 ) - 3
                    canvas.drawString(cab_pos,  top_l, res3[18])
                    top_l = top_l-l_offset
                    canvas.drawString(cab_pos,  top_l, res3[19])
                    top_l = (top_l-l_offset * 2 ) - 2
                    canvas.drawString(cab_pos,  top_l, res3[20])
                    top_l = (top_l-l_offset * 2 ) 

                    for i in range(21,29):
                        canvas.drawString(cab_pos,  top_l, res3[i])
                        top_l = top_l-l_offset

                if pages_count == 4:
                    top_l = 605
                    res4 = parsePage4(self.data['selected_file'])
                    for i in range(0,23):
                        canvas.drawString(cab_pos,  top_l, res4[i])
                        top_l = top_l-l_offset
                        if i == 10:
                            top_l-=5
                        if i == 19:
                            top_l-=3
                    
                canvas.showPage()
                pages_count += 1

            canvas.save()
    
        except Exception as e:
            print(traceback.format_exc())
            self.signals.error.emit(str(e))
            return

        self.signals.file_saved_as.emit(out_file_name, outfile)



class Generator2(QRunnable):
    """
    Worker thread

    Inherits from QRunnable to handle worker thread setup, signals
    and wrap-up.

    :param data: The data to add to the PDF for generating.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        try:
            out_file_name = 'rvr_cab' + str(self.data['cab']) + '.pdf'
            outfile = self.data.get("selected_folder", "") + '/' +out_file_name
            #template = PdfReader("parseMet\ceilo_template.pdf", decompress=False)
            template = PdfReader("parseMet/rvr_template.pdf", decompress=False)
            canvas = Canvas(outfile, pagesize='A4')

            names = self.data['name']
            form_date = self.data['date']
            cab = self.data['cab']
            week = self.data['week']

            column_1 = 210
            cab_offset = 68
            column_offset = 145
            column_2 = (column_offset + column_1)-5 # 310
            column_3 = (column_offset + column_2)-10 #450

            #top_l = 650
            l_offset = 14

            # create page objects
            pages = template.pages[0: 3]
            pages = [pagexobj(page) for page in pages]
            pages_count = 1
            column = column_1
            if week == 2:
                column = column_2
            elif week == 3:
                column = column_3

            cab_pos = column
            if cab == 28:
                if week > 1:
                    cab_pos = (column + cab_offset) - 10
                else:
                    cab_pos = column + cab_offset

            rvr = RVR(self.data['selected_file'])
            for page in pages:
                #canvas.setPageSize((page.BBox[2], page.BBox[3]))
                if self.data['preview']:
                    canvas.doForm(makerl(canvas, page))
                canvas.setFont("Helvetica", 9)
                #data = parse()
                top_l = 660
                canvas.drawString(column, top_l, names)
                top_l = 648
                canvas.drawString(column, top_l, form_date)
                top_l -= (l_offset * 4)

                if pages_count == 1:
                    res = rvr.parsePage1()
                    canvas.drawString(cab_pos, top_l, res[0])
                    top_l -= (l_offset * 2)
                    canvas.drawString(cab_pos, top_l, res[1])
                    top_l -= (l_offset * 2) + 4
                    for i in range(2,6):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l -= l_offset
                    top_l -= (l_offset+3)
                    for i in range(6,10):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l -= l_offset
                    top_l -= (l_offset * 2) - 2
                    for i in range(10,16):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l -= l_offset
                    top_l -= l_offset
                    for i in range(16,20):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l -= l_offset + 1
                    top_l -= l_offset
                    for i in range(20,23):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l -= l_offset +1
                    top_l -= l_offset + 1
                    canvas.drawString(cab_pos, top_l, res[23])
                    top_l -= (l_offset *2) + 1
                    canvas.drawString(cab_pos, top_l, res[24])
                    
                if pages_count == 2:
                    res = rvr.parsePage2()
                    top_l+=2
                    for i in range(0,4):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l -= l_offset
                    top_l -= l_offset
                    for i in range(4,10):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l -= l_offset
                        if i == 4:
                            top_l-=2
                        if i == 5:
                            top_l-=2
                        if i == 6:
                            top_l-=9
                    top_l -= l_offset 
                    for i in range(10,13):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l -= l_offset
                    top_l -= l_offset 
                    for i in range(13,32):
                        canvas.drawString(cab_pos, top_l, res[i])
                        if i >=15:
                            top_l -= l_offset + 1
                        else:
                            top_l -= l_offset 
                        if i == 25:
                            top_l -= + 2
                        if i == 30:
                            top_l -= + 9

                if pages_count == 3:
                    res = rvr.parsePage3()
                    top_l+=l_offset
                    for i in range(0,6):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l -= l_offset
                    top_l -= l_offset
                    for i in range(6,10):
                        canvas.drawString(cab_pos, top_l, res[i])
                        top_l -= l_offset + 1
                canvas.showPage()
                pages_count += 1

            canvas.save()
    
        except Exception as e:
            print(traceback.format_exc())
            self.signals.error.emit(str(e))
            return

        self.signals.file_saved_as.emit(out_file_name, outfile)

