import click
from tabulate import tabulate

# Define the PROGENy algorithm implementation function
def run_progeny_analysis(dataset_name):
    # PROGENy algorithm goes  here
    # For now, print message indicating the dataset name
    click.echo(f"Running PROGENy analysis on dataset: {dataset_name}")

@click.command()
@click.argument('datasetname', metavar='DATASET', required=True, type=str, help="Name of the dataset to analyze")
def main(datasetname):

    # Run PROGENy analysis
    run_progeny_analysis(datasetname)

    # Generating a simple table as testing output
    data = [
        ["this", "is", "test"],
        ["of", "the", "table"]
    ]
    headers = ["Column 1", "Column 2", "Column 3"]
    click.echo(tabulate(data, headers=headers))

if __name__ == "__main__":
    main()
