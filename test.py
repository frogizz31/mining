import requests
import GPUtil
from datetime import datetime
import discord
import message_discord


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
	
	if gpu_name == "NVIDIA GeForce RTX 3070":
		eth = get_dict_mining_info("ETH",62,135,1100,2600,135)
		etc = get_dict_mining_info("ETC",62,135,1100,2600,135)
		rvn = get_dict_mining_info("RVN",30.5,150,0,2100,150)
		flux = get_dict_mining_info("FLX",56.5,150,200,0,150)
		firo = get_dict_mining_info("FIR",30,150,100,2000,150)
		btg = get_dict_mining_info("BTG",110,200,150,0,200)
		ae = get_dict_mining_info("AE",10,140,1470,1600,140)
		aion = get_dict_mining_info("AION",405,180,125,500,180)
		beam = get_dict_mining_info("BEAM",30,140,0,0,140)
		vtc = get_dict_mining_info("VTC",1.23,130,1600,2100,135)
		exp = get_dict_mining_info("EXP",62,135,1100,2600,135)
		ubq = get_dict_mining_info("UBQ",62,135,1100,2600,135)
		ethw = get_dict_mining_info("ETHW",62,135,1100,2600,135)


	if gpu_name == "NVIDIA GeForce RTX 3080":
		eth = get_dict_mining_info("ETH",100,240,1200,2600,240)
		etc = get_dict_mining_info("ETC",100,240,1200,2600,240)
		rvn = get_dict_mining_info("RVN",42,250,0,2200,250)
		flux = get_dict_mining_info("FLX",81.5,255,150,0,255)
		firo = get_dict_mining_info("FIR",43.5,255,100,2000,255)
		btg = get_dict_mining_info("BTG",167,340,150,0,350)
		ae = get_dict_mining_info("AE",11.7,270,1560,2200,270)
		aion = get_dict_mining_info("AION",536,300,125,500,300)
		beam = get_dict_mining_info("BEAM",42.5,230,0,0,230)
		vtc = get_dict_mining_info("VTC",1.5,180,1600,2100,240)
		exp = get_dict_mining_info("EXP",100,240,1200,2600,240)
		ubq = get_dict_mining_info("UBQ",100,240,1200,2600,240)
		ethw = get_dict_mining_info("ETHW",100,240,1200,2600,240)

	
	list_gpus_mining_info = [rvn,flux,etc,firo,btg,ae,aion,beam,vtc,exp,ubq,ethw]

	return(list_gpus_mining_info)


def define_dict_mining_info_currency(currency,hashrate,conso):
	dict_mining_info_currency = { "currency" : currency,
								   "hashrate" : hashrate,
								   "conso" : conso
								}
	return(dict_mining_info_currency)

def get_mining_info(list_gpus_mining_info):
	
	dict_rvn_mining_info = define_dict_mining_info_currency("RVN",0,0)
	dict_flx_mining_info = define_dict_mining_info_currency("FLX",0,0)
	dict_etc_mining_info = define_dict_mining_info_currency("ETC",0,0)
	dict_fir_mining_info = define_dict_mining_info_currency("FIR",0,0)
	dict_btg_mining_info = define_dict_mining_info_currency("BTG",0,0)
	dict_ae_mining_info = define_dict_mining_info_currency("AE",0,0)
	dict_aion_mining_info = define_dict_mining_info_currency("AION",0,0)
	dict_beam_mining_info = define_dict_mining_info_currency("BEAM",0,0)
	dict_vtc_mining_info = define_dict_mining_info_currency("VTC",0,0)
	dict_exp_mining_info = define_dict_mining_info_currency("EXP",0,0)
	dict_ubq_mining_info = define_dict_mining_info_currency("UBQ",0,0)
	dict_ethw_mining_info = define_dict_mining_info_currency("ETHW",0,0)
	for gpu in list_gpus_mining_info:
		for settings in gpu:
			if settings["currency"] == "RVN":
				dict_rvn_mining_info["hashrate"]+=settings["hashrate"]
				dict_rvn_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "FLX":
				dict_flx_mining_info["hashrate"]+=settings["hashrate"]
				dict_flx_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "ETC":
				dict_etc_mining_info["hashrate"]+=settings["hashrate"]
				dict_etc_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "FIR":
				dict_fir_mining_info["hashrate"]+=settings["hashrate"]
				dict_fir_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "BTG":
				dict_btg_mining_info["hashrate"]+=settings["hashrate"]
				dict_btg_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "AE":
				dict_ae_mining_info["hashrate"]+=settings["hashrate"]
				dict_ae_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "AION":
				dict_aion_mining_info["hashrate"]+=settings["hashrate"]
				dict_aion_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "BEAM":
				dict_beam_mining_info["hashrate"]+=settings["hashrate"]
				dict_beam_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "VTC":
				dict_vtc_mining_info["hashrate"]+=settings["hashrate"]
				dict_vtc_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "EXP":
				dict_exp_mining_info["hashrate"]+=settings["hashrate"]
				dict_exp_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "UBQ":
				dict_ubq_mining_info["hashrate"]+=settings["hashrate"]
				dict_ubq_mining_info["conso"]+=settings["conso"]
			if settings["currency"] == "ETHW":
				dict_ethw_mining_info["hashrate"]+=settings["hashrate"]
				dict_ethw_mining_info["conso"]+=settings["conso"]

	list_mining_info = [dict_rvn_mining_info,dict_flx_mining_info,dict_etc_mining_info,dict_fir_mining_info,dict_btg_mining_info,dict_ae_mining_info,dict_aion_mining_info,dict_beam_mining_info,dict_vtc_mining_info,dict_exp_mining_info,dict_ubq_mining_info,dict_ethw_mining_info]
	return(list_mining_info)


