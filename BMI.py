from numpy.lib.stride_tricks import as_strided
import pandas as pd
from sklearn.metrics import accuracy_score


def main():
    df = pd.read_csv(
        "./Data/Obesity/ObesityDataSet_raw_and_data_sinthetic.csv")

    height = df.loc[:, 'Height'].values
    weight = df.loc[:, 'Weight'].values
    label = df.iloc[:, -1].values

    bmi_index = weight / (height ** 2)

    a = []
    for i in bmi_index:
        if i < 18.5:
            a.append("Insufficient_Weight")
        elif i < 25:
            a.append("Normal_Weight")
        elif i < 30:
            a.append("Overweight")
        elif i < 35:
            a.append("Obesity_Type_I")
        elif i < 40:
            a.append("Obesity_Type_II")
        else:
            a.append("Obesity_Type_III")

    raw_label = []
    for i in label:
        if i.startswith("Overweight"):
            raw_label.append("Overweight")
        else:
            raw_label.append(i)

    bmi_label = pd.array(a)
    raw_label = pd.array(raw_label)

    print(accuracy_score(bmi_label, raw_label) * 100)


if __name__ == "__main__":
    main()
