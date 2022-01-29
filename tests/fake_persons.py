from faker import Faker

fake = Faker("pl_PL")


class Person:
    def __init__(self):
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.street_address = fake.street_address().title()
        self.city = fake.city()
        self.postcode = fake.postcode()
        self.phone_number = fake.phone_number()
        self.email = None  # todo

    @property
    def full_address(self):
        return f"{self.street_address}; {self.postcode} {self.city}"

    def form_repr(self):
        form_data = (
            f"f_name={self.first_name}|s_name={self.last_name}"
            f"|street={self.street_address}|postcode={self.postcode}|city={self.city}|phone=no: {self.phone_number}\n"
        )
        return form_data.lower()

    def expected_format(self):
        output = (
            f"First Name: {self.first_name}\n"
            f"Second Name: {self.last_name}\n"
            f"Street: {self.street_address}\n"
            f"City: {self.city}\n"
            f"Postal Code: {self.postcode}\n"
            f"Phone Number: {self.phone_number}"
        )
        return output

        def __str__(self):
            return (
                f"{self.first_name} {self.last_name}\n"
                f"{self.street_address}\n"
                f"{self.postcode} {self.city}\n"
                f"tel: {self.phone_number}\n"
            )


if __name__ == "__main__":
    # person = Person()
    # print(person.__str__())
    # print("*"*25)
    # print(person.form_repr())
    # print("*"*25)
    # print(person.expected_format())
    for _ in range(5):
        person = Person()
        print(person.expected_format())
        print(person.form_repr())
