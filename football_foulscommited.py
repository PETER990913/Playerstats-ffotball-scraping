from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
# Create a ChromeOptions instance
options = webdriver.ChromeOptions()

# Replace this with the actual path to your Chrome user profile directory
# options.add_argument("user-data-dir=C:\\Users\\JS guru\\AppData\\Local\\Google\\Chrome\\User Data")

# Disable the "DevToolsActivePort" check, as it can sometimes cause issues
options.add_argument("--disable-dev-shm-usage")

# Disable the "sandbox" mode if you encounter issues
options.add_argument("--no-sandbox")

# Create a Chrome webdriver instance with the options
driver = webdriver.Chrome(options=options)

driver.maximize_window()
# Open a website
driver.get("https://playerstats.football/premier-league/liverpool/fouls-committed")

driver.find_element(By.XPATH, '/html/body/div[2]/nav/div/div[3]/a[1]').click()
# Find the one page table element
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('oscarthagando@hotmail.com')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('HiScott!')
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[4]/button').click()
driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[2]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[3]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[4]').click()
time.sleep(1)
element = driver.find_element(By.XPATH, '//*[@id="statsFilter"]')
actions = ActionChains(driver)
actions.click(element)  # Perform a click action on the element
for _ in range(3):
    actions.key_down(Keys.DOWN)  # Press down the "down" key
    actions.key_up(Keys.DOWN)  # Press down the Control key (modify the key if needed)
actions.key_down(Keys.ENTER)
actions.key_up(Keys.ENTER)
actions.perform()  # Perform the action
time.sleep(1)
Player_list = []
A_list = []
B_list = []
C_list = []    
D_list = []    
E_list = []    
F_list = []    
G_list = []    
H_list = []    
I_list = []    
J_list = []    
K_list = []    
L_list = []    
M_list = []    
N_list = []    
O_list = []    
P_list = []    
Q_list = []    
R_list = []    
S_list = []    
T_list = []    
U_list = []    
V_list = []    
W_list = []    
X_list = []    
Y_list = []    
Z_list = []    
A1_list = []    
B1_list = []    
C1_list = []    
D1_list = []    
E1_list = []    
F1_list = []    
G1_list = []    
H1_list = []    
J1_list = []    
K1_list = []    
L1_list = []    
M1_list = []    
N1_list = []    
O1_list = []    

Rows = driver.find_elements(By.XPATH, '//*[@id="content-wrapper"]/div[3]/div/div')

