# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"X27","system":"icd10"},{"code":"X26.4","system":"icd10"},{"code":"X26.5","system":"icd10"},{"code":"X29.9","system":"icd10"},{"code":"W56","system":"icd10"},{"code":"X29.8","system":"icd10"},{"code":"X29.1","system":"icd10"},{"code":"X27.1","system":"icd10"},{"code":"V40.4","system":"icd10"},{"code":"X27.5","system":"icd10"},{"code":"X29.0","system":"icd10"},{"code":"V70.5","system":"icd10"},{"code":"V10.5","system":"icd10"},{"code":"X26.1","system":"icd10"},{"code":"X29.4","system":"icd10"},{"code":"V70","system":"icd10"},{"code":"W56.2","system":"icd10"},{"code":"V10.4","system":"icd10"},{"code":"W56.8","system":"icd10"},{"code":"X29.7","system":"icd10"},{"code":"X26.7","system":"icd10"},{"code":"V10","system":"icd10"},{"code":"V70.4","system":"icd10"},{"code":"X29","system":"icd10"},{"code":"V80","system":"icd10"},{"code":"W56.0","system":"icd10"},{"code":"X29.5","system":"icd10"},{"code":"X26.2","system":"icd10"},{"code":"X27.2","system":"icd10"},{"code":"V40.7","system":"icd10"},{"code":"W56.1","system":"icd10"},{"code":"V40.5","system":"icd10"},{"code":"V70.9","system":"icd10"},{"code":"V10.9","system":"icd10"},{"code":"X26.0","system":"icd10"},{"code":"X26","system":"icd10"},{"code":"V40","system":"icd10"},{"code":"W56.4","system":"icd10"},{"code":"X27.8","system":"icd10"},{"code":"X26.9","system":"icd10"},{"code":"V40.6","system":"icd10"},{"code":"V70.6","system":"icd10"},{"code":"X27.0","system":"icd10"},{"code":"W56.7","system":"icd10"},{"code":"V10.3","system":"icd10"},{"code":"X27.4","system":"icd10"},{"code":"X27.7","system":"icd10"},{"code":"X27.9","system":"icd10"},{"code":"V70.7","system":"icd10"},{"code":"X26.8","system":"icd10"},{"code":"W56.5","system":"icd10"},{"code":"X29.2","system":"icd10"},{"code":"W56.9","system":"icd10"},{"code":"V40.9","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-animaldrawn---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-animaldrawn---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-animaldrawn---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
