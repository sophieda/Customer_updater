class Cli:
    def __init__(self, run_command: callable) -> None:
        self.original_run_command = run_command
        self.customer_file_path = ""
        self.purchase_file_path = ""

    def run(self):
        self.customer_file_path = input("Enter customer complete file path :")
        self.purchase_file_path = input("Enter purchase complete file path :")
        self.original_run_command(self.customer_file_path, self.purchase_file_path)
