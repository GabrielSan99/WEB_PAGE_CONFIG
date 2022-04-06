import configparser
import requests

cfg = configparser.ConfigParser()
cfg.read('config_test.ini')

r = requests.get('http://192.168.0.14:82/get_config')
r = r.json()
print(r.json())





# cfg['general']['api_key'] = 'nova chave'            #update value

# with open('config_test.ini', 'w') as configfile:    # save changes
#     cfg.write(configfile)

# x = cfg['general']['api_key']                       #read value
# print(x)