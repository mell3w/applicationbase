import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import main
from main import Workers
from datetime import datetime





def get_db_connection():
    conn = sqlite3.connect('mirodom.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_mirodom(mirodom_id):
    conn = get_db_connection()

    mirodom = conn.execute('SELECT * FROM mirodom WHERE id = ?',
                           (mirodom_id,)).fetchone()
    conn.close()

    if mirodom is None:
        abort(404)
    return mirodom

    #kolvo = conn.execute('''SELECT COUNT(address) FROM mirodom WHERE status='Открыта' and id = ?''',
                         #(mirodom_id,))
    #conn.close()
    #return render_template('mirodom.html', kolvo=kolvo)


app=Flask(__name__)
app.config['SECRET_KEY']='a1d123od1i04jfn04h'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)


@app.route('/')
def index():
    conn = get_db_connection()
    mirodom = conn.execute('SELECT * FROM mirodom').fetchall()
    conn.close()
    return render_template('index.html', mirodom = mirodom)



@app.route('/nikolaym')
def nikolaym():
    conn = get_db_connection()
    mirodom= conn.execute('''SELECT * FROM mirodom WHERE master ='Николай М.' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv = con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Николай М.' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Николай М.' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Николай М.' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    sdaet=str(c-c1)

    # =====================================================================================================

    rdall = 26
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Николай М.' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall-rd)

    # =====================================================================================================

    mfall = 139+100
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Николай М.' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall-mf)

    # =====================================================================================================

    tmall = 12
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Николай М.' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall-tm)

    # =====================================================================================================

    ykp7all = 7+2+7
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Николай М.' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 7+6+3+10+7
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Николай М.' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    conn.close()
    return render_template('nikolaym.html', mirodom = mirodom, kolvo=kolvo, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#def timeclosenm(id):
    #mirodom=get_mirodom(id)
    #conn = get_db_connection()
    #connt = conn.execute('''UPDATE mirodom SET closingdate''', [[datetime.utcnow()]])
    #return render_template('nikolaym.html', connt=connt)


@app.route('/nikolaymready')
def nikolaymready():
    #nikolam = "Николай М."
    conn = get_db_connection()
    mirodom= conn.execute('''SELECT * FROM mirodom WHERE master ='Николай М.' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Николай М.' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Николай М.' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    # =====================================================================================================

    sdaet = str(c - c1)
    # ======================================================================================================

    # =====================================================================================================

    rdall = 26
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Николай М.' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 139+100
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Николай М.' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 12
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Николай М.' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 7+2+7
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Николай М.' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 7+6+3+10+7
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Николай М.' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    return render_template('nikolaymready.html', mirodom = mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#==============================================================================================================
@app.route('/nikolaymvsevolzhsk')
def nikolaymvsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymvsevolzhsk.html', mirodom=mirodom)

@app.route('/nikolaympetr')
def nikolaympetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaympetr.html', mirodom=mirodom)

@app.route('/nikolaymvfrunza')
def nikolaymfrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymfrunza.html', mirodom=mirodom)

@app.route('/nikolaymprim')
def nikolaymprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymprim.html', mirodom=mirodom)

@app.route('/nikolaymzanevka')
def nikolaymzanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymzanevka.html', mirodom=mirodom)

@app.route('/nikolaymkolt')
def nikolaymkolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymkolt.html', mirodom=mirodom)

@app.route('/nikolaymstaraya')
def nikolaymstaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymstaraya.html', mirodom=mirodom)

@app.route('/nikolaymkyz')
def nikolaymkyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymkyz.html', mirodom=mirodom)

@app.route('/nikolaymkalin')
def nikolaymkalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymkalin.html', mirodom=mirodom)

@app.route('/nikolaymohta')
def nikolaymohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymohta.html', mirodom=mirodom)

@app.route('/nikolaymraz')
def nikolaymraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymraz.html', mirodom=mirodom)

@app.route('/nikolaymsheg')
def nikolaymsheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymsheg.html', mirodom=mirodom)

@app.route('/nikolaymyanino')
def nikolaymyanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Николай М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaymyanino.html', mirodom=mirodom)

@app.route('/nikolaymadressfiltr')
def nikolaymadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Николай М.' ''').fetchall()
    conn.close()
    return render_template('nikolaymadressfiltr.html', mirodom=mirodom)

#=====================================================================================================================================================================================


@app.route('/andrew')
def andrew():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Андрей' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv= con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Андрей' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Андрей' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Андрей' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    sdaet = str(c-c1)

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Андрей' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Андрей' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Андрей' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Андрей' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Андрей' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)




    return render_template('andrew.html', mirodom=mirodom, kolvo=kolvo, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)


