# ECE143-project-Group15
This is the Pet Analysis project for ECE 143

## Library
For running the top5 cat and dog code, need import plotly, plotly.io, numpy, pandas, json

## API access
There are five api and secert password in the code since the petfinder API can only access 1000 API calls pre day.

## Data collection
In the top_5 cat python file, load cat in seperate days since the api access 1000 call pre days. Due to that reason, manually add the data into dictionary.
In the top_5 dog data, we improve that and save all the data into json file.
All dog data is save in dog data with json file

## File explaination
All dog data: All dog data with their whole feature such as breeds, location, color, gender, age, size, etc. json format
Top5 data: Include the top 5 common breeds in each state for both cat and dog. csv format
