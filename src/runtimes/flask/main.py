#################################################################################
# Eclipse Tractus-X - Asset Administration Shell Suite
#
# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the
# License for the specific language govern in permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
#################################################################################

from controllers.flask.base import app
from tractusx_sdk.dataspace.services.connector import ServiceFactory
from tractusx_sdk.dataspace.tools.utils import get_arguments
from managers.config import ConfigManager, LoggingManager
from tractusx_sdk.dataspace.managers import AuthManager
from tractusx_sdk.dataspace.services.connector import BaseConnectorProviderService


## In memory authentication manager service
auth_manager: AuthManager
connector_service: BaseConnectorProviderService

def start_connector_service():
    global connector_service, logger
    
    api_key_header = ConfigManager.get_config(
        "edc.controlplane.apikeyheader"
    )
    api_key = ConfigManager.get_config(
        "edc.controlplane.apikey"
    )
    edc_headers = {
        api_key_header: api_key,
        "Content-Type": "application/json"
    }
    edc_controlplane_hostname = ConfigManager.get_config(
            "edc.controlplane.hostname"
        )
    edc_controlplane_management_api = ConfigManager.get_config(
            "edc.controlplane.managementpath"
        )

    connector_service = ServiceFactory.get_connector_provider_service(
        dataspace_version="jupiter",
        base_url=edc_controlplane_hostname,
        dma_path=edc_controlplane_management_api,
        headers=edc_headers,
        logger=logger,
        verbose=True
    )


def start():
    ## Load in memory data storages and authentication manager
    global auth_manager, logger
    
    # Initialize the server environment and get the comand line arguments
    args = get_arguments()
    
    # Configure the logging confiuration depending on the configuration stated
    logger = LoggingManager.get_logger('staging')
    if(args.debug):
        logger = LoggingManager.get_logger('development')

    ## Start the authentication manager
    auth_manager = AuthManager()
    start_connector_service()
        
    ## Once initial checks and configurations are done here is the place where it shall be included
    logger.info("[INIT] Application Startup Initialization Completed!")
    # Start the flask application     
    app.run(host=args.host, port=args.port, debug=args.debug)
    print("\nClosing the application... Thank you for using the Asset Administration Shell Suite!")
