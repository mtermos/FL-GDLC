# FL-GDLC

## Project Overview

FL-GDLC (Federated Learning - Graph Deep Learning framework based on Centrality measures) is a framework designed to enhance Network Intrusion Detection Systems (NIDS) using Federated Learning and GDLC framework. This project combines advanced deep learning techniques with complex networks algorithms to classify and detect malicious network activities efficiently and securely.

## Features

- **Federated Learning Integration**: Ensures data privacy by training models across distributed clients without sharing raw data.
- **Centrality Measures**: Incorporates graph centrality metrics (e.g., degree, closeness, betweenness) to improve model accuracy.
- **Customizable Clients**: Supports the creation and management of multiple federated learning clients.
- The code is easy to extend for further research and experimentation.

## Project Structure

```
FL-GDLC-Initial/
├── .gitignore                   # Git ignore file
├── conf/                        # Configuration files
├── create_clients.ipynb         # Jupyter notebook for setting up FL clients
├── main.ipynb                   # Main notebook for running the project
├── README.md                    # Project documentation (this file)
├── requirements.txt             # Project dependencies
├── testing_dfs/                 # A partition of main df, for faster experiments
├── src/                         # Source code directory
│   ├── data/                    # DatasetInfo helpers
│   ├── models/                  # Deep Learning Models
│   ├── network/                 # Scripts for some centrality measures
│   ├── add_centralities.py      # Adds centralities to a dataframe
│   ├── add_pca_columns.py       # Adds pca columns to a dataframe
│   └── graph_level_measures.py  # Compute Graph-level measures of a graph
```

## Installation

1. Clone the repository:
    
    ```bash
    git clone https://github.com/mtermos/FL-GDLC.git
    cd FL-GDLC-Initial
    ```
    
2. Create and activate a virtual environment:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```
    
3. Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    

## Usage

1. **Set Up Federated Clients**: Open and execute the `create_clients.ipynb` notebook to create federated learning clients.
    
2. **Run the Main Notebook**: Use `main.ipynb` to start training and evaluating the models.
    
3. **Customization**: Modify the configuration files in the `conf` directory to customize the setup, such as the number of clients, graph parameters, or model hyperparameters.
## Dependencies

All required Python libraries are listed in `requirements.txt`. Install them using:

```bash
pip install -r requirements.txt
```

## Key Notebooks

- **`create_clients.ipynb`**: Guides the setup of federated clients:
	- Preparing datasets by reading files and cleaning dataframes.
	- Making the list of all attacks (to make sure global model has all classes).
	- Splitting data into clients.
	- Calculating graph-level metrics on each client, in order to apply GDLC.
	- Choosing the set of measures for each client.
	- Adding centrality measures to each client's dataframe.
	- Applying PCA to make final dataframes with same number of columns.
	- Saving each dataframe as a separate client.
- **`main.ipynb`**: The primary notebook for model training and evaluation.
	- Loading FL clients (created in `create_clients.ipynb`).
	- Initializing the CNN_LSTM model.
	- Initializing the Federated Learning environment.
	- Making different experiments:
		- Baseline (without PCA or centrality measures)
		- PCA (using PCA columns)
		- Centralities - DiGraph to use centrality measures directly (works only if same centrality measures have been added to all clients. This is just for specific cases and not for GDLC)
Note: To make experiments easier and faster, I used a strategy where I add all columns (PCA and centrality measures), and according to what type of experiments I just drop the columns not needed. Because computing centralities each time I want to run experiments has a computation and time cost.

## Contact

For questions or feedback, please contact Mortada Termos at: [mtermos@cesi.fr].