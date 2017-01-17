#a1.py
# Nicolas Barone njb227 and Jeffrey Zhang jz674 
#9/18/16

"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

import urllib2

def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space
    
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    start = s.index('')
    end = s.index(' ')
    result = s[start:end]
    return result


def after_space(s):
    #s must be a string. This will give us the substring after the space.
    start = s.index(' ')
    end = s[start+1:]
    return end


def first_inside_quotes(s):
    """Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters
    inside."""
    #s must be a string. This will give us the quote character. 
    start = s.index('"')
    tail = s[start+1:]
    end = tail.index('"')
    result = tail[ :end]
    return result


def get_from(json):
    '''JSON response to a currency query, his returns the string inside double
    quotes (") immediately following the keyword "from.
    This will return The FROM value in the
    response to a currency query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''
    first_colon = json.index(':')
    start = json.index('"',first_colon)
    end = json.index('"', start+1)
    return json[start+1:end]
    
    
def get_to(json):
    """Returns: The TO value in the response to a currency query.

    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "to". For example,
    if the JSON is

    '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,
    "error":""}'
    then this function returns '1.825936 Euros' (not '"1.825936 Euros"').
    It returns the empty string if the JSON is the result of on invalid query.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    a = json.index('to')
    first_colon = json.index(':', a)
    start = json.index('"',first_colon)
    end = json.index('"', start+1)
    return json[start+1:end]
    
    
def has_error(json):
    s = json.find('false')
    result = (s != -1)
    return result
    

def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.
    
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
    
        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'
    
    where the values old-amount and new-amount contain the value and name 
    for the original and new currencies. If the query is invalid, both 
    old-amount and new-amount will be empty, while "valid" will be followed 
    by the value false.
    
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    u = urllib2.urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='
    +str(currency_from) + '&to=' + str(currency_to) + '&amt='+ str(amount_from))
    result = u.read() #s stores the json, from the url
    return result


def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    a = has_error(currency_response(currency, 'AED', 0))
    return a == False
    
    
def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    b = currency_response(currency_from, currency_to, amount_from)
    a = get_to(b)
    end = a.index(' ')
    result = a[ :end]
    number = float(result)
    return number
    """float(before_space(a))"""


