import common.utilities as utility
import config.database
import config.environment
import config.execute

import common.input_parser as IParser
import common.output_parser as OParser

print(dir())


# Main Work flow
# Parse Input (load database, environment config)
print('Loading database configurations')
IParser.load_database_config(config.database)
print('Loading environment configurations')
IParser.load_environment_config(config.environment)
# Validate Input
print('Validating Configurations')
IParser.valdiate_config(config)
# Override Transform file
utility.override_transformer(config.execute.parameter['metric_script'])
# Load Transform File
from common.transform import *
# Execute Transform file
# Validate Output
# Save Output