# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"V31.2","system":"icd10"},{"code":"V19.2","system":"icd10"},{"code":"V29.6","system":"icd10"},{"code":"V71.9","system":"icd10"},{"code":"V31.0","system":"icd10"},{"code":"V51.9","system":"icd10"},{"code":"V11.5","system":"icd10"},{"code":"V21.0","system":"icd10"},{"code":"V31.9","system":"icd10"},{"code":"V41.5","system":"icd10"},{"code":"V41.3","system":"icd10"},{"code":"V01.0","system":"icd10"},{"code":"V61.0","system":"icd10"},{"code":"V71.4","system":"icd10"},{"code":"V51.6","system":"icd10"},{"code":"V41.9","system":"icd10"},{"code":"V51","system":"icd10"},{"code":"V61","system":"icd10"},{"code":"V11","system":"icd10"},{"code":"V31.4","system":"icd10"},{"code":"V41.4","system":"icd10"},{"code":"V11.0","system":"icd10"},{"code":"V71.1","system":"icd10"},{"code":"V61.1","system":"icd10"},{"code":"V71.7","system":"icd10"},{"code":"V31","system":"icd10"},{"code":"V31.7","system":"icd10"},{"code":"V19.6","system":"icd10"},{"code":"V71.2","system":"icd10"},{"code":"V51.7","system":"icd10"},{"code":"V61.3","system":"icd10"},{"code":"V21.1","system":"icd10"},{"code":"V61.7","system":"icd10"},{"code":"V31.6","system":"icd10"},{"code":"V61.6","system":"icd10"},{"code":"V21.3","system":"icd10"},{"code":"V80.2","system":"icd10"},{"code":"V51.0","system":"icd10"},{"code":"V51.4","system":"icd10"},{"code":"V41.7","system":"icd10"},{"code":"V21","system":"icd10"},{"code":"V61.5","system":"icd10"},{"code":"V51.2","system":"icd10"},{"code":"V01.1","system":"icd10"},{"code":"V11.4","system":"icd10"},{"code":"V21.2","system":"icd10"},{"code":"V51.3","system":"icd10"},{"code":"V71.6","system":"icd10"},{"code":"V71.0","system":"icd10"},{"code":"V61.2","system":"icd10"},{"code":"V41.2","system":"icd10"},{"code":"V41","system":"icd10"},{"code":"V21.9","system":"icd10"},{"code":"V01","system":"icd10"},{"code":"V11.3","system":"icd10"},{"code":"V61.4","system":"icd10"},{"code":"V11.1","system":"icd10"},{"code":"V71.3","system":"icd10"},{"code":"V71.5","system":"icd10"},{"code":"V01.9","system":"icd10"},{"code":"V31.5","system":"icd10"},{"code":"V31.1","system":"icd10"},{"code":"V11.9","system":"icd10"},{"code":"V21.4","system":"icd10"},{"code":"V51.5","system":"icd10"},{"code":"V31.3","system":"icd10"},{"code":"V41.6","system":"icd10"},{"code":"V21.5","system":"icd10"},{"code":"V41.0","system":"icd10"},{"code":"V11.2","system":"icd10"},{"code":"V29.2","system":"icd10"},{"code":"V51.1","system":"icd10"},{"code":"V71","system":"icd10"},{"code":"V41.1","system":"icd10"},{"code":"V61.9","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-mcycle---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-mcycle---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-mcycle---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
