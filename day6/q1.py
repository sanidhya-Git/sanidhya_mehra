import pandas as pd
date = pd.Series(['2025-06-25 14:30:00', '2025-06-26 15:45:00', '2025-06-27 09:15:00'])

s = pd.to_datetime(date)
print(s)
