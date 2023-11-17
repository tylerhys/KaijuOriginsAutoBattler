1) Download Chrome Driver for your version of chrome here. Will need the path to be replaced in the code:
https://googlechromelabs.github.io/chrome-for-testing/


2) In cmd, run CDP by locating your chrome.exe and running:
chrome.exe --remote-debugging-port=9515

i.e. mine is in:
C:\Program Files (x86)\Google\Chrome\Application

3) In that browser, have Origins as the only tab. Walk to an easy opponent which you would like to farm.
Refer to example1.png

4) in main.py, replace path to chrome driver as such:
s = Service('C:/Program Files (x86)/Google/Chrome/Application/chromedriver-win64/chromedriver.exe')

5) Install selenium if you haven't.
pip install selenium

6) run code and profit.

Troubleshooting:
1) Sometimes the game will crash with memory full or sth.. Just stop the code, refresh and walk back to an opponent and run the code again.

2) Kaiju Origins only run when the browser is on screen, so remember to not minimize it.

3) Also if chromedriver doesnt work at first, try restarting pc.