def get_info_whattomine(list_mining_info):
	
	whattomine_coin = { 
						"RVN" : "234",
						"FLX" : "287",
						"ETC" : "162",
						"FIR" : "175",
						"BTG" : "214",
						"AE" : "297",
						"AION" : "272",
						"BEAM" : "294",
						"VTC" : "5",
						"EXP" : "154",
						"UBQ" : "173",
						"ETHW" : "353",
					  }

	objectif_vente = { 
						"RVN" : 0.23515,
						"FLX" : 3.15,
						"ETC" : 100,
						"FIR" : 18,
						"BTG" : 130,
						"AE" : 0.5516,
						"AION" : 0.5374,
						"BEAM" : 1.93,
						"VTC" : 1.64,
						"EXP" : 0.16,
						"UBQ" : 0.577,
						"ETHW" : 60,

					  }

	list_rentabilite = []

	for settings in list_mining_info:
		
		request = "https://whattomine.com/coins/"
		request += whattomine_coin[settings["currency"]]
		request += ".json?hr="
		request += str(settings["hashrate"])
		request += "&p="
		request += str(settings["conso"])
		request += "&cost=0.22&cost_currency=USD&hcost=0.0&span_br=1h&span_d=1h"
		rep = requests.get(request)
		rep = rep.json()
		quantite = float(rep['estimated_rewards'])
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
		
		list_rentabilite.append(dict_rentabilite)

	return(list_rentabilite)

		

def write_test(list_rentabilite):
	
	rentabilite_eth = 16

	text="\n"
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M")
	text += dt_string + "\n\nRentabilite\n\n" 
	for ligne in list_rentabilite:
		text += ligne["currency"]+" à "+str(ligne["objectif_vente"])+" : " + str(ligne["rentabilite"])+"\n"
		
		# if ligne["currency"] == "ETH":
			# rentabilite_eth = ligne["rentabilite"]
			
	text+="\nObjectif de vente pour rentabilite ETH au sommet\n\n"
	
	for ligne in list_rentabilite:
		objectif_vente_sur = (rentabilite_eth + ligne["cost"])  / ligne["quantite"]
		text += ligne["currency"]+" : " + str(objectif_vente_sur)+"\n"
			
	text+="\n"
	# f = open("/home/user/script/test.txt", "a")
	# f.write(text)
	# f.close()
	return(text)
	


list_gpus = get_gpu_info()
list_gpus_mining_info = []
for gpu in list_gpus:
	mining_info = get_gpu_mining_info(gpu["name"])
	list_gpus_mining_info.append(mining_info)
list_mining_info = get_mining_info(list_gpus_mining_info)
list_rentabilite = get_info_whattomine(list_mining_info)
text=write_test(list_rentabilite)
print(text)

client = message_discord.init_client()

async def on_ready(client,text):
        channel = client.get_channel(1019167836071022594)
        await channel.send(text)
        await client.close()

message_discord.run_client(client)

