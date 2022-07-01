__authors__ = 'Rajaram Kaliyaperumal , David Lagorce'

import os

INPUT_EXCEL_FILE = 'input/FAIRData.xlsx'

# Change this url when u deploy in the server
FDP_SERVER_URL = 'http://95.142.173.26:8090'
FDP_SERVER_P_URL = 'https://w3id.org/orphadata/fairdatapoint'
FDP_ADMIN_USER = 'albert.einstein@example.com' 
FDP_ADMIN_PASSWORD = 'QhG)z43MYyh4,4Jf'

CATALOG_POST_URL_SUFFIX = 'catalog'
DATASET_POST_URL_SUFFIX = 'dataset'
DISTRIBUTION_POST_URL_SUFFIX = 'distribution'

REPOSITORY_TTL = 'template/repository.ttl'
CATALOG_TEMPLATE_TTL = 'template/catalog-template.ttl'
DATASET_TEMPLATE_TTL = 'template/dataset-template.ttl'
DISTRIBUTION_TEMPLATE_TTL = 'template/distribution-template.ttl'
