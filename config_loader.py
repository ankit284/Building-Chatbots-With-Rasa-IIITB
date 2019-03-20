import json
config_file='./chatbot_config.json'

def validate_config(config_key):
    with open(config_file,'r') as json_file:
        json_config=json.load(json_file)
        if isinstance(json_config[config_key], dict):
            for k in json_config[config_key].keys():
                if json_config[config_key][k]=="":
                    return ("ERROR: Missing configuration value {}->{} ".format(config_key,k))
        else:
            if json_config[config_key]=="":
                return ("ERROR: Missing configuration value {} ".format(config_key))
    return json_config[config_key]

def get_zomato_config():
    return validate_config('zomato')

def get_slack_config():
    return validate_config('slack')

def validate_application_config():
    validation_status=True
    msg=validate_config('zomato')
    if str(msg).find('ERROR')!=-1:
        validation_status=False
    else:
        msg=validate_config('slack')
        if str(msg).find('ERROR')!=-1:
            validation_status=False
    return (validation_status, msg)

if __name__=='__main__':
    validate_application_config()