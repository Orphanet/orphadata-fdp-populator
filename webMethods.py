__authors__ = 'Rajaram Kaliyaperumal , David Lagorce'

import requests
import FDPClient
import configuration

FDP_CLIENT = FDPClient.FDPClient(configuration.FDP_SERVER_URL, configuration.FDP_ADMIN_USER,
                                 configuration.FDP_ADMIN_PASSWORD)

"""
Method to create and publish new metadata in the FDP
"""
def __create_metadata__(metadata_content, resource_type):
    # Create and publish metadata
    metadata_url = FDP_CLIENT.create_metadata(metadata_content, resource_type)
    return metadata_url

"""
Method to update repository metadata in the FDP
"""
def update_repository_metadata():
    repository_content = ""
    with open(configuration.REPOSITORY_TTL) as f:
        repository_content = f.read()

    FDP_CLIENT.update_metadata(configuration.FDP_SERVER_URL, repository_content)


"""
Method to create catalogs in the FDP
"""
def create_catalogs(catalog_matrix):
    catalog_template = ""
    catalog_uris = {}

    with open(configuration.CATALOG_TEMPLATE_TTL) as f:
        catalog_template = f.read()

    for catalog in catalog_matrix:
        title = catalog_matrix[catalog]['Title']
        version = catalog_matrix[catalog]['Version']
        description = catalog_matrix[catalog]['Description']
        catalogContent = catalog_template.replace('TITLE' , title )
        catalogContent = catalogContent.replace('VERSION' , version )
        catalogContent = catalogContent.replace('DESCRIPTION', description)
        catalogContent = catalogContent.replace('PARENT_IRI', configuration.FDP_SERVER_URL)
        catalog_uris[catalog] = __create_metadata__(catalogContent, configuration.CATALOG_POST_URL_SUFFIX)
    return catalog_uris

"""
Method to create datasets in the FDP
"""
def create_datasets(dataset_matrix, catalog_uris_matrix):
    dataset_template = ""
    datasets_uris = {}
    with open(configuration.DATASET_TEMPLATE_TTL) as f:
        dataset_template = f.read()
    for dataset in dataset_matrix:
        title = dataset_matrix[dataset]['Title']
        version = dataset_matrix[dataset]['Version']
        catalog_id = dataset_matrix[dataset]['catalog_id']
        description = dataset_matrix[dataset]['Description']
        theme = ''
        for uri in dataset_matrix[dataset]['theme_uri']:
            theme += '<' + uri + '>,'
        theme = theme[:-1]
        keywords = ''
        for keyword in dataset_matrix[dataset]['Keywords']:
            keywords += '\"' + keyword + '\",'
        keywords = keywords[:-1]
        datasetContent = dataset_template.replace('TITLE' , title )
        datasetContent = datasetContent.replace('VERSION' , version )
        datasetContent = datasetContent.replace('DESCRIPTION', description)
        datasetContent = datasetContent.replace('THEME_IRI', theme)
        datasetContent = datasetContent.replace('KEYWORD' , keywords)
        datasetContent = datasetContent.replace('PARENT_IRI', catalog_uris_matrix[catalog_id])
        datasets_uris[dataset] = __create_metadata__(datasetContent, configuration.DATASET_POST_URL_SUFFIX)
    return datasets_uris

"""
Method to create distributions in the FDP
"""
def create_distributions(distribution_matrix, dataset_uris_matrix):

    distribution_template = ""
    with open(configuration.DISTRIBUTION_TEMPLATE_TTL) as f:
        distribution_template = f.read()
    for distribution in distribution_matrix:
        dataset_id = distribution_matrix[distribution]['Dataset_id']
        title = distribution_matrix[distribution]['Title']
        version = distribution_matrix[distribution]['Version']
        license = distribution_matrix[distribution]['Licence']
        media_type = distribution_matrix[distribution]['media_type']
        file_size = distribution_matrix[distribution]['file_size']
        download_url = distribution_matrix[distribution]['download_url']
        content = distribution_template.replace('TITLE' , title )
        content = content.replace('VERSION' , version )
        content = content.replace('LICENSE', license)
        content = content.replace('MEDIA_TYPE', media_type)
        content = content.replace('BYTE_SIZE' , str(file_size))
        content = content.replace('PARENT_IRI', dataset_uris_matrix[dataset_id])
        content = content.replace('DOWNLOAD_URL', download_url)
        __create_metadata__(content, configuration.DISTRIBUTION_POST_URL_SUFFIX)

"""
Method to check if FAIR Data Point is online or offine
"""
def get_fdp_status(POST_URL):
    try:
        r = requests.get(POST_URL)
        return r.status_code
    except:
        print("FDP not online")
    return 500