from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc
import pyperclip

# Modulos
from .login import Login
from .test_stage import Stage

def main():
    driver = uc.Chrome(version_main=140)
    wait = WebDriverWait(driver, 10)

    usuarioStr:str = "mmurciab@unemi.edu.ec"
    contrasenaStr:str = "1751707280"

    test = pyperclip.paste()

    Urls = [
        "https://aprender.altissia.org/platform/learning-path/mission/GOING_TO_THE_RESTAURANT/lesson/EN_GB_A2_VOCABULARY_GOING_TO_THE_RESTAURANT_PART_1/activity/EN_GB_A2_VOCABULARY_GOING_TO_THE_RESTAURANT_PART_1_SUMMARY_TEST_GOING_TO_THE_RESTAURANT_RECAPITULATI?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/PREPARING_FOOD/lesson/EN_GB_A2_VOCABULARY_PREPARING_FOOD_PART_1/activity/EN_GB_A2_VOCABULARY_PREPARING_FOOD_PART_1_SUMMARY_TEST_PREPARING_FOOD_RECAPITULATIVE_TEST?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_THE_WEATHER/lesson/EN_GB_A2_VOCABULARY_TALKING_ABOUT_THE_WEATHER_PART_1/activity/EN_GB_A2_VOCABULARY_TALKING_ABOUT_THE_WEATHER_PART_1_SUMMARY_TEST_TALKING_ABOUT_THE_WEATHER_RECAPITU?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_YOUR_HOLIDAY/lesson/EN_GB_A2_VOCABULARY_PREPARING_FOR_A_TRIP_PART_1/activity/EN_GB_A2_VOCABULARY_PREPARING_FOR_A_TRIP_PART_1_SUMMARY_TEST_PREPARING_FOR_A_TRIP_RECAPITULATIVE_TES?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_YOUR_HOLIDAY/lesson/EN_GB_A2_VOCABULARY_TALKING_ABOUT_YOUR_VACATION_PART_1?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_DIFFERENT_CULTURES/lesson/EN_GB_A2_VOCABULARY_TALKING_ABOUT_DIFFERENT_CULTURES_PART_1/activity/EN_GB_A2_VOCABULARY_TALKING_ABOUT_DIFFERENT_CULTURES_PART_1_SUMMARY_TEST_TALKING_ABOUT_DIFFERENT_CUL?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_YOUR_HOBBIES/lesson/EN_GB_A2_VOCABULARY_TALKING_ABOUT_YOUR_HOBBIES_PART_1/activity/EN_GB_A2_VOCABULARY_TALKING_ABOUT_YOUR_HOBBIES_PART_1_SUMMARY_TEST_TALKING_ABOUT_YOUR_HOBBIES_RECAPI?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_YOUR_HOBBIES/lesson/EN_GB_A2_VOCABULARY_DOING_AND_PLAYING_SPORTS_PART_1?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/A_VISIT_TO_THE_BANK/lesson/EN_GB_A2_VOCABULARY_A_VISIT_TO_THE_BANK_PART_1/activity/EN_GB_A2_VOCABULARY_A_VISIT_TO_THE_BANK_PART_1_SUMMARY_TEST_A_VISIT_TO_THE_BANK_RECAPITULATIVE_TEST?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/SPEAKING_ON_THE_PHONE/lesson/EN_GB_A2_VOCABULARY_SPEAKING_ON_THE_PHONE_PART_1/activity/EN_GB_A2_VOCABULARY_SPEAKING_ON_THE_PHONE_PART_1_SUMMARY_TEST_SPEAKING_ON_THE_PHONE_RECAPITULATIVE_T?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/COMMUNICATING_BY_EMAIL/lesson/EN_GB_A2_VOCABULARY_COMMUNICATING_BY_EMAIL_PART_1?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_SCHOOL/lesson/EN_GB_A2_VOCABULARY_TALKING_ABOUT_SCHOOL_PART_1/activity/EN_GB_A2_VOCABULARY_TALKING_ABOUT_SCHOOL_PART_1_SUMMARY_TEST_TALKING_ABOUT_SCHOOL_RECAPITULATIVE_TES?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_UNIVERSITY_LIFE/lesson/EN_GB_A2_VOCABULARY_TALKING_ABOUT_UNIVERSITY_LIFE_PART_1/activity/EN_GB_A2_VOCABULARY_TALKING_ABOUT_UNIVERSITY_LIFE_PART_1_SUMMARY_TEST_TALKING_ABOUT_UNIVERSITY_LIFE_?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_LIFESTYLES/lesson/EN_GB_A2_VOCABULARY_TALKING_ABOUT_LIFESTYLES_PART_1/activity/EN_GB_A2_VOCABULARY_TALKING_ABOUT_LIFESTYLES_PART_1_SUMMARY_TEST_TALKING_ABOUT_LIFESTYLES_RECAPITULA?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_THE_ENVIRONMENT/lesson/EN_GB_A2_VOCABULARY_TALKING_ABOUT_THE_ENVIRONMENT_PART_1/activity/EN_GB_A2_VOCABULARY_TALKING_ABOUT_THE_ENVIRONMENT_PART_1_SUMMARY_TEST_TALKING_ABOUT_THE_ENVIRONMENT_?studyLg=en_GB",
    ]
    Login(driver,wait,usuarioStr,contrasenaStr)

    for url in Urls:
        try:
            Stage(driver,wait,url)
        except TimeoutException:
            print("JAjajaj")

