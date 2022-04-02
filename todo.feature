Feature: TODO task handling

    Scenario: Adding a new task to the application
        Given: the first task is "walk with the dog"
        When:the argument is "-l"
        Then:the result is
        """
        1 - walk
        2 - Buy
        """

    Scenario: Remove task
        Given: the terminal opened in the project directory
        And the file where you store your data
        And the file has at least 2 tasks
        When: the application is ran with the -r 2 argument
        Then: it should remove the second task from the file