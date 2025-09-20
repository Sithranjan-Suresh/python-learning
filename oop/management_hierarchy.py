"""
Problem: Management Hierarchy Tree
----------------------------------
Simulates an organizational hierarchy using a tree structure.
Each node represents an employee with a name and designation.
Supports:
1. Adding child nodes (reportees)
2. Calculating the level of a node
3. Printing the hierarchy based on name, designation, or both
"""

class TreeNode:
    def __init__(self, name, designation):
        self.name = name                  # Employee name
        self.designation = designation    # Employee designation
        self.parent = None                # Reference to parent node
        self.children = []                # List of child nodes

    def add_child(self, child):
        """Add a child node and set its parent"""
        self.children.append(child)
        child.parent = self

    def get_level(self):
        """Return the level (depth) of this node in the tree"""
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, whatprints):
        """
        Print the tree structure based on whatprints:
        - "name": print only names
        - "designation": print only designations
        - "both": print name and designation
        """
        spaces = '  ' * self.get_level()  # Indentation based on level

        if whatprints == "name":
            print(f"{spaces}|__{self.name}")
        elif whatprints == "designation":
            print(f"{spaces}|__{self.designation}")
        else:
            print(f"{spaces}|__{self.name} ({self.designation})")

        for child in self.children:
            child.print_tree(whatprints)


def build_management_tree():
    """Builds a sample management hierarchy and returns the root node"""
    # CEO level
    ceo = TreeNode("Nilupul", "CEO")

    # CTO and HR Head reporting to CEO
    cto = TreeNode("Chinmay", "CTO")
    hr_head = TreeNode("Gels", "HR Head")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    # CTO's team
    infra_head = TreeNode("Viswa", "Infra Head")
    app_head = TreeNode("Aamir", "Application Head")
    cto.add_child(infra_head)
    cto.add_child(app_head)

    # Infra Head's team
    cloud_manager = TreeNode("Dhaval", "Cloud Manager")
    app_manager = TreeNode("Abhijit", "App Manager")
    infra_head.add_child(cloud_manager)
    infra_head.add_child(app_manager)

    # HR Head's team
    recruit_manager = TreeNode("Peter", "Recruitment Manager")
    policy_manager = TreeNode("Waqas", "Policy Manager")
    hr_head.add_child(recruit_manager)
    hr_head.add_child(policy_manager)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()

    # Print only names
    print("=== Name Hierarchy ===")
    root_node.print_tree("name")

    # Print only designations
    print("\n=== Designation Hierarchy ===")
    root_node.print_tree("designation")

    # Print both names and designations
    print("\n=== Full Hierarchy ===")
    root_node.print_tree("both")
