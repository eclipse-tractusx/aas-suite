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

import logging
import urllib3
urllib3.disable_warnings()
logging.captureWarnings(True)

from managers.config.log_manager import LoggingManager
from managers.config.config_manager import ConfigManager

from runtimes.flask.main import start

# Initialize the logging system based on project configuration
LoggingManager.init_logging()

# Load application-specific configuration settings
ConfigManager.load_config()

"""
Currently only one connector is supported from consumer/provider side.
"""

if __name__ == "__main__":
    print("\nEclipse Tractus-X Asset Administration Suite\n")
    print(r"""
        ___   ___   ____  ______  ________________
       / _ | / _ | / __/ / __/ / / /  _/_  __/ __/
      / __ |/ __ |_\ \  _\ \/ /_/ // /  / / / _/  
     /_/ |_/_/ |_/___/ /___/\____/___/ /_/ /___/  
    """)
    print("\n\n\t\t\t\t\t\t\t\t\t\tv0.0.1")
    print("Application starting, listening to requests...\n")
    
    start()

    print("\nClosing the application... Thank you for using the Eclipse Tractus-X Asset Administration Shell Suite!")
