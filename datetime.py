import datetime
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")



import dateutil.parser
dt = dateutil.parser.parse("2016-04-15T08:27:18-0500")

