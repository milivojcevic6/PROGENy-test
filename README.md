# PROGENyTest

PROGENyTest is a Python package that provides an implementation of the PROGENy algorithm for analyzing gene expression data. The PROGENy algorithm, described in the paper "Perturbation-response genes reveal signaling footprints in cancer gene expression", allows users to infer pathway activity from gene expression data, providing insights into signaling pathways involved in cancer and other diseases.

## Installation

To use PROGENyTest, you can install the package from source:


```bash
git clone https://github.com/milivojcevic6/PROGENy-test.git
cd PROGENy-test
pip install .
```


## Usage

Once installed, you can run the PROGENyTest command-line interface (CLI) to analyze your datasets using the PROGENy algorithm.


```bash
progenytest datasetname
```


Replace `datasetname` with the name of the dataset you want to analyze. The CLI will execute the PROGENy algorithm on the provided dataset and display the results, including a table summarizing the analysis.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

