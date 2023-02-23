import pickle

class device_info:
    def __init__(self, device_name, device_ip, device_sr_no):
        self.device_name = device_name
        self.device_ip = device_ip
        self.device_sr_no = device_sr_no

    def get_device_info(self):
        print(f"Device name is: {self.device_name}")
        print(f"Device ip address is : {self.device_ip}")
        print(f"Device serial number is : {self.device_sr_no}")

"""device_obj = device_info("QNX", "192.168.92.42", 35)

#Pickling device object to file
with open('device_info_qnx.pickle', 'wb') as f:
    pickle.dump(device_obj, f)"""

#Unpickling device object from file
with open('device_info_qnx.pickle', 'rb') as f:
    p1 = pickle.load(f)
p1.get_device_info()