@app.route('/andrewr')
def andrewr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Андрей' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Андрей' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Андрей' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    sdaet = str(c-c1)

    # =====================================================================================================

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Андрей' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Андрей' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Андрей' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Андрей' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Андрей' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    # ======================================================================================================

    return render_template('andrewr.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#==============================================================================================================
@app.route('/andrewvsevolzhsk')
def andrewvsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewvsevolzhsk.html', mirodom=mirodom)

@app.route('/andrewpetr')
def andrewpetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewpetr.html', mirodom=mirodom)

@app.route('/andrewvfrunza')
def andrewfrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewfrunza.html', mirodom=mirodom)

@app.route('/andrewprim')
def andrewprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewprim.html', mirodom=mirodom)

@app.route('/andrewzanevka')
def andrewzanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewzanevka.html', mirodom=mirodom)

@app.route('/andrewkolt')
def andrewkolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewkolt.html', mirodom=mirodom)

@app.route('/andrewstaraya')
def andrewstaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewstaraya.html', mirodom=mirodom)

@app.route('/andrewkyz')
def andrewkyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewkyz.html', mirodom=mirodom)

@app.route('/andrewkalin')
def andrewkalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewkalin.html', mirodom=mirodom)

@app.route('/andrewohta')
def andrewohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewvohta.html', mirodom=mirodom)

@app.route('/andrewraz')
def andrewraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewraz.html', mirodom=mirodom)

@app.route('/andrewsheg')
def andrewsheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewsheg.html', mirodom=mirodom)

@app.route('/andrewyanino')
def andrewyanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Андрей' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('andrewyanino.html', mirodom=mirodom)

@app.route('/andreadressfiltr')
def andreadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Андрей' ''').fetchall()
    conn.close()
    return render_template('andreadressfiltr.html', mirodom=mirodom)

#=====================================================================================================================================================================================

@app.route('/michael')
def michael():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Михаил' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv = con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Михаил' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Михаил' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Михаил' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)
    sdaet = str(c-c1)

    conn.close()

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Михаил' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Михаил' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Михаил' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Михаил' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Михаил' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    return render_template('michael.html', mirodom=mirodom, kolvo=kolvo ,dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

@app.route('/michaelr')
def michaelr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Михаил' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

#======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Михаил' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)


#=====================================================================================================


    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Михаил' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

#=====================================================================================================

    sdaet = str(c-c1)
#======================================================================================================

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Михаил' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Михаил' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Михаил' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Михаил' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Михаил' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)


    return render_template('michaelr.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)


@app.route('/michaelvsevolzhsk')
def michaelvsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelvsevolzhsk.html', mirodom=mirodom)

@app.route('/michaelpetr')
def michaelpetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelpetr.html', mirodom=mirodom)

@app.route('/michaelvfrunza')
def michaelfrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelfrunza.html', mirodom=mirodom)

@app.route('/michaelprim')
def michaelprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelprim.html', mirodom=mirodom)

@app.route('/michaelzanevka')
def michaelwzanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelzanevka.html', mirodom=mirodom)

@app.route('/michaelkolt')
def michaelkolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelwkolt.html', mirodom=mirodom)

@app.route('/michaelstaraya')
def michaelstaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelstaraya.html', mirodom=mirodom)

@app.route('/michaelkyz')
def michaelkyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelkyz.html', mirodom=mirodom)

@app.route('/michaelkalin')
def michaelkalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelkalin.html', mirodom=mirodom)

@app.route('/michaelohta')
def michaelohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelohta.html', mirodom=mirodom)

@app.route('/michaelraz')
def michaelraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelraz.html', mirodom=mirodom)

@app.route('/michaelsheg')
def michaelsheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelsheg.html', mirodom=mirodom)

@app.route('/michaelyanino')
def michaelyanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Михаил' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('michaelyanino.html', mirodom=mirodom)

@app.route('/michaeladressfiltr')
def michaeladressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Михаил' ''').fetchall()
    conn.close()
    return render_template('michaeladressfiltr.html', mirodom=mirodom)


