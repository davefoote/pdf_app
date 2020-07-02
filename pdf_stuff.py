'''
Inspired by 'Automate the Boring Stuff' by Al Sweigart

Dave Foote
'''
import PyPDF2 as pdf
import sys

def pdf_stack(top_filename, bottom_filename, new_filename):
    merged = pdf.PdfFileMerger()
    merged.append(pdf.PdfFileReader(open(top_filename, 'rb')))
    merged.append(pdf.PdfFileReader(open(bottom_filename, 'rb')))
    
    merged.write(new_filename)
        
if __name__ == '__main__':
    front_file = sys.argv[1]
    back_file = sys.argv[2]
    new_file = sys.argv[3]
    pdf_stack(front_file, back_file, new_file)
        

