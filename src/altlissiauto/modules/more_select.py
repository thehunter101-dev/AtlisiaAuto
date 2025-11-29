from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def SafeMoreResult(wait, respuestas):
    resultadosList = []
    for respuesta in respuestas:
        resultadosList.append(respuesta.text)
    return resultadosList


def InsertMoreResult(wait, respuestas):
    input_container_padre = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="theme-provider"]/div/main/div/div[2]/div/p')
        )
    )

    hijos_input = input_container_padre.find_elements(By.CSS_SELECTOR,'input.c-iJOJc')
    if len(hijos_input) != 0:
        for i in range(len(respuestas)):
            hijos_input[i].send_keys(respuestas[i])
    else:
        for i in respuestas:
            btn_correct = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//ul[contains(@class,'c-gUbZqN')]//button[normalize-space()='{i}']")
                )
            )
            btn_correct.click()

def ordenar_frase(frase, partes):
    partes_ordenadas = sorted(
        partes,
        key=lambda x: frase.find(x)
    )

    return partes_ordenadas