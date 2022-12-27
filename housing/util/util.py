import yaml

def read_yaml_file(file_path)->dict:
   
    try:
        yaml_file=open(file_path, 'rb')
        return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e
