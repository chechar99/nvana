Feature: Get and consolidate user data

  Scenario: Get and consolidate data of one user
     Given we have the user Peter with member id "9999"
      When we request consolidated data
      Then we get this json data:
        """
        {"oop_max": 6000, "stop_loss": 13000, "deductible": 1200}
        """
