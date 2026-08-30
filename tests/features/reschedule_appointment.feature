Feature: Reschedule an appointment

  As a patient,
  I want to reschedule an appointment
  So that I can modify the date and time of the appointment

  Scenario: Patient successfully reschedules an appointment
    Given A patient is logged on the Medical Appointment platform
    And The patient is on the appointments page
    And The patient has at least one appointment
    When The patient clicks on the Reschedule button
    And The patient selects a date and a time
    And The patient clicks on the Confirm button
    Then The UI shows a success message
    And The appointment shows the new date and time selected
    