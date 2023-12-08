
from seleniumbase import Driver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
from selenium.webdriver.support.select import Select
import capsolver
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

website = 'https://amazon.com/'
proxies = [
        "204.217.194.251:3128:xyzh4525:jpatiosmxoksej",
        "204.217.194.250:3128:xyzh4525:jpatiosmxoksej",
        "204.217.194.249:3128:xyzh4525:jpatiosmxoksej",
        "204.217.194.248:3128:xyzh4525:jpatiosmxoksej",
        "204.217.194.247:3128:xyzh4525:jpatiosmxoksej"
    ]

    # Escolhe um proxy aleatório
proxy = random.choice(proxies)
user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/76.0.4017.177",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 EdgA/91.0.864.59"
    ]

    # Escolhe um agente de usuário aleatório
user_agent = random.choice(user_agents)
arguments = [f'--user-agent={user_agent}']

proxy = "xyzh4525:jpatiosmxoksej@204.217.194.247:3128"

driver = Driver(uc=True, proxy=proxy)

def natural1(searchtyped,search):
    for letter in searchtyped:
        search.send_keys(letter)
        sleep(random.randint(1,5)/30)
def natural2(emailtyped,email):
    for letter in emailtyped:
        email.send_keys(letter)
        sleep(random.randint(1,5)/30)
def natural3(passwordtyped,password):
    for letter in passwordtyped:
        password.send_keys(letter)
        sleep(random.randint(1,5)/30)
def natural4(passwordtyped,password_again):
    for letter in passwordtyped:
        password_again.send_keys(letter)
        sleep(random.randint(1,5)/30)

searchtyped = "hotor trash"
nametyped = 'zacks smitt'
emailtyped = 'fkdegfedffadkfdjghjk@gmail.com'
passwordtyped = 'mkxnjdfndj@5w364'

driver.get('https://www.amazon.com')
driver.maximize_window()
sleep(7)



search = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
natural1(searchtyped,search)

searching = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
searching.click()

sleep(3)

def rolar_suavemente(driver, destino):
    script = f"""
        var start = window.pageYOffset;
        var end = {destino};
        var distance = end - start;
        var step = Math.round(distance / 50);
        
        function smoothScroll() {{
            if (distance > 0 && start < end) {{
                window.scroll(0, start += step);
                distance -= step;
                setTimeout(smoothScroll, 10);
            }} else if (distance < 0 && start > end) {{
                window.scroll(0, start -= step);
                distance += step;
                setTimeout(smoothScroll, 10);
            }}
        }}
        
        smoothScroll();
    """
    driver.execute_script(script)

rolar_suavemente(driver, 10)  
sleep(3)

products = driver.find_elements(By.XPATH,"//div[@class='a-section aok-relative s-image-square-aspect']")
if products:
    # Escolha o elemento desejado (por exemplo, o primeiro elemento na lista)
    desired_product = products[0]

    # Clique no elemento desejado
    desired_product.click()

rolar_suavemente(driver, 10)  
sleep(3)
cart = driver.find_element(By.ID,'add-to-cart-button')
cart.click()
sleep(3)

go_to_cart = driver.find_element(By.ID,'sw-gtc')
go_to_cart.click()
sleep(3)

close_order = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[4]/div/div[1]/div[1]/div/form/div/div/span/span/span/input")
close_order.click()

sleep(10)

#Create account

create_account = driver.find_elements(By.XPATH,"//span[@class='a-button-inner']")
create_account[1].click()

sleep(3)

name = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/input')
natural1(nametyped,name)

action_chains = ActionChains(driver)
action_chains.move_to_element(name).perform()
sleep(1)  # Aguarde um segundo (opcional)
action_chains.move_by_offset(50, 50).perform()

sleep(1)
email = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[2]/div[2]/span/input')
natural2(emailtyped,email)

action_chains.move_to_element(email).perform()
sleep(1)  # Aguarde um segundo (opcional)
action_chains.move_by_offset(50, 50).perform()

sleep(1)
password = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/div[1]/input')
natural3(passwordtyped,password)

action_chains.move_to_element(password).perform()
sleep(1)  # Aguarde um segundo (opcional)
action_chains.move_by_offset(50, 50).perform()

sleep(1)
password_again = driver.find_element(By.XPATH, "//input[@id='ap_password_check']")
natural4(passwordtyped,password_again)

action_chains.move_to_element(password_again).perform()
sleep(1)  # Aguarde um segundo (opcional)
action_chains.move_by_offset(50, 50).perform()

sleep(1)
verify_email = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[6]/span/span/input')
verify_email.click()

