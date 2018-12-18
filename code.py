import csv

from matplotlib import pyplot as plt

# Plot data.

nbkills = []


fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(nbkills, c='red')

# Format plot.
plt.title("Kills for that round, 20170210", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Operator", fontsize=24)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

filename = 'dataDump_s5_summary_operator_loadout.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    nbkills = []
    for row in reader:
        nbkill = int(row[1])
        nbkills.append(nbkill)

    print(nbkills)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