@app.route('/german')
def german():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Герман' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv = con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Герман' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Герман' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Герман' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    sdaet=str(c-c1)

    # =====================================================================================================

    # =====================================================================================================

    rdall = 16
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Герман' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 132+20+32
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Герман' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 11
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Герман' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 10+5
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Герман' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 10+7
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Герман' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    conn.close()
    return render_template('german.html', mirodom=mirodom, kolvo=kolvo, dengi=dengi, prem=prem,sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

@app.route('/germanr')
def germanr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Герман' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Герман' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Герман' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    # =====================================================================================================

    sdaet = str(c-c1)
    # ======================================================================================================

    rdall = 16
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Герман' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 132+20+32
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Герман' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 11
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Герман' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 10+5
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Герман' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 10+7
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Герман' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    conn.close()

    return render_template('germanr.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#=======================================================================================================================

@app.route('/germanvsevolzhsk')
def germanvsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germanvsevolzhsk.html', mirodom=mirodom)

@app.route('/germanpetr')
def germanpetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germanpetr.html', mirodom=mirodom)

@app.route('/germanfrunza')
def germanfrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germanfrunza.html', mirodom=mirodom)

@app.route('/germanprim')
def germanprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germanprim.html', mirodom=mirodom)

@app.route('/germanzanevka')
def germanzanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germanzanevka.html', mirodom=mirodom)

@app.route('/germankolt')
def germankolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germankolt.html', mirodom=mirodom)

@app.route('/germanstaraya')
def germanstaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germanstaraya.html', mirodom=mirodom)

@app.route('/germankyz')
def germankyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germankyz.html', mirodom=mirodom)

@app.route('/germankalin')
def germankalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germankalin.html', mirodom=mirodom)

@app.route('/germanohta')
def germanohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germanohta.html', mirodom=mirodom)

@app.route('/germanraz')
def germanraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germanraz.html', mirodom=mirodom)

@app.route('/germansheg')
def germansheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germansheg.html', mirodom=mirodom)

@app.route('/germanyanino')
def germanyanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Герман' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('germanyanino.html', mirodom=mirodom)

@app.route('/germanadressfiltr')
def germanadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Герман' ''').fetchall()
    conn.close()
    return render_template('germanadressfiltr.html', mirodom=mirodom)

#========================================================================================================================

@app.route('/nikolaysemenov')
def nikolaysemenov():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Николай С.' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv = con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Николай С.' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Николай С.' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Николай С.'  AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = c1

    sdaet=str(c-c1)


    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Николай С.' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 66+5+30
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Николай С.' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Николай С.' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 2+5
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Николай С.' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 2+2+5+3
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Николай С.' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)



    conn.close()
    return render_template('nikolaysemenov.html', mirodom=mirodom, kolvo=kolvo, dengi=dengi, prem=prem,sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

@app.route('/nikolaysemenovready')
def nikolaysemenovready():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Николай С.' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Николай С.' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Николай С.' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    # =====================================================================================================

    sdaet = str(c-c1)
    # ======================================================================================================
    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Николай С.' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 66+5+30
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Николай С.' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Николай С.' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 2+5
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Николай С.' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 2+2+5+3
    
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Николай С.' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    return render_template('nikolaysemenovready.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#=======================================================================================================================

@app.route('/nikolaysemenovvsevolzhsk')
def nikolaysemenovvsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovvsevolzhsk.html', mirodom=mirodom)

@app.route('/nikolaysemenovpetr')
def nikolaysemenovpetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovpetr.html', mirodom=mirodom)

@app.route('/nikolaysemenovfrunza')
def nikolaysemenovfrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovfrunza.html', mirodom=mirodom)

@app.route('/nikolaysemenovprim')
def nikolaysemenovprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovprim.html', mirodom=mirodom)

@app.route('/nikolaysemenovzanevka')
def nikolaysemenovzanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovzanevka.html', mirodom=mirodom)

@app.route('/nikolaysemenovkolt')
def nikolaysemenovkolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovkolt.html', mirodom=mirodom)

@app.route('/nikolaysemenovstaraya')
def nikolaysemenovstaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovstaraya.html', mirodom=mirodom)

@app.route('/nikolaysemenovkyz')
def nikolaysemenovkyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovkyz.html', mirodom=mirodom)

@app.route('/nikolaysemenovkalin')
def nikolaysemenovkalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovkalin.html', mirodom=mirodom)

@app.route('/nikolaysemenovohta')
def nikolaysemenovohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovohta.html', mirodom=mirodom)

@app.route('/nikolaysemenovraz')
def nikolaysemenovraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovraz.html', mirodom=mirodom)

@app.route('/nikolaysemenovsheg')
def nikolaysemenovsheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovsheg.html', mirodom=mirodom)

@app.route('/nikolaysemenovyanino')
def nikolaysemenovyanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Николай С.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovyanino.html', mirodom=mirodom)

@app.route('/nikolaysemenovadressfiltr')
def nikolaysemenovadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Николай С.' ''').fetchall()
    conn.close()
    return render_template('nikolaysemenovadressfiltr.html', mirodom=mirodom)

#========================================================================================================================


@app.route('/ilya')
def ilya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Илья' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv = con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Илья' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Илья' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Илья' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)
    sdaet=str(c-c1)

    # =====================================================================================================

    rdall = 6
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Илья' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 7+130
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Илья' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 5
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Илья' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Илья' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 3+4+10
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Илья' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    conn.close()
    return render_template('ilya.html', mirodom=mirodom, kolvo=kolvo,dengi=dengi, prem=prem,sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

@app.route('/ilyar')
def ilyar():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Илья' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Илья' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Илья' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    # =====================================================================================================

    sdaet = str(c-c1)
    # ======================================================================================================

    # =====================================================================================================

    rdall = 6
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Илья' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 7+130
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Илья' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 5
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Илья' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Илья' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 3+4+10
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Илья' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    return render_template('ilyar.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#=======================================================================================================================

@app.route('/ilyavsevolzhsk')
def ilyavsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyavsevolzhsk.html', mirodom=mirodom)

@app.route('/ilyapetr')
def ilyapetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyapetr.html', mirodom=mirodom)

@app.route('/ilyafrunza')
def ilyafrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyafrunza.html', mirodom=mirodom)

@app.route('/ilyaprim')
def ilyaprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyaprim.html', mirodom=mirodom)

@app.route('/ilyazanevka')
def ilyazanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyazanevka.html', mirodom=mirodom)

@app.route('/ilyakolt')
def ilyakolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyakolt.html', mirodom=mirodom)

@app.route('/ilyastaraya')
def ilyastaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyastaraya.html', mirodom=mirodom)

@app.route('/ilyakyz')
def ilyakyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyakyz.html', mirodom=mirodom)

@app.route('/ilyakalin')
def ilyakalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyakalin.html', mirodom=mirodom)

@app.route('/ilyaohta')
def ilyaohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyaohta.html', mirodom=mirodom)

@app.route('/ilyaraz')
def ilyaraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyaraz.html', mirodom=mirodom)

@app.route('/ilyasheg')
def ilyasheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyasheg.html', mirodom=mirodom)

@app.route('/ilyayanino')
def ilyayanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Илья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ilyayanino.html', mirodom=mirodom)

@app.route('/ilyaadressfiltr')
def ilyaadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Илья' ''').fetchall()
    conn.close()
    return render_template('ilyaadressfiltr.html', mirodom=mirodom)

