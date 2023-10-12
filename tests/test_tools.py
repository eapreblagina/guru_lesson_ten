from pathlib import Path
from selene.support.shared import browser
from selene import have, by
from selene import command
import os
import tests
from tests import resources


def test_valid_Practice_Form():
    #when
    browser.open('/automation-practice-form')
    browser.element('#firstName').click().type('Kate')
    browser.element('#lastName').click().type('Preblagina')
    browser.element('#userEmail').click().type('Katitoporova@bk.ru')
    browser.element('[name=gender][value=Female] + label').click()
    browser.element('#userNumber').click().type(89515555555)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('August')
    browser.element('.react-datepicker__year-select').type('2000')
    browser.element('.react-datepicker__day--009').click()

# ручной ввод даты
    #browser.element('#dateOfBirthInput').perform(command.js.set_value('9 Aug 2000'))

    browser.element('#subjectsInput').type('Economics').press_enter()

    browser.all('.custom-checkbox').element_by(have.text('Sports')).click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/foto.jpg')
        )
    )

    browser.element('#currentAddress').type('Пушкина 15').perform(command.js.scroll_into_view)

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Karnal')).click()

    browser.element('#submit').press_enter()

    #then

    browser.element('.table').should(
        have.text(
            'Kate Preblagina'
            and 'Katitoporova@bk.ru'
            and 'Female'
            and '89515555555'
            and '09 Aug, 2000'
            and 'Economics'
            and 'Sports'
            and 'foto.jpg'
            and 'Haryana'
            and 'Karnal'
        ))