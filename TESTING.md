#### Google Developer Tools

I used Google Chrome Developer Tools throughout the project. It was an invaluable resource to check how HTML and CSS changes would look. It was a particularly useful tool to have when checking for responsiveness on difference sized devices. 

I used the Lighthouse tool to check over my website. I went through each page sequentially in the browser and made a note of any issues to resolve (see table below). Overall, on first tests the site performed well and most were green, but there were a few adjustments to improve the site. 

| Page       | Lighthouse Improvement | Action | Adjusted |
| -----------|:-------------:| 
| home.html | Add meta data  |  Write meta data in head | Yes |
| home.html | Make sure H1-6 are in sequential order | Made sure no gaps in order of headings | Yes |
| contact.html | Make sure H1-6 are in sequential order | Made sure no gaps in order of headings | Yes |
| contact.html | Improve contrast of text on form | Add white background to form | Yes |
| profile.html | Make sure H1-6 are in sequential order | Made sure no gaps in order of headings |Yes |
| add_cockney.html | Make sure H1-6 are in sequential order | Made sure no gaps in order of headings | Yes |


The final report for the home page can be viewed below and [here](static/testing/testing_lighthouse_pgtw.png)

<img src="static/testing/testing_lighthouse_pgtw.png" width="500"> 

#### HTML, CSS and JS Tests

### W3C Validator Testing
I used the W3C validators for HTML and CSS to check my code. 
All pages passed the checks after some adjustments to code. The main issue was in my semantic mark up of the pages. I had used main more than once and some sections did not have headings. This was rectified and here is an example below:

<img src="static/testing/testing_w3c_html_valid_pgtw.png" width="500"> 

<img src="static/testing/testing_w3c_css_valid_pgtw.png" width="500"> 


### BeautifyTools for JS????
http://beautifytools.com/javascript-validator.php On the final test there were no errors found. There were a few errors throughout my work on the project that I corrected as I developed.

#### Defensive Programming after initial tests

After a mentoring session where we tested through some of the features, I was advised to add in some defensive programming to secure my site better.
This meant that on the Log In page I added an extra layer of code so that a user needed to be "in session" to be able to access
the add to dictionary page. Otherwise, any user could retype the URL link themselves and access the add_cockney.html page.

Please refer to seperate document found [here](TESTING.md)

* Noticed bug with mobile view that navbar <a></a> link for brand-logo didn't display fully so adjusted design to use an icon which mixed up the media and worked better visually 
for responsiveness.

  if request == "POST":
        word = {
            "word": request.form.get("word"),
            "meaning": request.form.get("meaning"),
            "added_by": session["user"]
            }
        mongo.db.cockney_dictionary.insert_one(word)


* bug in display of dictionary showing first line the wrong way round for word and meaning. The html h5 tag I had added had made it display incorrectly.
