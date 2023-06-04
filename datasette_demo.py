#%%

import sqlite3
import datasette
import sqlite_utils

# %%
import os
os.system(f"""wget https://congress-legislators.datasettes.com/legislators.db""")
# %%

db=sqlite_utils.Database("legislators.db")

# %%
db.table_names()
# %%
for r in db["legislators"].rows:
    print(r)
# %%
