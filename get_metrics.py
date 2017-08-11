# > curl -i https://controltower.ea.com/api/v1/breaches > breach_api.txt
# replace true -> True, false -> False

import collections

with open("breach_api.txt", 'r') as input:

	source = input.readlines()[16]
	source_list = eval(source)

	metric_dict = collections.defaultdict(list)
	for d in source_list:
		metric_dict[d["metric_name"]].append(d)

	print(metric_dict.keys())

# conclusion:
## the metrics used by control tower so far are:
## ['AWS_USERS_CURRENTLY_CONNECTED', 'PSU']

# reference:
## https://apis.controltower.ea.com/apidocs/, BREACHES:
## breaches metrics: {PSU, LATENCY, TPM, OUTAGES, CRASHES, EPM_INTERNAL_SERVER_ERROR, EPM_400, CE ...}



