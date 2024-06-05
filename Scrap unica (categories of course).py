#!/usr/bin/env python
# coding: utf-8

# ## Scraping online courses infromation by categories
# ### E.g. Marketing, IT, Lifestype, Languages, Soft skills, business, Sales....  

# In[ ]:


# import esstential libs
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')


# In[ ]:


# Example of codes 
df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/ngoai-ngu')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link, 'Tên':name,'Danh mục':f'Ngoại Ngữ, Giảng Viên > {teacher}', 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian:{durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break

df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'


# In[ ]:


# Clean the errors and incorrect formats
df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
#df['Nội dung nút bấm']= 'Xem Chi Tiết'
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_ngoaingu.csv')


# In[ ]:


df


# # marketing
# # the marketing category

# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/marketing')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link, 'Tên':name, 'Danh mục':f'Marketing, Giảng Viên > {teacher}', 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian:{durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break

# Cleaning the raw data for the first category
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'


# In[ ]:


df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Nội dung nút bấm']= 'Xem Chi Tiết'
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_market.csv')


# # khóa học tin học
# # All the courses in office information category

# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/tin-hoc-van-phong')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link, 'Danh mục':f'Tin Học Văn Phòng, Giảng Viên > {teacher}', 'Tên':name, 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian: {durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break

df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'


# In[ ]:


df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Nội dung nút bấm']= 'Xem Chi Tiết'
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_tinhoc.csv')


# # Khóa học kinh doanh
# # All the courses in business categories

# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/kinh-doanh-va-khoi-nghiep')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link,'Danh mục':f'Kinh Doanh & Khởi Nghiệp, Giảng Viên > {teacher}', 'Tên':name, 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian:{durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break

df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'


# In[ ]:


df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_KD.csv')


# # Khóa học thiết kế
# # All the courses in Design categories

# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/thiet-ke')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link,'Danh mục':f'Thiết kế, Giảng Viên > {teacher}', 'Tên':name, 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian: {durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break
        

df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'

df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_TK.csv')


# In[ ]:


df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_TK.csv')


# # Kỹ năng mềm
# # All the courses in Soft Skills categories

# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/ky-nang-mem')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link,'Danh mục':f'Kỹ Năng Mềm, Giảng Viên > {teacher}', 'Tên':name, 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian: {durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break
        

df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'


# In[ ]:


df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_KNM.csv')


# # Sales

# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/sales-ban-hang')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link,'Danh mục':f'Kỹ năng Bán hàng, Giảng Viên > {teacher}', 'Tên':name, 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian: {durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break
        

df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'


# In[ ]:


df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_sales.csv')


# # Phong cách sống

# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/phong-cach-song')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link,'Danh mục':f'Phong Cách Sống, Giảng Viên > {teacher}', 'Tên':name, 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian: {durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break
        

df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'


# In[ ]:


df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_lifestyle.csv')


# # Nuôi dạy con

# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/nuoi-day-con')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link,'Danh mục':f'Nuôi Dạy Con, Giảng Viên > {teacher}', 'Tên':name, 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian: {durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break
        

df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'


# In[ ]:


df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_nuoidaytre.csv')


# # Công nghệ thông tin

# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/cong-nghe-thong-tin')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link,'Danh mục':f'Công Nghệ Thông Tin, Giảng Viên > {teacher}', 'Tên':name, 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian: {durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break
        

df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'


# In[ ]:


df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_IT.csv')


# # Sức khỏe

# In[ ]:


df = pd.read_csv(r'C:\Users\DELL\Downloads\DSSP.csv')
driver = webdriver.Chrome(r'C:\Users\DELL\Desktop\WEB SCRAPING\chromedriver.exe')
driver.get('https://unica.vn/course/suc-khoe')
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    courses = soup.find_all('a',class_ = "link-course")
    for course in courses:
        try:
            discription = course.find('div', class_="description-course").text
            name = course.find('h3', class_='name-course').text
            link = "https://unica.vn" + course.get('href') +"?aff=556833"
            teacher = course.find('div', class_='name-gv').text.replace('\n','')[44:]
            image = "https://unica.vn" + course.find('img', class_='img-responsive').get('src')
            price = course.find('div', class_ ='price_sale').text
            ori_price = course.find('div', class_="price_origin").text
            #star = len(course.find_all('i',class_="fa fa-star co-or"))
            durian = course.find('p',class_='total_time').text.replace('\n','')[98:]
            #mems = course.find('span', 'star-rate').text
            df = df.append({'URL ngoài':link,'Danh mục':f'Sức Khỏe & Cuộc Sống, Giảng Viên > {teacher}', 'Tên':name, 'Mô tả':discription, 'Mô tả ngắn':f'{teacher}\nThời gian: {durian}' ,'Hình ảnh':image,'Giá khuyến mãi':price,'Giá bán thường':ori_price}, ignore_index=True)
        except:
            pass
    time.sleep(4)
    try:
        btn = driver.find_element('xpath','//*[@id="list_product"]/div[2]/ul/li[7]/a')
       # class_name = btn.get_attribute("class")
        driver.execute_script ("arguments[0].click();",btn)
        
    except NoSuchElementException:
        print("element does not exist")
        break
        

df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace(',                                             ', ', '))
df['Mô tả ngắn']= df['Mô tả ngắn'].apply(lambda x: x.replace('                                        ', ''))
df['Mô tả ngắn'] = 'GV: '+df['Mô tả ngắn']
df = df.drop(0)
df['Loại']='external'
df['Đã đăng']=1
df['Nhãn nổi bật?']=0
df['Hiển thị trong danh mục']='visible'
df['Nội dung nút bấm']= 'Xem Chi Tiết'


# In[ ]:


df['Giá bán thường']=df['Giá bán thường'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df['Giá khuyến mãi']=df['Giá khuyến mãi'].apply(lambda x: int(x.replace('\n','').replace('                                                ','').replace('đ','').replace('.','')))
df.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_suc-khoe.csv')


# In[ ]:


df=pd.read_csv(r'C:\Users\DELL\Downloads\wc-product-export-19-5-2023-1684491570211.csv')


# In[ ]:


df['Danh mục']="Giảng Viên > " +df['Danh mục']


# In[ ]:


df['Danh mục'][833]='Giảng Viên > 123VIETNAMESE, Ngoại Ngữ'


# In[ ]:


df['Danh mục'][833]


# In[ ]:


.to_csv(r'C:\Users\DELL\Desktop\DSSP_unica_total.csv')


# In[ ]:


df=pd.read_csv(r'C:\Users\DELL\Desktop\DSSP_unica_lifestyle.csv')


# In[ ]:


df['Danh mục']


# In[ ]:




