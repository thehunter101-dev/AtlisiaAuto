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
        "https://aprender.altissia.org/platform/learning-path/mission/GOING_TO_THE_RESTAURANT/lesson/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS/activity/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS_EXERCISE_MEANING_ACTIVITY_2?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/GOING_TO_THE_RESTAURANT/lesson/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS/activity/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS_EXERCISE_FORM_ACTIVITY_1?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/GOING_TO_THE_RESTAURANT/lesson/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS/activity/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS_EXERCISE_FORM_ACTIVITY_2?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/GOING_TO_THE_RESTAURANT/lesson/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS/activity/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS_EXERCISE_PRACTICE_ACTIVITY_1?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/GOING_TO_THE_RESTAURANT/lesson/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS/activity/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS_EXERCISE_PRACTICE_ACTIVITY_2?studyLg=en_GB",
        "https://aprender.altissia.org/platform/learning-path/mission/GOING_TO_THE_RESTAURANT/lesson/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS/activity/EN_GB_A2_GRAMMAR_WILL_FOR_OFFERS_DECISIONS_EXERCISE_PRACTICE_ACTIVITY_3?studyLg=en_GB",
    ]
    Login(driver,wait,usuarioStr,contrasenaStr)
    #Stage(driver,wait,test)
    for url in Urls:
        try:
            Stage(driver,wait,url)
        except TimeoutException:
            print("JAjajaj")
