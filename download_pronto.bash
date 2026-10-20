cd cse583
mkdir pronto
cd pronto/
touch README.txt
echo "This is what the data is." > README.txt
mkdir data
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head 2015_station_data.csv
head 2015_status_data.csv
head 2015_trip_data.csv
head 2015_weather_data.csv
