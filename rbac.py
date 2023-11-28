class RBAC:
    def __init__(self):
        self.__roles = []
        self.__capabilities = {}

    def add_role(self, role: str):
        if role not in self.__roles:
            self.__roles.append(role)
            self.__capabilities[role] = set()

    def add_capability(self, role: str, capability: str):
        if role in self.__roles:
            self.__capabilities[role].add(capability)

    def list_capabilities(self, role: str):
        if role in self.__roles:
            print("Your capabilites include: ")
            capabilities = self.__capabilities[role]
            for capability in capabilities:
                print(capability)
