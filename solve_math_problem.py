import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from formula_parser import evaluate_formula
from formula_filter_test import formula_filter
import re

"""
# main file

preliminary requirements:
- install Selenium module and webdriver
- save formula_parser.py & formula_filter_test.py to the same working directory
 where solve_math_problem.py has been saved
"""


def solve_math_problem(url: str, level: str) -> None:
    """
    open given site
    find a problem description
    extract formula if possible, parse it and solve
    input an answer in an appropriate box
    click "Check answer" button
    click "See solution" button
    print answer and right solution
    """
    print(url)
    print(f'lavel: {level}')

    with webdriver.Chrome() as browser:
        browser.get(url+level+'/')

        for n, problem in enumerate(browser.find_elements(By.CLASS_NAME, "problemBox")):
            print(problem.text, '\n')

            row_formula = problem.find_element(By.CLASS_NAME, 'problemText').text
            formula = formula_filter(row_formula)

            if formula:
                data_dict = {var:int(var) for var in re.findall(r'\d+', formula)}
                answer = int(evaluate_formula(formula, data_dict))

                # input answer in a box
                problem.find_element(
                    By.XPATH,
                    f"//div[@class='problemBox'][{n+1}]/div[@class='problemText']/input[1]"
                ).send_keys(int(answer))

                # click "Check answer" button
                problem.find_element(
                    By.XPATH,
                    f"//div[@class='problemBox'][{n+1}]/div[@class='problemAnswer']/div/input[1]"
                ).click()

                # click "See solution" button
                problem.find_element(
                    By.XPATH, f"//div[@class='problemBox'][{n+1}]/div[@class='problemSolution']/input[1]"
                ).click()

                print(f'Your solution: {answer}')
                print('Right', problem.find_element(
                    By.XPATH,
                    f"//div[@class='problemBox'][{n+1}]/div[@class='problemSolution']"
                ).text)
                print('----*********----')
                print()

        time.sleep(3)


if __name__ == '__main__':
    start = datetime.now()
    levels = ['easy', 'normal', 'difficult']
    url_base = 'https://www.math10.com/problems/addition-and-subtraction-problems-up-to-100/'
    for level in levels:
        solve_math_problem(url_base, level)

    print(f'all {len(levels)} levels are done')
    end = datetime.now()
    print(end - start)