from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

here = Path(__file__).resolve().parent
page = here / "示例.html"
driver = webdriver.Chrome()

try:
    driver.get(page.resolve().as_uri())

    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "loginBtn").click()

    message = driver.find_element(By.ID, "message")
    actual = message.text
    print("实际结果：", actual)

    # 末尾多一个空格，肉眼看不出，但 == 不会通过
    expected = "登录成功！用户：testuser，城市：未选，性别：未选，爱好：无，记住我：false "
    print("预期结果：", expected)

    assert actual == expected, "页面提示与预期不一致"

    time.sleep(3)

except Exception:
    driver.save_screenshot(str(Path(__file__).with_suffix(".png")))
    raise
finally:
    driver.quit()