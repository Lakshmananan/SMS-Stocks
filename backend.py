# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:31:49 2020

@author: laksh
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from twilio.twiml.messaging_response import MessagingResponse

def helper():
    return 'Working on it...'


def ticker_overview(ticker):
    driver = webdriver.Chrome(executable_path=r"C:\Users\laksh\Desktop\Scrapers\SMS-Stocks\chromedriver.exe")
    driver.get(f'https://web.tmxmoney.com/quote.php?qm_symbol={ticker}')
    try:
        price = driver.find_element_by_xpath('//*[@id="contentWrapper"]/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div/span/span').text
    except NoSuchElementException:
        price = 'nan'  
    try:
        change = driver.find_element_by_xpath('//*[@id="contentWrapper"]/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/strong').text
    except NoSuchElementException:
        change = 'nan'
    driver.close()
    resp = MessagingResponse()
    resp.message(price)
    return str(resp)
        

def ticker_financials(ticker):
    return 'Working on it...'


def ticker_news(ticker):
    return 'Working on it...'

