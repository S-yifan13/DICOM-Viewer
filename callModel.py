import os
import shutil
import requests
from reportlab.platypus import SimpleDocTemplate

import config
from dicomUtil import Dicom
from pdfUtil import createReport

nidus_type = config.NIDUS_TYPE
def goThroughCheckResult(predictions, ratio=config.MIN_CHECK_SHOW_RATIO):
    result = []
    for i in range(len(predictions)):
        prediction = predictions[i]
        problem = {
            'frame_index': i
        }
        for j in range(len(prediction)):
            problem[nidus_type[j]] = []
            for rect in prediction[nidus_type[j]]:
                if rect[4] < ratio:
                    continue
                problem[nidus_type[j]].append(rect)
        if len(problem['js']) + len(problem['kq']) + len(problem['xs']) > 0:
            result.append(problem)
    return result


def getAllCheckResult(dicom):
    # if os.path.exists(config.TEMP_CHECK_DIR):
    #     shutil.rmtree(config.TEMP_CHECK_DIR)
    # os.mkdir(config.TEMP_CHECK_DIR)
    # dicom.frame2PngAll(config.TEMP_CHECK_DIR)
    # print('store temp check image success')

    batch_size = config.CHECK_BATCH_SIZE
    batch = dicom.frame_count // batch_size + 1
    predictions = []
    for i in range(batch):
        size = batch_size
        if i == batch - 1:
            size = dicom.frame_count - i * batch_size
        files = []
        for j in range(batch_size * i, batch_size * i + size):
            temp_path = config.TEMP_CHECK_DIR + "{}.png".format(i)
            files.append(('image', open(temp_path, 'rb')))
        response = requests.post(config.CHECK_MODEL_URL, files=files)
        predictions += response.json()['predictions']
        print('get check prediction success' + str(i))
    return predictions


if __name__ == '__main__':
    predictions = getAllCheckResult(Dicom('data/data'))
    result = goThroughCheckResult(predictions, 0.7)
    print(result)
    pdf = SimpleDocTemplate('output.pdf')
    createReport(result, pdf)