#Captcha
PAGE_URL = driver.current_url
proxy_ip = "204.217.194.247"
proxy_port = "3128"
proxy_username = "xyzh4525"
proxy_password = "jpatiosmxoksej"
PROXY = f"http://{proxy_username}:{proxy_password}@{proxy_ip}:{proxy_port}"
capsolver.api_key = "CAP-F5B1D40B17B5FEC502393BBFDBDADEFA"

def solve_aws_captcha(websiteURL, awsKey, awsIv, awsContext, awsChallengeJS):
    solution = capsolver.solve({
        "type": "AntiAwsWafTask",
        "websiteURL":websiteURL,
        "awsKey":awsKey,
        "awsIv":awsIv,
        "awsContext":awsContext,
        "awsChallengeJS":awsChallengeJS,
        "proxy": PROXY
    })
    
    return solution

def solve_aws_challenge(awsChallengeJS):
    solution = capsolver.solve({
        "type": "AntiAwsWafTask",
        "awsKey":"",
        "awsIv":"",
        "awsContext":"",
        "awsChallengeJS":awsChallengeJS,
        "websiteURL": PAGE_URL,
        "proxy": PROXY
    })
    
    return solution

def main():
    session = requests.Session()
    
    session.proxies = { 
       "http"  : PROXY, 
       "https" : PROXY, 
    }
    
    headers = {
        "cache-control": "max-age=0",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="107", "Chromium";v="107"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36/9uiP7EnX-09",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7"
    }
    response = session.get(
        headers=headers,
        url=PAGE_URL
    )
    print(response.status_code)
    ## Handling AWS Challenge
    solution = None
    if(response.status_code == 202):
        print("AWS Challenge Solve required")
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all script tags
        script_tags = soup.find_all('script')

        # Filter based on src attribute
        for script in script_tags:
            src = script.get('src')
            if src and 'token.awswaf.com' in src:
                print(f'Found AWS Challenge JS URL: {src}')  
                print("Solving AWS Challenge")
                
                solution = solve_aws_challenge(src)
                print("Received AWS Cookie: " + str(solution))
    ## Handling AWS Captcha + Challenge
    if response.status_code == 405:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the script tag that includes the source URL for "token.awswaf.com"
        script_tags = soup.find_all('script', {'src': re.compile(r'token\.awswaf\.com')})
        for script in script_tags:
            src = script.get('src')
            print(f'Found URL: {src}')

        # Extract JavaScript code and search for key, iv, and context values
        script_texts = soup.find_all('script', string=re.compile('.*key.*'))
        if script_texts:
            script_text = script_texts[0].string
            key_search = re.search('"key":"(.*?)"', script_text)
            iv_search = re.search('"iv":"(.*?)"', script_text)
            context_search = re.search('"context":"(.*?)"', script_text)
            
            key = key_search.group(1) if key_search else "Key not found"
            iv = iv_search.group(1) if iv_search else "IV not found"
            context = context_search.group(1) if context_search else "Context not found"

            print("Key:"+key)
            print("IV:"+iv)
            print("Context:"+context)
            
            print("Solving AWS Captcha")
            solution = solve_aws_captcha(PAGE_URL,key, iv, context, src)
            print("Received AWS Cookie: " + str(solution))
            # Extract the domain
    
        if solution is not None:
            parsed_url = urlparse(PAGE_URL)
            domain = parsed_url.netloc
            formatted_domain = f".{domain}"

            session.cookies.set(
                "aws-waf-token",
                solution.get("cookie"),
                domain=formatted_domain
            )
    
    headers = {
        "cache-control": "max-age=0",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="107", "Chromium";v="107"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36/9uiP7EnX-09",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "referer": PAGE_URL,
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7"
    }
    response = session.get(
        headers=headers,
        cookies = session.cookies,
        url=PAGE_URL
    )
    print(response.status_code)
    print(response.content)
    
main()

sleep(20)

#OTP Code part

user_response = ''

input_otp = driver.find_element(By.ID, "cvf-input-code")
sleep(1)
input_otp.send_keys(user_response)
sleep(2)
send_otp = driver.find_element(By.XPATH, "//input[@aria-labelledby='cvf-submit-otp-button-announce']")
sleep(1)
send_otp.click()

#Time for the customer send the OTP
sleep(100)

#Login if needed

"""type_email = driver.find_element(By.XPATH, "//input[@type='email']")
sleep(1)
type_email.send_keys('johnmadley118@gmail.com')
sleep(2)
continue2 = driver.find_element(By.XPATH, "//input[@id='continue']")
sleep(1)
continue2.click()
sleep(3)
type_password = driver.find_element(By.XPATH, "//input[@type='password']")
sleep(1)
type_password.send_keys('Carateka100#')
sleep(2)
sign = driver.find_element(By.XPATH, "//input[@id='signInSubmit']")
sleep(1)
sign.click()
sleep(25)
"""

#ADRESS AND CARD PART


