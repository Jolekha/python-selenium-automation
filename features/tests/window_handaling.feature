# Created by 17734 at 6/25/2021
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon T&C page
    When Store original windows
    When Click on Amazon Privacy Notice link
    When Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    Then User can close new window
    Then switch back to original


