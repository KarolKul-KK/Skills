import pandas as pd


print(pd.DataFrame({'BoB': ['I liked it', 'It was awful.'], 'Sue': ['Pretty good', 'Bland']},
                    index=['Product A', 'Product B']))

print('XXXXXXXXXXXXXX')

print(pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales',
                                        '2017 Sales'], name='Product A'))