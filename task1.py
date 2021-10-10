import pandas as pd
from tabulate import tabulate

df = pd.read_csv(open("muse_v3.csv", encoding="utf8"))

req = df[['track', 'artist', 'seeds', 'spotify_id', 'genre']]
final = req.sample(n=25)
print(tabulate(final, headers='keys', tablefmt='psql'))
final.to_csv('modified.csv')
