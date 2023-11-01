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
driver.get("https://playerstats.football/premier-league")
driver.find_element(By.XPATH, '/html/body/nav/div/div[3]/a[1]').click()
# Find the one page table element
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('oscarthagando@hotmail.com')
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('HiScott!')
driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[4]/button').click()
teams = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div/div/table/tbody/tr/td[1]/div/div[2]/div/a')
for team in teams:
    team_name = team.text
    print(team_name)
    team_URL = team.get_attribute('href')
    print(team_URL)
    driver1 = webdriver.Chrome(options=options)
    driver1.maximize_window()
    driver1.get(team_URL)
    driver1.find_element(By.XPATH, '/html/body/div[2]/nav/div/div[3]/a[1]').click()
# Find the one page table element
    driver1.find_element(By.XPATH, '//*[@id="email"]').send_keys('oscarthagando@hotmail.com')
    driver1.find_element(By.XPATH, '//*[@id="password"]').send_keys('HiScott!')
    driver1.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[4]/button').click()
    driver1.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div[1]/div[1]/div[2]/div/a[2]').click()
    time.sleep(1)
    try:
        driver1.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[2]').click()
        time.sleep(1)
        driver1.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[3]').click()
        time.sleep(1)
        driver1.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[4]').click()
        time.sleep(1)
        driver1.find_element(By.XPATH, '//*[@id="content-wrapper"]/div[1]/div[2]/div/div[1]/div[1]/div/div[5]').click()
        time.sleep(1)
    except:
        pass
    element = driver1.find_element(By.XPATH, '//*[@id="statsFilter"]')
    actions = ActionChains(driver1)
    actions.click(element)  # Perform a click action on the element
    for _ in range(3):
        actions.key_down(Keys.DOWN)  # Press down the "down" key
        actions.key_up(Keys.DOWN)  # Press down the Control key (modify the key if needed)
    actions.key_down(Keys.ENTER)
    actions.key_up(Keys.ENTER)
    actions.perform()  # Perform the action
    time.sleep(1)
    l = 0
    while l<4:
        if l == 0:
            season = '20_21'
        if l == 1:
            season = '21_22'
        if l == 2:
            season = '22_23'
        if l == 3:
            season = '23_24'
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
        Rows = driver1.find_elements(By.XPATH, '//*[@id="content-wrapper"]/div[3]/div/div')

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
                except:
                    A = ""                
                try:
                    B = columns[1].text
                except:
                    B = ""
                try:
                    C = columns[2].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    C = ""
                try:
                    D = columns[3].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    D = ""
                try:
                    E = columns[4].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    E = ""
                try:
                    F = columns[5].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    F = ""
                try:
                    G = columns[6].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    G = ""
                try:
                    H = columns[7].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    H = ""
                try:
                    I = columns[8].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    I = ""
                try:
                    J = columns[9].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    J = ""
                try:
                    K = columns[10].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    K = ""
                try:
                    L = columns[11].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    L = ""
                try:
                    M = columns[12].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    M = ""
                try:
                    N = columns[13].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    N = ""
                try:
                    O = columns[14].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    O = ""
                try:
                    P = columns[15].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    P = ""
                try:
                    Q = columns[16].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    Q = ""
                try:
                    R = columns[17].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    R = ""
                try:
                    S = columns[18].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    S = ""
                try:
                    T = columns[19].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    T = ""
                try:
                    U = columns[20].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    U = ""
                try:
                    V = columns[21].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    V = ""
                try:
                    W = columns[22].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    W = ""
                try:
                    X = columns[23].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    X = ""
                try:
                    Y = columns[24].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    Y = ""
                try:
                    Z = columns[25].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    Z = ""
                try:
                    A1 = columns[26].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    A1 = ""
                try:
                    B1 = columns[27].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    B1 = ""
                try:
                    C1 = columns[28].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    C1 = ""
                try:
                    D1 = columns[29].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    D1 = ""
                try:
                    E1 = columns[30].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    F1 = ""                    
                try:
                    F1 = columns[31].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    F1 = ""
                try:
                    G1 = columns[32].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    G1 = ""
                try:
                    H1 = columns[33].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    H1 = ""
                try:
                    J1 = columns[34].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    J1 = ""
                try:
                    K1 = columns[35].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    K1 = ""
                try:
                    L1 = columns[36].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    L1 = ""
                try:
                    M1 = columns[37].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    M1 = ""
                try:
                    N1 = columns[38].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
                    N1 = ""    
                try:
                    O1 = columns[39].find_element(By.TAG_NAME, 'img').get_attribute('title')
                except:
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
                except:
                    A = ""                
                try:
                    B = str(columns[1].text).replace('\n', ' ')
                except:
                    B = ""
                try:
                    C = str(columns[2].text).replace('\n', ' ')
                except:
                    C = ""
                try:
                    D = str(columns[3].text).replace('\n', ' ')
                except:
                    D = ""
                try:
                    E = str(columns[4].text).replace('\n', ' ')
                except:
                    E = ""
                try:
                    F = str(columns[5].text).replace('\n', ' ')
                except:
                    F = ""
                try:
                    G = str(columns[6].text).replace('\n', ' ')
                except:
                    G = ""
                try:
                    H = str(columns[7].text).replace('\n', ' ')
                except:
                    H = ""
                try:
                    I = str(columns[8].text).replace('\n', ' ')
                except:
                    I = ""
                try:
                    J = str(columns[9].text).replace('\n', ' ')
                except:
                    J = ""
                try:
                    K = str(columns[10].text).replace('\n', ' ')
                except:
                    K = ""
                try:
                    L = str(columns[11].text).replace('\n', ' ')
                except:
                    L = ""
                try:
                    M = str(columns[12].text).replace('\n', ' ')
                except:
                    M = ""
                try:
                    N = str(columns[13].text).replace('\n', ' ')
                except:
                    N = ""
                try:
                    O = str(columns[14].text).replace('\n', ' ')
                except:
                    O = ""
                try:
                    P = str(columns[15].text).replace('\n', ' ')
                except:
                    P = ""
                try:
                    Q = str(columns[16].text).replace('\n', ' ')
                except:
                    Q = ""
                try:
                    R = str(columns[17].text).replace('\n', ' ')
                except:
                    R = ""
                try:
                    S = str(columns[18].text).replace('\n', ' ')
                except:
                    S = ""
                try:
                    T = str(columns[19].text).replace('\n', ' ')
                except:
                    T = ""
                try:
                    U = str(columns[20].text).replace('\n', ' ')
                except:
                    U = ""
                try:
                    V = str(columns[21].text).replace('\n', ' ')
                except:
                    V = ""
                try:
                    W = str(columns[22].text).replace('\n', ' ')
                except:
                    W = ""
                try:
                    X = str(columns[23].text).replace('\n', ' ')
                except:
                    X = ""
                try:
                    Y = str(columns[24].text).replace('\n', ' ')
                except:
                    Y = ""
                try:
                    Z = str(columns[25].text).replace('\n', ' ')
                except:
                    Z = ""
                try:
                    A1 = str(columns[26].text).replace('\n', ' ')
                except:
                    A1 = ""
                try:
                    B1 = str(columns[27].text).replace('\n', ' ')
                except:
                    B1 = ""
                try:
                    C1 = str(columns[28].text).replace('\n', ' ')
                except:
                    C1 = ""
                try:
                    D1 = str(columns[29].text).replace('\n', ' ')
                except:
                    D1 = ""
                try:
                    E1 = str(columns[30].text).replace('\n', ' ')
                except:
                    F1 = ""                    
                try:
                    F1 = str(columns[31].text).replace('\n', ' ')
                except:
                    F1 = ""
                try:
                    G1 = str(columns[32].text).replace('\n', ' ')
                except:
                    G1 = ""
                try:
                    H1 = str(columns[33].text).replace('\n', ' ')
                except:
                    H1 = ""
                try:
                    J1 = str(columns[34].text).replace('\n', ' ')
                except:
                    J1 = ""
                try:
                    K1 = str(columns[35].text).replace('\n', ' ')
                except:
                    K1 = ""
                try:
                    L1 = str(columns[36].text).replace('\n', ' ')
                except:
                    L1 = ""
                try:
                    M1 = str(columns[37].text).replace('\n', ' ')
                except:
                    M1 = ""
                try:
                    N1 = str(columns[38].text).replace('\n', ' ')
                except:
                    N1 = ""    
                try:
                    O1 = str(columns[39].text).replace('\n', ' ')
                except:
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
            A_list = A_list[1:] 
            B_list.remove('')
            C_list.remove('')
            D_list.remove('')
            E_list.remove('')
            F_list.remove('')
            G_list.remove('')
            H_list.remove('')
            I_list.remove('')
            J_list.remove('')
            K_list.remove('')
            L_list.remove('')
            M_list.remove('')
            N_list.remove('')
            O_list.remove('')
            P_list.remove('')
            Q_list.remove('')
            R_list.remove('')
            S_list.remove('')
            T_list.remove('')
            U_list.remove('')
            V_list.remove('')
            W_list.remove('')
            X_list.remove('')
            Y_list.remove('')
            Z_list.remove('')
            A1_list.remove('')
            B1_list.remove('')
            C1_list.remove('')
            D1_list.remove('')
            E1_list.remove('')            
            F1_list.remove('')
            G1_list.remove('')
            H1_list.remove('')
            J1_list.remove('')
            K1_list.remove('')
            L1_list.remove('')
            M1_list.remove('')
            N1_list.remove('')
            O1_list.remove('')
        except:
            pass    
        print(Player_list, A_list, B_list, C_list, D_list, E_list, F_list, G_list, H_list, I_list, J_list, K_list, L_list, M_list, N_list, O_list, P_list, Q_list, R_list, S_list, T_list, 
              U_list, V_list, W_list, X_list, Y_list, Z_list, A1_list, B1_list, C1_list, D1_list, E1_list, F1_list, G1_list, H1_list, J1_list, K1_list, L1_list, M1_list, N1_list, O1_list)
        print(len(Player_list), len(A_list), len(B_list), len(C_list), len(D_list), len(E_list), len(F_list), len(G_list), len(H_list), len(I_list), len(J_list), len(K_list), len(L_list),
          len(M_list), len(N_list), len(O_list), len(P_list), len(Q_list), len(R_list), len(S_list), len(T_list), len(U_list),
           len(V_list), len(W_list), len(X_list), len(Y_list), len(Z_list), len(A1_list), len(B1_list), len(C1_list), len(D1_list), len(E1_list), len(F1_list), len(G1_list),
           len(H1_list), len(J1_list), len(K1_list), len(L1_list), len(M1_list), len(N1_list), len(O1_list)) 
        dict = {'1': Player_list, '2': A_list, '3': B_list, '4': C_list, '5': D_list, '6': E_list, '7': F_list, '8': G_list, '9': H_list, '10': I_list, '11': J_list, '12': K_list,
                '13': L_list, '14': M_list, '15': N_list, '16': O_list, '17': P_list, '18': Q_list, '19': R_list, '20': S_list, '21': T_list, '22': U_list, '23': V_list, '24': W_list,
                '25': X_list, '26': Y_list, '27': Z_list, '28': A1_list, '29': B1_list, '30': C1_list, '31': D1_list, '32': E1_list, '33': F1_list, '34': G1_list, '35': H1_list, '36': J1_list,
                '37': K1_list, '38': L1_list, '39': M1_list, '40': N1_list, '41': O1_list}
        # dict = {'1': Player_list, '2': A_list, '3': B_list, '4': C_list, '5': D_list, '6': E_list, '7': F_list, '8': G_list, '9': H_list, '10': I_list, '11': J_list, '12': K_list,
        #         '13': L_list, '14': M_list, '15': N_list, '16': O_list, '17': P_list, '18': Q_list, '19': R_list, '20': S_list, '21': T_list, '22': U_list, '23': V_list, '24': W_list,
        #         '25': X_list, '26': Y_list, '27': Z_list, '28': A1_list, '29': B1_list, '30': C1_list, '31': D1_list, '32': E1_list}
        df = pd.DataFrame(dict)
        df.to_csv(f'{team_name}_shotsontarget{season}.csv') 
        element1 = driver1.find_element(By.XPATH, '//*[@id="statsFilter"]')
        actions = ActionChains(driver1)
        actions.click(element1)  # Perform a click action on the element
        actions.key_down(Keys.DOWN)  # Press down the "down" key
        actions.key_up(Keys.DOWN)  # Press down the Control key (modify the key if needed)
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)
        actions.perform()  # Perform the action
        l += 1
    driver1.close()
    print('----------------One team finished-------------------')             
print('----------------All team finished-------------------')             

while True:
    pass
    