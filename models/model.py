try:
    from PIL import Image #OpenCV быстрей
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'F:\Codes\Projects\ML\KRUZHOK.PRO\tesseract\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

pdf = pytesseract.image_to_pdf_or_hocr('test.jpg', extension='pdf', lang='rus')
with open('test.pdf', 'w+b') as f:
    f.write(pdf)