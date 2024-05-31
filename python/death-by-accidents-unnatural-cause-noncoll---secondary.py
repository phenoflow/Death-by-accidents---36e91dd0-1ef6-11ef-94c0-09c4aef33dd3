# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"V87.5","system":"icd10"},{"code":"V18.1","system":"icd10"},{"code":"V38.9","system":"icd10"},{"code":"V68.3","system":"icd10"},{"code":"V48.1","system":"icd10"},{"code":"V18.5","system":"icd10"},{"code":"V87.8","system":"icd10"},{"code":"V78.7","system":"icd10"},{"code":"V38.1","system":"icd10"},{"code":"V58.5","system":"icd10"},{"code":"V58.4","system":"icd10"},{"code":"V48.6","system":"icd10"},{"code":"V68.2","system":"icd10"},{"code":"V58","system":"icd10"},{"code":"V18.2","system":"icd10"},{"code":"V48","system":"icd10"},{"code":"V68.1","system":"icd10"},{"code":"V87.4","system":"icd10"},{"code":"V68.5","system":"icd10"},{"code":"V87.2","system":"icd10"},{"code":"V48.4","system":"icd10"},{"code":"V28.5","system":"icd10"},{"code":"V78.3","system":"icd10"},{"code":"V18.9","system":"icd10"},{"code":"V78.9","system":"icd10"},{"code":"V58.1","system":"icd10"},{"code":"V48.7","system":"icd10"},{"code":"V88.2","system":"icd10"},{"code":"V88.8","system":"icd10"},{"code":"V78.4","system":"icd10"},{"code":"V78.1","system":"icd10"},{"code":"V81.1","system":"icd10"},{"code":"V68.4","system":"icd10"},{"code":"V78","system":"icd10"},{"code":"V88.6","system":"icd10"},{"code":"V28.4","system":"icd10"},{"code":"V68.7","system":"icd10"},{"code":"V38.7","system":"icd10"},{"code":"V58.9","system":"icd10"},{"code":"V28.9","system":"icd10"},{"code":"V87.6","system":"icd10"},{"code":"V28.1","system":"icd10"},{"code":"V78.6","system":"icd10"},{"code":"V28.3","system":"icd10"},{"code":"V48.0","system":"icd10"},{"code":"V28.2","system":"icd10"},{"code":"V88.7","system":"icd10"},{"code":"V68","system":"icd10"},{"code":"V88.4","system":"icd10"},{"code":"V80.4","system":"icd10"},{"code":"V80.6","system":"icd10"},{"code":"V78.5","system":"icd10"},{"code":"V38.6","system":"icd10"},{"code":"V78.2","system":"icd10"},{"code":"V48.9","system":"icd10"},{"code":"V38.0","system":"icd10"},{"code":"V58.0","system":"icd10"},{"code":"V38.5","system":"icd10"},{"code":"V58.2","system":"icd10"},{"code":"V58.7","system":"icd10"},{"code":"V87.7","system":"icd10"},{"code":"V68.6","system":"icd10"},{"code":"V48.2","system":"icd10"},{"code":"V38.4","system":"icd10"},{"code":"V48.3","system":"icd10"},{"code":"V18.4","system":"icd10"},{"code":"V18","system":"icd10"},{"code":"V58.6","system":"icd10"},{"code":"V18.0","system":"icd10"},{"code":"V88.5","system":"icd10"},{"code":"V18.3","system":"icd10"},{"code":"V38.2","system":"icd10"},{"code":"V80.0","system":"icd10"},{"code":"V28","system":"icd10"},{"code":"V28.0","system":"icd10"},{"code":"V87.1","system":"icd10"},{"code":"V48.5","system":"icd10"},{"code":"V78.0","system":"icd10"},{"code":"V88.1","system":"icd10"},{"code":"V68.9","system":"icd10"},{"code":"V38","system":"icd10"},{"code":"V68.0","system":"icd10"},{"code":"V58.3","system":"icd10"},{"code":"V38.3","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-noncoll---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-noncoll---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-noncoll---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
