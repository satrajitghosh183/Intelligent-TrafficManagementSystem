import os
from pathlib import Path
path = Path(os.getcwd())
final_data_path=os.path.join(path,"Traffic_Management","assorted_data")
print(final_data_path)

yaml_data="train: "+final_data_path+"/images/train\n"
yaml_data+="val: "+final_data_path+"/images/val\n"
yaml_data+="test: "+final_data_path+"/images/test\n"

rest_of_yaml_data='''nc: 2
names: ['Cars',
        'Bikes',
        'Trucks',
        'Buses'       
]'''

yaml_data=yaml_data+rest_of_yaml_data
print(yaml_data)

yaml_file = open("dataDiff.yaml", "w")
n = yaml_file.write(yaml_data)
yaml_file.close()