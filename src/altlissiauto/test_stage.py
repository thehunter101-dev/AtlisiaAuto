from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Modulos
from .modules.more_select import SafeMoreResult,InsertMoreResult


def Stage(driver, wait,test):
    driver.get(test)

    try:
        start_lesson = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="theme-provider"]/div/main/div/div/button')
            )
        )
        start_lesson.click()
    except TimeoutException:
        print("Haciendo una leccion Uwu")

    query = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="theme-provider"]/div/main/div/div[1]/p')
        )
    )

    queryNumber = int(query.text.split("/")[1].strip())

    resultado = []
    second_vuelta = False
    pasadas_validate = 2

    for p in range(2):
        for i in range(0, queryNumber):
            validate = False
            two_result = False
            for inner in range(pasadas_validate):
                btn_valid = wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.CSS_SELECTOR,'button.c-lfgsZH.c-PJLV.c-jUtMbh',
                        )
                    )
                )
                print(btn_valid)
                if second_vuelta:
                    if len(resultado[i]) >= 2 and isinstance(resultado[i], list):
                        print("Te inserto mas de 2 hijos weeeee")
                        InsertMoreResult(wait,resultado[i])
                    else:
                        inpu_t = wait.until(
                            EC.visibility_of_element_located(
                                (
                                    By.XPATH,
                                    '//*[@id="theme-provider"]/div/main/div/div[2]/div/p/input',
                                )
                            )
                        )
                        inpu_t.send_keys(resultado[i])
                    btn_valid.click()

                if not validate and not second_vuelta:
                    btn_valid.click()
                    validate = True

                    padre_container_result = wait.until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="theme-provider"]/div/main/div/div[2]/div/p')
                        )
                    )

                    respuestas = padre_container_result.find_elements(
                        By.CLASS_NAME, "c-gUxMKR-bkfbUO-isCorrect-true"
                    )

                    if len(respuestas) >= 2:
                        print("Mas de dos hijos weeeee")
                        resultados = SafeMoreResult(wait, respuestas)
                        resultado.append(resultados)
                    else:
                        respuesta = wait.until(
                            EC.visibility_of_element_located(
                                (
                                    By.CSS_SELECTOR,
                                    'span.c-gUxMKR.c-gUxMKR-bkfbUO-isCorrect-true',
                                )
                            )
                        )
                        resultado.append(respuesta.text)
                else:
                    btn_valid.click()

        pasadas_validate = 1
        second_vuelta = True
        btn_retry = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="theme-provider"]/div/main/div/div[3]/button')
            )
        )
        btn_retry.click()

    driver.quit()
