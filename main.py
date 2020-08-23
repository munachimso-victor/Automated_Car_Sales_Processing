from cars_functions import *
import os
import reports


def main():
    """Process the JSON data and generate a full report out of it."""
    folder = os.getcwd()
    json_file = os.path.join(folder, "cars_sales.json")
    data = load_data(json_file)
    summary = process_data(data)
    print(summary)

    #turn this into a PDF report
    table = cars_dict_to_table(data)
    filename = os.path.join(folder, "cars.pdf")
    reports.generate(filename, "Sales summary for last month",
                     "{}<br/>{}<br/>{}".format(summary[0], summary[1], summary[2]), table)

    print("\n")
    print(f"A Summary PDF file named 'cars.pdf' has been created. Check {folder}")
    print("\n")
    print(
        """NOTE: If the program is ran twice, close the cars.pdf file before running it the second time. Else, a permissions error would occur""")


if __name__ == "__main__":
    main()
