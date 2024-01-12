import unittest 
from scrapy import Selector
from scrapy.http import HtmlResponse
import scrapy
import requests
#The selector is required to be called with all keyword arguments filled in at least once!
class TestUsingSelectors(unittest.TestCase):
    def setUp(self):
        html_content = """
        <!DOCTYPE html>

        <html>
        <head>
            <base href='http://example.com/' />
            <title>Example website</title>
        </head>
        <body>
            <div id='images'>
            <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' alt='image1'/></a>
            <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' alt='image2'/></a>
            <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' alt='image3'/></a>
            <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' alt='image4'/></a>
            <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' alt='image5'/></a>
            </div>
        </body>
        </html>
        """

        response = HtmlResponse(url='http://example.com', body=html_content, encoding='utf-8')

        self.response = response
    def testSelectorShortcuts(self):
        # Example HTML content for testing
        html_content = """
        <div>
            <span>Scrapy is awesome!</span>
        </div>
        """

        # Create a Scrapy Response object
        response = HtmlResponse(url='http://example.com', body=html_content, encoding='utf-8')

        # Use assertEqual for the comparison
        self.assertEqual(response.selector.xpath("//span/text()").get(), response.xpath("//span/text()").get())
        self.assertEqual(response.selector.xpath("//span/text()").get(), Selector(text=response.body).xpath("//span/text()").get())

    def testGetall(self):
        html_content = """
        <div>
            <span>Scrapy is awesome!</span>
        </div>
        """
        
        # Create a Scrapy Response object
        response = HtmlResponse(url='http://example.com', body=html_content, encoding='utf-8')

        self.assertEqual(type(response.xpath("//span/text()").getall()), list)
        self.assertEqual(response.xpath("//span/text()").getall(), ['Scrapy is awesome!'])

        self.assertEqual(type(response.xpath("//span/text()").get()), str)
        self.assertEqual(response.xpath("//span/text()").get(), 'Scrapy is awesome!')

        self.assertNotEqual(response.xpath("//span/text()").getall(), '[Scrapy is awesome!]')
    
    def test_get_method_of_xpath_or_css(self):
        html_content = """
        <div>
            <span>Scrapy is awesome!</span>
        </div>
        """
        
        # Create a Scrapy Response object
        response = HtmlResponse(url='http://example.com', body=html_content, encoding='utf-8')

        result = response.xpath('//div[@id="not-exists"]/text()').get(default="not-found")

        self.assertEqual(result, "not-found")
        self.assertNotEqual(result, None)

    def test_css_and_xpath(self):
        response = self.response

        self.assertEqual(
            response.css("img").xpath("@src").getall(), 
            ['image1_thumb.jpg',
            'image2_thumb.jpg',
            'image3_thumb.jpg',
            'image4_thumb.jpg',
            'image5_thumb.jpg'])
        
        self.assertEqual(type(response.css("img")), scrapy.selector.unified.SelectorList)
        self.assertEqual(type(response.css("img")[0]), scrapy.selector.unified.Selector)

    def test_attrib_exhaustively(self):
        response = self.response
        
        self.assertEqual([img.attrib["src"] for img in response.css("img")], 
        ['image1_thumb.jpg',
        'image2_thumb.jpg',
        'image3_thumb.jpg',
        'image4_thumb.jpg',
        'image5_thumb.jpg'])

        imgTags = response.css("img")
        self.assertEqual([img.attrib["src"] for img in imgTags], response.xpath('//a[contains(@href, "image")]/img/@src').getall())

        self.assertEqual(response.xpath('//a[contains(@href, "image")]/img/@src').getall(), response.css("a[href*=image] img::attr(src)").getall())

class TestExtensionsToSelectors(unittest.TestCase):
    def setUp(self):
        html_content = """
        <!DOCTYPE html>

        <html>
        <head>
            <base href='http://example.com/' />
            <title>Example website</title>
        </head>
        <body>
            <div id='images'>
            <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' alt='image1'/></a>
            <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' alt='image2'/></a>
            <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' alt='image3'/></a>
            <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' alt='image4'/></a>
            <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' alt='image5'/></a>
            </div>
        </body>
        </html>
        """

        response = HtmlResponse(url='http://example.com', body=html_content, encoding='utf-8')

        self.response = response

    def testText(self):
        response = self.response
        
        self.assertEqual(response.css("title::text").get(), response.xpath("//title/text()").get())

        selector_context = "#images"
        select_all_descendant_text_nodes_of_the_current_selector_context = "*::text"
        cssPattern = selector_context + " " + select_all_descendant_text_nodes_of_the_current_selector_context


        self.assertEqual(response.css(cssPattern).getall(), ['\n            ',
'Name: My image 1 ',
'\n            ',
'Name: My image 2 ',
'\n            ',
'Name: My image 3 ',
'\n            ',
'Name: My image 4 ',
'\n            ',
'Name: My image 5 ',
'\n            '])
        self.assertEqual(response.css("li").get(), None)
        self.assertEqual(response.css("li").get(default="No lists in the response!"), "No lists in the response!")
        
