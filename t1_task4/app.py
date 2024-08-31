import pandas as pd

def process_data(file_path):
    data = pd.read_csv(file_path)
    return data


if __name__ == "__main__":
    file_path = 'data.csv'
    result = process_data(file_path)
    avg = result['age'].mean()
    print(f'Средняя зарплата всех сотрудников: {avg}')

    df_age30 = result.loc[result['age'] > 30]
    print('Список сотрудников старше 30 лет: ')
    print(df_age30)