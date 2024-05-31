# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"V64.7","system":"icd10"},{"code":"V85.5","system":"icd10"},{"code":"V81.5","system":"icd10"},{"code":"V85","system":"icd10"},{"code":"V85.2","system":"icd10"},{"code":"V81.6","system":"icd10"},{"code":"V64.4","system":"icd10"},{"code":"V85.0","system":"icd10"},{"code":"V64.3","system":"icd10"},{"code":"V85.7","system":"icd10"},{"code":"V81.7","system":"icd10"},{"code":"V64.1","system":"icd10"},{"code":"V81.8","system":"icd10"},{"code":"V85.1","system":"icd10"},{"code":"V85.3","system":"icd10"},{"code":"V64.5","system":"icd10"},{"code":"V88.9","system":"icd10"},{"code":"V64.9","system":"icd10"},{"code":"V64.0","system":"icd10"},{"code":"V80.9","system":"icd10"},{"code":"V64.2","system":"icd10"},{"code":"V81.4","system":"icd10"},{"code":"V09.2","system":"icd10"},{"code":"V85.6","system":"icd10"},{"code":"V81.3","system":"icd10"},{"code":"V80.1","system":"icd10"},{"code":"V85.9","system":"icd10"},{"code":"V64","system":"icd10"},{"code":"V82.1","system":"icd10"},{"code":"V82.0","system":"icd10"},{"code":"V64.6","system":"icd10"},{"code":"V82.7","system":"icd10"},{"code":"V87.9","system":"icd10"},{"code":"V85.4","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-injuring---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-injuring---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-injuring---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
