import pyttsx3
import PyPDF2

book = open('audiostory.pdf','rb')
pdfReader = PyPDF2.PdfReader(book)

pages = len(pdfReader.pages)
print(pages)

page = pdfReader.pages[5]
text = page.extractText()
friend = pyttsx3.init()
friend.say(text)
friend.runAndWait()