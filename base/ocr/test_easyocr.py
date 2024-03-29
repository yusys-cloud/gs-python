import base64
import io
import easyocr
import ddddocr
from PIL import Image

def ocr_image(image):
    rd = easyocr.Reader(['ch_sim','en']) # 支持中英文
    # 读取图像
    result = rd.readtext(image)

    print(result)
    # 提取识别的文本
    extracted_text = [entry[1] for entry in result]
    print(extracted_text)
    

def ocr_from_base64(encoded_image):
    head,context=encoded_image.split(",")
    print(head)
    img_data = base64.b64decode(context)
    ocr_image(img_data)

def ocr_by(encoded_image):
    ocr = ddddocr.DdddOcr(True,0)
    head,context=encoded_image.split(",")
    print(head)
    img_data = base64.b64decode(context)
    # with open('1.png', 'rb') as f:
    #     img_bytes = f.read()
    res = ocr.classification(img_data)

    print(res)


# ocr_image('tmp/ocr-road.jpg')


base64_image='data:image/png;base64,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'
# ocr_from_base64(base64_image)

ocr_by(base64_image)