import os
import pathlib
#to use this library make sure your machine has pdfkit(python pip install pdfkit) and wkhtmltopdf(locally) installed
import pdfkit

class userdefined:
    def ChangingimgFileName(self):
        print("hello")

        def readWrite(pathOfFile):
            fileToRead = open(pathOfFile, 'r+')
            data = int(fileToRead.read())
            # print(type(data))
            print("hello from the other side")

            newData = (data + 1)

            fileToRead.seek(0)
            fileToRead.write(str(newData))
            fileToRead.truncate()
            fileToRead.close()

            fileToReadForNewData = open(pathOfFile, 'r')
            readNewDatanum = fileToReadForNewData.read()
            fileToReadForNewData.close()

            return readNewDatanum

        counter = pathlib.Path(__file__).parent / "../conf_test/counter.txt"
        data = readWrite(counter)
        oldnumber = os.listdir(os.path.abspath("photos"))

        print("this is oldnumber{0}".format(oldnumber))
        name = oldnumber[1]
        oldname = os.path.abspath("photos/" + str(oldnumber[0]))
        print("this is oldname{0}".format(oldname))
        pathforphoto = pathlib.Path(__file__).parent / "photos/avatar.jpg"
        os.rename(oldname, os.path.abspath("photos/choco" + data + ".jpg"))
        newnumber = os.listdir(os.path.abspath("photos"))
        print("this is newnumber{0}".format(newnumber))
        newname = newnumber[1]
        print("this is newname{0}" .format(newname))
        print(type(newname))


        return newname
#
# new = userdefined
# new.ChangingimgFileName(1)
#htmlToPDF
#please don't use this function if your machine doesn't have pdfkit(python pip install pdfkit) and wkhtmltopdf(locally) installed
class convertToPdf:
    def htmltopdf(self,readnewdata1,time1):
        readNewData = str(readnewdata1)
        time = str(time1)
        # os.chdir("..")
        PathnameforHtmltoPdf = os.getcwd() + "/ReportHtml/report_" + time + "_" + readNewData + ".html"
        print(PathnameforHtmltoPdf)
        pdfkit.from_file(PathnameforHtmltoPdf, "report_" + time + "_" + readNewData + ".pdf")
#htmltopdfFunciton(PathnameforHtmltoPdf)

#endhtmlToPDF
