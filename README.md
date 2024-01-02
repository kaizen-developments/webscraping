# Web Scraping with Python Code Samples

These code samples are for the book <a href="http://shop.oreilly.com/product/0636920078067.do">Web Scraping with Python 2nd Edition</a>

If you're looking for the first edition code files, they can be found in the <a href="https://github.com/REMitchell/python-scraping/tree/master/v1">v1</a> directory.

Most code for the second edition is contained in <a href="https://jupyter.org/install.html">Jupyter notebooks</a>. Although these files can be viewed directly in your browser in Github, some formatting changes and oddities may occur. I recommend that you clone the repository, install Jupyter, and view them locally for the best experience.

The web changes, libraries update, and make mistakes and typos more frequently than I'd like to admit! If you think you've spotted an error, please feel free to make a pull request against this repository.

# My own documentation

Rules:
Indentation in propositions denote taking the parent as an assumption.
Propositions including terms, predicates can be written under predicates.
Terms, Propositions are not ending with any punctiation.
The punctuation "-" separates terms, predicates with functions, predicates applied to them, assuming that predicates reuturn true.
With indentating to a propositions involving universal, existential quantifiers, we might assume that instances are given for both the universally, and existentially bounded expressions.
classes in Python are structures, their methods are considered to be functions.
Print within decisions, and try-catch blocks, what conditions are true for the program, done by expressing that an error is not thrown in english, 
and printing what models are true during the program with respect to propositional models!
Assuming that access operator is applied on functions, therefore self.parse is meaningful -> self is a function.
By counting access operators and function call parameter lists, we can count the number of functions in a python code?

# Required
Formalize how do constants get substituted into expressions occuring within the text!
# On virtual environments

Virtual environments:
    Keeping all libraries separated by project using a virtual environment makes it easy to zip up the entire environment folder and send it to someone else. 
    A virtual environment is dependent on a Python version.

# Terms, Predicates, Propositions

Terms:
Modules:
   bs4 - arity ?
        Classes:
            BeautifulSoup
                Propositions:
                    Every time a BeautifulSoup object's tag accessed, it's smart to add a check to make sure the tag actually exists.
                        If you attempt to access a tag that does not exist, BeautifulSoup will return a None object.
                        The problem is, attempting to access a tag on a None object itself will result in an AttributeError being thrown.
                Methods:
                    .get_text - arity 1
                        Propositions:
                            Strips all tags from the document you are working with and returns a Unicode string containing the text only.
                                Example:
                                    Assume, that you are working with a large block of text that contains many hyperlinks, paragraphs, and other tags, all those will be stripped away, and you'll be left with a tagless block of text.
                                    Calling get_text is the last thing to do, immediately before printing, storing, or manipulating the final data.
                    .find(tag, attributes, recursive, text, keywords)
                        Propositions:
                            Filters HTML pages.
                                Finds lists of desired tags, or a single tag, based on their various attributes.
                    .find_all(tag, attributes, recursive, text, limit, keywords) - arity 6
                        Examples:
                            .find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                            .find_all('span', {'class':{'green', 'red'}}) = .find_all on which the substitution{tag<-'span', attributes<-{'class':{'green', 'red'}}} was applied on
                            .find_all with the substitution {limit <- 1} is equivalent to find!
                                Tag
                        Parameters and the expression of their result upon application:
                            TODO: Finish  ('a', href=re.compile('^(/|.*'+includeUrl+')')) - 'a' tags that ..., includeUrl is a string variable.
                Propositions:
                    Retrieved in lists, or retrieved individually by calling find and find_all on a BeautifulSoup object, or drilling down.
                    Example of drilling down is "bs.div.h1".
                Functions created with the module:
                    getTitle - arity 1, html link is the parameter.
            NavigableString
                Propostisions:
                    Used to represent text within tags, rather than the tags themeselves.
            Comment
                Propositions:
                    Used to find HTML comments in comment tags, <!--like this one-->. 
            Tag
                Methods:
                    .attrs - 
    urllib.request
        Methods:
            urlopen - arity ?
                Possible errors with applying urlopen to a html link:
                    1. The page is not found on the server or there was an error retrieving the page.
                        In  this case a HTTP error will be returned
                        urlopen throws the generic exception HTTPError
                    2. The server is not found at all.
                        urlopen throws URLError.
                        it is a possible cause, that the server is down, or the URL is mistyped.
    Traversing a single domain:
    Traversing ...:
        Functions:
            getLinks - Recursive algorithm for constructing a 

