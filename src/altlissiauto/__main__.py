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
    driver = uc.Chrome(version_main=147)
    wait = WebDriverWait(driver, 6)

    usuarioStr:str = "mmurciab@unemi.edu.ec"
    contrasenaStr:str = "1751707280"

    test = pyperclip.paste()

    Urls = [
        "https://aprender.altissia.org/platform/learning-path/mission/DECIDING_HOW_TO_TRAVEL/lesson/EN_GB_B1_GRAMMAR_PRESENT_SIMPLE_PRESENT_CONTINUOUS_GOING_TO_AND_WILL_FOR_FUTURE/activity/EN_GB_B1_GRAMMAR_PRESENT_SIMPLE_PRESENT_CONTINUOUS_GOING_TO_AND_WILL_FOR_FUTURE_EXERCISE_MEANING_ACT?customer=ECUADOR_EPUNEMI_2025",
        "https://aprender.altissia.org/platform/learning-path/mission/DECIDING_HOW_TO_TRAVEL/lesson/EN_GB_B1_GRAMMAR_PRESENT_SIMPLE_PRESENT_CONTINUOUS_GOING_TO_AND_WILL_FOR_FUTURE/activity/EN_GB_B1_GRAMMAR_PRESENT_SIMPLE_PRESENT_CONTINUOUS_GOING_TO_AND_WILL_FOR_FUTURE_EXERCISE_MEANING_A_2?customer=ECUADOR_EPUNEMI_2025",
        "https://aprender.altissia.org/platform/learning-path/mission/DECIDING_HOW_TO_TRAVEL/lesson/EN_GB_B1_GRAMMAR_PRESENT_SIMPLE_PRESENT_CONTINUOUS_GOING_TO_AND_WILL_FOR_FUTURE/activity/EN_GB_B1_GRAMMAR_PRESENT_SIMPLE_PRESENT_CONTINUOUS_GOING_TO_AND_WILL_FOR_FUTURE_EXERCISE_FORM_ACTIVI?customer=ECUADOR_EPUNEMI_2025",
        "https://aprender.altissia.org/platform/learning-path/mission/DECIDING_HOW_TO_TRAVEL/lesson/EN_GB_B1_GRAMMAR_PRESENT_SIMPLE_PRESENT_CONTINUOUS_GOING_TO_AND_WILL_FOR_FUTURE/activity/EN_GB_B1_GRAMMAR_PRESENT_SIMPLE_PRESENT_CONTINUOUS_GOING_TO_AND_WILL_FOR_FUTURE_EXERCISE_FORM_ACTI_2?customer=ECUADOR_EPUNEMI_2025",
        "https://aprender.altissia.org/platform/learning-path/mission/DECIDING_HOW_TO_TRAVEL/lesson/EN_GB_B1_GRAMMAR_PRESENT_SIMPLE_PRESENT_CONTINUOUS_GOING_TO_AND_WILL_FOR_FUTURE/activity/EN_GB_B1_GRAMMAR_PRESENT_SIMPLE_PRESENT_CONTINUOUS_GOING_TO_AND_WILL_FOR_FUTURE_EXERCISE_PRACTICE_AC?customer=ECUADOR_EPUNEMI_2025",
        "",
        "",
        "",
        "",
    ]
    Login(driver,wait,usuarioStr,contrasenaStr)
    #Stage(driver,wait,test)
    for url in Urls:
        try:
            Stage(driver,wait,url)
        except:
            print("AAAAAAA")
