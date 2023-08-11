import os

import requests

from config import *

def getCheckPrediction(frame_index, dicom):
    # 保存图片
    temp_path = os.path.join(TEMP_DIR, "frame_{}.png".format(frame_index))
    dicom.frame2Png(frame_index, temp_path)
    image = open(temp_path, 'rb')
    files = {'image': image}
    response = requests.post(CHECK_MODEL_URL, files=files)
    if response.status_code != 200:
        return False
    print('get check prediction success')
    image.close()
    os.remove(temp_path)
    return response.json()['prediction']

