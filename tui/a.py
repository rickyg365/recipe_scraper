import os

import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt



def initial_analysis(new_frame: pd.DataFrame | pd.Series) -> str:
    """ Initial Pandas Obj Analysis"""
    report = f"""
{new_frame.describe()}
{new_frame.head()}
{new_frame.tail()}

Columns: [ {", ".join([col for col in new_frame.columns])} ]
Size: {new_frame.size}
Shape: {new_frame.shape}
""" 
    print(report)
    return report


def main():
    filename = "data/2022_08_05_expected_budget_report.csv"
    new_data = pd.read_csv(filename)
    # initial_analysis(new_data)


    # Mask List - Works
    # masks = [
    #     new_data["store"] == "safeway",
    #     new_data["store"] == "trader joes",
    #     new_data["store"] == "99 cent",
    #     new_data["quantity"] == 1,
    #     new_data["total_price"] >= 9.98,
    #     new_data["total_price"] <= 5.00,
    # ]

    # for mask in masks:
    #     sub_data = new_data.loc[mask]
    #     print(sub_data.head())


    # Masks Dict - Works
    masks = {
        "safeway": new_data["store"] == "safeway",
        "trader": new_data["store"] == "trader joes",
        "cent": new_data["store"] == "99 cent",
        "single": new_data["quantity"] == 1,
        "expensive": new_data["total_price"] >= 9.98,
        "cheap": new_data["total_price"] <= 5.00,
    }

    for mask_name, mask in masks.items():
        sub_data = new_data.loc[mask]
        print(f"{mask_name}:\n", sub_data.head())

    # Save Excel
    # new_data.to_excel("data/report.xlsx")

    # Sorting
    new_data.sort_values("total_price", inplace=True)

    # Sub section
    sub_section = new_data[:4]

    # Plot - Matplotlib
    # new_data.plot(
    #     kind='bar',
    #     x='name',
    #     y='total_price'
    # )

    # Pie Chart - Matplotlib
    # plt.pie(new_data["total_price"], labels=new_data["name"])

    # Pair Plot - Seaborn
    # sns.pairplot(new_data)

    # plt.show()


if __name__ == '__main__':
    main()

    # for _ in range(10):
    #     # Cycle every 4, [0 1 2 3]
    #     print(_%4)

    loop = lambda m, d: [print(_%d) for _ in range(m)]
    loop(10, 3)