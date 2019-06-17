# Load implementations
def dummy_load_database_config(database_config):
    database_config.connection.update({'influxdb': {'host': '10.32.7.205', 'port': '33301', 'database': 'clientbook_new'}})
    database_config.connection.update({'cb_config_db': {'host': '10.32.7.205','port': 33306,'database': 'clientbook_new','user': 'cb_config_reader_grafana','pass': 'P@sswordReader'}})
    return None
def load_database_config(database_config):
    """
    ### Description:
    Parse cmd & env parameters to load following database configuration,
    * influxdb
    * archival server
    ### Parameter(s): Reference configuration object to load data
    ### Return(s): Nothing
    """
    dummy_load_database_config(database_config)
    return None
def dummy_load_environment_config(environment_config):
    return None
def load_environment_config(environment_config):
    """
    ### Description:
    Parse cmd & env parameters to load following database configuration,
    * metric_id
    * model_id
    * start_date
    * end_date
    ### Parameter(s): Reference configuration object to load data
    ### Return(s): Nothing
    """
    dummy_load_environment_config(environment_config)
    return None

# Validate implementations
def valdiate_environment_config(environment_config):
    return True
def valdiate_database_config(database_config):
    return True
def valdiate_config(config):
    error = False
    if valdiate_environment_config(config.environment) == False:
        error = True or error
    if valdiate_database_config(config.database) == False:
        error = True or error
    return not error