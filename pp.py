import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])


print(df)
#profile = ProfileReport(df, title="Pandas Profiling Report")
#profile.to_file("my_report.html")
