import os
from torch.utils.data import Dataset, DataLoader


class ObjectDetectionDataset(Dataset):
    def __init__(self, image_dir, label_dir):
        self.image_dir = image_dir
        self.label_dir = label_dir
        self.image_path_list = self._get_file_list(image_dir)
        self.label_path_list = self._get_file_list(label_dir)

        if not os.path.exists(image_dir):
            raise ValueError("图像文件夹不存在")
        if not os.path.exists(label_dir):
            raise ValueError("标签文件夹不存在")
        self.image_num = len(self.image_path_list)
        self.label_num = len(self.label_path_list)
        if self.image_num == 0:
            raise ValueError("图像数量为0")
        if self.label_num == 0:
            raise ValueError("标签数量为0")
        if self.image_num != self.label_num:
            raise ValueError("图像和标签数量不相等")
        if not self._check_dataset(self.image_path_list, self.label_path_list):
            raise ValueError("数据集可能损坏（图像和标签文件名不匹配）")
        else:
            print("数据集检查无误")

    def __getitem__(self, position):
        image_path = self.image_path_list[position]
        label_path = self.label_path_list[position]
        # todo: 返回图像和标签

    def __len__(self):
        return self.image_num

    @staticmethod
    def _get_file_list(file_dir):
        file_path_list = []
        for file in os.listdir(file_dir):
            file_path = os.path.join(file_dir, file)
            file_path_list.append(file_path)
        return file_path_list

    @staticmethod
    def _check_dataset(image_path_list, label_path_list):
        image_list = [os.path.basename(image).split('.')[0] for image in image_path_list]
        label_list = [os.path.basename(label).split('.')[0] for label in label_path_list]
        for image in image_list:
            if image not in label_list:
                return False
        return True


if __name__ == '__main__':
    dataset = ObjectDetectionDataset('../../data/general/images/test/', '../../data/general/labels/test')
