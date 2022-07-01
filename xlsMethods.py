__authors__ = 'Rajaram Kaliyaperumal , David Lagorce'

import pandas as pd
import configuration

def getCatalogMatrix(xlsfile):
    fair_catalog_matrix = {}
    catalog = pd.read_excel(xlsfile, sheet_name='catalog', engine='openpyxl')
    index = 1
    for index in catalog.index:
        fair_catalog_matrix[catalog['Id'][index]] = {  'Title' :'',
                                                       'Version': '',
                                                       'theme_taxonomy__uri': [],
                                                       'Description': ''}
        fair_catalog_matrix[catalog['Id'][index]]['Title'] = catalog['Title'][index]
        fair_catalog_matrix[catalog['Id'][index]]['Version'] = catalog['Version'][index]
        fair_catalog_matrix[catalog['Id'][index]]['Description'] = catalog['Description'][index]
        index += 1
    return fair_catalog_matrix




def getDatasetMatrix(xlsfile):
    fair_dataset_matrix = {}
    datasets = pd.read_excel(xlsfile , sheet_name='dataset')
    index = 1
    for index in datasets.index:
        fair_dataset_matrix[datasets['Id'][index]] = {  'catalog_id' : '',
                                                        'Title' : '' ,
                                                        'Version' : '' ,
                                                        'Keywords' : [] ,
                                                        'theme_uri' : [],
                                                        'Description' : ''
                                                        }
        fair_dataset_matrix[datasets['Id'][index]]['catalog_id'] = datasets['catalog_id'][index]
        fair_dataset_matrix[datasets['Id'][index]]['Title'] = datasets['Title'][index]
        fair_dataset_matrix[datasets['Id'][index]]['Version'] = datasets['Version'][index]
        fair_dataset_matrix[datasets['Id'][index]]['Description'] = datasets['Description'][index]

        for keyword in datasets['Keywords'][index].split(';'):
            fair_dataset_matrix[datasets['Id'][index]]['Keywords'].append(keyword)
        for uri in datasets['theme_uri'][index].split(';'):
            fair_dataset_matrix[datasets['Id'][index]]['theme_uri'].append(uri)
        index+=1
    return fair_dataset_matrix

def getDistributionMatrix(xlsfile):
    distribution = pd.read_excel(xlsfile , sheet_name='distribution')
    fair_distribution_matrix = {}
    index = 1
    for index in distribution.index:
        fair_distribution_matrix[distribution['Dataset_id'][index]] = {  'Dataset_id': '',
                                                                         'Title' : '' ,
                                                                        'Version' : '' ,
                                                                         'Licence' : '' ,
                                                                         'download_url' : '',
                                                                          'media_type' : '',
                                                                          'file_size' : ''
                                                                     }
        fair_distribution_matrix[distribution['Dataset_id'][index]]['Dataset_id'] = distribution['Dataset_id'][index]
        fair_distribution_matrix[distribution['Dataset_id'][index]]['Title'] = distribution['Title'][index]
        fair_distribution_matrix[distribution['Dataset_id'][index]]['Version'] = distribution['Version'][index]
        fair_distribution_matrix[distribution['Dataset_id'][index]]['Licence'] = distribution['Licence'][index]
        fair_distribution_matrix[distribution['Dataset_id'][index]]['download_url'] = distribution['download_url'][index]
        fair_distribution_matrix[distribution['Dataset_id'][index]]['media_type'] = distribution['media_type'][index]
        fair_distribution_matrix[distribution['Dataset_id'][index]]['file_size'] = distribution['file_size'][index]
        index+=1
    return fair_distribution_matrix