phone_typed = '2407254802'

phone = driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressPhoneNumber']")
phone.clear()
natural1(phone_typed, phone)
sleep(2)

street_typed = "FRNT ENT 18326 Reaper Hill Ct."

street = driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressLine1']")
sleep(1)
natural1(street_typed, street)
sleep(2)

comp_typed = "House"

comp = driver.find_element(By.ID, "address-ui-widgets-enterAddressLine2")
sleep(1)
natural1(comp_typed, comp)
sleep(2)

district_typed = "Triangle"

district = driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressCity']")
sleep(1)
natural1(district_typed, district)
sleep(3)

sleep(3)

dropdown_element = driver.find_element(By.XPATH, "//span[@id='address-ui-widgets-enterAddressStateOrRegion']")
sleep(0.9)
dropdown_element.click()
sleep(3)

driver.execute_script("window.scrollTo(0, 1250);")

state = driver.find_element(By.XPATH, "//a[@id='address-ui-widgets-enterAddressStateOrRegion-dropdown-nativeId_54']")
sleep(1)
state.click()

sleep(5)



zip_code_typed = "22172"

zip_code = driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressPostalCode']")
sleep(0.7)
zip_code.clear()
natural1(zip_code_typed, zip_code)
sleep(6)

driver.execute_script("window.scrollTo(0, 300);")

use_adress = driver.find_element(By.XPATH, "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']")
sleep(0.89)
use_adress.click()
sleep(3.05)

driver.execute_script("window.scrollTo(0, 100);")

use_adress = driver.find_element(By.XPATH, "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']")
sleep(0.89)
use_adress.click()
sleep(7)

add_card = driver.find_element(By.LINK_TEXT, "Add a credit or debit card")
sleep(1)
add_card.click()
sleep(10)

iframe_xpath = "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[7]/div/div[3]/div/div/div[2]/div/div[2]/div/div/iframe"
driver.switch_to.frame(driver.find_element(By.XPATH, iframe_xpath))

sleep(5)

number_typed = "5462910278306535"

number_card = driver.find_element(By.NAME, "addCreditCardNumber")
natural1(number_typed, number_card)
sleep(2)

name_typed = "Sonix 1"

holder_name = driver.find_element(By.NAME, "ppw-accountHolderName")
natural1(name_typed, holder_name)

expiration = driver.find_elements(By.XPATH, "//select[@name='ppw-expirationDate_month']")
ex_date = expiration[0]
sleep(1)
date = Select(ex_date)
date.select_by_visible_text("11")
sleep(2)

ex_year = driver.find_element(By.XPATH, "//select[@name='ppw-expirationDate_year']")
sleep(1.01)
year = Select(ex_year)
year.select_by_visible_text("2027")
sleep(2.05)

cvv_typed = "311"

cvv = driver.find_element(By.NAME, "addCreditCardVerificationNumber")
sleep(0.98)
natural1(cvv_typed, cvv)
sleep(1.79)

add_card = driver.find_element(By.XPATH, "//input[@name='ppw-widgetEvent:AddCreditCardEvent']")
sleep(1)
add_card.click()
sleep(5)

#Confirm everything

payment = driver.find_element(By.XPATH, "//input[@name='ppw-widgetEvent:SetPaymentPlanSelectContinueEvent']")

sleep(1.001)
payment.click()
sleep(5.456)

driver.execute_script("window.scrollTo(0, 200);")

#Prime

sleep(1)


driver.execute_script("window.scrollTo(0, 100);")

prime = driver.find_element(By.XPATH, "//span[@class='a-button a-button-supplemental']")
sleep(1)
prime.click()

driver.execute_script("window.scrollTo(0, 400);")
sleep(7)

#Pay

pay = driver.find_elements(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div[1]/span/span/span[1]/span/input")
pay_true = pay[0]
sleep(1.2)
pay_true.click()
sleep(7.1)

#Security Verification

verify_security_typed = '311'

verify_security = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[4]/div[1]/input")
sleep(1)
natural1(verify_security_typed, verify_security)
sleep(2)

confirm = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[6]/div/span/span/input")
sleep(1)
confirm.click()
sleep(7)

#Random time

tempo_aleatorio = random.uniform(8 * 60, 15 * 60)


sleep(tempo_aleatorio)

#Cancel order after the time

edit = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[5]/div[3]/div[2]/div/div[2]/div/div[2]/div/div/span[1]/span/a")
sleep(1)
edit.click()
sleep(6)

cancel = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/div[2]/div/div[2]/div/div/span[2]/span/a")
sleep(1)
cancel.click()
sleep(4)

cancel_again = driver.find_element(By.XPATH, "/html/body/div[1]/form/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr/td/p[1]/span/span/span/input")
sleep(1)
cancel_again.click()