connection_influxdb = {'host': 'influxdb', 'port': '8086', 'database': 'clientbook_new'}
connection_mysql_empty = {'host': '', 'port': '', 'database': '', 'user': '', 'pass': ''}
connection_mysql_cb_config_db = {'host': 'mysql','port': 3306,'database': 'clientbook_new','user': 'cb_config_reader_grafana','pass': 'P@sswordReader'}
connection_mysql_ai = {'host': '10.32.7.205', 'port': 3307, 'database': 'smexplorer', 'user': 'clientbook_app', 'pass': 'lct#2692@'}
connection_mysql_archival = {'host': '10.32.7.203', 'port': 3307, 'database': 'dgssatmap', 'user': 'clientbook_app', 'pass': 'lct#2692@'}

connection = {
    'influxdb' : connection_influxdb,
    'mysql_ai': connection_mysql_ai,
    'mysql_archival': connection_mysql_archival,
    'cb_config_db': connection_mysql_cb_config_db,
    'empty': connection_mysql_empty
}