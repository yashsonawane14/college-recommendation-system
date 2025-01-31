import csv
from django.core.management.base import BaseCommand
from myapp.models import CollegeData
from django.db import transaction

class Command(BaseCommand):
    help = 'Import CSV data into the CollegeData model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            college_data_list = []
            for row in reader:
                college_data = CollegeData(
                    rank=row['rank'],
                    percentile=row['percentile'],
                    branch=row['branch'],
                    gender=row['gender'],
                    category=row['category'],
                    fulfillment=row['fulfillment'],
                    seat_type=row['seat_type'],
                    primary_seat_type=row['primary_seat_type'],
                    secondary_seat_type=row['secondary_seat_type'],
                    score_type=row['score_type'],
                    college_name=row['college_name'],
                    enrollment_no=row['enrollment_no'],
                    branch_code=row['branch_code'],
                )
                college_data_list.append(college_data)

            with transaction.atomic():
                CollegeData.objects.bulk_create(college_data_list)

        self.stdout.write(self.style.SUCCESS('Successfully imported data from %s' % csv_file))
