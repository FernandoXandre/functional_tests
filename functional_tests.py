self.assertTrue(
    any(row.text == '1: Estudar testes funcionais' for row in rows),
    "New to-do item did not appear in table"
)