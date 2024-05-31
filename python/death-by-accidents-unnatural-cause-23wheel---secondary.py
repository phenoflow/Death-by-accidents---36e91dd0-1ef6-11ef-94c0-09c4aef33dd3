# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"V39.4","system":"icd10"},{"code":"V36.5","system":"icd10"},{"code":"V34","system":"icd10"},{"code":"V30.6","system":"icd10"},{"code":"V34.9","system":"icd10"},{"code":"V39","system":"icd10"},{"code":"V32.4","system":"icd10"},{"code":"V52.6","system":"icd10"},{"code":"V32.6","system":"icd10"},{"code":"V52","system":"icd10"},{"code":"V36.4","system":"icd10"},{"code":"V30","system":"icd10"},{"code":"V35.6","system":"icd10"},{"code":"V62.9","system":"icd10"},{"code":"V32","system":"icd10"},{"code":"V87.0","system":"icd10"},{"code":"V62.4","system":"icd10"},{"code":"V34.6","system":"icd10"},{"code":"V52.5","system":"icd10"},{"code":"V36.7","system":"icd10"},{"code":"V39.9","system":"icd10"},{"code":"V35.7","system":"icd10"},{"code":"V35.9","system":"icd10"},{"code":"V35","system":"icd10"},{"code":"V32.5","system":"icd10"},{"code":"V34.7","system":"icd10"},{"code":"V39.6","system":"icd10"},{"code":"V52.7","system":"icd10"},{"code":"V32.7","system":"icd10"},{"code":"V33.6","system":"icd10"},{"code":"V32.9","system":"icd10"},{"code":"V33.7","system":"icd10"},{"code":"V33.4","system":"icd10"},{"code":"V62.7","system":"icd10"},{"code":"V62.6","system":"icd10"},{"code":"V35.5","system":"icd10"},{"code":"V39.8","system":"icd10"},{"code":"V52.4","system":"icd10"},{"code":"V30.5","system":"icd10"},{"code":"V62","system":"icd10"},{"code":"V36.6","system":"icd10"},{"code":"V39.5","system":"icd10"},{"code":"V36.9","system":"icd10"},{"code":"V62.5","system":"icd10"},{"code":"V30.7","system":"icd10"},{"code":"V36","system":"icd10"},{"code":"V30.9","system":"icd10"},{"code":"V52.9","system":"icd10"},{"code":"V30.4","system":"icd10"},{"code":"V33","system":"icd10"},{"code":"V34.5","system":"icd10"},{"code":"V34.4","system":"icd10"},{"code":"V33.5","system":"icd10"},{"code":"V33.9","system":"icd10"},{"code":"V35.4","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-23wheel---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-23wheel---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-23wheel---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
