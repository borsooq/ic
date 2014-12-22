'''
Created on 19-12-2014

@author: mirko.boruc@gmail.com
'''

from selenium import webdriver

#setting the browser
browser = webdriver.Firefox()
#maximize browser
browser.maximize_window()
#set baseURL
baseURL = 'http://www.motointegrator.pl/'
#get main page
browser.get(baseURL) 


searchButton = browser.find_element_by_xpath("//html/body/header/div[3]/div/button")
#searchButton by xpath. Refactor this
searchButton.click()
#search button clicked
fancyBoxWrap = browser.find_element_by_id("fancybox-wrap")
#first container set

#some assertions
assert(fancyBoxWrap)
assert(browser.find_element_by_id("fancybox-outer"))
assert(browser.find_element_by_id("fancybox-content"))
assert(browser.find_element_by_id("jqs-vehicle-chain-selector"))
assert(browser.find_element_by_id("jqs-user-vehicle-states"))
assert(browser.find_element_by_id("jqs-vehicle-chain"))
#end of assertions

#cfixes = fancyBoxWrap.find_elements_by_class_name("clearfix")
#browser.implicitly_wait(0)


def checkIfMatch(string, strings):
    counter=0
    #print string.split()
    #print strings
    listGot=string.split()
    for item in strings:
        for gotItem in listGot:
            if str(gotItem)==str(item):
                counter=counter+1
    if counter == len(strings):
        return True
    else:
        return False

def setSelection(container, componentBy, componentByProperty, componentAttribute, componentAttributeValue, uiClass, uiText, uiStyle, uiDisabled, selectionXpath, selection):
    cfixes = container.find_elements_by_class_name("clearfix")
    for clearfix in cfixes:
        if componentBy=="class_name":
            jqsInitials = clearfix.find_elements_by_class_name(componentByProperty)
        if componentBy=="tag":
            jqsInitials = clearfix.find_elements_by_tag_name(componentByProperty)
        for jqsInitial in jqsInitials:
            if jqsInitial.get_attribute(componentAttribute)==componentAttributeValue:
                try:
                    uiSelectMenu = clearfix.find_element_by_class_name(uiClass)
                    if (uiSelectMenu.text == uiText and uiSelectMenu.get_attribute("style") == uiStyle and uiSelectMenu.get_attribute("aria-disabled") == uiDisabled):
                        uiSelectMenu.click()
                        uiSelectMenuMenus = browser.find_element_by_id(str(uiSelectMenu.get_attribute("id")).replace("button", "menu"))
                        try:
                            options = uiSelectMenuMenus.find_elements_by_xpath(selectionXpath)
                            for option in options:
                                if option.text!="":
                                    if checkIfMatch(option.text, selection):
                                        option.click()
                        except:
                            print "cannot find options"
                except:
                    print "cannot find"    
                    
setSelection(fancyBoxWrap, "class_name", "jqs-initial", "name", "year", "ui-selectmenu", "Wybierz...", "width: 465px;", "false", "//ul/li[@role='presentation']/a", ["2014"])   
print "year Set"
setSelection(fancyBoxWrap, "class_name", "jqs-initial", "name", "manufacturer_id", "ui-selectmenu", "Wybierz...", "width: 465px;", "false", "//ul/li[@role='presentation']/a", ["Opel"])  
print "manufacturer set"
setSelection(fancyBoxWrap, "tag", "select" ,"name", "model_id", "ui-selectmenu", "Wybierz...", "width: 465px;", "false", "//ul/li[@role='presentation']/a/div[1]/table/tbody/tr", ["ASTRA","J","2009"])  
print "model set"
setSelection(fancyBoxWrap, "class_name", "jqs-vehicle-type", "name", "vehicle_id", "ui-selectmenu", "Wybierz...", "width: 465px;", "false", "//ul/li[@role='presentation']/a", ['1.4', 'Turbo', '(A', '14', 'NET)', '1364', '140', '103', 'od', '2009'])
print "engine set"
submitButton = fancyBoxWrap.find_element_by_class_name("btn").click()
print "submitted"

browser.find_element_by_link_text("Opony").click()
print "tyres selected"

print "beggining of new view"
container = browser.find_element_by_id("container")
#second container set  
setSelection(container, "class_name", "jqs-size-for-your-car", "name", "tiresize", "ui-selectmenu", '215/60 R16" (oryginalny)', "width: 220px;", "false", "//ul/li[@role='presentation']/a", ['225/50','R17"','(opcjonalny)'])   
print "tiresize set" 

print "niestety nie byem w stanie zrobic wiecej"
print "potrzebowalbym jakies 2 dni wiecej, zeby dokonczyc."
print "niestety idzie mi to dosc wolno, bo dosc dawno nie robilem tetsow automatycznych po GUI"

print "Pozdrawiam"
print "Kamil Boruc"
print "finish"

