df_grouped = df1[['id', 'seller_type']].groupby('seller_type')

df_grouped = df_grouped.count().reset_index()

df_grouped = df_grouped.rename(columns={'id': 'count'})

df_grouped
