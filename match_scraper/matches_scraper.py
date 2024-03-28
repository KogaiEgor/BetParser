from selenium.webdriver.common.by import By


def find_esports_soccer_matches(driver):
    esoccer_logo = driver.find_element(By.XPATH,
                                       "//div[@class='ovm-EsportsCompetitionList_Title ovm-EsportsClassificationHeader ' and text()='Esoccer']")
    esoccer_tab = esoccer_logo.find_element(By.XPATH, "../..")
    matches = esoccer_tab.find_elements(By.XPATH,
                                        ".//div[@class='ovm-FixtureDetailsTwoWaySoccer ovm-FixtureDetailsTwoWaySoccer-1 ']")
    return matches
