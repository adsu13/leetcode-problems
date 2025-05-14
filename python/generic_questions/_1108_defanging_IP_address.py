import re
class Solution:
    @staticmethod
    def isIPv4(address: str) -> bool:
        ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})$'
        return bool(re.match(ipv4_pattern, address))

    @staticmethod
    def defangIPaddr(address: str) -> str:
        if Solution.isIPv4(address):
            return address.replace(".", "[.]")
        else:
            raise ValueError("The provided address is not a valid IPv4 address.")