Predicates:
HTTP error
    Examples:
        "404 Page Not Found", "500 Internal Server Error"
    Traversing a single domain:
Redirect:
    Server Side redirect:
        The URL is changed before the page is loaded.
    Client side redirect:
        The page loads before redirecting to the new one, such as when "You will be redirected in 10 seconds." is shown.


Propositions:
    classes in Python are structures, their methods are considered to be functions.
    Beautiful Soup documentation:
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    BeaitifulSoup:
        BeautifulSoup tries to make sense of the nonsensical, helps to
        format and organize the messy web by fixing bad HTML and 
        presenting us with easily traversible Python objects representing XML structures.

        It is possible that a scraper hits on an unexpected data format and stops
        execution. 
            (N) There exists an error, which can be catched by a try catch block, allowing the code to proceed running.

        Any information can be extracted from any HTML or XML file as long as 
        the information has an identifying tag surrounding the information or 
        near the information.
        Therefore extracting information is dependent on an identifying tag.

        Popular parsers are lxml for HTML parsing html5lib.
        The lxml parser requires third-aprty C libraries to function.

        the_structure_of_the_beautiful_soup_object  = """ 
        html → <html><head>...</head><body>...</body></html>
            head → <head><title>A Useful Page<title></head>
                title → <title>A Useful Page</title>
            body → <body><h1>An Int...</h1><div>Lorem ip...
            </div></body>
                h1 → <h1>An Interesting Title</h1>
                div → <div>Lorem Ipsum dolor...</div>
        """

        the_structure_of_the_h1_tag = """ 
        html -> body -> h1
        """

        Every time a BeautifulSoup object is accessed, it is smart to add a check to make sure the tag actually exists.

        It is necessary for a line to have the possibility of throwing the exception occuring after an except keyword, if the line exists between that except keyword and a "try:" keyword.
    a tag x is a children of another tag y iff x is exactly one tag below y in a html document.
    a tag x is a descendant of another tag y iff x is 
    Until page 49, we have looked at accessing, filtering tags, and accessing content within them.
        Use cases:
            See problems!
    Chapter 3:
        Traversing a Single Domain:
            Propositions:
                It is possible, that a randow walk has to be taken going through a website, link to link.
            On links:
                If you examine the links that point to article pages (as
                opposed to other internal pages), you’ll see that they all have three things in
                common:
                    1. They reside within the 'div' with the 'id' set to 'bodyContent'.
                    2. The URL's don't contain colons.
                    3. The URL's begin with '/wiki/'.
        Crawling an entire site:
            Propositions:
                It is possible, that it is required to systematically catalog  or search every page on a site?
                Crawling an entire site, especially a large one, is a
                memory-intensive process that is best suited to applications for which a
                database to store crawling results is readily available.
                Use cases for Web scrapers traversing an entire site:
                    Generating a site map
                        For some important client an estimate was required for a web-redisign, dependent on a site map of the given website.
                    Gathering data
                        For some client a working prototype of a search platform was dependent on articles gathered from some sites.
                The general approach to an exhaustive site crawl is a directed BFS site crawl applied on a top level-page, where nodes are pages, and two pages are neighbours if and only if there is an internal link on the first page pointing to the second page (the internal links, or the edges have to be found).

            Expressions:
                Explore the behavior of these types of applications without running them full-scale!
            Collecting data across an entire site:
                Handling redirects:
                    urllib handles redirects automatically.
                        Allow redirect flag has to be set - such as in "r = requests.get('http://github.com', allow_redirects=True)" -.
        Crawling across the internet:
            Requirements to do cross-domain data analysis:
                Build crawlers that can interpret and store data across myriad of pages on the internet.
                    TODO: Find an implementation of an interpretation function of data on the internet used by a crawler!
            Before writing a crawler, determine
                1. what data am I trying to gather.
                2. whether gathering data can be accomplished by scraping just a few predefined websites (the easier option), or does my crawler need to be able to discover 3. new websites i might not know about?
                4. when my crawler reaches a particular website, will it immediately follow the next outbound link to a new website, or will the crawler stick around for a while and drill down into the current website?
                5. the conditions under which I would not want to scrape a particular site.
                6. whether am I interested in non-english content or not.
                7. how am I protecting myself against legal action if my web-crawler catches the attention of a webmaster on one of the sites the web crawler runs across?
    Chapter4:
        Writing code for web crawlers, which may need to scrape and store a variety of data from diverse sets of websites that the programmer has no control over, often presents unique organizational challenges.
            You may be asked to collect news articles or blog posts from a variety of websites, each with different templates and layouts.
                One website’s h1 tag contains the title of the article, another’s h1 tag contains the title of the website itself, and the article title is in <span id="title">.
                TODO: Collect news articles from https://www.nytimes.com/ with a free profile!
            You may need flexible control over which websites are scraped and how
            they’re scraped, and a way to quickly add new websites or modify existing ones, as fast as possible, without writing multiple lines of code.
                TODO: Define control over which websites are scraped and how they are scraped explicitly for a crawler!
            You may be asked to scrape product prices from different websites, with the ultimate aim of comparing prices for the same product. Perhaps these prices
            are in different currencies, and perhaps you’ll also need to combine this with
            external data from some other nonweb source.
        Patterns/Models of large scalable crawlers:
        Determine what are my requirements instead of determining what exists to solve the issue of choosing a header for the data to gather.
            Example:
                Perhaps what you really want to do is compare product prices among multiple stores and track those product prices over time. In this case, you need enough information to uniquely identify the product, and that’s it:
                    (Product Title, Manufacturer, Product ID Number (if available, relevant))
                Type of the example: (Requirement, necessary data) pair.
        Have a checklist (like a predicate) for each item to consider (TODO: Determine items to consider for a given parser), such as
            Will this information help with the project goals? 
            Will it be a roadblock if I don’t have it, or is it just “nice to have” but won’t ultimately impact anything?
            If it might help in the future, but I’m unsure, how difficult will it be to go back and collect the data at a later time?
            Is this data redundant to data I’ve already collected?
            Does it make logical sense to store the data within this particular object? (As mentioned before, storing a description in a product doesn’t make sense if that description changes from site to site for the same product.)
        If you do decide that you need to collect the data, it’s important to ask a few more questions to then decide how to store and handle it in code:
            Is this data sparse or dense? Will it be relevant and populated in every listing, or just a handful out of the set?
            How large is the data?
            Especially in the case of large data, will I need to regularly retrieve it every time I run my analysis, or only on occasion?
            How variable is this type of data? 
            Will I regularly need to add new attributes, modify types (such as fabric patterns, which may be added frequently), or is it set in stone (shoe sizes)?
        If the data available is sparse and we might have to modify attributes frequently, it is a good practice to create a product type, like (Product title, manufacturer, Product ID number, Attributes), and an attribute type that looks like this (Attribute name, attribute value)
            Allows:
                Flexibly add new product attributes over time, without requiring you to redesign your data schema or rewrite code
        Own:
            Smilarly as Google's search engine with Google's search engine's domain is a good product for us humans, assuming Google's search engine being a web crawler, providing probably relevant information dependent on a search string, a web-crawler could be a good product for any software product for some domain, providing probably elevant data to the software product from the domain.
                Generalizations:
                    Google's search enginer -> Arbitrary web-crawler, humans -> Software product
        Dealing with Different Website Layouts:
        Every site’s parsing function does essentially the same thing:
            1. Selects the title element and extracts the text for the title
                TODO: Implement this functionality in a crawler!
            2. Selects the main content of the article
                TODO: Implement this functionality in a crawler!
            3. Selects other content items as needed!
                TODO: Implement this functionality in a crawler!
            4. Returns a Content object instantiated with the strings found previously!
                TODO: Implement this functionality in a crawler!
        Headers for items:
            Item type = (Product ID, Instance type)
            Instance type = (Product Instance ID, Store ID, Price, Date/Timestamp price was found at)
            Examples:
                ("CBA piros papírzsebkendő, 3 réteg, 100db", (5999558954543, None, None, None)),
                ("Pénzfelvét", (8151, 82220042, 160000 HUF, 2023/12/11/12:16))
        Header for scraping news articles:  
            News article = (Title, Author, Date, Content)
            The following are either important or not:
                revision date, related articles, number of social media shares.
        
