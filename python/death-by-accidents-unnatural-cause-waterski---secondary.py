# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"W70.4","system":"icd10"},{"code":"X54.7","system":"icd10"},{"code":"V92.7","system":"icd10"},{"code":"V94","system":"icd10"},{"code":"W69.4","system":"icd10"},{"code":"W70.3","system":"icd10"},{"code":"W16.8","system":"icd10"},{"code":"W69.8","system":"icd10"},{"code":"W16.5","system":"icd10"},{"code":"V93.7","system":"icd10"},{"code":"W16.0","system":"icd10"},{"code":"X54.2","system":"icd10"},{"code":"W16","system":"icd10"},{"code":"X54.8","system":"icd10"},{"code":"W70.0","system":"icd10"},{"code":"X54.1","system":"icd10"},{"code":"W16.2","system":"icd10"},{"code":"X54.3","system":"icd10"},{"code":"W70","system":"icd10"},{"code":"X54.5","system":"icd10"},{"code":"X54","system":"icd10"},{"code":"W69.9","system":"icd10"},{"code":"X54.0","system":"icd10"},{"code":"W70.5","system":"icd10"},{"code":"W69.5","system":"icd10"},{"code":"W70.8","system":"icd10"},{"code":"W69.2","system":"icd10"},{"code":"W69.3","system":"icd10"},{"code":"V94.1","system":"icd10"},{"code":"W70.1","system":"icd10"},{"code":"W16.4","system":"icd10"},{"code":"W69","system":"icd10"},{"code":"W16.7","system":"icd10"},{"code":"W16.9","system":"icd10"},{"code":"W16.1","system":"icd10"},{"code":"W70.9","system":"icd10"},{"code":"X54.4","system":"icd10"},{"code":"W69.7","system":"icd10"},{"code":"W16.3","system":"icd10"},{"code":"W70.7","system":"icd10"},{"code":"W69.1","system":"icd10"},{"code":"W69.0","system":"icd10"},{"code":"V94.7","system":"icd10"},{"code":"W70.2","system":"icd10"},{"code":"X54.9","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-waterski---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-waterski---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-waterski---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