#========================================================================================================================

@app.route('/dmitriy')
def dmitriy():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Дмитрий' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv = con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Дмитрий' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)
    sdaet=str(c-c1)

    # =====================================================================================================

    rdall = 7
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 17
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 6
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 1
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 2+10
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    conn.close()
    return render_template('dmitriy.html', mirodom=mirodom, kolvo=kolvo, dengi=dengi, prem=prem,sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

@app.route('/dmitriyr')
def dmitriyr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Дмитрий' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    # =====================================================================================================

    sdaet = str(c-c1)
    # ======================================================================================================

    # =====================================================================================================

    rdall = 7
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 17
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 6
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 1
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 2+10
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Дмитрий' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    return render_template('dmitriyr.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#=======================================================================================================================

@app.route('/dmitriyvsevolzhsk')
def dmitriyvsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriyvsevolzhsk.html', mirodom=mirodom)

@app.route('/dmitriypetr')
def dmitriypetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriypetr.html', mirodom=mirodom)

@app.route('/dmitriyfrunza')
def dmitriyfrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriyfrunza.html', mirodom=mirodom)

@app.route('/dmitriyprim')
def dmitriyprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriyprim.html', mirodom=mirodom)

@app.route('/dmitriyzanevka')
def dmitriyzanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriyzanevka.html', mirodom=mirodom)

@app.route('/dmitriykolt')
def dmitriykolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriykolt.html', mirodom=mirodom)

@app.route('/dmitriystaraya')
def dmitriystaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriystaraya.html', mirodom=mirodom)

@app.route('/dmitriykyz')
def dmitriykyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriykyz.html', mirodom=mirodom)

@app.route('/dmitriykalin')
def dmitriykalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriykalin.html', mirodom=mirodom)

@app.route('/dmitriyohta')
def dmitriyohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriyohta.html', mirodom=mirodom)

@app.route('/dmitriyraz')
def dmitriyraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriyraz.html', mirodom=mirodom)

@app.route('/dmitriysheg')
def dmitriysheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriysheg.html', mirodom=mirodom)

@app.route('/dmitriyyanino')
def dmitriyyanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Дмитрий' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('dmitriyyanino.html', mirodom=mirodom)

@app.route('/dmitriyadressfiltr')
def dmitriyadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Дмитрий' ''').fetchall()
    conn.close()
    return render_template('dmitriyadressfiltr.html', mirodom=mirodom)

