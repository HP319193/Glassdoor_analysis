import json
from utils import get_similar_words
import pandas as pd

################
#### convert standard to the list of similar words

# with open('dashboard/standard.json', 'r') as file:
#     standard_data = json.load(file)

# sim_words = {}
# for key, value in standard_data.items():
#     sim_words[key] = []
    
#     pos_value = value[0][0]
#     neg_value = value[1][0]

#     pos_data = [(pos_value, 1)]
#     neg_data = [(neg_value, 1)]

#     pos_data.extend(get_similar_words(pos_value, 0.6))
#     neg_data.extend(get_similar_words(neg_value, 0.6))    

#     sim_words[key].append(pos_data)
#     sim_words[key].append(neg_data)

# with open('dashboard/sim_words.json', 'w') as file:
#     json.dump(sim_words, file, indent=4)

##################
##### Prepare data for transcripts.csv

# reviews = pd.read_csv("dashboard/transcripts.csv")

# with open('dashboard/common_isin.json', 'r') as file:
#     common_isins = json.load(file)

# res_data = {}
# res_dim = {}

# for index, row in reviews.iterrows():
#     isin = row['ISIN']

#     if isin in common_isins:
#         content = row['content']

#         if isin not in res_data:
#             res_data[isin] = {}
        
#         with open('dashboard/sim_words.json', 'r') as file:
#             sim_words = json.load(file)

#         sum = 0

#         for key, value in sim_words.items():
#             if key not in res_dim:
#                 res_dim[key] = 0
            
#             if key not in res_data[isin]:
#                 res_data[isin][key] = 0

#             pos_words = value[0]
#             neg_words = value[1]

#             for pos_word in pos_words:
#                 count = content.count(pos_word[0])
#                 sum = sum + count * pos_word[1]
            
#             for neg_word in neg_words:
#                 count = content.count(neg_word[0])
#                 sum = sum - count * neg_word[1]
            
#             res_dim[key] = res_dim[key] + sum
#             res_data[isin][key] = res_data[isin][key] + sum

# with open('dashboard/2_call_data.json', 'w') as json_file:
#     json.dump(res_data, json_file, indent=4)

# with open('dashboard/2_call_dim.json', 'w') as json_file:
#     json.dump(res_dim, json_file, indent=4)

##################
##### Prepare data for reviews.csv

# reviews = pd.read_csv("dashboard/reviews.csv")

# res_data = {}
# res_dim = {}

# with open('dashboard/common_isin.json', 'r') as file:
#     common_isins = json.load(file)

# for index, row in reviews.iterrows():
#     isin = row['ISIN']
#     if isin in common_isins:
#         content = f"{row['pros']} {row['cons']}"

#         if isin not in res_data:
#             res_data[isin] = {}
        
#         with open('dashboard/sim_words.json', 'r') as file:
#             sim_words = json.load(file)

#         sum = 0

#         for key, value in sim_words.items():
#             if key not in res_dim:
#                 res_dim[key] = 0
            
#             if key not in res_data[isin]:
#                 res_data[isin][key] = 0

#             pos_words = value[0]
#             neg_words = value[1]

#             for pos_word in pos_words:
#                 count = content.count(pos_word[0])
#                 sum = sum + count * pos_word[1]
            
#             for neg_word in neg_words:
#                 count = content.count(neg_word[0])
#                 sum = sum - count * neg_word[1]
            
#             res_dim[key] = res_dim[key] + sum
#             res_data[isin][key] = res_data[isin][key] + sum

# with open('dashboard/2_glassdoor_data.json', 'w') as json_file:
#     json.dump(res_data, json_file, indent=4)

# with open('dashboard/2_glassdoor_dim.json', 'w') as json_file:
#     json.dump(res_dim, json_file, indent=4)