import csv
import requests
import time

nameOrg = [None]*100
id_org = [None] * 100
token =  [None] * 100

orgname = [None]*100
orgnum_accept_badges = [0]*100
orgnum_pendin_badges = [0]*100
orgnum_reject_badges = [0]*100

i=0

print("Iniciando programa ...")
time.sleep(0.5)
print("--------------------------------------------------------")
print("GENERADOR DE INFORMES AUTOMATIZADOS DE YOURACCLAIM V.0.1")
print("--------------------------------------------------------")

print("/////////////////////////////////////////////////////////")
print("/////////////////////////////////////////////////////////")
print("POR: ACREDITTA --- COLOMBIA")

print("--------------------------------------------------------")
print("DESARROLLADO POR ING. GABRIEL GALINDO")
print("--------------------------------------------------------")

print("version 0.1 -- Agosto 2020")
print("/////////////////////////////////////////////////////////")
print("/////////////////////////////////////////////////////////")

print("cargando informacion proporcionada en el csv")
print("--------------------------------------------------------")



def lectura_Acclaim(acclaim_token,idOrg):
  next_page = True
  resp_array = [0, 0, 0]
  req_url = 'https://api.youracclaim.com/v1/organizations/'+idOrg+'/high_volume_issued_badge_search'
  
  while next_page:
      
      print("Haciendo peticion al url -- "+req_url)
      r = requests.get(req_url, auth=(acclaim_token, ''))
      status_code = r.status_code
      resp_json = r.json()
      data1 = resp_json["data"]
      longitud_resp_data1 = len(data1)

      for i in range(0,longitud_resp_data1):
          badge1 = data1[i]
          if badge1["state"] == "accepted":
              resp_array[0] += 1
          if badge1["state"] == "pending":
              resp_array[1] += 1
          if badge1["state"] == "rejected":
              resp_array[2] += 1

      metada1 = resp_json["metadata"]
      if metada1["next_page_url"] is None:
          next_page = False
      else:
          req_url = metada1["next_page_url"]

  return resp_array



      
  
  
  
  


with open('prueba_formato3.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        id_org[i] = line[1]
        token[i] = line[2]
        nameOrg[i] = line[0]
        i+=1

c = 0

print("Se han detectado "+str(i-1)+" organizaciones en la hoja CSV ")
time.sleep(2)



for c in range(i):

  if c !=0:
    print("--------------------------------------------------------")
    time.sleep(0.25)
    print("Se esta cargando el proceso para la organizacion #"+str(c))
    print(nameOrg[c])
    respuesta = lectura_Acclaim(token[c],id_org[c])
    orgname[c] = nameOrg[c]
    orgnum_accept_badges[c] = respuesta[0]
    orgnum_pendin_badges[c] = respuesta[1]
    orgnum_reject_badges[c] = respuesta[2]



    
print("--------------------------------------------------------")
print("Generando informe: Espere un momento")
time.sleep(5)
    
with open ('informe.csv','w') as f:
    writer = csv.DictWriter(f, fieldnames=["Organizacion", "Accept","Pending","Rejected", "Total_Emitidas"])
    writer.writeheader()
    c=0
    for c in range(i):
      if c!=0:
        total = orgnum_accept_badges[c] + orgnum_pendin_badges[c] + orgnum_reject_badges[c]
        writer.writerow({'Organizacion':orgname[c],'Accept': orgnum_accept_badges[c], 'Pending':orgnum_pendin_badges[c], 'Rejected':orgnum_reject_badges[c],'Total_Emitidas':total})
    f.close()

print("--------------------------------------------------------")
print("informe generado satisfactoriamente")
    
    
