from assessment.models import Contract
import csv, arabic_reshaper

path = 'C:/Users/rest/Desktop/text.csv'

def run():
    with open(path, encoding='utf-8') as file:
        reader = csv.reader(file)
        Contract.objects.all().delete()

        for row in reader:
            Contract.objects.get_or_create(
                company_name = row[1],
                product_name = row[0],
                contract_number = row[2]+'/'+'پ'+'/'+'م',
                date_of_contract = row[3])
