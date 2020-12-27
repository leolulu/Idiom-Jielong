import os
import csv
# from utils.decorator_utils import get_exec_time


class JieLong:
    '''
    data stucture:
    idiom, freq, py, py1, tone1, py2, tone2, py3, tone3, py4, tone4
    '''

    def __init__(self):
        self.get_asset_path()
        self.get_idiom_data()
        self.switch_only_top1_freq = True

    def get_asset_path(self):
        self.asset_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'assets',
            '成语结果.csv'
        )

    def get_idiom_data(self):
        with open(self.asset_path, 'r', encoding='utf-8') as f:
            csv_data = csv.DictReader(f)
            csv_data = [i for i in csv_data]
        self.idiom_data = csv_data

    # @get_exec_time
    def query_by_py1(self, pingyin):
        result = [i['idiom'] for i in self.idiom_data if i['py1'] == pingyin]
        return result

    def get_freq_list(self):
        freq_list = list(set([i['freq'] for i in self.idiom_data]))
        freq_list.sort(reverse=True)
        print(freq_list)


if __name__ == "__main__":
    f = JieLong()
    f.get_freq_list()
