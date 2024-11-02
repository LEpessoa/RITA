import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


######## CSV IMPORTING #########
# Devices
@anvil.server.callable
def getDevices_resource():
    list = anvil.server.call("getDevices")
    return list


#   for dvc in list:
#     app_tables.iot_critical_object.add_row(id=dvc[0], name=dvc[1],acronym=dvc[2])
#   return app_tables.iot_critical_object.search();


@anvil.server.callable
def cleanDevices_resource():
    app_tables.iot_critical_object.delete_all_rows()


# Threats
@anvil.server.callable
def getThreats_resource():
    return anvil.server.call("getThreats")


#   list = anvil.server.call('getThreats')
#   for t in list:
#      app_tables.threat_type.add_row(id=t[0], iot_criticl_objects=t[1],iot_threat_id=t[2], name=t[3], description=t[4],reference=t[5],resilient_solution_ids=t[6])
#   return app_tables.iot_critical_object.search();


@anvil.server.callable
def cleanThreats_resource():
    app_tables.threat_type.delete_all_rows()


## Solutions
@anvil.server.callable
def getSolutions_resource():
    list = anvil.server.call("getResilientSolutions")
    return list


#   for t in list:
#      app_tables.resilient_solution.add_row(id=t[0],
#                                            resilient_solution_id=t[1],
#                                            name=t[2],
#                                            description=t[3],
#                                            reference=t[4])
#   return app_tables.resilient_solution.search();


@anvil.server.callable
def cleanSolutions_resource():
    app_tables.resilient_solution.delete_all_rows()


# Link Threats to Objects
@anvil.server.callable
def link_threats_to_objects():
    threats = app_tables.threat_type.search()
    for th in threats:
        listOfDevices = th["iot_criticl_objects"].split(" ")
        for dvc in listOfDevices:
            dvcRows = app_tables.iot_critical_object.search(acronym=dvc)
            if dvcRows == None:
                return f"Objeto não encontrado para acronimo {dvc}"
            for dv in dvcRows:
                if dv["threats"] == None:
                    dv["threats"] = []
                dv["threats"] += [th]


@anvil.server.callable
def clear_link_threats_to_objects():
    threats = app_tables.threat_type.search()
    for th in threats:
        th["iot_criticl_objects"] = []