#========================================================================================================================

@app.route('/gena')
def gena():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Гена' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv = con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Гена' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Гена' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Гена' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    sdaet=str(c-c1)

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Гена' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Гена' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Гена' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Гена' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Гена' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    conn.close()
    return render_template('gena.html', mirodom=mirodom, kolvo=kolvo,dengi=dengi, prem=prem,sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

@app.route('/genar')
def genar():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Гена' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Гена' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Гена' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    # =====================================================================================================

    sdaet = str(c-c1)
    # ======================================================================================================

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Гена' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Гена' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Гена' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Гена' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Гена' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    return render_template('genar.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#=======================================================================================================================

@app.route('/genavsevolzhsk')
def genavsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genavsevolzhsk.html', mirodom=mirodom)

@app.route('/genapetr')
def genapetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genapetr.html', mirodom=mirodom)

@app.route('/genafrunza')
def genafrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genafrunza.html', mirodom=mirodom)

@app.route('/genaprim')
def genaprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genaprim.html', mirodom=mirodom)

@app.route('/genazanevka')
def genazanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genazanevka.html', mirodom=mirodom)

@app.route('/genakolt')
def genakolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genakolt.html', mirodom=mirodom)

@app.route('/genastaraya')
def genastaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genastaraya.html', mirodom=mirodom)

@app.route('/genakyz')
def genakyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genakyz.html', mirodom=mirodom)

@app.route('/genakalin')
def genakalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genakalin.html', mirodom=mirodom)

@app.route('/genaohta')
def genaohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genaohta.html', mirodom=mirodom)

@app.route('/genaraz')
def genaraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genaraz.html', mirodom=mirodom)

@app.route('/genasheg')
def genasheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genasheg.html', mirodom=mirodom)

@app.route('/genayanino')
def genayanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Гена' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('genayanino.html', mirodom=mirodom)

@app.route('/genaadressfiltr')
def genaadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Гена' ''').fetchall()
    conn.close()
    return render_template('genaadressfiltr.html', mirodom=mirodom)

#========================================================================================================================



@app.route('/im')
def im():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Илья М.' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv= con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Илья М.' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Илья М.' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Илья М.' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    sdaet=str(c-c1)
    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Илья М.' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Илья М.' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Илья М.' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Илья М.' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Илья М.' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    return render_template('im.html', mirodom=mirodom, kolvo=kolvo,dengi=dengi, prem=prem,sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)


@app.route('/imr')
def imr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Илья М.' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Илья М.' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Илья М.' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    # =====================================================================================================

    sdaet = str(c-c1)
    # ======================================================================================================

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Илья М.' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Илья М.' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Илья М.' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Илья М.' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Илья М.' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    return render_template('imr.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#=======================================================================================================================

@app.route('/imvsevolzhsk')
def imvsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imvsevolzhsk.html', mirodom=mirodom)

@app.route('/impetr')
def impetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('impetr.html', mirodom=mirodom)

@app.route('/imfrunza')
def imfrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imfrunza.html', mirodom=mirodom)

@app.route('/imprim')
def imprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imprim.html', mirodom=mirodom)

@app.route('/imzanevka')
def imzanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imzanevka.html', mirodom=mirodom)

@app.route('/imkolt')
def imkolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imkolt.html', mirodom=mirodom)

@app.route('/imstaraya')
def imstaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imstaraya.html', mirodom=mirodom)

@app.route('/imkyz')
def imkyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imkyz.html', mirodom=mirodom)

@app.route('/imkalin')
def imkalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imkalin.html', mirodom=mirodom)

@app.route('/imohta')
def imohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imohta.html', mirodom=mirodom)

@app.route('/imraz')
def imraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imraz.html', mirodom=mirodom)

@app.route('/imsheg')
def imsheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imsheg.html', mirodom=mirodom)

@app.route('/imyanino')
def imyanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Илья М.' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('imyanino.html', mirodom=mirodom)

@app.route('/imadressfiltr')
def imadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Илья М.' ''').fetchall()
    conn.close()
    return render_template('imadressfiltr.html', mirodom=mirodom)

#========================================================================================================================


@app.route('/nina')
def nina():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Нина' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv= con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Нина' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Нина' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Нина' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    sdaet=str(c-c1)

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Нина' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Нина' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Нина' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Нина' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Нина' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)


    return render_template('nina.html', mirodom=mirodom, kolvo=kolvo, dengi=dengi, prem=prem,sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)


@app.route('/ninar')
def ninar():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Нина' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Нина' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Нина' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    # =====================================================================================================

    sdaet = str(c-c1)
    # ======================================================================================================

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Нина' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Нина' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Нина' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Нина' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Нина' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    return render_template('ninar.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#=======================================================================================================================

@app.route('/ninavsevolzhsk')
def ninavsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninavsevolzhsk.html', mirodom=mirodom)

@app.route('/ninapetr')
def ninapetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninapetr.html', mirodom=mirodom)

@app.route('/ninafrunza')
def ninafrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninafrunza.html', mirodom=mirodom)

@app.route('/ninaprim')
def ninaprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninarim.html', mirodom=mirodom)

@app.route('/ninazanevka')
def ninazanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninazanevka.html', mirodom=mirodom)

@app.route('/ninakolt')
def ninakolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninakolt.html', mirodom=mirodom)

@app.route('/ninastaraya')
def ninastaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninastaraya.html', mirodom=mirodom)

@app.route('/ninakyz')
def ninakyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninakyz.html', mirodom=mirodom)

@app.route('/ninakalin')
def ninakalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninakalin.html', mirodom=mirodom)

@app.route('/ninaohta')
def ninaohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninaohta.html', mirodom=mirodom)

@app.route('/ninaraz')
def ninaraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninaraz.html', mirodom=mirodom)

@app.route('/ninasheg')
def ninasheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninasheg.html', mirodom=mirodom)

@app.route('/ninayanino')
def ninayanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Нина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('ninayanino.html', mirodom=mirodom)

@app.route('/ninaadressfiltr')
def ninaadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Нина' ''').fetchall()
    conn.close()
    return render_template('ninaadressfiltr.html', mirodom=mirodom)

#========================================================================================================================

@app.route('/natalia')
def natalia():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Наталья' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv= con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Наталья' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Наталья' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Наталья' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)
    sdaet=str(c-c1)

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Наталья' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Наталья' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Наталья' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Наталья' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Наталья' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all - ykp12)

    return render_template('natalia.html', mirodom=mirodom, kolvo=kolvo,dengi=dengi, prem=prem,sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)


@app.route('/nataliar')
def nataliar():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Наталья' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Наталья' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Наталья' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    # =====================================================================================================

    sdaet = str(c-c1)
    # ======================================================================================================

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Наталья' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Наталья' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Наталья' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Наталья' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Наталья' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all-ykp12)

    return render_template('nataliar.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#=======================================================================================================================

@app.route('/nataliavsevolzhsk')
def nataliavsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliavsevolzhsk.html', mirodom=mirodom)

@app.route('/nataliapetr')
def nataliapetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliapetr.html', mirodom=mirodom)

@app.route('/nataliafrunza')
def nataliafrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliafrunza.html', mirodom=mirodom)

@app.route('/nataliaprim')
def nataliaprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliarim.html', mirodom=mirodom)

@app.route('/nataliazanevka')
def nataliazanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliazanevka.html', mirodom=mirodom)

@app.route('/nataliakolt')
def nataliakolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliakolt.html', mirodom=mirodom)

@app.route('/nataliastaraya')
def nataliastaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliastaraya.html', mirodom=mirodom)

@app.route('/nataliakyz')
def nataliakyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliakyz.html', mirodom=mirodom)

@app.route('/nataliakalin')
def nataliakalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliakalin.html', mirodom=mirodom)

@app.route('/nataliaohta')
def nataliaohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliaohta.html', mirodom=mirodom)

@app.route('/nataliaraz')
def nataliaraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliaraz.html', mirodom=mirodom)

@app.route('/nataliasheg')
def nataliasheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliasheg.html', mirodom=mirodom)

@app.route('/nataliayanino')
def nataliayanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Наталья' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('nataliayanino.html', mirodom=mirodom)

@app.route('/nataliaadressfiltr')
def nataliaadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Наталья' ''').fetchall()
    conn.close()
    return render_template('nataliaadressfiltr.html', mirodom=mirodom)

#========================================================================================================================

@app.route('/yana')
def yana():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Янина' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv= con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Янина' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Янина' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Янина' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)
    sdaet=str(c-c1)

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Янина' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Янина' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Янина' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Янина' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Янина' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all-ykp12)

    return render_template('yana.html', mirodom=mirodom, kolvo=kolvo, dengi=dengi, prem=prem,sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)


