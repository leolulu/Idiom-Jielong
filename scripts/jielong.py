import os
import csv
import time


class JieLong:
    '''
    data stucture:
    idiom, freq, py, pinyin1, tone1, pinyin2, tone2, pinyin3, tone3, pinyin4, tone4
    '''
    def __init__(self):
        self.asset_path = self.get_asset_path()




    def get_asset_path(self):
        return os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'assets',
            '成语结果.csv'
        )

    def get_idiom_data(self):
        with open(self.asset_path, 'r', encoding='utf-8') as f:
            csv_data = csv.DictReader(f)
            csv_data = [i for i in csv_data]
        self.csv_data = csv_data

    def query_by(self,pingyin):
        pass

if __name__ == "__main__":
    data = get_idiom_data(get_assets_path())
    print(data)
