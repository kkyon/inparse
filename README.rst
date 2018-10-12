=======
In.parse
=======
0.1.0


Collaborative AI  Driven Web Scraping, Data Extraction and Crawling,Knowledge Graph


Installing
----------

Install and update using ``pip``:

`pip install -U inparse`

Documentation
------------

http://inparse.com




Philosophy
==========


What's data-driven programming?
===============================

All functions are connected by pipes (queues) and communicate by data.  

When data come in, the function will be called and return the result.



.. code-block:: python

    from inparse import Inparse
    p=Inparse('b45beddc',\  #parser no is generator by inparse.com parser builder.
               'd50cb533f69b6a78892afbd093f95fc1')  #access token can be found in your user page  .


    d=p.parse_url('https://qz.com/india/1413291/trulymadly-ceo-on-how-dating-apps-like-bumble-india-must-localise/')
    Inparse.pretty_print(d)




**Or write in chain style**

.. code-block:: python

    from inparse import Inparse
    import requests
    p=Inparse('b45beddc',\  #parser no is generator by inparse.com parser builder.
               'd50cb533f69b6a78892afbd093f95fc1')  #access token can be found in your user page  .

    html=requests.get('https://qz.com/india/1413291/trulymadly-ceo-on-how-dating-apps-like-bumble-india-must-localise/').text
    d=p.parse(html)
    Inparse.pretty_print(d)



** Parser web result without write any xpath or css selector.
.. code-block:: python

    {   'article_body': '<div><p>Last week, American dating app <a '
                        'href="https://qz.com/india/1413051/priyanka-chopra-invests-in-dating-app-bumble-to-rival-tinder/">Bumble '
                        'It’s from smaller cities. And varied people are coming '
                        'from different backgrounds. So that’s really '
                        'encouraging.</p></div>',
        'author': 'Kuwar Singh',
        'publish_date': None,
        'title': 'Young Indians are using dating apps for so much more than just '
                 'dating',
        'top_image': [   'https://cms.qz.com/wp-content/uploads/2018/10/AP_900509923043-e1538971405267.jpg?quality=75&strip=all&w=410&h=231']
    }



More about Botflow
===============

Data-driven programming is typically applied to streams of structured data for filtering, transforming, aggregating (such as computing statistics), or calling other programs.

Botflow has a few basic concepts to implement Data-driven programming .

- **Source**
        It is emit stream data to the pipe.

    * **Timer**: It will send a message in the pipe by timer param. **delay**, **max_time** **until** some finished
    * **Pipe.run**: you can use Pipe.run to trigger the data into pipe. By default it will feed int **0**
    * **CCT**:  Cryptocurrency Ticker .**TODO** will release on 0.2.1


- **Function**
        It is callable unit.Any callable function and object can work as Node. It is driven by data. Custom functions work as Map unit.
        There are some built-in nodes:

   

   * **Fetch**: (Alias:HttpLoader)  Get a url and return the HTTP response
   * **AioFile**: for file I/O.
   * **SpeedLimit**: limit the stream speed limit
   * **Delay**: delay in special second.
   * **Map**  : Work ad Convert unit.
   * **Filter** : Drop data from pipe if it does not match some condition
   * **Flat** : Drop data from pipe if it does not match some condition


- **Route**
        It will be used to create a complex data flow network, not just one main process. Botflow can nest Routes inside Routes.
        It is a powerful concept.
        There are some pre built-in Route:
    * **Pipe**: It is the main stream process of the program. All units will work inside.
    * **Branch** : (Alias:Tee) Duplicate data from parent pipe to a child pipe as branch.
    * **Zip** :   Combine multi pipes result to list.
    * **Link**: (Alias: LinkTo)  Route flow to any Node or Route for making loop , circle


All units (Pipe, Node, Route) communicate via queues and perform parallel computation in coroutines.
This is abstracted so that Botflow can be used with only limited knowledge of ``asyncio``.


      

Contributing
------------


Donate
------


Links
-----
