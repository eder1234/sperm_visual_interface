import pandas as pd


def trajFrame(df):
    traj_df = pd.DataFrame({"name": [], "date": [], "quantity": [], "exposure": [], "tracked_id": [], "traj": []})

    df1 = df.groupby('name')
    for k1, v1 in df1:
        df2 = df1.get_group(k1)
        df3 = df2.groupby('date')
        for k3, v3 in df3:
            df4 = df3.get_group(k3)
            df5 = df4.groupby('quantity')
            for k5, v5 in df5:
                df6 = df5.get_group(k5)
                df7 = df6.groupby('exposure')
                for k7, v7 in df7:
                    df8 = df7.get_group(k7)
                    df9 = df8.groupby('tracked_id')
                    for k9, v9 in df9:
                        df10 = df9.get_group(k9)
                        x = df10['x'].to_numpy()
                        y = df10['y'].to_numpy()
                        temp_df = pd.DataFrame(
                            {"name": [k1], "date": [k3], "quantity": [k5], "exposure": [k7], "tracked_id": [k9],
                             "traj": [[x, y]]})
                        traj_df = pd.concat([temp_df, traj_df], ignore_index=True)
    return traj_df
