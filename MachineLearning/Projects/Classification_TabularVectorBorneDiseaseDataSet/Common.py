import pandas as pd

def csv_to_latex_table(df, output_file=None, table_caption="Table", label="tab:table"):
    """
    Converts a CSV file into a LaTeX table and optionally saves it to a file.

    Parameters:
    - csv_file (str): Path to the CSV file.
    - output_file (str, optional): Path to save the LaTeX table. If None, it prints the table.
    - table_caption (str): Caption for the LaTeX table.
    - label (str): Label for referencing the table in LaTeX.

    Returns:
    - latex_table (str): The LaTeX table as a string.
    """
    
    # Generate LaTeX table
    latex_table = df.to_latex(index=False, caption=table_caption, label=label, escape=False)

    # If output_file is specified, save to file
    if output_file:
        with open(output_file, "w") as f:
            f.write(latex_table)
        print(f"LaTeX table saved to {output_file}")
    else:
        print("Generated LaTeX Table:\n")
        print(latex_table)

    return latex_table

