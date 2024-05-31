# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"W27.8","system":"icd10"},{"code":"V93.6","system":"icd10"},{"code":"V95.1","system":"icd10"},{"code":"W27.0","system":"icd10"},{"code":"V96.2","system":"icd10"},{"code":"W27.3","system":"icd10"},{"code":"V96.0","system":"icd10"},{"code":"X14","system":"icd10"},{"code":"W94.8","system":"icd10"},{"code":"W94.1","system":"icd10"},{"code":"X14.3","system":"icd10"},{"code":"W29.7","system":"icd10"},{"code":"X14.8","system":"icd10"},{"code":"V94.6","system":"icd10"},{"code":"W28.6","system":"icd10"},{"code":"V97.3","system":"icd10"},{"code":"V95.9","system":"icd10"},{"code":"V97","system":"icd10"},{"code":"W94.7","system":"icd10"},{"code":"W27.2","system":"icd10"},{"code":"V97.2","system":"icd10"},{"code":"V97.0","system":"icd10"},{"code":"W28.4","system":"icd10"},{"code":"W94","system":"icd10"},{"code":"X14.7","system":"icd10"},{"code":"W28.0","system":"icd10"},{"code":"V91.3","system":"icd10"},{"code":"W94.3","system":"icd10"},{"code":"W29.1","system":"icd10"},{"code":"W29.0","system":"icd10"},{"code":"W27.4","system":"icd10"},{"code":"V92.6","system":"icd10"},{"code":"W94.9","system":"icd10"},{"code":"V90.6","system":"icd10"},{"code":"W27.6","system":"icd10"},{"code":"V92.3","system":"icd10"},{"code":"X14.1","system":"icd10"},{"code":"X14.9","system":"icd10"},{"code":"W28.7","system":"icd10"},{"code":"V95.3","system":"icd10"},{"code":"V95.4","system":"icd10"},{"code":"W29.9","system":"icd10"},{"code":"W28.1","system":"icd10"},{"code":"W28.3","system":"icd10"},{"code":"W28.9","system":"icd10"},{"code":"W29.4","system":"icd10"},{"code":"X14.2","system":"icd10"},{"code":"V96.1","system":"icd10"},{"code":"X14.4","system":"icd10"},{"code":"V90.3","system":"icd10"},{"code":"W27.9","system":"icd10"},{"code":"W29.3","system":"icd10"},{"code":"W29.2","system":"icd10"},{"code":"V95","system":"icd10"},{"code":"W28.2","system":"icd10"},{"code":"W94.2","system":"icd10"},{"code":"W94.6","system":"icd10"},{"code":"V94.3","system":"icd10"},{"code":"W94.5","system":"icd10"},{"code":"W28.5","system":"icd10"},{"code":"V96.9","system":"icd10"},{"code":"W29.6","system":"icd10"},{"code":"V96","system":"icd10"},{"code":"V97.1","system":"icd10"},{"code":"W29","system":"icd10"},{"code":"V95.8","system":"icd10"},{"code":"V95.2","system":"icd10"},{"code":"W94.4","system":"icd10"},{"code":"X14.5","system":"icd10"},{"code":"W27","system":"icd10"},{"code":"X14.6","system":"icd10"},{"code":"W94.0","system":"icd10"},{"code":"W27.1","system":"icd10"},{"code":"X14.0","system":"icd10"},{"code":"W27.5","system":"icd10"},{"code":"W29.8","system":"icd10"},{"code":"W29.5","system":"icd10"},{"code":"V95.0","system":"icd10"},{"code":"W27.7","system":"icd10"},{"code":"V96.8","system":"icd10"},{"code":"W28.8","system":"icd10"},{"code":"V91.6","system":"icd10"},{"code":"V93.3","system":"icd10"},{"code":"W28","system":"icd10"},{"code":"V97.8","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-nonpoweredaircraft---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-nonpoweredaircraft---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-nonpoweredaircraft---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
