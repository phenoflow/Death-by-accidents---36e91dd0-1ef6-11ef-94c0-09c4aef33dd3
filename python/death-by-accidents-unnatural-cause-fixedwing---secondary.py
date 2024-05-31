# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"V77.5","system":"icd10"},{"code":"V37.0","system":"icd10"},{"code":"V17.3","system":"icd10"},{"code":"V17.1","system":"icd10"},{"code":"V57.1","system":"icd10"},{"code":"V27.5","system":"icd10"},{"code":"V67.4","system":"icd10"},{"code":"V47.4","system":"icd10"},{"code":"V37.9","system":"icd10"},{"code":"V47.5","system":"icd10"},{"code":"V67.2","system":"icd10"},{"code":"V57.2","system":"icd10"},{"code":"V27.9","system":"icd10"},{"code":"V57.6","system":"icd10"},{"code":"V77","system":"icd10"},{"code":"V67.3","system":"icd10"},{"code":"V57.9","system":"icd10"},{"code":"V57","system":"icd10"},{"code":"V67.1","system":"icd10"},{"code":"V57.4","system":"icd10"},{"code":"V47","system":"icd10"},{"code":"V47.1","system":"icd10"},{"code":"V57.0","system":"icd10"},{"code":"V77.4","system":"icd10"},{"code":"V27","system":"icd10"},{"code":"V67.9","system":"icd10"},{"code":"V77.7","system":"icd10"},{"code":"V77.9","system":"icd10"},{"code":"V67.6","system":"icd10"},{"code":"V77.3","system":"icd10"},{"code":"V37","system":"icd10"},{"code":"V17.0","system":"icd10"},{"code":"V57.7","system":"icd10"},{"code":"V27.3","system":"icd10"},{"code":"V37.4","system":"icd10"},{"code":"V57.5","system":"icd10"},{"code":"V27.0","system":"icd10"},{"code":"V67.7","system":"icd10"},{"code":"V47.0","system":"icd10"},{"code":"V17.5","system":"icd10"},{"code":"V47.7","system":"icd10"},{"code":"V17.4","system":"icd10"},{"code":"V27.1","system":"icd10"},{"code":"V77.2","system":"icd10"},{"code":"V80.8","system":"icd10"},{"code":"V27.2","system":"icd10"},{"code":"V37.1","system":"icd10"},{"code":"V57.3","system":"icd10"},{"code":"V77.6","system":"icd10"},{"code":"V47.2","system":"icd10"},{"code":"V37.6","system":"icd10"},{"code":"V17.9","system":"icd10"},{"code":"V37.5","system":"icd10"},{"code":"V37.3","system":"icd10"},{"code":"V37.2","system":"icd10"},{"code":"V17.2","system":"icd10"},{"code":"V17","system":"icd10"},{"code":"V67","system":"icd10"},{"code":"V37.7","system":"icd10"},{"code":"V67.5","system":"icd10"},{"code":"V47.3","system":"icd10"},{"code":"V47.6","system":"icd10"},{"code":"V77.1","system":"icd10"},{"code":"V67.0","system":"icd10"},{"code":"V77.0","system":"icd10"},{"code":"V27.4","system":"icd10"},{"code":"V47.9","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-fixedwing---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-fixedwing---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-fixedwing---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
