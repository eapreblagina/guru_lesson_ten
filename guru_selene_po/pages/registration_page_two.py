import os

from selene import have
from selene.support.shared import browser
from guru_selene_po.data.users import User


class RegistrationPageSteps:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')


    def open(self):
        browser.open('/automation-practice-form')
        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('footer').execute_script('element.remove()')
        browser.should(have.title('DEMOQA'))
        browser.element('.main-header').should(have.text('Practice Form'))

    def register(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        browser.all('[name="gender"]').element_by(have.value(user.gender)).element('..').click()
        browser.element('#userNumber').type(user.mobile_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.date_of_birth.strftime("%B"))
        browser.element('.react-datepicker__year-select').type(user.date_of_birth.year)
        browser.element(f'.react-datepicker__day--0{user.date_of_birth.day}').click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        browser.all('.custom-checkbox').element_by(have.text(user.hobbies)).click()
        browser.element('#uploadPicture').set_value(os.path.abspath(f'resources/{user.picture}'))
        browser.element('#currentAddress').type(user.address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').press_enter()


    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.mobile_number,
                f'{user.date_of_birth.day} {user.date_of_birth.strftime("%B")},{user.date_of_birth.year}',
                user.subjects,
                user.hobbies,
                user.picture,
                user.address,
                f'{user.state} {user.city}'
            ))
