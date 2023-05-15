
import ifcjson

jsonFilePath = './PN1206-1_05_EXE_BIM_007190_1_0704P_IGC_EVO1.json'
ifcFilePath = 'output.ifc'
ifc_json = ifcjson.JSON2IFC(jsonFilePath)
ifc_model = ifc_json.ifcModel()
ifc_model.write("evo1" + '_roundtrip.ifc')
