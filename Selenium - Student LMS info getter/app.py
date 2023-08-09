from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from IPython.display import display, HTML

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/timetable")
def timetable():
    options = Options()
    options.add_experimental_option("detach", True)  # to open window after work is done
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get("https://edusmartz.ssuet.edu.pk/StudentPortal/Login")  # link to visit
    driver.maximize_window()
    driver.implicitly_wait(30)

    rollno = driver.find_element("xpath", "//input[@id='txtRegistrationNo_cs']")
    rollno.clear()
    rollno.send_keys("2020F-BCS-096")

    password = driver.find_element("xpath", "//input[@id='txtPassword_m6cs']")
    password.clear()
    password.send_keys("9E5D0F3C82CA")

    driver.implicitly_wait(30)

    signinbtn = driver.find_element("xpath", "//input[@id='btnlgn']")
    signinbtn.click()

    driver.implicitly_wait(30)

    sidebar = driver.find_elements(
        "xpath", "//li[@class='menu-item menu-item-submenu']"
    )
    sidebar[0].click()
    timetable = driver.find_element(
        "xpath", "//li[@class='menu-item'][.//span[text()[contains(.,'Time Table')]]]"
    )
    timetable.click()

    driver.implicitly_wait(30)

    table = driver.find_element(
        "xpath", "//div[@id='ctl00_ContentPlaceHolder1_DynamicTimeTable']"
    )
    text = table.get_attribute("innerHTML")

    driver.quit()

    return render_template("timetable.html", data=text)


@app.route("/ledger")
def ledger():
    options = Options()
    options.add_experimental_option("detach", True)  # to open window after work is done
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get("https://edusmartz.ssuet.edu.pk/StudentPortal/Login")  # link to visit
    driver.maximize_window()
    driver.implicitly_wait(30)

    rollno = driver.find_element("xpath", "//input[@id='txtRegistrationNo_cs']")
    rollno.clear()
    rollno.send_keys("2020F-BCS-096")

    password = driver.find_element("xpath", "//input[@id='txtPassword_m6cs']")
    password.clear()
    password.send_keys("9E5D0F3C82CA")

    driver.implicitly_wait(30)

    signinbtn = driver.find_element("xpath", "//input[@id='btnlgn']")
    signinbtn.click()

    driver.implicitly_wait(30)

    view = driver.find_elements(
        "xpath", "//a[@class='btn btn-info font-weight-bolder font-size-sm mr-3']"
    )
    driver.execute_script("window.scrollTo(0, 2500);")
    view[-1].click()
    arrow = driver.find_element(
        "xpath",
        "//a[@id='ctl00_ContentPlaceHolder1_TgrdStudentGeneralLedger_ctl00_ctl03_ctl01_PageSizeComboBox_Arrow']",
    )
    arrow.click()
    alltxt = driver.find_elements("xpath", "//li[@class='rcbItem']")
    alltxt[-1].click()
    table = driver.find_element("xpath", "//div[@class='col-md-12 gridmargin']")
    text = table.get_attribute("innerHTML")

    driver.quit()

    return render_template("ledger.html", data=text)


@app.route("/gpa")
def gpa():
    options = Options()
    options.add_experimental_option("detach", True)  # to open window after work is done
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get("https://edusmartz.ssuet.edu.pk/StudentPortal/Login")  # link to visit
    driver.maximize_window()
    driver.implicitly_wait(30)

    rollno = driver.find_element("xpath", "//input[@id='txtRegistrationNo_cs']")
    rollno.clear()
    rollno.send_keys("2020F-BCS-096")

    password = driver.find_element("xpath", "//input[@id='txtPassword_m6cs']")
    password.clear()
    password.send_keys("9E5D0F3C82CA")

    driver.implicitly_wait(30)

    signinbtn = driver.find_element("xpath", "//input[@id='btnlgn']")
    signinbtn.click()

    driver.implicitly_wait(30)

    roadmap = driver.find_element(
        "xpath",
        "//a[contains(@class, 'btn btn-success btn-shadow-hover font-weight-bolder w-100 py-3')]",
    )
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    roadmap.click()

    driver.implicitly_wait(30)

    table = driver.find_element(
        "xpath", "//table[@id='ctl00_ContentPlaceHolder1_TgrdCGPA_ctl00']"
    )
    text = table.get_attribute("innerHTML")
    text = "<table>" + text + "</table>"

    driver.quit()

    return render_template("gpa.html", data=text)


@app.route("/attendance")
def attendance():
    options = Options()
    options.add_experimental_option("detach", True)  # to open window after work is done
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get("https://edusmartz.ssuet.edu.pk/StudentPortal/Login")  # link to visit
    driver.maximize_window()
    driver.implicitly_wait(30)

    rollno = driver.find_element("xpath", "//input[@id='txtRegistrationNo_cs']")
    rollno.clear()
    rollno.send_keys("2020F-BCS-096")

    password = driver.find_element("xpath", "//input[@id='txtPassword_m6cs']")
    password.clear()
    password.send_keys("9E5D0F3C82CA")

    driver.implicitly_wait(30)

    signinbtn = driver.find_element("xpath", "//input[@id='btnlgn']")
    signinbtn.click()

    driver.implicitly_wait(30)

    sidebar = driver.find_elements(
        "xpath", "//li[@class='menu-item menu-item-submenu']"
    )
    sidebar[0].click()
    attendance = driver.find_element(
        "xpath", "//li[@class='menu-item'][.//span[text()[contains(.,'Attendance')]]]"
    )
    attendance.click()

    table = driver.find_element(
        "xpath", "//table[@id='ctl00_ContentPlaceHolder1_TgridAttedance_ctl00']"
    )
    text = table.get_attribute("innerHTML")
    driver.quit()
    start_text = '<th scope="col" class="rgHeader">View'
    end_text = "</th>"
    split_text = text.split(start_text, 1)
    text = split_text[0] + split_text[1].split(end_text, 1)[1]

    start_text = "<colgroup>"
    end_text = "</colgroup>"
    split_text = text.split(start_text, 1)
    text = split_text[0] + split_text[1].split(end_text, 1)[1]

    start_text = "<a id="
    end_text = "</a>"

    pattern = re.escape(start_text) + "(.*?)" + re.escape(end_text)
    attendance_table = re.sub(pattern, "", text)
    attendance_table = "<table>" + attendance_table + "</table>"

    return render_template("attendance.html", data=attendance_table)


if __name__ == "__main__":
    app.run()
