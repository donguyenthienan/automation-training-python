# Import the 'modules' that are required for execution
import pytest
import pytest_html
from selenium import webdriver

# @pytest.fixture(params=["chrome", "firefox", "ie", "edge", "safari", "opera"],scope="class")
# @pytest.fixture(params=["chrome", "firefox", "safari", "opera"],scope="class")
@pytest.fixture(params=["chrome"],scope="class")
def driver_init(request):
  if request.param == "chrome":
    driver = webdriver.Chrome()
  if request.param == "firefox":
    driver = webdriver.Firefox()
  # if request.param == "ie":
  #   driver = webdriver.IE()
  # if request.param == "edge":
  #   driver = webdriver.MicrosoftEdge()
  if request.param == "safari":
    driver = webdriver.Safari()
  if request.param == "opera":
    driver = webdriver.Opera()
  request.cls.driver = driver
  yield
  driver.close()

@pytest.fixture(params=["chrome", "firefox", "phantomjs", "opera"],scope="class")
def driver_headless_init(request):
  if request.param == "chrome":
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
  if request.param == "firefox":
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
  if request.param == "phantomjs":
    driver = webdriver.PhantomJS()
  if request.param == "opera":
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Opera(options=options)
  request.cls.driver = driver
  yield
  driver.close()

#Fixture for Firefox
@pytest.fixture(scope="class")
def firefox_driver_init(request):
  ff_driver = webdriver.Firefox() 
  request.cls.driver = ff_driver
  yield
  ff_driver.close()

#Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):   
  chrome_driver = webdriver.Chrome()   
  request.cls.driver = chrome_driver
  yield
  chrome_driver.close()  

def pytest_generate_tests(metafunc):
  "test generator function to run tests across different parameters"
  if "browser" in metafunc.fixturenames:
      metafunc.parameterize("browser", metafunc.config.option.browser)

def pytest_runtest_makereport(item, call):
  if "incremental" in item.keywords:
    if call.excinfo is not None:
      parent = item.parent
      parent._previousfailed = item
 
def pytest_runtest_setup(item):
  previousfailed = getattr(item.parent, "_previousfailed", None)
  if previousfailed is not None:
    pytest.xfail("previous test failed (%s)" % previousfailed.name)