@app.route('/yanar')
def yanar():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Янина' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Янина' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Янина' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    # =====================================================================================================

    sdaet = str(c-c1)
    # ======================================================================================================

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Янина' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Янина' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Янина' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Янина' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Янина' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all-ykp12)

    return render_template('yanar.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#=======================================================================================================================

@app.route('/yanavsevolzhsk')
def yanavsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanavsevolzhsk.html', mirodom=mirodom)

@app.route('/yanapetr')
def yanapetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanapetr.html', mirodom=mirodom)

@app.route('/yanafrunza')
def yanafrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanafrunza.html', mirodom=mirodom)

@app.route('/yanaprim')
def yanaprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanarim.html', mirodom=mirodom)

@app.route('/yanazanevka')
def yanazanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanazanevka.html', mirodom=mirodom)

@app.route('/yanakolt')
def yanakolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanakolt.html', mirodom=mirodom)

@app.route('/yanastaraya')
def yanastaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanastaraya.html', mirodom=mirodom)

@app.route('/yanakyz')
def yanakyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanakyz.html', mirodom=mirodom)

@app.route('/yanakalin')
def yanakalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanakalin.html', mirodom=mirodom)

@app.route('/yanaohta')
def yanaohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanaohta.html', mirodom=mirodom)

@app.route('/yanaraz')
def yanaraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanaraz.html', mirodom=mirodom)

@app.route('/yanasheg')
def yanasheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanasheg.html', mirodom=mirodom)

@app.route('/yanayanino')
def yanayanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Янина' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('yanayanino.html', mirodom=mirodom)

@app.route('/yanaadressfiltr')
def yanaadressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Янина' ''').fetchall()
    conn.close()
    return render_template('yanaadressfiltr.html', mirodom=mirodom)

#========================================================================================================================

@app.route('/vl')
def vl():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Владимир' AND status='Открыта' ORDER BY timestamp ASC ''').fetchall()

    cons = sqlite3.connect('mirodom.db')
    con = cons.cursor()

    kolv= con.execute('''SELECT COUNT(address) FROM mirodom WHERE master='Владимир' AND status='Открыта' ''')
    kolvo = kolv.fetchone()
    conn.close()

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Владимир' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Владимир' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)

    sdaet=str(c-c1)

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Владимир' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Владимир' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Владимир' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Владимир' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Владимир' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all-ykp12)


    return render_template('vl.html', mirodom=mirodom, kolvo=kolvo, dengi=dengi, prem=prem,sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)


@app.route('/vlr')
def vlr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Владимир' AND status='Выполнена' ORDER BY closingdate DESC ''').fetchall()
    conn.close()

    # ======================================================================================================================

    fcon = sqlite3.connect('mirodom.db')
    fc = fcon.cursor()
    f = fc.execute('''SELECT money FROM mirodom WHERE master='Владимир' AND status='Выполнена' AND sdal='false' ''')
    fr = f.fetchall()
    c = 0
    for x in fr:
        c = sum(i[0] for i in fr)

    dengi = str(c)

    # =====================================================================================================

    f1 = fc.execute('''SELECT price FROM mirodom WHERE master='Владимир' AND status='Выполнена' AND sdal='false' ''')
    fr1 = f1.fetchall()
    c1 = 0
    for x in fr1:
        c1 = sum(i[0] for i in fr1)

    prem = str(c1)
    sdaet=str(c-c1)

    # =====================================================================================================

    # =====================================================================================================

    rdall = 0
    rdused = fc.execute('''SELECT keyrd FROM mirodom WHERE master='Владимир' AND status='Выполнена' ''')
    rduse = rdused.fetchall()
    rd = 0
    for x in rduse:
        rd = sum(i[0] for i in rduse)

    ostrd = str(rdall - rd)

    # =====================================================================================================

    mfall = 0
    mfused = fc.execute('''SELECT keymf FROM mirodom WHERE master='Владимир' AND status='Выполнена' ''')
    mfuse = mfused.fetchall()
    mf = 0
    for x in mfuse:
        mf = sum(i[0] for i in mfuse)

    ostmf = str(mfall - mf)

    # =====================================================================================================

    tmall = 0
    tmused = fc.execute('''SELECT keytm FROM mirodom WHERE master='Владимир' AND status='Выполнена' ''')
    tmuse = tmused.fetchall()
    tm = 0
    for x in tmuse:
        tm = sum(i[0] for i in tmuse)

    osttm = str(tmall - tm)

    # =====================================================================================================

    ykp7all = 0
    ykp7used = fc.execute('''SELECT ykpseven FROM mirodom WHERE master='Владимир' AND status='Выполнена' ''')
    ykp7use = ykp7used.fetchall()
    ykp7 = 0
    for x in ykp7use:
        ykp7 = sum(i[0] for i in ykp7use)

    ostykp7 = str(ykp7all - ykp7)

    # =====================================================================================================

    ykp12all = 0
    ykp12used = fc.execute('''SELECT ykptwelve FROM mirodom WHERE master='Владимир' AND status='Выполнена' ''')
    ykp12use = ykp12used.fetchall()
    ykp12 = 0
    for x in ykp12use:
        ykp12 = sum(i[0] for i in ykp12use)

    ostykp12 = str(ykp12all-ykp12)

    # ======================================================================================================

    return render_template('vlr.html', mirodom=mirodom, dengi=dengi, prem=prem, sdaet=sdaet, rd=rd,mf=mf, ostrd=ostrd, ostmf=ostmf, tm=tm, osttm=osttm,
                           ykp7=ykp7, ostykp7=ostykp7, ykp12=ykp12, ostykp12=ostykp12)

