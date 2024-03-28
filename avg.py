import pandas as pd

df = pd.read_csv('V1_1x1_mse\VAE.csv')
average_value = df.mean()[0]
print(f"The average value miyawaki dataset is: {average_value}")

df = pd.read_csv('V1_1x1_mse\VAEVG.csv')
average_value = df.mean()[0]
print(f"The average value van gerven dataset is: {average_value}")