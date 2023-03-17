# ECE143-project-Group15
This is the Pet Analysis project for ECE 143

## Library
For running the top5 cat and dog code, need to import plotly, plotly.io, numpy, pandas, json, plotly.graph_objs, plotly.express

## API Access
There are five API and secret passwords in the code since the Petfinder API can only access 1000 API calls per day.

## Data Collection
In the top_5 cat python file, load cat in separate days since the API access 1000 call pre days. Due to that reason, manually add the data into the dictionary.
In the top_5 dog data, we improve that and save all the data into json file.
All dog data is saved in dog data with json file

## File Structure

### Directories
All Dog Data: All dog data with their whole feature such as breeds, location, color, gender, age, size, etc. json format. <br />
Top 5 data: The top 5 common breeds in each state for both cat and dog. csv format. <br />
Friendly Result: The probability that a certain breed is comfortable in some certain living environment(with dog, cat, and children). <br />
Top5_pet_with_interactive: In the case the plot in 143Project_code_final_version.ipynb not work properly due to the interactive ploty function. There include two gifs that shows the visualization with interaction.


```
├── All Dog Data
│   ├── 1-4000.zip
│   └── 4001-all.zip
├── Group15_Pet_anlysis_presentaion.pdf
├── README.md
├── Top5_data
│   ├── each_state_cat.csv
│   └── each_state_dog.csv
├── Top5_pet_with_interactive
│   ├── cat.gif
│   └── dog.gif
├── friendly_result
│   ├── cat_result.csv
│   └── dog_result.csv
├── plot
│   ├── Cats_Cats.png
│   ├── Cats_Children.png
│   ├── Cats_Dogs.png
│   ├── Dogs_Cats.png
│   ├── Dogs_Children.png
│   └── Dogs_Dogs.png
└── src
    ├── 143Project_code_final_version.ipynb
    └── dog_and_cat_data_process.py
```

## Run the Code
Install all the third-party modules mentions in the library. <br />
Download json file in All Dog Data folder <br />
Download two csv files in friendly result folder <br />
Download two csv files in Top5 Data folder <br />
Add all them to one folder and you are able to run the 143Project_code_final_version.ipynb for data visualization!
