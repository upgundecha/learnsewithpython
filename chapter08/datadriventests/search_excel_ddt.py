import xlrd, unittest
from ddt import ddt, data, unpack
from selenium import webdriver


def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the specified Excel spreadsheet as workbook
    book = xlrd.open_workbook(file_name)
    # get the first sheet
    sheet = book.sheet_by_index(0)
    # iterate through the sheet and get data from rows in list
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows


@ddt
class SearchExcelDDT(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://demo.magentocommerce.com/")

    # get the data from specified Excel spreadsheet
    # by calling the get_data function
    @data(*get_data("TestData.xlsx"))
    @unpack
    def test_search(self, search_value, expected_count):
            self.search_field = self.driver.find_element_by_name("q")
            self.search_field.clear()

            # enter search keyword and submit.
            self.search_field.send_keys(search_value)
            self.search_field.submit()

            # get all the anchor elements which have product names displayed
            # currently on result page using find_elements_by_xpath method
            products = self.driver\
                .find_elements_by_xpath("//h2[@class='product-name']/a")
            if expected_count > 0:
                # check count of products shown in results
                self.assertEqual(expected_count, len(products))
            else:
                msg = self.driver.find_element_by_class_name("note-msg")
                self.assertEqual("Your search returns no results.", msg.text)

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
