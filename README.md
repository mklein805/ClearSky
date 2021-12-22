# ClearSky
Pulls evening forecast for the next week from the NWS

# About
This is meant to pull the nightly forecast for the next seven nights according to the National Weather Service. This is of partiular use to astronomers. This class requires: requests, json, and geopy.

# How to Use
This class is relatively straightforward to use. An example is below:

```
sky = ClearSky()
sky.getForecast('Wellesley, MA')
```

First, initialize a ClearSky object and then call getForecast. getForecast takes a string location and then pulls from the National Weather Service to find the forecast for the coming nights.
