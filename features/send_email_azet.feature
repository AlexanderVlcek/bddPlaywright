# Created by testify at 11/04/2023
Feature: Azet email functions
  Functions of azet email client

  Scenario: Send email
    Given user with credentials "alesvlcek@azet.sk", "M9Ng8XC8yd97Y@q" is logged in azet email
    When starts to write new email
    And chose email address from contacts
    And write message with text "some text body"
    And click send email
    Then email is sent