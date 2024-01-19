# Location & Traveling Analysis through Galery Metadata &middot
> The detailed results and steps are given in the .ipynb 

A project that contains creating JSON data from a photo gallery which has GPS Infos, DateTime and File Name information. Visualize these metadata and mark them on map. conducts sentiment analysis on photos taken, exploring patterns and intensity of the statistical data.

## Installing / Getting Started

To get started, clone the project and navigate to the project directory. Install the required dependencies:

```shell
git clone https://github.com/wurat/CS210_FINAL_PROJECT.git
cd CS210_Term_Project/
pip install -r requirements.txt
```

## Developing

## Built With
- Python
- Jupyter Notebook

## Prerequisites
- Python (>=3.6)
- Jupyter Notebook
- Pillow Lıbrary (2.9.0)
- At least 8GB ram to open html file
  
#### To reproduce the analysis:
- Install the necessary libraries mentioned in the notebook.
```shell
!pip install pandas
!pip install Pilow==2.9.0
!pip install folium
!pip install -r requirements.txt
```
- Resources/Images folder will be %99 emptied for privacy purposes.
- Fill it with your own data.
- Run the notebook in a Jupyter environment, following each step.

## Building
This project does not require any additional building steps.

## Deploying / Publishing
There are no specific deployment steps for this project. It is designed for analysis and exploration purposes.

## Configuration
No user-configurable parameters. The configuration involves installing the required dependencies and setting up the environment.

## API Reference
This project does not rely on external APIs. Python libraries are employed for sentiment analysis and spell-checking.

## Steps for Analysis
To perform analysis using this project, follow these steps:

- Data Collection
  - Collecting conversational data from any type of image (.jpg, .png etc.), checking if the metadata has the GPS location itself. Save as gps_info.json.
- Data Visualization
  - Marking the Date, and file name info in the Turkey Map using the folium library. Clustering the necessary groups of images to prevent mess.
- Data Cleaning:
    - Handle Missing Values:
Ensure any missing values in the dataset are appropriately addressed, whether through imputation or removal, depending on the context.

    - Convert Filenames to Lowercase:
Standardize filenames by converting them to lowercase to maintain consistency.

     -  Remove Special Characters:
Eliminate special characters from the dataset to facilitate smoother analysis.

     -  Check Coordinates:
Verify the correctness and consistency of geographical coordinates, addressing any anomalies or errors in the dataset.

- Setting the Data Frame 
  - Setting the proper data frame and diversifying columns for detailed analysis.

### Visualization on Map
> After the data collection in the main.py, necessary location and time data are marked on the map via locator.py
- Folium library's MarkerCluster function is used.
- Observe them with clustered shapes for easy viewing.
- Easy access to the photo itself via popup features of marks.

### Analysis of the Data
> The data processed in this file undergoes a lot of analysis and gives us a lot of very useful information.
- JSON, pandas, seaborn, matplotlib, geopy and sklearn libraries are used.
- Visualisation of different types of charts.
- accepting/rejecting the hypothesis after each observation.

> Continuous of my report is at: Location Analysis Through My Gallery.pdf


## Licensing
This project is licensed under the MIT License. For details, refer to the LICENSE file.
