#!/bin/bash
# get current water level
water_level=$(curl -s https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/593647aa-9fea-43ec-a7d6-6476a76ae868/W/currentmeasurement.json | jq .value)
echo $water_level