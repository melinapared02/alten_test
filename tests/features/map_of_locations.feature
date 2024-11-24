Feature: Map of locations

  Scenario: Verify interactive map display with site data
    Given I am on the home page
    When I go to the map section
    Then I verify that the map is visible
    And I verify that the office data is visible


  Scenario Outline: Verify that the correct data is displayed when selecting the office
    Given I am on the home page
    When I go to the map section
    And select the office <office>
    Then I verify that the data of the office <office> are <name>, <data> and <phone>

    Examples:
      | office | name       | data                                                                                                 | phone              |
      | 43     | BARCELONA  | Avinguda Parc Logístic, 22-26 Edificio B, Planta 1ª 08040 Barcelona                                  | (+34) 93 550 99 00 |
      | 45     | MADRID     | Parque Empresarial Cristalia C/ Vía de los Poblados, 3 Edificio 5 – Planta 2ª 28033 Madrid           | (+34) 91 791 00 00 |
      | 46     | VALLADOLID | Parque Tecnológico de Boecillo Edificio Galileo Módulo Rojo, Oficina 103 47151 Boecillo (Valladolid) | (+34) 983 54 81 68 |
      | 48     | CÁDIZ      | Av. Isaac Newton, 14 11500 El Puerto de Santa María (Cádiz)                                          | (+34) 91 791 00 00 |