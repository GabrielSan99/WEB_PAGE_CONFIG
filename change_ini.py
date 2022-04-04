import configparser

cfg= configparser.ConfigParser()
cfg.read('config_test.ini')

x = cfg['general']['api_key']
print(x)

cfg['general']['api_key'] = 'nova chave'            #update value

with open('config_test.ini', 'w') as configfile:    # save
    cfg.write(configfile)