#=======================================================================================================================

@app.route('/vlvsevolzhsk')
def vlvsevolzhsk():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Всеволожск' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlvsevolzhsk.html', mirodom=mirodom)

@app.route('/vlpetr')
def vlpetr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Петроградский' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlpetr.html', mirodom=mirodom)

@app.route('/vlfrunza')
def vlfrunza():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Фрунзенский' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlfrunza.html', mirodom=mirodom)

@app.route('/vlprim')
def vlprim():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Приморский' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlrim.html', mirodom=mirodom)

@app.route('/vlzanevka')
def vlzanevka():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='ЖКК Заневка' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlzanevka.html', mirodom=mirodom)

@app.route('/vlkolt')
def vlkolt():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Колтуши' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlkolt.html', mirodom=mirodom)

@app.route('/vlstaraya')
def vlstaraya():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='д.Старая' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlstaraya.html', mirodom=mirodom)

@app.route('/vlkyz')
def vlkyz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Кузьмолово' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlkyz.html', mirodom=mirodom)

@app.route('/vlkalin')
def vlkalin():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Калининский' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlkalin.html', mirodom=mirodom)

@app.route('/vlohta')
def vlohta():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='УК Охта-Сервис' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlohta.html', mirodom=mirodom)

@app.route('/vlraz')
def vlraz():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='пос.Разметелево' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlraz.html', mirodom=mirodom)

@app.route('/vlsheg')
def vlsheg():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Щеглово' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlsheg.html', mirodom=mirodom)

@app.route('/vlyanino')
def vlyanino():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE city='Янино' AND master ='Владимир' AND status='Открыта' ''').fetchall()
    conn.close()
    return render_template('vlyanino.html', mirodom=mirodom)

@app.route('/vladressfiltr')
def vladressfiltr():
    conn = get_db_connection()
    mirodom = conn.execute('''SELECT * FROM mirodom WHERE master ='Владимир' ''').fetchall()
    conn.close()
    return render_template('vladressfiltr.html', mirodom=mirodom)

#========================================================================================================================






@app.route('/<int:mirodom_id>')
def mirodom(mirodom_id):
    mirodom = get_mirodom(mirodom_id)
    return render_template('mirodom.html', mirodom=mirodom)

@app.route('/<int:id>/edit', methods=('GET','POST'))


def edit(id):
    mirodom=get_mirodom(id)

    if request.method == 'POST':
        if request.form['submit_button'] == 'Добавить/Изменить':
            other = request.form['other']
            status = request.form['status']
            keytm = request.form['keytm']
            keymf = request.form['keymf']
            keyrd = request.form['keyrd']
            ykpseven = request.form['ykpseven']
            ykptwelve = request.form['ykptwelve']
            money = request.form['money']
            price = request.form['price']
            closingdata= datetime.now()
            closingdate = str(closingdata)
            conn = get_db_connection()
            conn.execute('UPDATE mirodom SET other=?, status=?, keytm=?, keymf=?, keyrd=?, ykpseven=?, ykptwelve=?, money=?, price=?, closingdate=?'
                         'WHERE id = ?',
                         (other, status, keytm, keymf, keyrd, ykpseven, ykptwelve, money, price, closingdate, id,))
            conn.commit()
            conn.close()
        elif request.form['submit_button'] == 'Быстрое закрытие':
            datecloze = datetime.now()
            dateclose = str(datecloze)
            conn = get_db_connection()
            conn.execute('''UPDATE mirodom SET status='Выполнена', closingdate=? WHERE id=?''', (dateclose, id,))
            conn.commit()
            conn.close()






        return redirect(url_for('index'))  #request.url, code=302


    return render_template('edit.html', mirodom=mirodom)

