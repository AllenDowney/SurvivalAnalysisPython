# Lamps survival graph from Menon and Agrawal (2007)
from pandas import pd
df = pd.read_csv("https://bit.ly/2FleDbZ", index_col=0)
df.plot(x="h", y="K", title="Survival graph, 50 lightbulbs")