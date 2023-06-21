import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем столбцы для кодирования в one-hot формате
data['robot'] = 0
data['human'] = 0

# Заполняем столбцы единицами, где это необходимо
for i in range(len(data)):
    if data.loc[i, 'whoAmI'] == 'robot':
        data.loc[i, 'robot'] = 1
    else:
        data.loc[i, 'human'] = 1

# Удаляем исходный столбец 'whoAmI'
data.drop('whoAmI', axis=1, inplace=True)

print(data.head())