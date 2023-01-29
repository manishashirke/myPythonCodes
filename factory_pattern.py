
class sshProto():
    def __init__(self):
        pass
    def get_method(self):
        print("This is using ssh proto")

class serilProto():
    def __init__(self):
        pass
    def get_method(self):
        print("This is using serial proto")

class protoFactory():
    def get_proto(self, choice):
        if choice == "ssh":
            return sshProto()
        elif choice == "serial":
            return serilProto()
        else:
            raise Exception("Please enter valid proto")

proto = protoFactory().get_proto(input("Enter proto here : \n"))
proto.get_method()
