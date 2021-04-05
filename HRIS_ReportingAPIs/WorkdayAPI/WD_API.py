#!python3 

# import modules
import WDconfig
import json
import requests
import pandas as pd

def WD_api(url):
    '''
    Utilizes RaaS feature of workday to takes a workday webservices url, send a get request, parse json, and return a dataframe.
        Parameters:
            url: web_services report url.
        Returns:
            dataframe of said report.
        Notes:
            url should be json version.
    '''
    # get credentials from environment variables
    USER = WDconfig.username
    PASS = WDconfig.password

    # perform get request to obtain json data

    r = requests.get(url , auth=(USER, PASS))

    # convert json to a datafram

    r_json = r.json()
    df = pd.DataFrame.from_dict(r_json['Report_Entry'])
    return df