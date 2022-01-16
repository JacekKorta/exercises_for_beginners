from tests.fake_factories import Person

from strings.person import persons_data_converter


class TestPerson:
    def test_person_data_converter(self):
        for _ in range(100):
            person = Person()
            _input = person.form_repr()
            expected_output = person.expected_format()
            output = persons_data_converter(_input)

            assert output == expected_output
