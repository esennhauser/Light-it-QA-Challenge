Feature: Patient login

  As a patient,
  I want to successfully log in to the MedAppoint platform
  So that I can access my appointments

  Scenario: Patient successfully logs in to MedAppoint
    Given The patient is at the login page
    When The patient fills in his email and password
    And The patient clicks on the Sign In button
    Then The patient can see the dashboard page
    