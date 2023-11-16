from spire.doc.common import *
from spire.doc import *

outputFile = "HelloWorld.docx"
#Create a word document
document = Document()

document.remove_EvalInformation

#Create a new section
section = document.AddSection()

#Create a new paragraph
paragraph = section.AddParagraph()

paragraph.AppendText("clusterIPs用于给服务配置一个或者多个集群内部IP地址。出现这个错误的常见原因:在clusterIPs字段中设置了一个空的IP地址数组。")

#Append Text
paragraph.AppendText("Hello World!222")

#Save doc file.
document.SaveToFile(outputFile, FileFormat.Docx)

#Close the document object
document.Close()


inputFile = outputFile
outputFile =  "ToImage.png"
#Create word document
document = Document()
document.LoadFromFile(inputFile)
#Obtain image data in the default format of png,you can use it to convert other image format.
imageStream = document.SaveImageToStreams(0, ImageType.Bitmap)
with open(outputFile,'wb') as imageFile:
    imageFile.write(imageStream.ToArray())
document.Close()