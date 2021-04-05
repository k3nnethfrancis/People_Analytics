#! python3

import WDconfig
from WD_API import WD_api
import pandas as pd

url = r"webservices_report_json_url"

report = WD_api(url)

print(report.head())