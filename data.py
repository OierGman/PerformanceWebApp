import pandas as pd
import message


df_driver = pd.read_csv('driver_data.csv')

df_performance = pd.read_csv('performance_data.csv')


def get_data():
    target_IDs = df_performance['TransID'].tolist()
    print(target_IDs)

    for i in target_IDs:
        try:
            target_name = i
            select_perf = df_performance[df_performance['TransID'] == target_name]
            select_driver = df_driver[df_driver['TransID'] == target_name]
            merge_data = pd.merge(select_perf, select_driver, on='TransID', how='inner')
            merge_data['Num'] = merge_data['Num'].str.replace('"', '')
            main_data = merge_data.to_dict(orient='records')[0]
            print(main_data)

            message.sendperformancemessage(main_data)
            target_IDs.remove(i)
            print(target_IDs)

        except Exception as e:
            print("Error: " + str(e))
            print(e)