for i in range(2, len(Rows)):
    try:
        Player = Rows[i].find_element(By.CLASS_NAME, 'stat__player').text
    except:
        Player = "none"
    print('Player:', Player)
    Player_list.append(Player)
    columnss = Rows[i].find_elements(By.CLASS_NAME, 'stat__fixture')
    columns = []
    for element in columnss:
        if 'hidden' not in element.get_attribute('class'):
            columns.append(element)        
    print(len(columnss))
    print(len(columns))
    if i == 2:
        try:
            A = columns[0].text
            B = columns[1].text
            C = columns[2].find_element(By.TAG_NAME, 'img').get_attribute('title')
            D = columns[3].find_element(By.TAG_NAME, 'img').get_attribute('title')
            E = columns[4].find_element(By.TAG_NAME, 'img').get_attribute('title')
            F = columns[5].find_element(By.TAG_NAME, 'img').get_attribute('title')
            G = columns[6].find_element(By.TAG_NAME, 'img').get_attribute('title')
            H = columns[7].find_element(By.TAG_NAME, 'img').get_attribute('title')
            I = columns[8].find_element(By.TAG_NAME, 'img').get_attribute('title')
            J = columns[9].find_element(By.TAG_NAME, 'img').get_attribute('title')
            K = columns[10].find_element(By.TAG_NAME, 'img').get_attribute('title')
            L = columns[11].find_element(By.TAG_NAME, 'img').get_attribute('title')
            M = columns[12].find_element(By.TAG_NAME, 'img').get_attribute('title')
            N = columns[13].find_element(By.TAG_NAME, 'img').get_attribute('title')
            O = columns[14].find_element(By.TAG_NAME, 'img').get_attribute('title')
            P = columns[15].find_element(By.TAG_NAME, 'img').get_attribute('title')
            Q = columns[16].find_element(By.TAG_NAME, 'img').get_attribute('title')
            R = columns[17].find_element(By.TAG_NAME, 'img').get_attribute('title')
            S = columns[18].find_element(By.TAG_NAME, 'img').get_attribute('title')
            T = columns[19].find_element(By.TAG_NAME, 'img').get_attribute('title')
            U = columns[20].find_element(By.TAG_NAME, 'img').get_attribute('title')
            V = columns[21].find_element(By.TAG_NAME, 'img').get_attribute('title')
            W = columns[22].find_element(By.TAG_NAME, 'img').get_attribute('title')
            X = columns[23].find_element(By.TAG_NAME, 'img').get_attribute('title')
            Y = columns[24].find_element(By.TAG_NAME, 'img').get_attribute('title')
            Z = columns[25].find_element(By.TAG_NAME, 'img').get_attribute('title')
            A1 = columns[26].find_element(By.TAG_NAME, 'img').get_attribute('title')
            B1 = columns[27].find_element(By.TAG_NAME, 'img').get_attribute('title')
            C1 = columns[28].find_element(By.TAG_NAME, 'img').get_attribute('title')
            D1 = columns[29].find_element(By.TAG_NAME, 'img').get_attribute('title')
            E1 = columns[30].find_element(By.TAG_NAME, 'img').get_attribute('title')            
            F1 = columns[31].find_element(By.TAG_NAME, 'img').get_attribute('title')
            G1 = columns[32].find_element(By.TAG_NAME, 'img').get_attribute('title')
            H1 = columns[33].find_element(By.TAG_NAME, 'img').get_attribute('title')
            J1 = columns[34].find_element(By.TAG_NAME, 'img').get_attribute('title')
            K1 = columns[35].find_element(By.TAG_NAME, 'img').get_attribute('title')
            L1 = columns[36].find_element(By.TAG_NAME, 'img').get_attribute('title')
            M1 = columns[37].find_element(By.TAG_NAME, 'img').get_attribute('title')
            N1 = columns[38].find_element(By.TAG_NAME, 'img').get_attribute('title')
            O1 = columns[39].find_element(By.TAG_NAME, 'img').get_attribute('title')
        except:
            A = ""  
            B = ""  
            C = ""  
            D = ""  
            E = ""  
            F = ""  
            G = ""  
            H = ""  
            I = ""  
            J = ""  
            K = ""  
            L = ""  
            M = ""  
            N = ""  
            O = ""  
            P = ""  
            Q = ""  
            R = ""  
            S = ""  
            T = ""  
            U = ""  
            V = ""  
            W = ""  
            X = ""  
            Y = ""  
            Z = ""  
            A1 = ""  
            B1 = ""  
            C1 = ""  
            D1 = ""  
            E1 = ""              
            F1 = ""  
            G1 = ""  
            H1 = ""  
            J1 = ""  
            K1 = ""  
            L1 = ""  
            M1 = ""  
            N1 = ""  
            O1 = ""
        A_list.append(A)
        B_list.append(B)
        C_list.append(C)
        D_list.append(D)
        E_list.append(E)
        F_list.append(F)
        G_list.append(G)
        H_list.append(H)
        I_list.append(I)
        J_list.append(J)
        K_list.append(K)
        L_list.append(L)
        M_list.append(M)
        N_list.append(N)
        O_list.append(O)
        P_list.append(P)
        Q_list.append(Q)
        R_list.append(R)
        S_list.append(S)
        T_list.append(T)
        U_list.append(U)
        V_list.append(V)
        W_list.append(W)
        X_list.append(X)
        Y_list.append(Y)
        Z_list.append(Z)
        A1_list.append(A1)
        B1_list.append(B1)
        C1_list.append(C1)
        D1_list.append(D1)
        E1_list.append(E1)        
        F1_list.append(F1)
        G1_list.append(G1)
        H1_list.append(H1)
        J1_list.append(J1)
        K1_list.append(K1)
        L1_list.append(L1)
        M1_list.append(M1)
        N1_list.append(N1)
        O1_list.append(O1)
    else:
        try:
            A = str(columns[0].text).replace('\n', ' ')
            B = str(columns[1].text).replace('\n', ' ')
            C = str(columns[2].text).replace('\n', ' ')
            D = str(columns[3].text).replace('\n', ' ')
            E = str(columns[4].text).replace('\n', ' ')
            F = str(columns[5].text).replace('\n', ' ')
            G = str(columns[6].text).replace('\n', ' ')
            H = str(columns[7].text).replace('\n', ' ')
            I = str(columns[8].text).replace('\n', ' ')
            J = str(columns[9].text).replace('\n', ' ')
            K = str(columns[10].text).replace('\n', ' ')
            L = str(columns[11].text).replace('\n', ' ')
            M = str(columns[12].text).replace('\n', ' ')
            N = str(columns[13].text).replace('\n', ' ')
            O = str(columns[14].text).replace('\n', ' ')
            P = str(columns[15].text).replace('\n', ' ')
            Q = str(columns[16].text).replace('\n', ' ')
            R = str(columns[17].text).replace('\n', ' ')
            S = str(columns[18].text).replace('\n', ' ')
            T = str(columns[19].text).replace('\n', ' ')
            U = str(columns[20].text).replace('\n', ' ')
            V = str(columns[21].text).replace('\n', ' ')
            W = str(columns[22].text).replace('\n', ' ')
            X = str(columns[23].text).replace('\n', ' ')
            Y = str(columns[24].text).replace('\n', ' ')
            Z = str(columns[25].text).replace('\n', ' ')
            A1 = str(columns[26].text).replace('\n', ' ')
            B1 = str(columns[27].text).replace('\n', ' ')
            C1 = str(columns[28].text).replace('\n', ' ')
            D1 = str(columns[29].text).replace('\n', ' ')
            E1 = str(columns[30].text).replace('\n', ' ')            
            F1 = str(columns[31].text).replace('\n', ' ')
            G1 = str(columns[32].text).replace('\n', ' ')
            H1 = str(columns[33].text).replace('\n', ' ')
            J1 = str(columns[34].text).replace('\n', ' ')
            K1 = str(columns[35].text).replace('\n', ' ')
            L1 = str(columns[36].text).replace('\n', ' ')
            M1 = str(columns[37].text).replace('\n', ' ')
            N1 = str(columns[38].text).replace('\n', ' ')
            O1 = str(columns[39].text).replace('\n', ' ')                
        except:
            A = ""  
            B = ""  
            C = ""  
            D = ""  
            E = ""  
            F = ""  
            G = ""  
            H = ""  
            I = ""  
            J = ""  
            K = ""  
            L = ""  
            M = ""  
            N = ""  
            O = ""  
            P = ""  
            Q = ""  
            R = ""  
            S = ""  
            T = ""  
            U = ""  
            V = ""  
            W = ""  
            X = ""  
            Y = ""  
            Z = ""  
            A1 = ""  
            B1 = ""  
            C1 = ""  
            D1 = ""  
            E1 = ""              
            F1 = ""  
            G1 = ""  
            H1 = ""  
            J1 = ""  
            K1 = ""  
            L1 = ""  
            M1 = ""  
            N1 = ""  
            O1 = "" 
        A_list.append(A)
        B_list.append(B)
        C_list.append(C)
        D_list.append(D)
        E_list.append(E)
        F_list.append(F)
        G_list.append(G)
        H_list.append(H)
        I_list.append(I)
        J_list.append(J)
        K_list.append(K)
        L_list.append(L)
        M_list.append(M)
        N_list.append(N)
        O_list.append(O)
        P_list.append(P)
        Q_list.append(Q)
        R_list.append(R)
        S_list.append(S)
        T_list.append(T)
        U_list.append(U)
        V_list.append(V)
        W_list.append(W)
        X_list.append(X)
        Y_list.append(Y)
        Z_list.append(Z)
        A1_list.append(A1)
        B1_list.append(B1)
        C1_list.append(C1)
        D1_list.append(D1)
        E1_list.append(E1)        
        F1_list.append(F1)
        G1_list.append(G1)
        H1_list.append(H1)
        J1_list.append(J1)
        K1_list.append(K1)
        L1_list.append(L1)
        M1_list.append(M1)
        N1_list.append(N1)
        O1_list.append(O1)
