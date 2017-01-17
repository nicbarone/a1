#a1.py
#Nicolas Barone njb227 and Jeffrey Zhang jz674 
#9/18/16

"""Unit test for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1."""

import cornelltest
import a1   

def testA():
    """Test procedure for back_space and after_space"""
    #Test case 1a
    result = a1.before_space('0.8963 Euro')
    cornelltest.assert_equals('0.8963', result)
    #Test case 2a
    result = a1.before_space('0.8963   Euro')
    cornelltest.assert_equals('0.8963', result)
    #Test case 3a
    result = a1.before_space('  0.8963 Euro')
    cornelltest.assert_equals('', result)
   
    #Test case 1b
    result = a1.after_space('0.8963 Euro')
    cornelltest.assert_equals('Euro', result)
    #Test case 2b
    result = a1.after_space('0.8963   Euro')
    cornelltest.assert_equals('  Euro', result)
    #Test case 3b
    result = a1.after_space('   0.8963 Euro')
    cornelltest.assert_equals('  0.8963 Euro', result)
    #Test case 1b
    result = a1.after_space('0.8963 Euro  ')
    cornelltest.assert_equals('Euro  ', result)
    #Test case 1b
    result = a1.after_space('0.8963Euro  ')
    cornelltest.assert_equals(' ', result)
   

def testB():
    """Test procedure for first_inside_quotes(s). Will extract substrings."""
    #Test case 1
    result = a1.first_inside_quotes('Johnny"apple"seed')
    cornelltest.assert_equals('apple', result)
    #Test case 2
    result = a1.first_inside_quotes('Harvard" sucks "poo')
    cornelltest.assert_equals(' sucks ', result)
    #Test case 2
    result = a1.first_inside_quotes('Harvard"  "poo')
    cornelltest.assert_equals('  ', result)
    #Test case 2
    result = a1.first_inside_quotes('Harvard""poo')
    cornelltest.assert_equals('', result)
    result = a1.first_inside_quotes('Jeffrey, "Don\'t panic!" about assign. 1')
    cornelltest.assert_equals('Don\'t panic!', result)
    result = a1.first_inside_quotes('Jeffrey, "Don\'t panic!" you will "be" ok')
    cornelltest.assert_equals('Don\'t panic!', result)
    
    """Test procedure for get_from(json)."""
    #Test case 1a
    result = a1.get_from('"from" : "2.5 United States Dollars",'+
    '"to" : "2.24075 Euros", "success" : true, "error" : ""')
    cornelltest.assert_equals('2.5 United States Dollars', result)
    result = a1.get_from('{"from":"2 United States Dollars",'+
    '"to":"1.825936 Euros","success":true,"error":""}')
    cornelltest.assert_equals('2 United States Dollars', result)
    result = a1.get_from('{ "from" : "", "to" : "", "success" : false, "error"'+
    ' : "Exchange currency code is invalid." }')
    cornelltest.assert_equals('',result)
    
    
    #Test case 2b
    result = a1.get_to('"from" : "2 United States Dollars","to"'+
    ' : "1.825936 Euros","success":true,"error":""')
    cornelltest.assert_equals('1.825936 Euros', result)
    result = a1.get_to('{ "from" : "", "to" : "", "success" : false, "error"'+
    ' : "Exchange currency code is invalid." }')
    cornelltest.assert_equals('',result)
    
    
    #Test case 1c
    result = a1.has_error('"from" : "2 United States Dollars","to"'
    +' : "1.825936 Euros","success":true,"error":""')
    cornelltest.assert_equals(False, result)
    #Test case 2c
    result = a1.has_error('"from" : "", "to" : "", "success"'
    +' : false, "error" : "Source currency code is invalid."')
    cornelltest.assert_equals(True, result)
    
    
def testC():
    #Test case 1
    result = a1.currency_response('USD', 'EUR', 2.5)
    cornelltest.assert_equals('{ "from" : "2.5 United States Dollars", "to"'+
    ' : "2.24075 Euros", "success" : true, "error" : "" }', result)
    result = a1.currency_response('USD', 'ETB', 1.0)
    cornelltest.assert_equals('{ "from" : "1 United States Dollar", "to"'+
    ' : "22.09099 Ethiopian Birr", "success" : true, "error" : "" }', result) 
    result = a1.currency_response('ETB', 'USD', 22.09099)
    cornelltest.assert_equals('{ "from" : "22.09099 Ethiopian Birr", "to"'+
    ' : "1 United States Dollar", "success" : true, "error" : "" }', result)



def testD():
    result = a1.iscurrency('AED')
    cornelltest.assert_true(result == True)
    result = a1.iscurrency('LOL')
    cornelltest.assert_true(result == False)
    result = a1.iscurrency('MOM')
    cornelltest.assert_true(result == False)
    result = a1.iscurrency('USD')
    cornelltest.assert_true(result == True)

    
    #Test exchange(currency_from, currency_to, amount_from)
    result = a1.exchange('USD', 'EUR', 2.5)
    cornelltest.assert_floats_equal(2.24075, result)
    result = a1.exchange('CAD', 'CNY', 1.0)
    cornelltest.assert_floats_equal(5.1369278716282, result)
    result = a1.exchange('CAD', 'CNY', 1.09)
    cornelltest.assert_floats_equal(5.5992513800748, result)
    result = a1.exchange('CAD', 'CNY', 1.09999)
    cornelltest.assert_floats_equal(5.6505692895124, result)
    
    
testA()    
testB()
testC()
testD()
print "Module a1 passed all tests"