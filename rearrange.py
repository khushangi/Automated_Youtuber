from download import *

class shuffle:
    def rearrange_statements(statements):
        # Initialize a list to store the order of statements
        order = []

        # Manually rearrange the statements
        print("Manually rearrange the statements:")
        for i, statement in enumerate(statements, start=1):
            print(f"'{statement}'  [{i}]")
            order.append(int(input(f"Enter the order for statement '{statement}': ")))

        # Sort the statements based on the order
        sorted_statements = [statement for _, statement in sorted(zip(order, statements))]

        # Print the rearranged statements
        print("\nRearranged statements:")
        for statement in sorted_statements:
            print(f"'{statement}' ,")
        return sorted_statements

   