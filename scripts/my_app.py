from assessment.models import Assessment
import csv, arabic_reshaper


def run():
    with open('C:/Users/rest/Desktop/text.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        Assessment.objects.all().delete()

        for row in reader:
            Assessment.objects.get_or_create(
                company_name = row[1],
                product_name = row[0],
                contract_number = row[2],
                date_of_contract = row[3])