try:
    A_list.remove('none')    
    B_list.remove('none')
    C_list.remove('none')
    D_list.remove('none')
    E_list.remove('none')
    F_list.remove('none')
    G_list.remove('none')
    H_list.remove('none')
    I_list.remove('none')
    J_list.remove('none')
    K_list.remove('none')
    L_list.remove('none')
    M_list.remove('none')
    N_list.remove('none')
    O_list.remove('none')
    P_list.remove('none')
    Q_list.remove('none')
    R_list.remove('none')
    S_list.remove('none')
    T_list.remove('none')
    U_list.remove('none')
    V_list.remove('none')
    W_list.remove('none')
    X_list.remove('none')
    Y_list.remove('none')
    Z_list.remove('none')
    A1_list.remove('none')
    B1_list.remove('none')
    C1_list.remove('none')
    D1_list.remove('none')
    E1_list.remove('none')    
    F1_list.remove('none')
    G1_list.remove('none')
    H1_list.remove('none')
    J1_list.remove('none')
    K1_list.remove('none')
    L1_list.remove('none')
    M1_list.remove('none')
    N1_list.remove('none')
    O1_list.remove('none')
except:
    pass    
dict = {'1': Player_list, '2': A_list, '3': B_list, '4': C_list, '5': D_list, '6': E_list, '7': F_list, '8': G_list, '9': H_list, '10': I_list, '11': J_list, '12': K_list,
        '13': L_list, '14': M_list, '15': N_list, '16': O_list, '17': P_list, '18': Q_list, '19': R_list, '20': S_list, '21': T_list, '22': U_list, '23': V_list, '24': W_list,
        '25': X_list, '26': Y_list, '27': Z_list, '28': A1_list, '29': B1_list, '30': C1_list, '31': D1_list, '32': E1_list, '33': F1_list, '34': G1_list, '35': H1_list, '36': J1_list,
        '37': K1_list, '38': L1_list, '39': M1_list, '40': N1_list, '41': O1_list}
# dict = {'1': Player_list, '2': A_list, '3': B_list, '4': C_list, '5': D_list, '6': E_list, '7': F_list, '8': G_list, '9': H_list, '10': I_list, '11': J_list, '12': K_list,
#         '13': L_list, '14': M_list, '15': N_list, '16': O_list, '17': P_list, '18': Q_list, '19': R_list, '20': S_list, '21': T_list, '22': U_list, '23': V_list, '24': W_list,
#         '25': X_list, '26': Y_list, '27': Z_list, '28': A1_list, '29': B1_list, '30': C1_list, '31': D1_list, '32': E1_list}
df = pd.DataFrame(dict)
df.to_csv('Liverpool_foulscommited.csv')     

print('----------------finished-------------------')             

    
while True:
    pass

