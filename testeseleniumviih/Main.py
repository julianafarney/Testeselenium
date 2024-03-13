from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:\\Users\\LabInfo\\OneDrive\\Documentos\\Downloads\\chromedriver-win32 (1)\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://the-internet.herokuapp.com/key_presses?")

    def enviarDados(usuario):
        email_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "target"))
        )
        email_login.clear
        email_login.send_keys(usuario)
        driver.implicitly_wait(5)  
        alert = driver.find_element(By.ID, "result").text
        return alert
    
    alert = enviarDados('A')
    if 'You entered: A' in alert :
        print("Teste ok")
    else:
        print("Usuário incorreto não reconhecido, teste falhou")
    
    alert = enviarDados(Keys.F2)
    if 'You entered: F2' in alert:
        print("F2 ok")
    else:
        print("Senha incorreta não reconhecida, teste falhou")

    alert = enviarDados(Keys.DELETE)
    if 'You entered: DELETE' in alert:
        print("Del ok")
    else:
        print("Falaha ao efetuar login, teste falhou")

    print("Todos os testes concluídos com sucesso!")

except:
    print("Teste Falhou! Erro na execução")

driver.quit()