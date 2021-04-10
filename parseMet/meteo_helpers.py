
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from reportlab.pdfgen.canvas import Canvas

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from ceilo_parse import parsePage1


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
            template = PdfReader("parseMet\ceilo_template.pdf", decompress=False)
            canvas = Canvas(outfile, pagesize='A4')

            names = self.data['name']
            form_date = self.data['date']
            cab = self.data['cab']
            week = self.data['week']

            column_1 = 180
            cab_offset = 77
            column_offset = 145
            column_2 = column_offset + column_1 # 310
            column_3 = column_offset + column_2 #450

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
                    for i in range(1,9):                
                        canvas.drawString(cab_pos,  top_l-(l_offset*i), res[i])
                    canvas.drawString(cab_pos, top_l-(l_offset*10), res[9])
                    canvas.drawString(cab_pos, top_l-(l_offset*11), res[10])
                    canvas.drawString(cab_pos, top_l-(l_offset*12), res[11])
                    canvas.drawString(cab_pos, top_l-(l_offset*13), res[12])
                    canvas.drawString(cab_pos, top_l-(l_offset*14), res[13])
                    canvas.drawString(cab_pos, top_l-(l_offset*15), res[14])
                    
                canvas.showPage()
                pages_count += 1

            canvas.save()
            
            pass
        except Exception as e:
            self.signals.error.emit(str(e))
            return

        self.signals.file_saved_as.emit(out_file_name, outfile)

