# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"W65.5","system":"icd10"},{"code":"W66.1","system":"icd10"},{"code":"W67.8","system":"icd10"},{"code":"W67.0","system":"icd10"},{"code":"W68.9","system":"icd10"},{"code":"W68.8","system":"icd10"},{"code":"V92.1","system":"icd10"},{"code":"W67.4","system":"icd10"},{"code":"W74.0","system":"icd10"},{"code":"W74.5","system":"icd10"},{"code":"W68.4","system":"icd10"},{"code":"W68.5","system":"icd10"},{"code":"W66.9","system":"icd10"},{"code":"W73","system":"icd10"},{"code":"W68.1","system":"icd10"},{"code":"W67.9","system":"icd10"},{"code":"W67","system":"icd10"},{"code":"W67.1","system":"icd10"},{"code":"W65.7","system":"icd10"},{"code":"W66","system":"icd10"},{"code":"W66.5","system":"icd10"},{"code":"W73.5","system":"icd10"},{"code":"V92","system":"icd10"},{"code":"W65.2","system":"icd10"},{"code":"W67.2","system":"icd10"},{"code":"W74.7","system":"icd10"},{"code":"W65.4","system":"icd10"},{"code":"W74.1","system":"icd10"},{"code":"W67.7","system":"icd10"},{"code":"W65.1","system":"icd10"},{"code":"W66.8","system":"icd10"},{"code":"W66.7","system":"icd10"},{"code":"W65","system":"icd10"},{"code":"W73.7","system":"icd10"},{"code":"W68.2","system":"icd10"},{"code":"W73.9","system":"icd10"},{"code":"W74.8","system":"icd10"},{"code":"W73.1","system":"icd10"},{"code":"W73.8","system":"icd10"},{"code":"W68.7","system":"icd10"},{"code":"W73.0","system":"icd10"},{"code":"W67.5","system":"icd10"},{"code":"W73.4","system":"icd10"},{"code":"W66.0","system":"icd10"},{"code":"W68","system":"icd10"},{"code":"W65.0","system":"icd10"},{"code":"W73.2","system":"icd10"},{"code":"W74.9","system":"icd10"},{"code":"W74","system":"icd10"},{"code":"W74.2","system":"icd10"},{"code":"W65.9","system":"icd10"},{"code":"W66.2","system":"icd10"},{"code":"W66.4","system":"icd10"},{"code":"W65.8","system":"icd10"},{"code":"W68.0","system":"icd10"},{"code":"W74.4","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-drowng---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-drowng---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-drowng---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
