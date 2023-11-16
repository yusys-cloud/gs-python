
import base64

from pydantic import BaseModel
import ddddocr
import uvicorn
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    base64Image:str

def ocr_byddd(encoded_image):
    ocr = ddddocr.DdddOcr(True,0)
    head,context=encoded_image.split(",")
    print(head)
    img_data = base64.b64decode(context)
    # with open('1.png', 'rb') as f:
    #     img_bytes = f.read()
    res = ocr.classification(img_data)

    print(res)
    return res

@app.post("/api/v1/ocr")
async def read_root(item:Item):
    return {"code": ocr_byddd(item.base64Image)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8101)


