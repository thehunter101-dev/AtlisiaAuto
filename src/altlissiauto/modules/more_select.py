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
    print(len(hijos_input))
    print(len(respuestas))

    for i in range(len(respuestas)):
        hijos_input[i].send_keys(respuestas[i])