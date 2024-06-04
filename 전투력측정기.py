import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import random as rd
rd.seed(time.time())

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

st.set_page_config(layout="wide")
def ReturnTrue():
    return True

def SaveFile(Format, Name):
    numbering = rd.randint(1, 100)
    Fname = Name + str(numbering) + '.txt'
    save_path = os.path.join(os.getcwd(), Fname)

    with open(save_path, "wt", encoding="utf8") as file:
        file.write(Format)
        st.success(f'파일 저장에 성공했습니다!\n{save_path}')

if 'PersonList' not in st.session_state:
    st.session_state['PersonList'] = []

if 'PersonDict' not in st.session_state:
    st.session_state['PersonDict'] = {}

Menu = ['프로필 업로드', '전투력 확인', '프로필 파일 만들기', '도움말 및 크레딧']
choice = st.sidebar.selectbox('메뉴', Menu)
if choice == '프로필 업로드':
    st.title('\n\n\n\n\n\n')
    st.divider()
    html_code = """
    <div style="text-align: center;">
        <h1>⚔️</h1>
        <h1>전투력 측정기</h1>
        <p>파일을 업로드해 프로필을 추가해주세요.</p>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
    st.divider()
    uploaded_files = st.file_uploader(
        "양식에 맞는 텍스트 파일을 업로드 해 주세요.",
        type=['txt'],
        accept_multiple_files=False
    )
    if uploaded_files is not None:
        newprofile = {}
        status = {}
        profile_data =uploaded_files.getvalue().decode('utf-8')
        profile_data_list = profile_data.split('\n')
        try:
            name = profile_data_list[0]
            newprofile['age'] = profile_data_list[1]
            newprofile['gender'] = profile_data_list[2]
            newprofile['class'] = profile_data_list[3]
            newprofile['belong'] = profile_data_list[4]
            newprofile['personal color'] = profile_data_list[5]
            newprofile['main weapon'] = profile_data_list[18]
            status['power'] = profile_data_list[6]
            status['health'] = profile_data_list[7]
            status['speed'] = profile_data_list[8]
            status['tenacity'] = profile_data_list[9]
            status['agility'] = profile_data_list[10]
            status['intelligence'] = profile_data_list[11]
            status['mana'] = profile_data_list[12]
            status['attractiveness'] = profile_data_list[13]
            status['concentration'] = profile_data_list[14]
            status['mentality'] = profile_data_list[15]
            status['hangmaryuk'] = profile_data_list[16]
            status['luck'] = profile_data_list[17]
            newprofile['feature'] = profile_data_list[19]
            newprofile['status'] = status
            if name not in st.session_state['PersonList']:
                upload = st.button('업로드', on_click=ReturnTrue)
                if upload:
                    st.session_state['PersonList'].append(name)
                    st.session_state['PersonDict'][name] = newprofile
                    st.success('업로드 성공!')
            else:
                st.error('이미 업로드 된 프로필입니다!')
        except IndexError:
            st.error('올바르지 않은 파일 양식입니다!')
    else:
        st.warning('파일이 없습니다.')

elif choice == '전투력 확인':
    statusscreen,graphscreen = st.columns([1, 5])
    select_person = st.sidebar.selectbox(
        '전투력을 확인할 사람을 선택하세요.',
        st.session_state['PersonList'],
        index=None,
        placeholder='업로드한 프로필 중 선택...'
    )
    with statusscreen:
        if select_person:
            infomessage = """
                            <div style="text-align: center;">
                                <h6>기본정보</h6s>
                            </div>
                            """
            st.write(infomessage, unsafe_allow_html=True)
            st.write(f'이름 : {select_person}')
            st.write('나이 : ' + st.session_state['PersonDict'][select_person]['age'])
            st.write('성별 : '+ st.session_state['PersonDict'][select_person]['gender'])
            st.write('클래스 : '+ st.session_state['PersonDict'][select_person]['class'])
            st.write('소속 : ' + st.session_state['PersonDict'][select_person]['belong'])
            personal_color = '퍼스널 컬러 : <span style="color: '+ st.session_state['PersonDict'][select_person]['personal color'] +';">■</span>'
            st.write(personal_color, unsafe_allow_html=True)
            st.write('주무기 : ' + st.session_state['PersonDict'][select_person]['main weapon'])
            statusmessage = """
                <div style="text-align: center;">
                    <h6>스탯</h6s>
                </div>
                """
            st.write(statusmessage, unsafe_allow_html=True)
            Powdict = {}
            div = list(range(100, -1, -5))
            lev = ['OP', 'S++', 'S+', 'S', 'S-', 'A++', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-','E+', 'E', 'E-', 'O']
            for stat in st.session_state['PersonDict'][select_person]['status']:
                for i in range(len(lev)):
                    if int(st.session_state['PersonDict'][select_person]['status'][stat]) > div[i]:
                        Powdict[stat] = lev[i]
                        break
            STATLIST = ['power', 'health', 'speed', 'tenacity', 'agility', 'intelligence', 'mana', 'attractiveness', 'concentration', 'mentality', 'hangmaryuk', 'luck']
            STATNAME = ['근력🗡️', '체력❤️', '속도👟', '맷집🛡️', '민첩🏃', '지능🗝️', '마력/잠재력🪄', '매력😍', '집중력✏️', '정신력♟️', '항마력👹', '운🍀']
            for i in range(len(STATLIST)):
                st.write(STATNAME[i] + ' :  ' + Powdict[STATLIST[i]] + ' ( ' + st.session_state['PersonDict'][select_person]['status'][STATLIST[i]] + ')')
        else:
            infomessage = """
                                        <div style="text-align: center;">
                                            <h6>기본정보</h6s>
                                        </div>
                                        """
            st.write(infomessage, unsafe_allow_html=True)
            st.write(f'이름 : ?')
            st.write('나이 : ?')
            st.write('성별 : ?')
            st.write('클래스 : ?')
            st.write('소속 : ?')
            personal_color = '퍼스널 컬러 : <span style="color: #505050;">■</span>'
            st.write(personal_color, unsafe_allow_html=True)
            st.write('주무기 : ?')
            statusmessage = """
                            <div style="text-align: center;">
                                <h6>스탯</h6s>
                            </div>
                            """
            st.write(statusmessage, unsafe_allow_html=True)
            STATLIST = ['power', 'health', 'speed', 'tenacity', 'agility', 'intelligence', 'mana', 'attractiveness',
                        'concentration', 'mentality', 'hangmaryuk', 'luck']
            STATNAME = ['근력🗡️', '체력❤️', '속도👟', '맷집🛡️', '민첩🏃', '지능🗝️', '마력/잠재력🪄', '매력😍', '집중력✏️', '정신력♟️', '항마력👹', '운🍀']
            for i in range(len(STATLIST)):
                st.write(STATNAME[i] + ' :  - ( O )')
            pass

    with graphscreen:
        Score1_Boundary, Score2_Boundary, Score3_Boundary, Score4_Boundary, Score5_Boundary, Score6_Boundary = st.columns([1, 1, 1, 1, 1, 1])
        Graph3_Boundary, Graph4_Boundary, Graph5_Boundary = st.columns([1, 1, 1])
        Graph6_Boundary, Feature_Boundary = st.columns([2, 1])
        with Score1_Boundary:
            if select_person:
                PhysicalStatus = [
                            (int(st.session_state['PersonDict'][select_person]['status']['power'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['health'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['speed'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['tenacity'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['agility']))]
                TotalPhysicalStatus = 0
                PhysicalStatus.sort()
                for i in range(1, 6, 1):
                    TotalPhysicalStatus += PhysicalStatus[i-1] * 3
                TotalPhysicalStatus /= 15

                TotalPhysicalScore = 'O'
                div = list(range(100, -1, -5))
                lev = ['OP', 'S++', 'S+', 'S', 'S-', 'A++', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D',
                       'D-', 'E+', 'E', 'E-', 'O']
                for i in range(len(lev)):
                    if TotalPhysicalStatus > div[i]:
                        TotalPhysicalScore = lev[i]
                        break
                st.metric('평균신체등급', TotalPhysicalScore)
            else:
                st.metric('평균신체등급', '-')
        with Score2_Boundary:
            if select_person:
                PhysicalStatus = [
                            (int(st.session_state['PersonDict'][select_person]['status']['power'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['health'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['speed'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['tenacity'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['agility']))]
                TotalPhysicalStatus = 0
                PhysicalStatus.sort()
                for i in range(1, 6, 1):
                    TotalPhysicalStatus += PhysicalStatus[i-1] * i
                TotalPhysicalStatus /= 15

                TotalPhysicalScore = 'O'
                div = list(range(100, -1, -5))
                lev = ['OP', 'S++', 'S+', 'S', 'S-', 'A++', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D',
                       'D-', 'E+', 'E', 'E-', 'O']
                for i in range(len(lev)):
                    if TotalPhysicalStatus > div[i]:
                        TotalPhysicalScore = lev[i]
                        break
                st.metric('최고 신체등급', TotalPhysicalScore)
            else:
                st.metric('최고 신체등급', '-')
        with Score3_Boundary:
            if select_person:
                PhysicalStatus = [
                            (int(st.session_state['PersonDict'][select_person]['status']['power'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['health'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['speed'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['tenacity'])),
                            (int(st.session_state['PersonDict'][select_person]['status']['agility']))]
                TotalPhysicalStatus = 0
                PhysicalStatus.sort(reverse=True)
                for i in range(1, 6, 1):
                    TotalPhysicalStatus += PhysicalStatus[i-1] * i
                TotalPhysicalStatus /= 15

                TotalPhysicalScore = 'O'
                div = list(range(100, -1, -5))
                lev = ['OP', 'S++', 'S+', 'S', 'S-', 'A++', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D',
                       'D-', 'E+', 'E', 'E-', 'O']
                for i in range(len(lev)):
                    if TotalPhysicalStatus > div[i]:
                        TotalPhysicalScore = lev[i]
                        break
                st.metric('최저 신체등급', TotalPhysicalScore)
            else:
                st.metric('최저 신체등급', '-')
        with Score4_Boundary:
            if select_person:
                MentalStatus = [
                    (int(st.session_state['PersonDict'][select_person]['status']['intelligence'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['mana'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['attractiveness'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['concentration'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['mentality'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['hangmaryuk']))]
                TotalMentalStatus = 0
                MentalStatus.sort()
                for i in range(1, 7, 1):
                    TotalMentalStatus += MentalStatus[i - 1] * 3.5
                TotalMentalStatus /= 21

                TotalMentalScore = 'O'
                div = list(range(100, -1, -5))
                lev = ['OP', 'S++', 'S+', 'S', 'S-', 'A++', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+',
                       'D',
                       'D-', 'E+', 'E', 'E-', 'O']
                for i in range(len(lev)):
                    if TotalMentalStatus > div[i]:
                        TotalMentalScore = lev[i]
                        break
                st.metric('평균 정신등급', TotalMentalScore)
            else:
                st.metric('평균 정신등급', '-')
        with Score5_Boundary:
            if select_person:
                MentalStatus = [
                    (int(st.session_state['PersonDict'][select_person]['status']['intelligence'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['mana'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['attractiveness'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['concentration'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['mentality'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['hangmaryuk']))]
                TotalMentalStatus = 0
                MentalStatus.sort()
                for i in range(1, 7, 1):
                    TotalMentalStatus += MentalStatus[i - 1] * i
                TotalMentalStatus /= 21

                TotalMentalScore = 'O'
                div = list(range(100, -1, -5))
                lev = ['OP', 'S++', 'S+', 'S', 'S-', 'A++', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+',
                       'D',
                       'D-', 'E+', 'E', 'E-', 'O']
                for i in range(len(lev)):
                    if TotalMentalStatus > div[i]:
                        TotalMentalScore = lev[i]
                        break
                st.metric('최고 정신등급', TotalMentalScore)
            else:
                st.metric('최고 정신등급', '-')
        with Score6_Boundary:
            if select_person:
                MentalStatus = [
                    (int(st.session_state['PersonDict'][select_person]['status']['intelligence'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['mana'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['attractiveness'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['concentration'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['mentality'])),
                    (int(st.session_state['PersonDict'][select_person]['status']['hangmaryuk']))]
                TotalMentalStatus = 0
                MentalStatus.sort(reverse=True)
                for i in range(1, 7, 1):
                    TotalMentalStatus += MentalStatus[i - 1] * i
                TotalMentalStatus /= 21

                TotalMentalScore = 'O'
                div = list(range(100, -1, -5))
                lev = ['OP', 'S++', 'S+', 'S', 'S-', 'A++', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+',
                       'D',
                       'D-', 'E+', 'E', 'E-', 'O']
                for i in range(len(lev)):
                    if TotalMentalStatus > div[i]:
                        TotalMentalScore = lev[i]
                        break
                st.metric('최저 정신등급', TotalMentalScore)
            else:
                st.metric('최저 정신등급', '-')
        with Graph3_Boundary:
            st.write('스탯 분포 비율')
            categories3 = ['근력', '체력', '속도', '맷집', '민첩', '지능', '마력/잠재력', '매력', '집중력', '정신력', '항마력', '운']
            if select_person:
                status3 = [
                    int(st.session_state['PersonDict'][select_person]['status']['power']),
                    int(st.session_state['PersonDict'][select_person]['status']['health']),
                    int(st.session_state['PersonDict'][select_person]['status']['speed']),
                    int(st.session_state['PersonDict'][select_person]['status']['tenacity']),
                    int(st.session_state['PersonDict'][select_person]['status']['agility']),
                    int(st.session_state['PersonDict'][select_person]['status']['intelligence']),
                    int(st.session_state['PersonDict'][select_person]['status']['mana']),
                    int(st.session_state['PersonDict'][select_person]['status']['attractiveness']),
                    int(st.session_state['PersonDict'][select_person]['status']['concentration']),
                    int(st.session_state['PersonDict'][select_person]['status']['mentality']),
                    int(st.session_state['PersonDict'][select_person]['status']['hangmaryuk']),
                    int(st.session_state['PersonDict'][select_person]['status']['luck'])
                ]
                colors = []
                div = list(range(100, -1, -5))
                col = ['maroon', 'yellow', 'gold', 'goldenrod', 'darkgoldenrod', 'mediumspringgreen', 'springgreen', 'mediumseagreen', 'seagreen', 'royalblue', 'cornflowerblue', 'lightsteelblue', 'violet', 'plum', 'thistle', 'brown', 'indianred',
                       'lightcoral', 'chocolate', 'sandybrown', 'peachpuff', 'white']
                for stat in st.session_state['PersonDict'][select_person]['status']:
                    for i in range(len(col)):
                        if int(st.session_state['PersonDict'][select_person]['status'][stat]) > div[i]:
                            colors.append(col[i])
                            break
                fig, ax = plt.subplots()
                ax.pie(status3, labels=categories3, autopct='%.1f%%', colors=colors)
            else:
                status3 = [1]*12
                fig, ax = plt.subplots()
                ax.pie(status3, labels=categories3, colors=['lightgrey']*12)
            st.pyplot(fig)

        with Graph4_Boundary:
            st.write('신체적 능력')
            comp4 = st.selectbox(
                '비교',
                st.session_state['PersonList'],
                index=None,
                placeholder='비교 대상 선택...'
            )
            categories4 = ['근력', '체력', '속도', '맷집', '민첩']
            categories4 = [*categories4, categories4[0]]
            if select_person:
                status4 = [min(int(st.session_state['PersonDict'][select_person]['status']['power']), 100),
                          min(int(st.session_state['PersonDict'][select_person]['status']['health']), 100),
                          min(int(st.session_state['PersonDict'][select_person]['status']['speed']), 100),
                          min(int(st.session_state['PersonDict'][select_person]['status']['tenacity']), 100),
                          min(int(st.session_state['PersonDict'][select_person]['status']['agility']), 100)]
                status4 = [*status4, status4[0]]

                label_loc = np.linspace(start=0, stop=2*np.pi, num=len(status4))

                colR = (int(st.session_state['PersonDict'][select_person]['personal color'][1:3], 16)+1)/256
                colG = (int(st.session_state['PersonDict'][select_person]['personal color'][3:5], 16)+1)/256
                colB = (int(st.session_state['PersonDict'][select_person]['personal color'][5:7], 16)+1)/256
                fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
                ax.set_ylim(0, 100)
                plt.xticks(label_loc, labels=categories4, fontsize=15)
                ax.plot(label_loc, status4, linestyle='dashed', color=(colR, colG, colB), label=select_person)
                ax.fill(label_loc, status4, color=(colR, colG, colB), alpha=0.75)
                if comp4:
                    status4_ = [min(int(st.session_state['PersonDict'][comp4]['status']['power']), 100),
                               min(int(st.session_state['PersonDict'][comp4]['status']['health']), 100),
                               min(int(st.session_state['PersonDict'][comp4]['status']['speed']), 100),
                               min(int(st.session_state['PersonDict'][comp4]['status']['tenacity']), 100),
                               min(int(st.session_state['PersonDict'][comp4]['status']['agility']), 100)]
                    status4_ = [*status4_, status4_[0]]
                    ncolR = (int(st.session_state['PersonDict'][comp4]['personal color'][1:3], 16) + 1) / 256
                    ncolG = (int(st.session_state['PersonDict'][comp4]['personal color'][3:5], 16) + 1) / 256
                    ncolB = (int(st.session_state['PersonDict'][comp4]['personal color'][5:7], 16) + 1) / 256
                    ax.plot(label_loc, status4_, linestyle='dashed', color=(ncolR, ncolG, ncolB), label=comp4)
                    ax.fill(label_loc, status4_, color=(ncolR, ncolG, ncolB), alpha=0.6)

            else:
                status4 = [50]*5
                status4 = [*status4, status4[0]]
                label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(status4))
                fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
                ax.set_ylim(0, 100)
                plt.xticks(label_loc, labels=categories4, fontsize=15)
                ax.plot(label_loc, status4, linestyle='dashed', color='lightgrey')
                ax.fill(label_loc, status4, color='lightgrey', alpha=1)
            st.pyplot(fig)

        with Graph5_Boundary:
            st.write('정신적 능력')
            comp5 = st.selectbox(
                '비교',
                st.session_state['PersonList'],
                index=None,
                placeholder='비교 대상 선택...',
                key='a'
            )
            categories5 = ['지능', '마력/잠재력', '매력', '집중력', '정신력', '항마력']
            categories5 = [*categories5, categories5[0]]
            if select_person:
                status5 = [min(int(st.session_state['PersonDict'][select_person]['status']['intelligence']), 100),
                          min(int(st.session_state['PersonDict'][select_person]['status']['mana']), 100),
                          min(int(st.session_state['PersonDict'][select_person]['status']['attractiveness']), 100),
                          min(int(st.session_state['PersonDict'][select_person]['status']['concentration']), 100),
                          min(int(st.session_state['PersonDict'][select_person]['status']['mentality']), 100),
                          min(int(st.session_state['PersonDict'][select_person]['status']['hangmaryuk']), 100)]
                status5 = [*status5, status5[0]]

                label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(status5))

                colR = (int(st.session_state['PersonDict'][select_person]['personal color'][1:3], 16) + 1) / 256
                colG = (int(st.session_state['PersonDict'][select_person]['personal color'][3:5], 16) + 1) / 256
                colB = (int(st.session_state['PersonDict'][select_person]['personal color'][5:7], 16) + 1) / 256

                fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
                ax.set_ylim(0, 100)
                plt.xticks(label_loc, labels=categories5, fontsize=15)
                ax.plot(label_loc, status5, linestyle='dashed', color=(colR, colG, colB))
                ax.fill(label_loc, status5, color=(colR, colG, colB), alpha=0.75)
                if comp5:
                    status5_ = [min(int(st.session_state['PersonDict'][comp5]['status']['intelligence']), 100),
                               min(int(st.session_state['PersonDict'][comp5]['status']['mana']), 100),
                               min(int(st.session_state['PersonDict'][comp5]['status']['attractiveness']), 100),
                               min(int(st.session_state['PersonDict'][comp5]['status']['concentration']), 100),
                               min(int(st.session_state['PersonDict'][comp5]['status']['mentality']), 100),
                               min(int(st.session_state['PersonDict'][comp5]['status']['hangmaryuk']), 100)]
                    status5_ = [*status5_, status5_[0]]
                    ncolR = (int(st.session_state['PersonDict'][comp5]['personal color'][1:3], 16) + 1) / 256
                    ncolG = (int(st.session_state['PersonDict'][comp5]['personal color'][3:5], 16) + 1) / 256
                    ncolB = (int(st.session_state['PersonDict'][comp5]['personal color'][5:7], 16) + 1) / 256
                    ax.plot(label_loc, status5_, linestyle='dashed', color=(ncolR, ncolG, ncolB), label=comp5)
                    ax.fill(label_loc, status5_, color=(ncolR, ncolG, ncolB), alpha=0.6)
            else:
                status5 = [50]*6
                status5 = [*status5, status5[0]]
                label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(status5))
                fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
                ax.set_ylim(0, 100)
                plt.xticks(label_loc, labels=categories5, fontsize=15)
                ax.plot(label_loc, status5, linestyle='dashed', color='lightgrey')
                ax.fill(label_loc, status5, color='lightgrey', alpha=1)
            st.pyplot(fig)
        with Graph6_Boundary:
            st.write('전체 스탯 한번에 보기')
            comp6 = st.selectbox(
                '비교',
                st.session_state['PersonList'],
                index=None,
                placeholder='비교 대상 선택...',
                key='b'
            )
            x = np.arange(12)
            categories1 = ['근력', '체력', '속도', '맷집', '민첩', '지능', '마력/잠재력', '매력', '집중력', '정신력', '항마력', '운']
            if select_person:
                status1 = [
                    int(st.session_state['PersonDict'][select_person]['status']['power']),
                    int(st.session_state['PersonDict'][select_person]['status']['health']),
                    int(st.session_state['PersonDict'][select_person]['status']['speed']),
                    int(st.session_state['PersonDict'][select_person]['status']['tenacity']),
                    int(st.session_state['PersonDict'][select_person]['status']['agility']),
                    int(st.session_state['PersonDict'][select_person]['status']['intelligence']),
                    int(st.session_state['PersonDict'][select_person]['status']['mana']),
                    int(st.session_state['PersonDict'][select_person]['status']['attractiveness']),
                    int(st.session_state['PersonDict'][select_person]['status']['concentration']),
                    int(st.session_state['PersonDict'][select_person]['status']['mentality']),
                    int(st.session_state['PersonDict'][select_person]['status']['hangmaryuk']),
                    int(st.session_state['PersonDict'][select_person]['status']['luck'])
                ]
                fig, ax = plt.subplots(figsize=(8, 5))

                if comp6:
                    status2 = [
                        int(st.session_state['PersonDict'][comp6]['status']['power']),
                        int(st.session_state['PersonDict'][comp6]['status']['health']),
                        int(st.session_state['PersonDict'][comp6]['status']['speed']),
                        int(st.session_state['PersonDict'][comp6]['status']['tenacity']),
                        int(st.session_state['PersonDict'][comp6]['status']['agility']),
                        int(st.session_state['PersonDict'][comp6]['status']['intelligence']),
                        int(st.session_state['PersonDict'][comp6]['status']['mana']),
                        int(st.session_state['PersonDict'][comp6]['status']['attractiveness']),
                        int(st.session_state['PersonDict'][comp6]['status']['concentration']),
                        int(st.session_state['PersonDict'][comp6]['status']['mentality']),
                        int(st.session_state['PersonDict'][comp6]['status']['hangmaryuk']),
                        int(st.session_state['PersonDict'][comp6]['status']['luck'])
                    ]

                    ncolR = (int(st.session_state['PersonDict'][comp6]['personal color'][1:3], 16) + 1) / 256
                    ncolG = (int(st.session_state['PersonDict'][comp6]['personal color'][3:5], 16) + 1) / 256
                    ncolB = (int(st.session_state['PersonDict'][comp6]['personal color'][5:7], 16) + 1) / 256

                    bars1 = ax.bar(x - 0.2, status1, width=0.4, label=select_person, color=(colR, colG, colB))
                    bars2 = ax.bar(x + 0.2, status2, width=0.4, label=comp6, color=(ncolR, ncolG, ncolB))
                    ax.set_xticks(x)
                    ax.set_ylim(0, 100)

                else:
                    ax.bar(x, status1, width=0.4, color=(colR, colG, colB))
                    ax.set_xticks(x)
                    ax.set_ylim(0, 100)

                ax.set_xticklabels(categories1, rotation=45, ha="right")
            else:
                status1 = [50]*12
                fig, ax = plt.subplots(figsize=(8, 3.5))
                ax.bar(x, status1, width=0.4, color='lightgrey')
                ax.set_xticks(x)
                ax.set_ylim(0, 100)
                ax.set_xticklabels(categories1, rotation=45, ha="right")
            st.pyplot(fig)
        with Feature_Boundary:
            st.write('특징')
            if select_person:
                st.write(st.session_state['PersonDict'][select_person]['feature'])
            else:
                st.write('-')

elif choice == '프로필 파일 만들기':
    st.title('프로필 파일 만들기')
    st.write('모든 항목이 필수 입력입니다.')
    st.divider()

    name = st.text_input(
        '이름 입력',
        placeholder='7글자 이내로 입력하세요.',
        max_chars=7
    )
    if not name:
        st.write('⚠️항목을 입력하세요!')

    age = st.number_input(
        '나이 입력',
        min_value=1,
        value = 20,
        placeholder='나이를 입력해주세요.'
    )
    if not age:
        st.write('⚠️항목을 입력하세요!')

    sex_list = ['남', '여', 'Others...']
    sex = st.selectbox(
        '성별 선택',
        sex_list,
        index=None,
        placeholder='성별을 선택하세요.'
    )
    if not sex:
        st.write('⚠️항목을 입력하세요!')

    class_list = ['무투가', '마법사', '선생님', '전사', '레인저', '학생', '군인', '서포터', '힐러', '암살자', '기술자', '백수']
    Pclass = st.selectbox(
        '클래스 선택',
        class_list,
        index=None,
        placeholder='클래스를 선택하세요.'
    )
    if not Pclass:
        st.write('⚠️항목을 입력하세요!')

    belong = st.text_input(
        '소속 입력',
        placeholder='25글자 이내로 입력하세요.',
        max_chars=25
    )
    if not belong:
        st.write('⚠️항목을 입력하세요!')

    color = st.color_picker(
        '퍼스널 컬러 선택',
        '#000000'
    )
    if not color:
        st.write('⚠️항목을 입력하세요!')

    weapon = st.text_input(
        '주무기 입력',
        placeholder='20글자 이내로 입력하세요.',
        max_chars=20
    )
    if not weapon:
        st.write('⚠️항목을 입력하세요!')

    st.divider()
    st.write('스탯 입력\n최대치 : 100(이상으로 설정 가능함)')

    power = st.number_input(
        '근력',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not power:
        st.write('⚠️항목을 입력하세요!')

    health = st.number_input(
        '체력',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not health:
        st.write('⚠️항목을 입력하세요!')

    speed = st.number_input(
        '속도',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not speed:
        st.write('⚠️항목을 입력하세요!')

    tenacity = st.number_input(
        '맷집',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not tenacity:
        st.write('⚠️항목을 입력하세요!')

    agility = st.number_input(
        '민첩',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not agility:
        st.write('⚠️항목을 입력하세요!')

    intelligence = st.number_input(
        '지능',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not intelligence:
        st.write('⚠️항목을 입력하세요!')

    mana = st.number_input(
        '마력/잠재력',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not mana:
        st.write('⚠️항목을 입력하세요!')

    attractiveness = st.number_input(
        '매력',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not attractiveness:
        st.write('⚠️항목을 입력하세요!')

    concentration = st.number_input(
        '집중력',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not concentration:
        st.write('⚠️항목을 입력하세요!')

    mentality = st.number_input(
        '정신력',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not mentality:
        st.write('⚠️항목을 입력하세요!')

    hangmaryuk = st.number_input(
        '항마력',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not hangmaryuk:
        st.write('⚠️항목을 입력하세요!')

    luck = st.number_input(
        '운',
        min_value=0,
        value=50,
        placeholder='값을 입력해주세요.'
    )
    if not luck:
        st.write('⚠️항목을 입력하세요!')

    st.divider()

    feature = st.text_area(
        '특징 입력',
        placeholder='특징을 입력하세요.',
        height=100
    )
    if not feature:
        st.write('⚠️항목을 입력하세요!')

    st.divider()

    ItemList = [name, age, sex, Pclass, belong, color, power, health ,speed ,tenacity ,agility ,intelligence ,mana ,attractiveness ,concentration ,mentality ,hangmaryuk ,luck, weapon, feature]
    FileFormat = ''
    for txt in ItemList:
        FileFormat += str(txt) + '\n'
    if name and  age and  sex and  Pclass and  belong and  color and  power and  health  and speed  and tenacity  and agility  and intelligence  and mana  and attractiveness  and concentration  and mentality  and hangmaryuk  and luck and  weapon and  feature:
        save = st.button(
            '컴퓨터에 저장',
            type='primary',
            on_click=SaveFile,
            kwargs=dict(Format=FileFormat, Name=name)
        )
elif choice == '도움말 및 크레딧':
    st.divider()
    html_code = """
    <div style="text-align: center;">
        <h1>⚔️</h1>
        <h1>전투력 측정기</h1>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)
    st.divider()
    st.title('도움말')
    st.write('-전투력 확인')
    st.write('  1.프로필 업로드 창으로 들어간다.')
    st.write('  2.중앙에 browse file 버튼을 눌러 컴퓨터에서 원하는 파일을 가져온다.')
    st.write('  3.업로드 버튼을 누르고, 초록색 영역이 생기는지 확인한다.')
    st.write('  4.전투력 확인 창으로 들어가 업로드한 프로필 중 원하는 프로필을 선택한다.')
    st.write('  5.비교를 선택해 다른 프로필과 비교할 수 있다.')
    st.write('')
    st.write('-프로필 만들기')
    st.write('  1.프로필 파일 만들기 창으로 들어간다.')
    st.write('  2.모든 양식을 꼼꼼히 작성한다.')
    st.write('  3.컴퓨터에 저장 버튼을 누르고, 최상단에 초록색 영역이 생기는지 확인한다.')
    st.write('  4.초록색 영역에 뜨는 경로로 찾아가 파일이 제대로 저장되었는지 확인한다.')
    st.divider()
    st.title('크레딧')
    st.write('Chat GPT(MatplotLib 코드 참고용)')