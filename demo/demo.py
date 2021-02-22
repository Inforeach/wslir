from atlas import *
import pandas as pd
import chart_studio.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
from ipywidgets import widgets

e = engine.Instance()
s = e.get_session('mktdata')
c = s.get_connection()
ds = c.get_datastore('mktdata',access_mode.read_write())

def getTkrs():
    tkrs = []
    rs = ds.regex_name_search('[a-z]+\.close')
    while rs.next():
        tkrs.append( rs.name()[0:-6] )
    return tkrs

def countTS():
    count = 0
    rs = ds.regex_name_search('.*')
    while rs.next():
        count += 1
    return count

def countPts():
    count = 0
    rs = ds.regex_name_search('.*')
    while rs.next():
        #print(rs.name()) 
        #ts = ds.get_time_series(rs.name())
        #count += ts.get_last_date_int() - ts.get_first_date_int() + 1
        count += 7800
    return count
    
def getOHLCV(tkr):
    o = ds.get_time_series("{}.open".format(tkr))
    h = ds.get_time_series("{}.high".format(tkr))
    L = ds.get_time_series("{}.low".format(tkr))
    c = ds.get_time_series("{}.close".format(tkr))
    v = ds.get_time_series("{}.volume".format(tkr))
    
    index = []; values = []
    l = o.get_last_date_int(); b = l - 10;
    cal = o.get_calendar()
    for i in range(b,l):
        if o.is_normal(i):
            index.append( "{}".format( cal.to_date(i) ) )
            row = [ "{}".format( cal.to_date(i) ),
                "{:,.2f}".format( o.get_double(i) ), 
                "{:,.2f}".format( h.get_double(i) ),
                "{:,.2f}".format( L.get_double(i) ),
                "{:,.2f}".format( c.get_double(i) ),
                "{:,.0f}".format( v.get_double(i) ) ]
            values.append(row)
            
    df = pd.DataFrame(values, index=index, columns=['Date','Open','High','Low','Close','Volume'])
    return( df )
