class Term():
    """An object to simplify terminal inputs and outputs
    """

    def asciiArt(self, lines):
        """Takes a list as an argument and prints out that list line by line in the terminal

        Args: 
            self (Term): An instance of Term.
            lines (list): A list containing the lines to print to draw the picture.
        """
        for line in lines:
            print(line)

    def Input(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (Term): An instance of Term.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)
        
    def Output(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (Term): An instance of Term.
            text (string): The text to display.
        """
        print(text)