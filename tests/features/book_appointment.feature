Feature: Book an appointment

  As a patient,
  I want to access the appointment booking form
  So that I can schedule an appointment with a doctor

  Scenario: Patient can access the book appointment form
    Given A patient is logged on the Medical Appointment platform
    And The patient is on the appointments page
    When The patient clicks on the Book Appointment button
    Then The book appointment form is displayed
    And The doctor field is visible
    And The date field is visible
    And The time slot field is visible
    And The notes field is visible
    And The Book Appointment button is visible
    