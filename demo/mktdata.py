from atlas import *
from demo import *

e = engine.Instance()
s = e.get_session('mktdata')
c = s.get_connection()

ds = c.get_datastore('mktdata', access_mode.read_write())
c = ds.get_time_series("msft.close")
print(c)

# Run demo.py and retriev sample series
a = getTkrs()
adf = pd.DataFrame(a)
adf

# Get a list of available tkrs
tkr=a[430]
ts = ds.get_time_series('{}.close'.format(tkr))
print(ts.get_name())

# Get the close series and print first and last values
print("{} {:2.2f}".format(ts.get_first_date(), ts.get_double(ts.get_first_date_int())))
print('...')
print("{} {:2.2f}".format(ts.get_last_date(), ts.get_double(ts.get_last_date_int())))

tkr=a[134]
# Get ALL history, but display only 2 weeks
b = getOHLCV(tkr)
print("Tkr: {}".format(tkr.upper()))
b

# Just time retrieval and instantiation of TS
tkr='spy'
ts = ds.get_time_series("{}.close".format(tkr))
print(ts)