class TestingNestingSelectors(unittest.TestCase):
    """
    Tests must start with 'test'.
    """
    def setUp(self):
        html_content = """
        <!DOCTYPE html>

        <html>
        <head>
            <base href='http://example.com/' />
            <title>Example website</title>
        </head>
        <body>
            <div id='images'>
            <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' alt='image1'/></a>
            <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' alt='image2'/></a>
            <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' alt='image3'/></a>
            <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' alt='image4'/></a>
            <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' alt='image5'/></a>
            </div>
        </body>
        </html>
        """
        response = HtmlResponse(url='http://example.com', body=html_content, encoding='utf-8')

        self.response = response

    def testNestingXpathSelectors(self):
        response = self.response
        links = response.xpath('//a[contains(@href, "image")]')

        links.getall()

        hrefs   = ['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']
        imgs    = ['image1_thumb.jpg', 'image2_thumb.jpg', 'image3_thumb.jpg', 'image4_thumb.jpg', 'image5_thumb.jpg']
        for index, link in enumerate(links):

            href_by_xpath = link.xpath("@href").get()

            img_by_xpath = link.xpath("img/@src").get()

            self.assertEqual(href_by_xpath, hrefs[index])
            self.assertEqual(img_by_xpath, imgs[index])


class TestSelectingElementAttributes(unittest.TestCase):
    def setUp(self):
        html_content = """
        <!DOCTYPE html>

        <html>
        <head>
            <base href='http://example.com/' />
            <title>Example website</title>
        </head>
        <body>
            <div id='images'>
            <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' alt='image1'/></a>
            <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' alt='image2'/></a>
            <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' alt='image3'/></a>
            <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' alt='image4'/></a>
            <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' alt='image5'/></a>
            </div>
        </body>
        </html>
        """
        response = HtmlResponse(url='http://example.com', body=html_content, encoding='utf-8')

        self.response = response
    
    def test(self):
        response = self.response

        filter_xpath = "@href"
        self.assertEqual(response.xpath("//a/" + filter_xpath).getall(), ['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html'])
        self.assertEqual([a.attrib["href"] for a in response.css("a")], response.xpath("//a/" + filter_xpath).getall())

        self.assertEqual(response.css("base").attrib, {'href': 'http://example.com/'})
        self.assertEqual(response.css("foo").attrib, dict())

        self.assertEqual(response.css("base").attrib["href"], 'http://example.com/')

        self.assertEqual(response.css("foo").attrib, dict())

class TestSelectorsWithRegularExpressions(unittest.TestCase):
    def setUp(self):
        html_content = """
        <!DOCTYPE html>

        <html>
        <head>
            <base href='http://example.com/' />
            <title>Example website</title>
        </head>
        <body>
            <div id='images'>
            <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' alt='image1'/></a>
            <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' alt='image2'/></a>
            <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' alt='image3'/></a>
            <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' alt='image4'/></a>
            <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' alt='image5'/></a>
            </div>
        </body>
        </html>
        """
        response = HtmlResponse(url='http://example.com', body=html_content, encoding='utf-8')

        self.response = response
    
    def testRegularExpressionsWith_xpath(self):
        response = self.response

        self.assertEqual(response.xpath('//a[contains(@href, "image")]/text()').re(r"Name:\s*(.*)"), ['My image 1 ',
    'My image 2 ',
    'My image 3 ',
    'My image 4 ',
    'My image 5 '])
    
    def test_get_getall_extract_extract_first(self):
        response = self.response

        #Goal: SelectorList.get() is the same as SelectorList.extract_first().
        self.assertEqual(response.css("a::attr(href)").get(), response.css("a::attr(href)").extract_first())

        #Goal: SelectorList.getall() is the same as SelectorList.extract().
        self.assertEqual(response.css("a::attr(href)").getall(), response.css("a::attr(href)").extract())

        #Selector.get() is the same as Selector.extract().
        self.assertEqual(response.css("a::attr(href)")[0].get(), response.css("a::attr(href)")[0].extract())

        #Selector.getall() returns a list.
        self.assertEqual(response.css("a::attr(href)")[0].getall(), ['image1.html'])
        self.assertEqual(type(response.css("a::attr(href)")[0].getall()), list)

