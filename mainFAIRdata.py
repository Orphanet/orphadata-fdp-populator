__authors__ = 'Rajaram Kaliyaperumal , David Lagorce'

import sys
import configuration
import json
import xlsMethods
import webMethods
import time


def populateFDP():
    ## testing if FDP server is running
    status_code = webMethods.get_fdp_status(configuration.FDP_SERVER_URL)
    while status_code != 200:
        print("Waiting for FDP command line")
        time.sleep(10)
        status_code = webMethods.get_fdp_status(configuration.FDP_SERVER_URL)

    print("FDP is online")

    #####################################################
    # Read input excel sheet to get FDP content matrix's
    #####################################################

    # Get catalog matrix from catolog sheet
    fair_catalog_matrix = xlsMethods.getCatalogMatrix(configuration.INPUT_EXCEL_FILE)

    # Get dataset matrix from dataset sheet
    fair_dataset_matrix = xlsMethods.getDatasetMatrix(configuration.INPUT_EXCEL_FILE)

    # Get distribution matrix from distribution sheet
    fair_distribution_matrix = xlsMethods.getDistributionMatrix(configuration.INPUT_EXCEL_FILE)

    #############################################################
    # Interact with FAIR Data Point API to create/update content
    #############################################################

    # Change the content of respository layer of the FAIR Data Point
    webMethods.update_repository_metadata()

    # Create catalogs in FAIR Data Point and get their URIs
    catalogURIsMatrix = webMethods.create_catalogs(fair_catalog_matrix)

    # Create datasets in FAIR Data Point and get their URIs
    datasetURIsMatrix = webMethods.create_datasets(fair_dataset_matrix, catalogURIsMatrix)

    # Create distributions in FAIR Data Point and get their URIs
    webMethods.create_distributions(fair_distribution_matrix, datasetURIsMatrix)

    print('FAIR DataPoint done !')

    ### need to see how to run web server docker
    # need to see how to retreive docker
    # swagger-ui?
    # docker-compose


if __name__ == "__main__":
    populateFDP()
