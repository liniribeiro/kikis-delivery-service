import csv
import os

from src.apm.apm_decorator import apm_capture_span


class ReportFile:
    def __init__(self, main_headers):
        self.file_name = None
        self.main_headers = main_headers

    @apm_capture_span
    def start_file(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.main_headers,
                                    delimiter=";", quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()

    @apm_capture_span
    def write_rows_on_file(self, rows):
        with open(self.file_name, 'a', newline='') as csv_file:
            dict_writer = csv.DictWriter(csv_file, fieldnames=self.main_headers,
                                         delimiter=";", quoting=csv.QUOTE_MINIMAL)
            for row in rows:
                dict_writer.writerow(row)

    @staticmethod
    def delete_file(file_name):
        os.remove(file_name)

    @apm_capture_span
    def write_file_filter_legend(self, **kwargs):
        with open(self.file_name, 'a', newline='') as csv_file:
            csv_file.write("\nFiltros utilizados: \n")

            for key in kwargs.keys():
                csv_file.write(f"{key}: {kwargs[key]} \n")

