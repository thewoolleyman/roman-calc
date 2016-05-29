Feature: add roman numerals
In order to demo mob progamming Jason wants to add Roman numerals

  Scenario Outline: Add I + I and get II
  Given that I have the Roman Calculator installed
    When I run "python rome_calc.py <arguments>"
    Then I should get "<result>"

  Examples: Calculations
    |arguments|result|
    |I + I|II|

  Scenario: Add I + I + I and get III
  Given that I have the Roman Calculator installed
    When I run "python rome_calc.py I + I + I"
    Then I should get "III"

  Scenario: Add I + III and get IV
  Given that I have the Roman Calculator installed
    When I run "python rome_calc.py I + III"
    Then I should get "IV"
