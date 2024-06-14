import json

class Person:
    def __init__(self, name, ecode, designation):
        self.name = name
        self.ecode = ecode
        self.designation = designation
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def __repr__(self):
        return f"{self.name} (Ecode: {self.ecode}, Designation: {self.designation})"


class HierarchyTree:
    def __init__(self, root_person):
        self.root = root_person

    def find_person_by_ecode(self, ecode, person=None):
        if person is None:
            person = self.root
        
        if person.ecode == ecode:
            return person
        
        for subordinate in person.subordinates:
            found_person = self.find_person_by_ecode(ecode, subordinate)
            if found_person:
                return found_person
        return None

    def get_hierarchy(self, ecode):
        person = self.find_person_by_ecode(ecode)
        if person is None:
            return f"Person with ecode {ecode} not found in the hierarchy."
        
        hierarchy = []
        self._build_hierarchy(person, hierarchy)
        return hierarchy

    def _build_hierarchy(self, person, hierarchy):
        hierarchy.append(person.__repr__())
        for subordinate in person.subordinates:
            self._build_hierarchy(subordinate, hierarchy)

    def add_person(self, name, ecode, designation, manager_ecode):
        manager = self.find_person_by_ecode(manager_ecode)
        if manager is None:
            return f"Manager with ecode {manager_ecode} not found in the hierarchy."
        
        new_person = Person(name, ecode, designation)
        manager.add_subordinate(new_person)
        return f"Added {name} (Ecode: {ecode}, Designation: {designation}) under manager {manager.name} (Ecode: {manager_ecode})"

    def remove_person(self, ecode, person=None):
        if person is None:
            person = self.root
        
        for subordinate in person.subordinates:
            if subordinate.ecode == ecode:
                person.subordinates.remove(subordinate)
                return f"Removed {subordinate.name} (Ecode: {ecode}) from the hierarchy."
            
            result = self.remove_person(ecode, subordinate)
            if result:
                return result
        return f"Person with ecode {ecode} not found in the hierarchy."

    def change_designation(self, ecode, new_designation):
        person = self.find_person_by_ecode(ecode)
        if person is None:
            return f"Person with ecode {ecode} not found in the hierarchy."
        
        person.designation = new_designation
        return f"Changed designation of {person.name} (Ecode: {ecode}) to {new_designation}"

    def change_manager(self, ecode, new_manager_ecode):
        person = self.find_person_by_ecode(ecode)
        if person is None:
            return f"Person with ecode {ecode} not found in the hierarchy."

        new_manager = self.find_person_by_ecode(new_manager_ecode)
        if new_manager is None:
            return f"New manager with ecode {new_manager_ecode} not found in the hierarchy."

        if person.ecode == self.root.ecode:
            return "Cannot change the manager of the root person."

        current_manager = self.find_person_manager(ecode)
        if current_manager:
            current_manager.subordinates.remove(person)

        new_manager.add_subordinate(person)
        return f"Changed manager of {person.name} (Ecode: {ecode}) to {new_manager.name} (Ecode: {new_manager_ecode})"

    def find_person_manager(self, ecode, person=None):
        if person is None:
            person = self.root
        
        for subordinate in person.subordinates:
            if subordinate.ecode == ecode:
                return person
            
            manager = self.find_person_manager(ecode, subordinate)
            if manager:
                return manager
        return None

    def get_hierarchy_as_dict(self, person=None):
        if person is None:
            person = self.root
        
        person_dict = {
            'name': person.name,
            'ecode': person.ecode,
            'designation': person.designation,
            'subordinates': [self.get_hierarchy_as_dict(sub) for sub in person.subordinates]
        }
        return person_dict

    def print_hierarchy_as_json(self):
        hierarchy_dict = self.get_hierarchy_as_dict()
        hierarchy_json = json.dumps(hierarchy_dict, indent=2)
        print(hierarchy_json)
        return hierarchy_json


# Example usage:
if __name__ == "__main__":
    # Create the root person
    ceo = Person("CEO", "E001", "Chief Executive Officer")

    # Create the hierarchy tree
    company_hierarchy = HierarchyTree(ceo)

    # Add subordinates
    print(company_hierarchy.add_person("Head of Engineering", "E002", "Head of Engineering", "E001"))
    print(company_hierarchy.add_person("Head of Marketing", "E003", "Head of Marketing", "E001"))
    
    # Add further subordinates
    print(company_hierarchy.add_person("Senior Engineer", "E004", "Senior Engineer", "E002"))
    print(company_hierarchy.add_person("Junior Engineer", "E005", "Junior Engineer", "E004"))
    print(company_hierarchy.add_person("Marketing Executive", "E006", "Marketing Executive", "E003"))
    
    # Get the hierarchy of a specific person
    person_ecode = "E002"
    hierarchy = company_hierarchy.get_hierarchy(person_ecode)
    print(f"Hierarchy for ecode {person_ecode}: {hierarchy}")
    
    # Output the full hierarchy from the root
    full_hierarchy = company_hierarchy.get_hierarchy("E001")
    print(f"Full hierarchy from CEO: {full_hierarchy}")
    
    # Add a new person under a manager using manager's ecode
    result = company_hierarchy.add_person("Product Manager", "E007", "Product Manager", "E001")
    print(result)
    
    # Change the designation of an employee
    result = company_hierarchy.change_designation("E005", "Lead Engineer")
    print(result)
    
    # Change the manager of an employee
    result = company_hierarchy.change_manager("E005", "E002")
    print(result)
    
    # Remove a person from the hierarchy
    result = company_hierarchy.remove_person("E004")
    print(result)
    
    # Output the full hierarchy from the root again to see changes
    print("Updated hierarchy from CEO:")
    hierarchy_json = company_hierarchy.print_hierarchy_as_json()
    print(hierarchy_json)