# Processes

Processes:
Install BeautifulSoup 4!
    In a Linux terminal:
        1. sudo apt-get install python-bs4
        2. pip install beautifulsoup4
#Generalize from the previous code!
#   Copy the previous code!
#   Start a parameter list above the copied previous code!
#   Indent the previous code by one!
#   In parallel(parameter list of the generalized function):
    #   Create the generalized function!
    #       Create the parameter list!
    #           If the parameter list of the generalized function does not match the parameter list in the construction of the example, update the generalized function parameters!
    #       Start a parameter list above the copied previous code!
    #       3. If the parameter list of the generalized function exists, fill it up with names of the values to be generalized, that can be found
    #       in the parameter list of the special case, by finding names for the values!
    #       If the name of the function does not exist yet, create the name of the generalized function, 
    #       which must contain all the parameters of its parameter list in the order of the elements of the parameter list!
    #       If a name in the generalized function's definition corresponds to a value in the special case, in the generalized function definition change the value accordingly!
    #       If some block has to be generalized, then go and find a proper substitution fo the block, take the block out from the function definition, put the block above it, generalize the block aswell accordingly, and make a substitution for the block accordingly!
    #       Repeat from the 3rd step
    #   Create the previous example from the generalization!
    #       Create the first - "(" - part of the parameter list of the special case!
    #       Create the parameters!
    #           Fill the parameter list below the example code for the special case, if more values can be determined or modify the order of the values according to the
    #           changes in the generalized function's parameter's order, otherwise close the parameter list with ")".
    #       Create the function name!
    #           If the generalized function had not been named yet, create the function name,  until then wait repeat from creating the parameters!
