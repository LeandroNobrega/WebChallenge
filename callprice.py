# Biblioteca para cálculo das ligações

def callprice(region1, region2, plan, duration):
	pricetable = {'11-16':1.9,'16-11':2.9,'11-17':1.7,'17-11':2.7,'11-18':0.9,'18-11':1.9}
	if (region1 + "-" + region2 in pricetable): roaming = pricetable[region1 + "-" + region2]
	else: return '-','-'
	if plan == "FaleMais30":
		if duration > 30: return roaming*(duration-30)*1.1, roaming*duration
		else: return 0, roaming*duration
	elif plan == "FaleMais60":
		if duration > 60: return roaming*(duration-60)*1.1, roaming*duration
		else: return 0, roaming*duration
	elif plan == "FaleMais120":
		if duration > 120: return roaming*(duration-120)*1.1, roaming*duration
		else: return 0, roaming*duration

