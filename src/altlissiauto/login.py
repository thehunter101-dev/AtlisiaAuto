from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def Login(driver,wait, usuarioStr, contrasenaStr):
    driver.get(
        "https://aprender.altissia.org/platform/learning-path/mission/TALKING_ABOUT_YOUR_FAMILY/lesson/EN_GB_A2_VOCABULARY_TALKING_ABOUT_YOUR_FAMILY_PART_1/activity/EN_GB_A2_VOCABULARY_TALKING_ABOUT_YOUR_FAMILY_PART_1_SUMMARY_TEST_TALKING_ABOUT_YOUR_FAMILY_RECAPITU?studyLg=en_GB"
    )

    usuario = wait.until(EC.presence_of_element_located((By.ID, "username")))
    usuario.send_keys(usuarioStr)

    contrasena = driver.find_element(By.ID, "password")
    contrasena.send_keys(contrasenaStr)

    boton_login = driver.find_element(By.CSS_SELECTOR, "button.c-lfgsZH")
    boton_login.click()

    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[aria-label='Open more options menu']")
        )
    )

    print("Iniciaste session :)")