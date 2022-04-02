Pandas dtype	Python type	NumPy type	Usage
object	str or mixed	string_, unicode_, mixed types	Text or mixed numeric and non-numeric values
int64	int	int_, int8, int16, int32, int64, uint8, uint16, uint32, uint64	Integer numbers
float64	float	float_, float16, float32, float64	Floating point numbers
bool	bool	bool_	True/False values
datetime64	NA	datetime64[ns]	Date and time values
timedelta[ns]	NA	NA	Differences between two datetimes
category	NA	NA	Finite list of text values


Use astype() to force an appropriate dtype
Create a custom function to convert the data
Use pandas functions such as to_numeric() or to_datetime()

cols_to_exclude = ['Program_Year', 'Date_of_Payment', 'Payment_Publication_Date']
for col in df.columns:
    if df[col].nunique() < 600 and col not in cols_to_exclude:
        df[col] = df[col].astype('category')

