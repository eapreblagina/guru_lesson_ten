from guru_selene_po.data import users
from guru_selene_po.pages.registration_page_two import RegistrationPageSteps


def test_form_demoqa():
    registration_page = RegistrationPageSteps()
    student = users.student

    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
