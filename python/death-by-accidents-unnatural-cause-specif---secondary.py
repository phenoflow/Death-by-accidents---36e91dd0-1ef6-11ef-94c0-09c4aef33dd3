# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"W31.1","system":"icd10"},{"code":"W54.9","system":"icd10"},{"code":"W84.8","system":"icd10"},{"code":"W84.7","system":"icd10"},{"code":"W83.5","system":"icd10"},{"code":"W83.8","system":"icd10"},{"code":"X28.7","system":"icd10"},{"code":"W83.1","system":"icd10"},{"code":"W83.7","system":"icd10"},{"code":"W31","system":"icd10"},{"code":"W84.9","system":"icd10"},{"code":"X53.9","system":"icd10"},{"code":"X28.9","system":"icd10"},{"code":"W31.7","system":"icd10"},{"code":"X28.8","system":"icd10"},{"code":"W84.1","system":"icd10"},{"code":"W31.2","system":"icd10"},{"code":"W83.9","system":"icd10"},{"code":"W54.8","system":"icd10"},{"code":"X28.2","system":"icd10"},{"code":"W31.5","system":"icd10"},{"code":"W84.5","system":"icd10"},{"code":"W83","system":"icd10"},{"code":"X28","system":"icd10"},{"code":"W31.0","system":"icd10"},{"code":"W84","system":"icd10"},{"code":"X28.5","system":"icd10"},{"code":"W84.2","system":"icd10"},{"code":"X28.1","system":"icd10"},{"code":"W31.9","system":"icd10"},{"code":"W31.8","system":"icd10"},{"code":"W84.0","system":"icd10"},{"code":"W83.2","system":"icd10"},{"code":"X53.8","system":"icd10"},{"code":"W83.0","system":"icd10"},{"code":"X28.0","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-specif---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-specif---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-specif---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
