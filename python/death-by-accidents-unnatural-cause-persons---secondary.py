# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"W51.0","system":"icd10"},{"code":"W04.0","system":"icd10"},{"code":"W51.2","system":"icd10"},{"code":"W51.9","system":"icd10"},{"code":"W51.1","system":"icd10"},{"code":"W51","system":"icd10"},{"code":"V89.1","system":"icd10"},{"code":"V89.3","system":"icd10"},{"code":"W04.1","system":"icd10"},{"code":"W51.8","system":"icd10"},{"code":"W04.8","system":"icd10"},{"code":"W51.7","system":"icd10"},{"code":"W04.4","system":"icd10"},{"code":"V76.7","system":"icd10"},{"code":"W04.2","system":"icd10"},{"code":"W51.5","system":"icd10"},{"code":"W04.7","system":"icd10"},{"code":"W04","system":"icd10"},{"code":"V89.9","system":"icd10"},{"code":"V89.0","system":"icd10"},{"code":"V89.2","system":"icd10"},{"code":"W04.5","system":"icd10"},{"code":"W51.4","system":"icd10"},{"code":"W04.9","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-persons---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-persons---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-persons---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
