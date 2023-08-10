import os

import pydicom
import requests

baseurl = 'http://127.0.0.1:8000/api/'
# response = requests.post(baseurl + 'try', data={
#     'data': '100'
# })
filepath = 'data/data'
# with open(filepath, 'rb') as file:
#     response1 = requests.post(baseurl + 'storeDicom', data={
#         'dicom': file
#     }, stream=True)
#     print(response1.json())

def upload_file(file_path, url):
    chunk_size = 1024 * 1024  # 分片大小，这里设置为 1MB
    total_size = os.path.getsize(file_path)
    total_chunks = (total_size // chunk_size) + 1

    with open(file_path, 'rb') as file:
        for chunk_number in range(total_chunks):
            start_byte = chunk_number * chunk_size
            end_byte = min((chunk_number + 1) * chunk_size, total_size)
            chunk_data = file.read(end_byte - start_byte)

            files = {
                'file': (file_path.split('/')[-1], chunk_data),
            }

            params = {
                'filename': file_path.split('/')[-1],
                'chunk_number': chunk_number,
                'total_chunks': total_chunks,
            }

            response = requests.post(url, files=files, data=params)

            if response.status_code != 200:
                print(f"上传分片 {chunk_number} 失败")
                return False
            else:
                print(f"上传分片 {chunk_number} 成功")

    # 通知上传完成
    params = {
        'filename': file_path.split('/')[-1],
        'total_chunks': total_chunks,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200 and response.json()['errno'] == 200:
        print("通知上传完成成功")
        return True

    print("通知上传完成失败")
    return False


upload_file(filepath, baseurl + 'storeDicom')
# dicom = pydicom.dcmread(filepath)
# name = dicom.PatientName
# print(name.alphabetic)