#     Make sure, that the special case is equal to the result of the previous code!

# Tasks and sources

Feladatok
    Mutassunk meg minden olyan osztályt, melynek példányai eredményezhetnek AttributeErrort a bs4 modulon belül!
    BeautifulSoup:
        Find useful examples of get_text() by removing paragraphs, and unnecessary tags in a text, obtaining only the useful block of text!
    Create a language interface, that would recognize the "TODO:" string in a text, and which, in turn, would allow defining a task to do within any website for managing task related to a VSC code! Create the language interface with a parser of C++ and 
    

Sources:
    Beautiful Soup documentation:
        https://www.crummy.com/software/BeautifulSoup/bs4/doc/


# Stats

Stat:
    Események:
        3
            dátum 2022.12.17
            kezdőpont 14:35
            befejezés ideje 18:35

TODO:
    Set out 5 hours of learning besides an 8 hour learning day!


Misc:
Crawling through forms is a function, defined in the 10th chapter.

Coding convention to produce nice code, based on data obtained from the book Web scraping with Python_ collecting more data from the modern web by O'Reilly with nice code!
	Name variables with predicates!
	Name variables of collections with plural form!
	Name variables of objects other than collections with singular form!
	Have getter functions, that start with the keyword "get" and are followed by the predicate being equal to the variable, receiving the object from the getter!
		Example: historyIPs = getHistoryIPs(link.attrs['href'])
	Make variables denote the class into which the return value of the function belongs to, showing information of the output of a function within the name of a variable!
		Example: ipAddresses = bs.findAll('a', {'class':'mw-anonuserlink'})
	Variable names start with lowercase letters, and are camelCase!
	Eliminate the need for variables by having keyword arguments taking parameters inside the program, to which keyword arguments the same principles apply to as to variables!
		Example:
			driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
    If possible, to the right of a return statement show the type of the data that gets returned with the parameters instantiatin that type, or make the type of the return data obvious by the constants occuring in the returned expression!
	
	Interpretations:(Which can be written next to a function)
		driver.get_cookies() - From the driver get cookies!, Get cookies from the driver!
		driver.implicitly_wait(1) - Implicitly wait 1 second with the driver!
		driver.get('http://pythonscraping.com') - Get 'http://pythonscraping.com' with the driver!
		time.sleep(3) - Using time sleep 3 units (Using can be applied more generally, than the previous relations.)
		link.is_displayed() - Link is displayed.
		myElement.click() - Click my element!
		myElement.double_click() - Double click my element!
		myElement.send_keys_to_element('content to enter') - Using my element send keys to element 'content to enter'!
		actions = ActionChains(driver).click(firstnameField).send_keys('Ryan')
										.click(lastnameField).send_keys('Mitchell')
										.send_keys(Keys.RETURN) - Using the action chains of driver click firstnameField, then send keys to 'Ryan', then click lastnameField, then send keys to 'Mitchell'.
		self.done = False - Crawler is not done.
            try:
                title = bs.find('h1').text
                body = bs.find('div', {'class', 'post-body'}).text #body = bs.find('div', {'class', 'post-body'}).text resulted in a 'NoneType' object has no attribute 'text' error.
            except AttributeError as e:
                return None #Try to proceed the execution with the two lines, except when attributeError is thrown, then return None.

Product types:
	Product required to be generated for every program code, requirement during learning:								
		Use Case of some function =(Requirement, description of solution with a process, function naming the realization of the process in an interface describing the solution of the requirement, Realization of the function)
		Requirements met by function=(function, requirements met)
			A requirement met could be "avoids getting banned", that could be realized in a private interface.