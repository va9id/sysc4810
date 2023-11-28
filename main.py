from rbac import RBAC
import password


def add_roles_to_rbac(rbac: RBAC) -> RBAC:
    """
    Adds all the necessary roles to the RBAC.
    """
    rbac.add_role("C")  # Client
    rbac.add_role("PC")  # Premium Client
    rbac.add_role("FA")  # Financial Advisor
    rbac.add_role("FP")  # Financial Planner
    rbac.add_role("IA")  # Investment Analyst
    rbac.add_role("TS")  # Tech Support
    rbac.add_role("T")  # Teller
    rbac.add_role("CO")  # Compliance Officers
    return rbac


def add_role_capabilities(rbac: RBAC) -> RBAC:
    """
    Adds all the capabilities for each role to the RBAC.
    """
    rbac.add_capability("C", "View Account Balance")
    rbac.add_capability("C", "View Investment Portfolio")
    rbac.add_capability("C", "Contact your Financial Adviser")

    rbac.add_capability("PC", "View Account Balance")
    rbac.add_capability("PC", "View Investment Portfolio")
    rbac.add_capability("PC", "Modify Investment Portfolio")
    rbac.add_capability("PC", "Contact your Investment Analyst")
    rbac.add_capability("PC", "Contact your Financial Adviser")
    rbac.add_capability("PC", "Contact your Financial Planner")

    rbac.add_capability("FA", "View a Client's Account Balance")
    rbac.add_capability("FA", "View a Client's Investment Portfolio")
    rbac.add_capability("FA", "Modify a Client's Investment Portfolio")
    rbac.add_capability("FA", "View Private Consumer Instruments")

    rbac.add_capability("FP", "View a Client's Account Balance")
    rbac.add_capability("FP", "View a Client's Investment Portfolio")
    rbac.add_capability("FP", "Modify a Client's Investment Portfolio")
    rbac.add_capability("FP", "View Private Consumer Instruments")
    rbac.add_capability("FP", "View Money Market Instruments")

    rbac.add_capability("IA", "View a Client's Account Balance")
    rbac.add_capability("IA", "View a Client's Investment Portfolio")
    rbac.add_capability("IA", "Modify a Client's Investment Portfolio")
    rbac.add_capability("IA", "View Private Consumer Instrument")
    rbac.add_capability("IA", "View Money Market Instrument")
    rbac.add_capability("IA", "View Interest Instrument")
    rbac.add_capability("IA", "View Derivates Trading")

    rbac.add_capability("TS", "View Client's Information")
    rbac.add_capability("TS", "Request Access to Client's Account")

    rbac.add_capability("T", "View a Client's Account Balance")
    rbac.add_capability("T", "View a Client's Investment Portfolio")
    rbac.add_capability("T", "Modify a Client's Investment Portfolio")

    rbac.add_capability("CO", "View a Client's Account Balance")
    rbac.add_capability("CO", "View a Client's Investment Portfolio")
    rbac.add_capability("CO", "Modify a Client's Investment Portfolio")
    rbac.add_capability("CO", "Validate Investment Portfolio Modifications")

    return rbac


if __name__ == "__main__":
    rbac = RBAC()
    add_roles_to_rbac(rbac)
    add_role_capabilities(rbac)
    rbac.list_capabilities("FP")

    # exclusions = password.get_exclusions()
    #  # print(password.check_username_exists("vahid1"))
    # password.write_to_passwd("vahid", "fjdI*323f", "IA")
    # print(password.login("vahid", "fjdI*323f"))