class TestWorkingWithRelativeXpaths(unittest.TestCase):
#Keep in mind that if you are nesting selectors and use an XPath that starts with /, 
#that XPath will be absolute to the document and not relative to the Selector you’re calling it from.
    def setUp(self):
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Quotes to Scrape</title>
            <link rel="stylesheet" href="/static/bootstrap.min.css">
            <link rel="stylesheet" href="/static/main.css">
        </head>
        <body>
            <div class="container">
                <div class="row header-box">
                    <div class="col-md-8">
                        <h1>
                            <a href="/" style="text-decoration: none">Quotes to Scrape</a>
                        </h1>
                    </div>
                    <div class="col-md-4">
                        <p>
                        
                            <a href="/login">Login</a>
                        
                        </p>
                    </div>
                </div>
            

        <div class="row">
            <div class="col-md-8">

            <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
                <span>by <small class="author" itemprop="author">Albert Einstein</small>
                <a href="/author/Albert-Einstein">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="change,deep-thoughts,thinking,world" /    > 
                    
                    <a class="tag" href="/tag/change/page/1/">change</a>
                    
                    <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
                    
                    <a class="tag" href="/tag/thinking/page/1/">thinking</a>
                    
                    <a class="tag" href="/tag/world/page/1/">world</a>
                    
                </div>
            </div>

            <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>
                <span>by <small class="author" itemprop="author">J.K. Rowling</small>
                <a href="/author/J-K-Rowling">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="abilities,choices" /    > 
                    
                    <a class="tag" href="/tag/abilities/page/1/">abilities</a>
                    
                    <a class="tag" href="/tag/choices/page/1/">choices</a>
                    
                </div>
            </div>

            <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>
                <span>by <small class="author" itemprop="author">Albert Einstein</small>
                <a href="/author/Albert-Einstein">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="inspirational,life,live,miracle,miracles" /    > 
                    
                    <a class="tag" href="/tag/inspirational/page/1/">inspirational</a>
                    
                    <a class="tag" href="/tag/life/page/1/">life</a>
                    
                    <a class="tag" href="/tag/live/page/1/">live</a>
                    
                    <a class="tag" href="/tag/miracle/page/1/">miracle</a>
                    
                    <a class="tag" href="/tag/miracles/page/1/">miracles</a>
                    
                </div>
            </div>

            <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”</span>
                <span>by <small class="author" itemprop="author">Jane Austen</small>
                <a href="/author/Jane-Austen">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="aliteracy,books,classic,humor" /    > 
                    
                    <a class="tag" href="/tag/aliteracy/page/1/">aliteracy</a>
                    
                    <a class="tag" href="/tag/books/page/1/">books</a>
                    
                    <a class="tag" href="/tag/classic/page/1/">classic</a>
                    
                    <a class="tag" href="/tag/humor/page/1/">humor</a>
                    
                </div>
            </div>

            <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“Imperfection is beauty, madness is genius and it&#39;s better to be absolutely ridiculous than absolutely boring.”</span>
                <span>by <small class="author" itemprop="author">Marilyn Monroe</small>
                <a href="/author/Marilyn-Monroe">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="be-yourself,inspirational" /    > 
                    
                    <a class="tag" href="/tag/be-yourself/page/1/">be-yourself</a>
                    
                    <a class="tag" href="/tag/inspirational/page/1/">inspirational</a>
                    
                </div>
            </div>

            <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“Try not to become a man of success. Rather become a man of value.”</span>
                <span>by <small class="author" itemprop="author">Albert Einstein</small>
                <a href="/author/Albert-Einstein">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="adulthood,success,value" /    > 
                    
                    <a class="tag" href="/tag/adulthood/page/1/">adulthood</a>
                    
                    <a class="tag" href="/tag/success/page/1/">success</a>
                    
                    <a class="tag" href="/tag/value/page/1/">value</a>
                    
                </div>
            </div>

            <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“It is better to be hated for what you are than to be loved for what you are not.”</span>
                <span>by <small class="author" itemprop="author">André Gide</small>
                <a href="/author/Andre-Gide">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="life,love" /    > 
                    
                    <a class="tag" href="/tag/life/page/1/">life</a>
                    
                    <a class="tag" href="/tag/love/page/1/">love</a>
                    
                </div>
            </div>

            <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“I have not failed. I&#39;ve just found 10,000 ways that won&#39;t work.”</span>
                <span>by <small class="author" itemprop="author">Thomas A. Edison</small>
                <a href="/author/Thomas-A-Edison">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="edison,failure,inspirational,paraphrased" /    > 
                    
                    <a class="tag" href="/tag/edison/page/1/">edison</a>
                    
                    <a class="tag" href="/tag/failure/page/1/">failure</a>
                    
                    <a class="tag" href="/tag/inspirational/page/1/">inspirational</a>
                    
                    <a class="tag" href="/tag/paraphrased/page/1/">paraphrased</a>
                    
                </div>
            </div>

            <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it&#39;s in hot water.”</span>
                <span>by <small class="author" itemprop="author">Eleanor Roosevelt</small>
                <a href="/author/Eleanor-Roosevelt">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="misattributed-eleanor-roosevelt" /    > 
                    
                    <a class="tag" href="/tag/misattributed-eleanor-roosevelt/page/1/">misattributed-eleanor-roosevelt</a>
                    
                </div>
            </div>

            <div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
                <span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>
                <span>by <small class="author" itemprop="author">Steve Martin</small>
                <a href="/author/Steve-Martin">(about)</a>
                </span>
                <div class="tags">
                    Tags:
                    <meta class="keywords" itemprop="keywords" content="humor,obvious,simile" /    > 
                    
                    <a class="tag" href="/tag/humor/page/1/">humor</a>
                    
                    <a class="tag" href="/tag/obvious/page/1/">obvious</a>
                    
                    <a class="tag" href="/tag/simile/page/1/">simile</a>
                    
                </div>
            </div>

            <nav>
                <ul class="pager">
                    
                    
                    <li class="next">
                        <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
                    </li>
                    
                </ul>
            </nav>
            </div>
            <div class="col-md-4 tags-box">
                
                    <h2>Top Ten tags</h2>
                    
                    <span class="tag-item">
                    <a class="tag" style="font-size: 28px" href="/tag/love/">love</a>
                    </span>
                    
                    <span class="tag-item">
                    <a class="tag" style="font-size: 26px" href="/tag/inspirational/">inspirational</a>
                    </span>
                    
                    <span class="tag-item">
                    <a class="tag" style="font-size: 26px" href="/tag/life/">life</a>
                    </span>
                    
                    <span class="tag-item">
                    <a class="tag" style="font-size: 24px" href="/tag/humor/">humor</a>
                    </span>
                    
                    <span class="tag-item">
                    <a class="tag" style="font-size: 22px" href="/tag/books/">books</a>
                    </span>
                    
                    <span class="tag-item">
                    <a class="tag" style="font-size: 14px" href="/tag/reading/">reading</a>
                    </span>
                    
                    <span class="tag-item">
                    <a class="tag" style="font-size: 10px" href="/tag/friendship/">friendship</a>
                    </span>
                    
                    <span class="tag-item">
                    <a class="tag" style="font-size: 8px" href="/tag/friends/">friends</a>
                    </span>
                    
                    <span class="tag-item">
                    <a class="tag" style="font-size: 8px" href="/tag/truth/">truth</a>
                    </span>
                    
                    <span class="tag-item">
                    <a class="tag" style="font-size: 6px" href="/tag/simile/">simile</a>
                    </span>
                    
                
            </div>
        </div>

            </div>
            <footer class="footer">
                <div class="container">
                    <p class="text-muted">
                        Quotes by: <a href="https://www.goodreads.com/quotes">GoodReads.com</a>
                    </p>
                    <p class="copyright">
                        Made with <span class='zyte'>❤</span> by <a class='zyte' href="https://www.zyte.com">Zyte</a>
                    </p>
                </div>
            </footer>
        </body>
        </html>
        """

        response = HtmlResponse(url='http://example.com', body=html_content, encoding='utf-8')

        self.response = response

    def testAbsolute_and_relative_paths(self):
        response = self.response
        absolute_xpath = "//div"
        response.xpath("//div")

        self.assertEqual(response.xpath("//div").xpath("//div"), response.xpath("//div").xpath("//div"))
    

if __name__ == '__main__':
    unittest.main()