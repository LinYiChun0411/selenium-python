#windows 環境可直接執行

#以Linux 環境安裝 需修改webdriver路徑
ex: driver = webdriver.Chrome("/home/yichun/selenium-python/chromedriver")

#1. 安裝selenium套件

pip3 install selenium

#2. 安裝google-chrome

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome-stable_current_amd64.deb

**報錯誤時執行下列

sudo apt-get install -f

#3. 下載chromedirver

https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.106/


