# =================== Lift Coefficient Over Time Graph =================== #

#Created on Fri June 20 2025
#@author: 23mlq
#Plots lift coeffcients from forceCoeffs.dat file of 3 series (different aoa) over a period of time

# ================================ Start ================================= #
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# === USER INPUT START ===
file_paths = [
    ("AOA5.dat", r"(AOA 5$^\circ$)"), #file 1 path, Series1 Name
    ("AoA8.5_OFF.dat", r"(AOA 8.5$^\circ$)"), # file 2 path, Series2 Name
    ("AOA10NoPlasma.dat", r"(AOA 10$^\circ$)"), #file 3 path, Series3 Name
]

start_time = 1.50 #start
end_time = 2.00 #end
# === USER INPUT END ===

# Column names from forceCoeffs.dat file
columns = ["Time", "Cd", "Cd(f)", "Cd(r)", "Cl", "Cl(f)", "Cl(r)",
           "CmPitch", "CmRoll", "CmYaw", "Cs", "Cs(f)", "Cs(r)"]

colors = ['#bf3afe', '#75bdff', '#fea316'] #colour hex codes of the 3 series
plt.figure(figsize=(10, 5)) #figure size

for (file_path, label), color in zip(file_paths, colors):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    data_lines = [line for line in lines if not line.strip().startswith('#') and line.strip()]
    data_str = "\n".join(data_lines)
    df = pd.read_csv(StringIO(data_str), sep='\s+', names=columns)

    df_filtered = df[(df["Time"] >= start_time) & (df["Time"] <= end_time)]

    plt.plot(df_filtered["Time"], df_filtered["Cl"], label=label, color=color)

# Labels and formatting
plt.xlabel("Time [s]", fontsize=30) #Time [s] on x axis
plt.ylabel(r"$\overline{C}_L$", fontsize=30) #Lift coeff on y axis
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# Legend in upper right corner, single column
plt.legend(fontsize=18, loc='upper right', ncol=1)

plt.grid(False)
plt.tight_layout()
plt.show()

# ================================= End ================================== #
