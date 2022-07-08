import requests
import GPUtil
from datetime import datetime

def get_gpu_info():
	gpus = GPUtil.getGPUs()
	list_gpus = []
	for gpu in gpus:
		info = {"id": gpu.id,
				"name": gpu.name}
		list_gpus.append(info)
	return(list_gpus)

def get_dict_mining_info(currency,hashrate,conso,core,mem,power):
	dict_mining_info = { "currency" : currency,
						  "hashrate": hashrate,
						  "conso": conso,
						  "core": core,
						  "mem": mem,
						  "power": power
						}
	return (dict_mining_info)

def get_gpu_mining_info(gpu_name):
	
	list_gpus_mining_info = []
	if gpu_name == "NVIDIA GeForce RTX 3070":
		eth = get_dict_mining_info("ETH",62,135,1100,2600,135)
		etc = get_dict_mining_info("ETC",62,135,1100,2600,135)
		rvn = get_dict_mining_info("RVN",30.5,150,0,2100,150)
		flux = get_dict_mining_info("FLX",56.5,150,200,0,150)


	if gpu_name == "NVIDIA GeForce RTX 3080":
		eth = get_dict_mining_info("ETH",100,240,1200,2600,240)
		etc = get_dict_mining_info("ETC",100,240,1200,2600,240)
		rvn = get_dict_mining_info("RVN",42,250,0,2200,250)
		flux = get_dict_mining_info("FLX",81.5,255,150,0,255)

	list_gpus_mining_info.append(eth)
	list_gpus_mining_info.append(rvn)
	list_gpus_mining_info.append(flux)
	list_gpus_mining_info.append(etc)


	return(list_gpus_mining_info)


def define_dict_mining_info_currency(currency,hashrate,conso):
	dict_mining_info_currency = { "currency" : currency,
								   "hashrate" : hashrate,
								   "conso" : conso
								}
	return(dict_mining_info_currency)

def get_mining_info(list_gpus_mining_info):

	dict_eth_mining_info = define_dict_mining_info_currency("ETH",0,0)
	dict_rvn_mining_info = define_dict_mining_info_currency("RVN",0,0)
	dict_flx_mining_info = define_dict_mining_info_currency("FLX",0,0)
	dict_etc_mining_info = define_dict_mining_info_currency("ETC",0,0)
	for gpu in list_gpus_mining_info:
		for settings in gpu:
			if settings["currency"] == "ETH":
				dict_eth_mining_info["hashrate"]+=settings["hashrate"]
				dict_eth_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "RVN":
				dict_rvn_mining_info["hashrate"]+=settings["hashrate"]
				dict_rvn_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "FLX":
				dict_flx_mining_info["hashrate"]+=settings["hashrate"]
				dict_flx_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "ETC":
				dict_etc_mining_info["hashrate"]+=settings["hashrate"]
				dict_etc_mining_info["conso"]+=settings["conso"]

	list_mining_info = [dict_eth_mining_info,dict_rvn_mining_info,dict_flx_mining_info,dict_etc_mining_info]
	return(list_mining_info)


def get_info_whattomine(list_mining_info):
	
	whattomine_coin = { "ETH" : "151",
						"RVN" : "234",
						"FLX" : "287",
						"ETC" : "162",
					  }

	objectif_vente = { "ETH" : 4000,
						"RVN" : 0.23515,
						"FLX" : 3.15,
						"ETC" : 100,
					  }

	list_rentabilite = []

	for settings in list_mining_info:
		
		request = "https://whattomine.com/coins/"
		request += whattomine_coin[settings["currency"]]
		request += ".json?hr="
		request += str(settings["hashrate"])
		request += "&p="
		request += str(settings["conso"])
		request += "&fee=0.0&cost=0.22&cost_currency=USD&hcost=0.0&span_br=1h&span_d=1h"
		rep = requests.get(request)
		rep = rep.json()
		quantite = float(rep['estimated_rewards'])
		print(quantite)
		objectif = objectif_vente[settings["currency"]]
		cost = float(rep["cost"].replace("$",""))
		rentabilite = round(quantite*objectif-cost,2)
		
		dict_rentabilite = {
			"currency" : settings["currency"],
			"quantite" : quantite,
			"objectif_vente" : objectif_vente[settings["currency"]],
			"cost" : cost,
			"rentabilite" : rentabilite
		}
		
		print(settings["currency"] + "  Rentabilite a " , objectif , " : " , rentabilite)

		list_rentabilite.append(dict_rentabilite)

	return(list_rentabilite)

		

def write_test(list_rentabilite):
	
	rentabilite_eth = 0

	text="\n"
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M")
	text += dt_string + "\nRentabilite\n" 
	for ligne in list_rentabilite:
		text += ligne["currency"]+"," + str(ligne["rentabilite"])+"\n"
		
		if ligne["currency"] == "ETH":
			rentabilite_eth = ligne["rentabilite"]
			
	text+="Objectif de vente pour rentabilite ETH a 4000\n"
	
	for ligne in list_rentabilite:
		objectif_vente_sur = (rentabilite_eth + ligne["cost"])  / ligne["quantite"]
		text += ligne["currency"]+"," + str(objectif_vente_sur)+"\n"
			
	text+="\n"
	f = open("/home/user/script/test.txt", "a")
	f.write(text)
	f.close()

#write_test()
list_gpus = get_gpu_info()
list_gpus_mining_info = []
for gpu in list_gpus:
	mining_info = get_gpu_mining_info(gpu["name"])
	list_gpus_mining_info.append(mining_info)
list_mining_info = get_mining_info(list_gpus_mining_info)
list_rentabilite = get_info_whattomine(list_mining_info)
write_test(list_rentabilite)
