Scrapy Demo
===

這是我學習 Scrapy 的項目。

## 創建一個 Scrapy 項目

1. 安裝 pip，並利用 pip下載 Scrapy 並加入環境變量 PATH

```zsh
# 我的系統是 ArchLinux
sudo pacman -S python-pip
pip install scrapy
```

為將 pip 引入環境變量，在 `~/.profile` 和 `~/.zshrc` 裡面添加下面一行並 `source`。

```
# PIP
export PATH=~/.local/bin:$PATH
```

```bash
source ~/.profile
source ~/.zshrc
```

2. 創建項目


```bash
# 創建一個名為 **DEMO** 的項目
scrapy startproject DEMO
# 進入資料夾
cd DEMO
# 輸入 爬蟲名(取代 example) 和 爬的網域(取代 example.com)
scrapy genspider example example.com
```
> genspider：general spider 生成爬蟲
