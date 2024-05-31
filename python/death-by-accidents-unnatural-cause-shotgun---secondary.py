# John, A, McGregor, J., Jones, I., Lee, S. C., Walters, J. T. R., Owen, M. J., O'Donovan, M., DelPozo-Banos, M., Berridge, D., and Lloyd, K., 2024.

import sys, csv, re

codes = [{"code":"X10","system":"icd10"},{"code":"X11.9","system":"icd10"},{"code":"X10.0","system":"icd10"},{"code":"X16.0","system":"icd10"},{"code":"X19.7","system":"icd10"},{"code":"X19.0","system":"icd10"},{"code":"X19.1","system":"icd10"},{"code":"X11","system":"icd10"},{"code":"X16.9","system":"icd10"},{"code":"X17.8","system":"icd10"},{"code":"X15.8","system":"icd10"},{"code":"X16.7","system":"icd10"},{"code":"X15.9","system":"icd10"},{"code":"X18.4","system":"icd10"},{"code":"X10.7","system":"icd10"},{"code":"X16","system":"icd10"},{"code":"X11.7","system":"icd10"},{"code":"X11.2","system":"icd10"},{"code":"X17.0","system":"icd10"},{"code":"X16.1","system":"icd10"},{"code":"X15.1","system":"icd10"},{"code":"X18.2","system":"icd10"},{"code":"X10.9","system":"icd10"},{"code":"X11.5","system":"icd10"},{"code":"X18.0","system":"icd10"},{"code":"X17","system":"icd10"},{"code":"X17.1","system":"icd10"},{"code":"X18.1","system":"icd10"},{"code":"X15.4","system":"icd10"},{"code":"X15.0","system":"icd10"},{"code":"X17.5","system":"icd10"},{"code":"X11.0","system":"icd10"},{"code":"X10.2","system":"icd10"},{"code":"X15","system":"icd10"},{"code":"X11.1","system":"icd10"},{"code":"X10.1","system":"icd10"},{"code":"X16.5","system":"icd10"},{"code":"X19.2","system":"icd10"},{"code":"X16.8","system":"icd10"},{"code":"X17.7","system":"icd10"},{"code":"X17.2","system":"icd10"},{"code":"X17.9","system":"icd10"},{"code":"X15.7","system":"icd10"},{"code":"X11.8","system":"icd10"},{"code":"X17.4","system":"icd10"},{"code":"X18.7","system":"icd10"},{"code":"X19","system":"icd10"},{"code":"X10.8","system":"icd10"},{"code":"X15.5","system":"icd10"},{"code":"X18","system":"icd10"},{"code":"X10.4","system":"icd10"},{"code":"X19.9","system":"icd10"},{"code":"X15.2","system":"icd10"},{"code":"X11.4","system":"icd10"},{"code":"X19.4","system":"icd10"},{"code":"X18.5","system":"icd10"},{"code":"X19.5","system":"icd10"},{"code":"X16.4","system":"icd10"},{"code":"X18.8","system":"icd10"},{"code":"X16.2","system":"icd10"},{"code":"X10.5","system":"icd10"},{"code":"X18.9","system":"icd10"},{"code":"X19.8","system":"icd10"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('death-by-accidents-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["death-by-accidents-unnatural-cause-shotgun---secondary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["death-by-accidents-unnatural-cause-shotgun---secondary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["death-by-accidents-unnatural-cause-shotgun---secondary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
