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
All dog data: All dog data with their whole feature such as breeds, location, color, gender, age, size, etc. json format. <br />
Top 5 data: The top 5 common breeds in each state for both cat and dog. csv format. <br />
Friendly Result: The probability that a certain breed is comfortable in some certain living environment(with dog, cat, and children). <br />
Top5_pet_with_interactive: In the case the plot in 143Project_code_final_version.ipynb not work properly due to the interactive ploty function. There include two gifs that shows the visualization with interaction.

## Run the Code
Install all the third-party modules mentions in the library. <br />
Download json file in All Dog Data folder <br />
Download two csv files in friendly folder <br />
Download two csv files in Top5 folder <br />
All them to one folder and you are able to run the 143Project_code_final_version.ipynb for data visualization!
