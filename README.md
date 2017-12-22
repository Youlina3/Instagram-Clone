# Instagram 克隆版

作為一開始練習Django2.0的Project，因為許多中文文檔案與書籍仍停在較早期版本，可以使用這份專案來做一個參照，關於router的用法有些差異(正則/include)，render的方法也有不同，可以參照我fork的那份做一個區別。

# 安裝

    git clone https://github.com/realdennis/instagram.git && cd instagram

# 目標

* 實作出生活所觸及的網站。
* 基於benigls的Django1.8移植

# 環境
* Python 3.6 
* Django 2.0 
* django-braces 1.12.0 
* django-crispy-forms 1.7.0


# Instagram clone with Django 2.0

A Instagram clone made with django framework.

# Dependencies

* Python 3.x
* Django==2.0
* django-braces==1.12.0
* django-crispy-forms==1.7.0

# Installation

// assuming you've already install virtualenvwrapper
mkvirtualenv --python=`which python3` instagram
git clone https://github.com/benigls/instagram.git && cd instagram
    
    git clone https://github.com/realdennis/instagram.git && cd instagram
    
pip install -r requirements.txt
cd instagram
python manage.py runserver

#Contributions

Feel free to fork the project if you wish to contribute.
