import docx
import os

def getAllDocx(directory = os.getcwd()):
    files = []
    for f in os.listdir(directory):
        if f.endswith('.docx') or f.endswith('.doc'):
            files.append(f)
    return files

# start recording text on "ЭКЗАМЕНАЦИОННЫЙ БИЛЕТ № **" end on "Составитель ст.преподаватель кафедры «РЭТ»                           Наурыз К.Ж."
def copyAllDocsToOne(path, mainDoc, docs):
    for docName in docs:
        copyFlag = False
        paragraphsToCopy = []
        partOfEverythingDoc = docx.Document(os.path.join(path, docName))
        for paragraph in partOfEverythingDoc.paragraphs:
            if "ЭКЗАМЕНАЦИОННЫЙ БИЛЕТ" in paragraph.text:
                copyFlag = True
            elif "Составитель ст.преподаватель кафедры «РЭТ»                           Наурыз К.Ж." in paragraph.text:
                copyFlag = False
            if copyFlag:
                paragraphsToCopy.append(paragraph.text)
        addParagraphsToMainDoc(mainDoc, paragraphsToCopy)
    mainDoc.save('AssemledDocs.docx')

def addParagraphsToMainDoc(mainDoc, paragraphsToCopy):
    for i in paragraphsToCopy:
        mainDoc.add_paragraph(i)
path = '/home/deus'
docs = getAllDocx(path)
mainDoc = docx.Document()
copyAllDocsToOne(path, mainDoc, docs)

