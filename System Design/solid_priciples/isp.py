"""
Interface Segregation Principle (ISP):
The Interface Segregation Principle states that clients should not be forced
to depend on interfaces they don't use.
This principle encourages creating smaller, more cohesive interfaces tailored to the needs of specific clients,
rather than one large interface that tries to satisfy all clients.
Example: Consider an interface Machine with methods for both printing and scanning.
If a client only needs printing functionality, it is forced to depend on the scanning method, violating ISP.
"""

class Machine:
    def print_document(self, document):
        pass

    def scan_document(self):
        pass

"""
To adhere to ISP, we can split the interface into smaller,
more focused interfaces tailored to the needs of specific clients.
"""

class Printer:
    def print_document(self, document):
        pass

class Scanner:
    def scan_document(self):
        pass
