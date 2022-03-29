Feature: TODO task handling

    Scenario: Adding a new task to the application
        Given: the first task is "walk with the dog"
        When:the argument is "-l"
        Then:the result is
        """
        1 - walk
        2 - Buy
        """
