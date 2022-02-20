# form-automation-selenium
Automated form-filling using Selenium.

#### For processing a large amount of csv data to be filled into a form or multiple forms. 
#### Written using Python with Selenium framework.

##### Notes:
Initially I used Mechanize module instead of Selenium, however I realised the webpage was dynamic which made it difficult to retrieve certain fields that required Javascript processing depending on previous inputs. After additional research I switched over to Selenium instead for browser automation. In retrospect, I highly recommend using Mechanize for 100% static forms as it is much easier to use. However, for dynamic forms, Selenium would be a better fit.

## Installation
Ensure Git and Python 3.9.1 or above are both installed in your computer.
1. Clone the repository

        git clone https://github.com/peanutooo/form-automation-selenium.git
    
2. Install the latest stable release of ChromeDriver [here](https://chromedriver.chromium.org/).
3. Customize the fields in the code as needed.
4. Run the code.
`python form-automation.py`
    
