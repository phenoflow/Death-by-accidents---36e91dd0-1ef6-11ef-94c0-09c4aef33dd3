# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"X43.7","system":"icd10"},{"code":"V69","system":"icd10"},{"code":"V59.9","system":"icd10"},{"code":"V19.9","system":"icd10"},{"code":"W80.1","system":"icd10"},{"code":"W80.7","system":"icd10"},{"code":"X43.0","system":"icd10"},{"code":"X43.4","system":"icd10"},{"code":"V76.6","system":"icd10"},{"code":"V76.9","system":"icd10"},{"code":"V19","system":"icd10"},{"code":"X43.9","system":"icd10"},{"code":"V82.8","system":"icd10"},{"code":"X43.5","system":"icd10"},{"code":"V76.5","system":"icd10"},{"code":"V19.8","system":"icd10"},{"code":"V76","system":"icd10"},{"code":"X43.2","system":"icd10"},{"code":"W80.0","system":"icd10"},{"code":"V59","system":"icd10"},{"code":"W80.8","system":"icd10"},{"code":"W80.5","system":"icd10"},{"code":"W80.4","system":"icd10"},{"code":"V16.9","system":"icd10"},{"code":"X43.1","system":"icd10"},{"code":"V16.5","system":"icd10"},{"code":"V59.8","system":"icd10"},{"code":"V16.4","system":"icd10"},{"code":"V69.8","system":"icd10"},{"code":"W80","system":"icd10"},{"code":"X43","system":"icd10"},{"code":"W80.2","system":"icd10"},{"code":"V16","system":"icd10"},{"code":"X43.8","system":"icd10"},{"code":"V69.9","system":"icd10"},{"code":"W80.9","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-clothing---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-clothing---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-clothing---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
