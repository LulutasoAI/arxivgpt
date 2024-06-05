default_system_message = """
[Attention! READ BELOW REALLY CAREFULLY!] 
When given a research request from the user, it's your job to generate the best search query on the Arxiv platform. As it will be processed programmatically, [[[you must return only the search query]]]. The query must be returned in English. Your response does not include anything but the query! Your response must be in accordance with the rules above. If you do not follow these rules, your response will be marked as incorrect.
EXAMPLES:
all:Reinforcement learning
all:maths
all:cats
"""
'''
default_system_message = """
5.1. Details of Query Construction
As outlined in the Structure of the API section, the interface to the API is quite simple. This simplicity, combined with search_query construction, and result set filtering through id_list makes the API a powerful tool for harvesting data from the arXiv. In this section, we outline the possibilities for constructing search_query's to retrieve our desired article lists. We outlined how to use the id_list parameter to filter results sets in search_query and id_list logic.

In the arXiv search engine, each article is divided up into a number of fields that can individually be searched. For example, the titles of an article can be searched, as well as the author list, abstracts, comments and journal reference. To search one of these fields, we simply prepend the field prefix followed by a colon to our search term. For example, suppose we wanted to find all articles by the author Adrian Del Maestro. We could construct the following query

http://export.arxiv.org/api/query?search_query=au:del_maestro

This returns nine results. The following table lists the field prefixes for all the fields that can be searched.

prefix	explanation
ti	Title
au	Author
abs	Abstract
co	Comment
jr	Journal Reference
cat	Subject Category
rn	Report Number
id	Id (use id_list instead)
all	All of the above
Note: The id_list parameter should be used rather than search_query=id:xxx to properly handle article versions. In addition, note that all: searches in each of the fields simultaneously.

The API allows advanced query construction by combining these search fields with Boolean operators. For example, suppose we want to find all articles by the author Adrian DelMaestro that also contain the word checkerboard in the title. We could construct the following query, using the AND operator:

http://export.arxiv.org/api/query?search_query=au:del_maestro+AND+ti:checkerboard

As expected, this query picked out the one of the nine previous results with checkerboard in the title. Note that we included + signs in the urls to the API. In a url, a + sign encodes a space, which is useful since spaces are not allowed in url's. It is always a good idea to escape the characters in your url's, which is a common feature in most programming libraries that deal with url's. Note that the <title> of the returned feed has spaces in the query constructed. It is a good idea to look at <title> to see if you have escaped your url correctly.

The following table lists the three possible Boolean operators.

AND
OR
ANDNOT
The ANDNOT Boolean operator is particularly useful, as it allows us to filter search results based on certain fields. For example, if we wanted all of the articles by the author Adrian DelMaestro with titles that did not contain the word checkerboard, we could construct the following query:

http://export.arxiv.org/api/query?search_query=au:del_maestro+ANDNOT+ti:checkerboard

As expected, this query returns eight results.

Finally, even more complex queries can be used by using parentheses for grouping the Boolean expressions. To include parentheses in in a url, use %28 for a left-parens (, and %29 for a right-parens ). For example, if we wanted all of the articles by the author Adrian DelMaestro with titles that did not contain the words checkerboard, OR Pyrochore, we could construct the following query:

http://export.arxiv.org/api/query?search_query=au:del_maestro+ANDNOT+%28ti:checkerboard+OR+ti:Pyrochlore%29

This query returns three results. Notice that the <title> element displays the parenthesis correctly meaning that we used the correct url escaping.

So far we have only used single words as the field terms to search for. You can include entire phrases by enclosing the phrase in double quotes, escaped by %22. For example, if we wanted all of the articles by the author Adrian DelMaestro with titles that contain quantum criticality, we could construct the following query:

http://export.arxiv.org/api/query?search_query=au:del_maestro+AND+ti:%22quantum+criticality%22

This query returns one result, and notice that the feed <title> contains double quotes as expected. The table below lists the two grouping operators used in the API.

symbol	encoding	explanation
( )	%28 %29	Used to group Boolean expressions for Boolean operator precedence.
double quotes	%22 %22	Used to group multiple words into phrases to search a particular field.
space	+	Used to extend a search_query to include multiple fields.

5.1.1. A Note on Article Versions
Each arXiv article has a version associated with it. The first time an article is posted, it is given a version number of 1. When subsequent corrections are made to an article, it is resubmitted, and the version number is incremented. At any time, any version of an article may be retrieved.

When using the API, if you want to retrieve the latest version of an article, you may simply enter the arxiv id in the id_list parameter. If you want to retrieve information about a specific version, you can do this by appending vn to the id, where n is the version number you are interested in.

For example, to retrieve the latest version of cond-mat/0207270, you could use the query http://export.arxiv.org/api/query?id_list=cond-mat/0207270. To retrieve the very first version of this article, you could use the query http://export.arxiv.org/api/query?id_list=cond-mat/0207270v1

[Attention! READ BELOW REALLY CAREFULLY!] 
When given a research request from the user, it's your job to generate the best search query on the Arxiv platform. As it will be processed programmatically, [[[you must return only the search query]]]. The query must be returned in English. Your response does not include anything but the query! Your response must be in accordance with the rules above. If you do not follow these rules, your response will be marked as incorrect.
EXAMPLES:
all:del_maestro

all:"del_maestro"+AND+ti:"checkerboard"

all:"del_maestro"+ANDNOT+ti:"checkerboard"

all:"del_maestro"+ANDNOT+%28ti:"checkerboard"+OR+ti:"Pyrochlore"%29

all:"del_maestro"+AND+ti:%22"quantum"+"criticality"%22

all:"del_maestro"+AND+%28ti:%22"quantum"+"criticality"%22+OR+abs:%22"quantum"+"criticality"%22%29

all:"del_maestro"+AND+%28ti:"checkerboard"+OR+ti:"Pyrochlore"%29

all:"del_maestro"+AND+ti:%22"quantum"+"criticality"%22+ANDNOT+%28ti:"checkerboard"+OR+ti:"Pyrochlore"%29
"""
'''
summary_message = "Based on the extensive text provided, generate a concise summary that captures the main points and essential details."
translation_message = "Please translate the following English text into Japanese, ensuring the highest possible precision and accuracy in conveying the meaning."