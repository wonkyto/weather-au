from weather_au import observations

# Read and parse the XML file ftp://ftp.bom.gov.au/anon/gen/fwo/IDV60920.xml
obs_data = observations.Observations('Vic')
print(obs_data.acknowedgment, '\n')

# <observations>
for station in obs_data.stations():

    # <station wmo-id="95936" ... description="Melbourne (Olympic Park)">
    wmo_id = station['wmo-id']
    description = station['description']

    # <element units="Celsius" type="air_temperature">9.8</element>
    air_temperature = obs_data.air_temperature(wmo_id)

    if air_temperature is None:
        print(f'{wmo_id} {description}')
    else:
        print(f'{wmo_id} {description}   {air_temperature}°C')

wmo_id = '95936'
air_temperature = obs_data.air_temperature(wmo_id)
rainfall = obs_data.rainfall(wmo_id)
period = obs_data.period_attribute(wmo_id, 'time-local')
description = obs_data.station_attribute(wmo_id, 'description')

print(f'\nStation ID: {wmo_id}\nDescription: {description}\nTime: {period}\nAir Temperature: {air_temperature}\nRainfall: {rainfall}')
