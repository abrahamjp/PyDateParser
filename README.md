# PyDateParser
Simple date parser Python package, to transform datetime inputs in a human friendly way. 
For instance, if you want users to pass yesterdays datetime, they can specify 'yday' instead of 
explicitly specifying yesterdays date and time.

Supports, adding and subtracting seconds, minutes, hours, days and weeks from current UTC date and time. 
In case if you want to use a different date time reference point other than UTC, you even can pass the custom
date time value.

**Syntax:**
 
```
[+-](Float)(s|m|h|d|w) | now, tmrw, yday, dby, dat

Legend:
[]  - Values inside the square brackets are optional
|   - OR
()  - Values inside the rounded brackets are mandatory
```

**Usage:**
 
```
import PyDateParser 

dt = new DateParser()

# Add five second to current datetime and returns new date time in UTC
val = dt.parse("5s") 

# Add five and half seconds to current datetime and returns new date time in UTC
val = dt.parse("5.5s") 

# Subtract five and half seconds to current datetime and returns new date time in UTC
val = dt.parse("-5.5s") 

# Add 10 minutes to current datetime and returns new date time in UTC
val = dt.parse("10s") 

# Add 2 hours to current datetime and returns new date time in UTC
val = dt.parse("2h") 

# Add 3 days to current datetime and returns new date time in UTC
val = dt.parse("3d")

# Add 4 weeks to current datetime and returns new date time in UTC
val = dt.parse("4w")

# Add 1 hour to current date time
val = dt.parse("1h", relative_datetime=datetime.now())


#Keywords
# Returns current date time in UTC
val = dt.parse("now")

# Returns yesterdays date time in UTC
val = dt.parse("yday")

# Returns tomorrow's date time in UTC
val = dt.parse("tmrw")

# Returns 'day after tomorrow' (dat) date time in UTC
val = dt.parse("dat")

# Returns 'day before yesterday' (dby) date time in UTC
val = dt.parse("dby")

``` 
