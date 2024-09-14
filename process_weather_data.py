import datetime
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

current_date_time = None


def get_latest_weather_data():
    global current_date_time
    filename = './weather.json'
    with open(filename) as f:
        data = json.load(f)
        
    df = pd.DataFrame(data['hourly'])
    
    # Convert time into a proper datetime object
    df['time'] = pd.to_datetime(df['dt'], unit='s')
    
    # Set the current date time of the data in the global variable. This will be accessed later.
    current_date_time = datetime.datetime.fromtimestamp(data['current']['dt']).strftime('%Y_%m_%d_%H_%M')
    return df


def write_csv_file(dataframe):
    folder_name = 'openweathermap_data/output_data/{0}'.format(current_date_time)
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)
        
    filename = os.path.join(folder_name, 'output.csv')
    dataframe.to_csv(filename, index=False)
    

def calculate_temperature_stats(dataframe):
    temperature_data = {'stat': 'temp'}
    temperature_data['max'] = dataframe['temp'].max()
    temperature_data['min'] = dataframe['temp'].min()
    temperature_data['average'] = dataframe['temp'].mean()
    return temperature_data


def calculate_windspeed_stats(dataframe):
    temperature_data = {'stat': 'wind_speed'}
    temperature_data['max'] = dataframe['wind_speed'].max()
    temperature_data['min'] = dataframe['wind_speed'].min()
    temperature_data['average'] = dataframe['wind_speed'].mean()
    return temperature_data


def plot_temperature(dataframe):
    folder_name = 'openweathermap_data/output_data/{0}'.format(current_date_time)
    filename = os.path.join(folder_name, 'temperature.png')
    df.plot.line(x='time', y='temp')
    plt.savefig(filename)
    

def plot_windspeed(dataframe):
    folder_name = 'openweathermap_data/output_data/{0}'.format(current_date_time)
    filename = os.path.join(folder_name, 'wind_speed.png')
    df.plot.line(x='time', y='wind_speed')
    plt.savefig(filename)
    
    
if True:  #__name__ == '__main__':
    df = get_latest_weather_data()
    write_csv_file(df)
    stats = []
    stats.append(calculate_temperature_stats(df))
    stats.append(calculate_windspeed_stats(df))

    # Write the stats to a csv file
    folder_name = 'openweathermap_data/output_data/{0}'.format(current_date_time)
    filename = os.path.join(folder_name, 'output.csv')
    pd.DataFrame(stats).to_csv(filename, index=False)
    plot_temperature(df)
    plot_windspeed(df)