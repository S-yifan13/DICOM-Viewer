import cv2
import pydicom
import numpy as np
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMessageBox


class Patient:
    def __init__(self, name, pid, birthday, sex, age):
        self.name = str(name.original_string)
        self.pid = pid
        self.birthday = birthday
        self.sex = sex
        self.age = age

    def __str__(self):
        return 'name: ' + self.name + '\n' + \
            'pid: ' + self.pid + '\n' + \
            'birthday: ' + self.birthday + '\n' + \
            'sex:' + self.sex + '\n' + \
            'age: ' + self.age + '\n'


class Dicom:
    def __init__(self, file_path):
        try:
            dataset = pydicom.dcmread(file_path)
            self.dataset = dataset

            if dataset.Modality != 'OCT':
                raise ValueError(dataset.Modality + ' is not supported. Only OCT is supported.')

            self.file_path = file_path

            # 病人信息
            self.patient = Patient(dataset.PatientName, dataset.PatientID,
                                   dataset.PatientBirthDate, dataset.PatientSex,
                                   dataset.PatientAge)

            # dicom 信息
            self.study_date = dataset.StudyDate
            self.study_time = dataset.StudyTime
            self.institution_name = dataset.InstitutionName
            self.body_part_examined = dataset.BodyPartExamined

            # 保存图像尺寸
            self.rows = dataset.Rows
            self.columns = dataset.Columns
            # regions 0, 1, 2分别代表横截面，纵截面，半径视图
            regions = dataset.SequenceOfUltrasoundRegions

            # 横截面起始X坐标
            self.transverseMinX = regions[0].RegionLocationMinX0
            self.transverseMaxX = regions[0].RegionLocationMaxX1
            # 横截面起始Y坐标
            self.transverseMaxY = regions[0].RegionLocationMaxY1
            self.transverseMinY = regions[0].RegionLocationMinY0

            # 纵截面起始X坐标
            self.longitudinalMinX = regions[1].RegionLocationMinX0
            self.longitudinalMaxX = regions[1].RegionLocationMaxX1
            # 纵截面起始X坐标
            self.longitudinalMaxY = regions[1].RegionLocationMaxY1
            self.longitudinalMinY = regions[1].RegionLocationMinY0

            # 保存像素数据
            self.pixel_array = dataset.pixel_array

            # 保存位深度
            self.bits_allocated = dataset.BitsAllocated
            self.bits_stored = dataset.BitsStored

            self.image_type = dataset.ImageType

        except (pydicom.errors.InvalidDicomError, FileNotFoundError, ValueError) as e:
            error_msg = str(e)
            app = QApplication([])
            msg_box = QMessageBox()
            msg_box.setWindowTitle('Error')
            msg_box.setText('Error')
            msg_box.setInformativeText(error_msg)
            msg_box.exec_()

    def showTransverse(self, frame_index, colormap='afmhot'):
        if frame_index < 0 or frame_index >= self.pixel_array.shape[0]:
            raise ValueError('frame_index out of range.')

        transverse_view = self.pixel_array[frame_index, :self.transverseMaxY, :, 0]
        plt.imshow(transverse_view, cmap=colormap)
        plt.title("Transverse View " + str(frame_index))
        plt.show()

    def showSagittal(self, colormap='afmhot'):
        z = (self.transverseMaxX + self.transverseMinX) // 2
        sagittal_view = self.pixel_array[:, :self.transverseMaxY, z, 0].transpose(1, 0)
        sagittal_view = self.resizeXY(sagittal_view)
        plt.imshow(sagittal_view, cmap=colormap)
        plt.title("Sagittal View ")
        plt.show()

    def showCoronal(self, colormap='afmhot'):
        y = (self.transverseMinY + self.transverseMaxY) // 2
        coronal_view = self.pixel_array[:, y, self.transverseMinX:self.transverseMaxX, 0].transpose(1, 0)
        coronal_view = self.resizeXY(coronal_view)
        plt.imshow(coronal_view, cmap=colormap)
        plt.title("Coronal View ")
        plt.show()

    def resizeXY(self, data):
        x = self.longitudinalMaxX - self.longitudinalMinX + 1
        y = self.longitudinalMaxY - self.longitudinalMinY + 1
        data_resized = cv2.resize(data, (x, y))
        return data_resized


if __name__ == '__main__':
    dicom = Dicom('data/data')
    print(dicom.patient)
    print(dicom.pixel_array.shape)
    print(dicom.image_type)
    dicom.showTransverse(1)
    dicom.showSagittal()
    dicom.showCoronal()



