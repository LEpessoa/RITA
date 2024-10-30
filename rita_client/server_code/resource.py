# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
import anvil.server

import mysql.connector
import spacy

mydb = mysql.connector.connect(
    # host="addm4riota_db_2.0",
    host="localhost",    
    user="root",
    password="addm4riota",
    database="ADDM4RIOTA",
    # port=3306,
    port=3336
)

MODEL_PATH = "./model-best"
mycursor = mydb.cursor()

######## CSV IMPORTING #########

# @anvil.server.callable
# def cleanDevices_resource():
#   app_tables.iot_critical_object.delete_all_rows()

# Threats
@anvil.server.callable
def getThreats_resource():
  # return anvil.server.call('getThreats')
  mycursor.execute("SELECT * FROM threat_type")
  return mycursor.fetchall()

# @anvil.server.callable
# def cleanThreats_resource():
#   app_tables.threat_type.delete_all_rows()
  
## Solutions
@anvil.server.callable
def getSolutions_resource():
  # list = anvil.server.call('getResilientSolutions')
    mycursor.execute("SELECT * FROM resilient_solution")
    return [
        {
            "id": obj[0],
            "resilient_solution_id": obj[1],
            "name": obj[2],
            "description": obj[3],
        }
        for obj in mycursor.fetchall()
    ]

# @anvil.server.callable
# def cleanSolutions_resource():
#   app_tables.resilient_solution.delete_all_rows()
  
#Link Threats to Objects
@anvil.server.callable
def link_threats_to_objects():
  threats = app_tables.threat_type.search()
  for th in threats:
    listOfDevices = th['iot_criticl_objects'].split(' ')
    for dvc in listOfDevices:
      dvcRows = app_tables.iot_critical_object.search(acronym=dvc)
      if dvcRows == None:
        return f"Objeto não encontrado para acronimo {dvc}"
      for dv in dvcRows:
        if dv['threats'] == None:
          dv['threats'] = []
        dv['threats'] += [th]
      
      
# @anvil.server.callable
# def clear_link_threats_to_objects():
#   threats = app_tables.threat_type.search()
#   for th in threats:
#     th['iot_criticl_objects'] = []

nlp = spacy.load(MODEL_PATH)
 
# CHECK FROM HERE DOWN

def separateText(text):
    text_separate_dot = str.split(text, ".")
    final_separated_phrases = []
    for phrase in text_separate_dot:
        sep_comma = str.split(phrase, ",")
        for txt in sep_comma:
            final_separated_phrases.append(txt)
    print(f"Count of phrases found: {len(final_separated_phrases)}")
    return final_separated_phrases


@anvil.server.callable
def getDevices_resource():
    mycursor.execute("SELECT * FROM iot_critical_object")
    return mycursor.fetchall()


@anvil.server.callable
def getThreats_resource():
    mycursor.execute("SELECT * FROM threat_type")
    return mycursor.fetchall()


@anvil.server.callable
def getSolutions_resource():
    mycursor.execute("SELECT * FROM resilient_solution")
    return [
        {
            "id": obj[0],
            "resilient_solution_id": obj[1],
            "name": obj[2],
            "description": obj[3],
        }
        for obj in mycursor.fetchall()
    ]


@anvil.server.callable
def getAllThreatTypes():
    mycursor.execute("select * from threat_type_enum")
    return mycursor.fetchall()


@anvil.server.callable
def getAllSolutionTypes():
    mycursor.execute("select * from resilient_solution_enum")
    return mycursor.fetchall()


@anvil.server.callable
def getAllIoTObjectsDropdown():
    mycursor.execute("select * from iot_critical_object")
    return [(obj[1] + " - (" + obj[2] + ")", obj[2]) for obj in mycursor.fetchall()]


@anvil.server.callable
def getAllThreatTypesDropdown():
    mycursor.execute("select * from threat_type_enum")
    return [(obj[1] + " - (" + obj[2] + ")", obj[2]) for obj in mycursor.fetchall()]


@anvil.server.callable
def getAllSolutionTypesDropdown():
    mycursor.execute("select * from resilient_solution_enum")
    return [(obj[1] + " - (" + obj[2] + ")", obj[2]) for obj in mycursor.fetchall()]


