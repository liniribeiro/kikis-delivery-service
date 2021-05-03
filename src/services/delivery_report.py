import datetime
import uuid

from src.apm.apm_decorator import apm_capture_span
from src.database.queries import get_delivery_report
from src.services.report_file import ReportFile
from src.services.s3 import S3Service
from src.services.zip import zip_file

HEADERS = ['status']


class ReportService(ReportFile):

    def __init__(self):
        self.file_name_base = 'kikis-delivery-report-report'
        super().__init__(HEADERS)

    def make_file_name(self):
        today = str(datetime.date.today())
        return f"{today}-{self.file_name_base}-{uuid.uuid4()}.csv"

    @apm_capture_span
    def parse_instalment_payload(self, delivery):

        status = delivery.status

        report_data = {
            'status': status.name
        }

        output = {}
        for key in self.main_headers:
            output.update({
                key: report_data[key],
            })
        return output

    def process_report(self):
        self.start_file(self.make_file_name())

        yield_deliveries = get_delivery_report()
        for deliveries in yield_deliveries:
            output_payload = [self.parse_instalment_payload(delivery) for delivery in deliveries]
            self.write_rows_on_file(output_payload)

        zip_filename, password = zip_file(self.file_name)
        # s3_download_link = S3Service().send_file_to_s3(zip_filename)
        self.delete_file(self.file_name)
