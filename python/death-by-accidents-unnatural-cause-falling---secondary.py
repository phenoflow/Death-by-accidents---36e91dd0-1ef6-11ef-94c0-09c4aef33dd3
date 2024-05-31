# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"W17.5","system":"icd10"},{"code":"W13.2","system":"icd10"},{"code":"W18.9","system":"icd10"},{"code":"W19.0","system":"icd10"},{"code":"W18.4","system":"icd10"},{"code":"W06.1","system":"icd10"},{"code":"W17.4","system":"icd10"},{"code":"W17.2","system":"icd10"},{"code":"W14.1","system":"icd10"},{"code":"W14.9","system":"icd10"},{"code":"W14.8","system":"icd10"},{"code":"W13.0","system":"icd10"},{"code":"W19.2","system":"icd10"},{"code":"W18.7","system":"icd10"},{"code":"W13.7","system":"icd10"},{"code":"W19.8","system":"icd10"},{"code":"W13.4","system":"icd10"},{"code":"W18.2","system":"icd10"},{"code":"W17.8","system":"icd10"},{"code":"W13.1","system":"icd10"},{"code":"W19","system":"icd10"},{"code":"W18.5","system":"icd10"},{"code":"W19.7","system":"icd10"},{"code":"W17","system":"icd10"},{"code":"W14.0","system":"icd10"},{"code":"W18.1","system":"icd10"},{"code":"W06.0","system":"icd10"},{"code":"W06.7","system":"icd10"},{"code":"W06.4","system":"icd10"},{"code":"W14.7","system":"icd10"},{"code":"W06","system":"icd10"},{"code":"W17.0","system":"icd10"},{"code":"W06.5","system":"icd10"},{"code":"W13.5","system":"icd10"},{"code":"W13","system":"icd10"},{"code":"W13.8","system":"icd10"},{"code":"W06.9","system":"icd10"},{"code":"W18","system":"icd10"},{"code":"W17.7","system":"icd10"},{"code":"W06.8","system":"icd10"},{"code":"W14","system":"icd10"},{"code":"W14.5","system":"icd10"},{"code":"W06.2","system":"icd10"},{"code":"W17.9","system":"icd10"},{"code":"W13.9","system":"icd10"},{"code":"W19.5","system":"icd10"},{"code":"W18.0","system":"icd10"},{"code":"W18.8","system":"icd10"},{"code":"W14.4","system":"icd10"},{"code":"W17.1","system":"icd10"},{"code":"W19.9","system":"icd10"},{"code":"W19.1","system":"icd10"},{"code":"W14.2","system":"icd10"},{"code":"W19.4","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-falling---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-falling---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-falling---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
