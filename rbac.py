class RBAC:
    def __init__(self):
        self.__roles = []
        self.__capabilities = {}

    def add_role(self, role: str) -> None:
        if role not in self.__roles:
            self.__roles.append(role)
            self.__capabilities[role] = set()

    def add_capability(self, role: str, capability: str) -> None:
        if role in self.__roles:
            self.__capabilities[role].add(capability)

    def list_capabilities(self, role: str) -> None:
        if role in self.__roles:
            print("\nYour capabilites include: ")
            capabilities = self.__capabilities[role]
            for capability in capabilities:
                print(f"\t{capability}")