@anvil.server.callable
def filterSolutions(solutionDTO):
    # solutionDTO has the format below, the values between quotes should be replaced by the wanted values, or None.
    # ("id", "resilient_solution_id", 'name', 'description', 'references', 'resilient_solution_enum', 'TT_id')
    print("Solution DTO")
    print(solutionDTO)
    query = """select rs.*
            from (ADDM4RIOTA.resilient_solution_enum rse inner join ADDM4RIOTA.resilient_solution rs
            on rse.id = rs.resilient_solution_enum )
            inner join
            ADDM4RIOTA.BRIDGE_resilient_solution_threat_type rstt
            on rstt.RESSOL_id = rs.resilient_solution_id            
            where
            cast(rs.id as CHAR) like ifnull(%s,'%') AND
            ( (isnull(%s) = 1) OR rse.acronym like %s) AND
            rs.name like ifnull(%s,'%') AND
            rs.description like CONCAT('%',ifnull(%s,''),'%') AND
            rs.references like CONCAT('%',ifnull(%s,''),'%') AND
            rs.resilient_solution_enum like CONCAT('%',ifnull(%s,''),'%') AND
            rstt.TT_id like CONCAT('%',ifnull(%s,''),'%')
            group by rs.resilient_solution_id;"""
    # Repeat resilient_solution_id parameter in the list
    resilient_solution_id = solutionDTO[1]
    solutionDTO.insert(1, resilient_solution_id)

    # Run the query
    mycursor.execute(query, solutionDTO)
    print(mycursor.statement)
    return [
        {
            "id": obj[0],
            "resilient_solution_id": obj[1],
            "name": obj[2],
            "description": obj[3],
        }
        for obj in mycursor.fetchall()
    ]


@anvil.server.callable
def filterIoTObjects(iotObjectsDTO):
    # solutionDTO has the format below, the values between quotes should be replaced by the wanted values, or None.
    # ("id", 'name', 'acronym')
    query = """select rs.* from (ADDM4RIOTA.threat_type_enum B inner join ADDM4RIOTA.resilient_solution rs
            on B.id = rs.resilient_solution_enum ) where
            cast(rs.id as CHAR) like ifnull(%s,'%') AND
            cast(rs.resilient_solution_id as char) like ifnull(%s,'%') AND
            rs.name like ifnull(%s,'%') AND
            rs.description like ifnull(%s,'%') AND
            rs.references like ifnull(%s,'%') AND
            rs.resilient_solution_enum like ifnull(%s,'%') AND
            B.acronym like ifnull(%s,'%');"""
    mycursor.execute(query, iotObjectsDTO)
    print(mycursor.statement)
    return [
        {
            "id": obj[0],
            "resilient_solution_id": obj[1],
            "name": obj[2],
            "description": obj[3],
        }
        for obj in mycursor.fetchall()
    ]


@anvil.server.callable
def filterThreatTypes(threatTypeDTO):
    print("Filter Threat types called!")
    print(f"Showing threat typeDTO")
    print(threatTypeDTO)
    print("FIN")
    query = """select tt.* from ADDM4RIOTA.threat_type tt
                WHERE tt.IoTCriticalObjects like CONCAT('%',ifnull(%s, ''),'%')
                AND tt.iot_threat_id like CONCAT('%',ifnull(%s,''),'%')
                AND (
                    tt.name like CONCAT('%',ifnull(%s,''),'%')
                    OR tt.description like CONCAT('%',ifnull(%s,''),'%')
                    OR tt.ResilientSolutionIds like CONCAT('%',ifnull(%s,''),'%')
                );"""
    print(f"Showing query:\n{query}")
    mycursor.execute(query, threatTypeDTO)
    print(mycursor.statement)
    return mycursor.fetchall()

@anvil.server.callable
def findIco(stringInputText):
    print(f"Received text: {stringInputText}")
    if stringInputText == "":
        print("Received empty string")

    query = """select ico.* from iot_critical_object ico where ico.name like %s"""
    reply = []

    #####
    for sep_phrase in separateText(stringInputText.lower()):
        doc = nlp(sep_phrase)
        for ent in doc.ents:
            print(f"Found entity {ent.text}")
            print(f"{ent.text:<20}    {ent.label_:<20}")
            mycursor.execute(query, [ent.label_])
            ico_list = [
                {
                    "id": obj[0],
                    "name": ent.label_,
                    "acronym": obj[2],
                    "quantity": 1,
                    "threats": [],
                    "textReference": ent.text,
                }
                for obj in mycursor.fetchall()
            ]
            reply.extend(ico_list)
    print(f"Showing reply: {reply}")
    return reply

@anvil.server.callable
def create_pdf():
    # pdf = anvil.pdf.render_form("pdf_page")
    pdf = anvil.media.from_file("./pdf_generated.pdf")
    return pdf
