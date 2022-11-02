import pandas as pd
import os

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, 'Dataoverzicht.csv')
    
    #filepath = 'C:\\Users\\heili\\OneDrive\\Workspace\\project-biogasten\\src\\main\\resources\\Dataoverzicht.csv'
    dataset = pd.read_csv(filepath, sep=';')

    dataset.loc[dataset['EC-nummer'].str.contains('EC 3.2', regex=False), 'Class'] = 'hydrolysis'
    acido = ['EC 2.7.1.1',
             'EC 5.3.1.9',
             'EC 2.7.1.11',
             'EC 4.1.2.13',
             'EC 5.3.1.1',
             'EC 1.2.1.12',
             'EC 2.7.2.3',
             'EC 5.4.2.11',
             'EC 5.4.2.12',
             'EC 4.2.1.11',
             'EC 2.7.1.40',
             'EC 1.1.1.49',
             'EC 1.1.1.43',
             'EC 4.1.2.14',
             'EC 1.1.1.27',
             'EC 1.2.7.1',
             'EC 1.18.1.3',
             'EC 1.12.7.2',
             'EC 2.3.1.8',
             'EC 2.7.2.1',
             'EC 1.1.1.1',
             'EC 1.2.1.10',
             'EC 2.3.1.9',
             'EC 1.1.1.157',
             'EC 4.2.1.55',
             'EC 1.3.8.1',
             'EC 1.3.1.109',
             'EC 2.3.1.19',
             'EC 2.7.2.7',
             'EC 2.3.1.54',
             'EC 1.17.98.4',
             'EC 6.4.1.1',
             'EC 1.1.1.37',
             'EC 4.2.1.2',
             'EC 1.3.5.4',
             'EC 1.3.1.6',
             'EC 6.2.1.4',
             'EC 5.4.99.2',
             'EC 5.1.99.1',
             'EC 7.2.4.3',
             'EC 2.8.3.1',
             'EC 1.1.1.27',
             'EC 1.1.1.28',
             'EC 1.3.1.110',
             'EC 2.7.2.1',
             'EC 2.3.1.9',
             'EC 1.1.1.157',
             'EC 4.2.1.55',
             'EC 1.3.1.109',
             'EC 2.8.3.8',
             'EC 1.17.1.10',
             'EC 6.3.4.3',
             'EC 3.5.4.9',
             'EC 1.5.1.5',
             'EC 1.5.7.1',
             'EC 1.5.1.20',
             'EC 2.1.1.258',
             'EC 1.2.7.4',
             'EC 2.3.1.169',
             'EC 1.1.1.6',
             'EC 2.7.1.29',
             'EC 4.2.1.30',
             'EC 1.1.1.202',
             'EC 1.4.1.21',
             'EC 1.4.1.8',
             'EC 1.4.1.1',
             'EC 1.4.1.9',
             'EC 1.21.4.2',
             'EC 2.7.2.1',
             'EC 1.21.4.1',
             'EC 4.3.1.17',
             'EC 4.3.1.19',
             'EC 5.4.99.1',
             'EC 4.3.1.2',
             'EC 4.2.1.34',
             'EC 4.1.3.22',
             'EC 1.4.1.2',
             'EC 1.1.99.2',
             'EC 2.8.3.12',
             'EC 4.2.1.167',
             'EC 7.2.4.5']
    aceto = ['EC 2.3.3.1',
             'EC 4.2.1.3',
             'EC 1.1.1.42',
             'EC 1.2.7.3',
             'EC 2.8.3.18',
             'EC 1.3.5.1',
             'EC 4.2.1.2',
             'EC 1.1.1.37',
             'EC 2.8.3.9',
             'EC 1.3.5.1',
             'EC 1.2.1.3',
             'EC 1.2.1.10',
             'EC 1.3.1.110']
    metha = ['EC 1.2.7.12',
             'EC 2.3.1.101',
             'EC 3.5.4.27',
             'EC 1.5.98.1',
             'EC 1.12.98.2',
             'EC 1.5.98.2',
             'EC 2.1.1.86',
             'EC 2.8.4.1',
             'EC 1.8.98.1',
             'EC 2.7.2.1',
             'EC 2.3.1.8',
             'EC 6.2.1.1',
             'EC 2.3.1.169',
             'EC 2.1.1.245',
             'EC 1.2.7.4',
             'EC 2.8.4.1',
             'EC 1.8.98.1',
             'EC 2.1.1.90',
             'EC 2.1.1.246',
             'EC 2.1.1.248',
             'EC 2.1.1.249',
             'EC 2.1.1.247',
             'EC 2.8.4.1',
             'EC 1.8.98.1']
    dataset.loc[dataset['EC-nummer'].isin(acido), 'Class'] = 'acidogenesis'
    dataset.loc[dataset['EC-nummer'].isin(aceto), 'Class'] = 'acetogenesis'
    dataset.loc[dataset['EC-nummer'].isin(metha), 'Class'] = 'methanogenesis'
    classes = ['hydrolysis', 'acidogenesis', 'acetogenesis', 'methanogenesis']
    print(dataset[dataset['Class'].isin(classes)])
    dataset.to_csv('C:\\Users\\heili\\OneDrive\\Workspace\\project-biogasten\\src\\main\\resources\\Dataoverzicht.csv',
                   sep=';', index=False)











