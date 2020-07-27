Scrapy demo
===

# 創建一個 Scrapy 項目

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