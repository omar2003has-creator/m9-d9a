def q1():
    return """
PREFIX : <http://example.org/library/>
SELECT ?book ?title
WHERE {
    ?book a :Book ;
          :title ?title .
}
"""

def q2():
    return """
PREFIX : <http://example.org/library/>
SELECT ?book ?year
WHERE {
    ?book a :Book ;
          :year ?year .
    FILTER (?year > 2010)
}
"""

def q3():
    return """
PREFIX : <http://example.org/library/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?book ?author_name
WHERE {
    ?book a :Book ;
          :author ?a .
    ?a rdfs:label ?author_name .
}
"""

def q4():
    return """
PREFIX : <http://example.org/library/>
SELECT ?book ?topic
WHERE {
    ?book a :Book .
    OPTIONAL { ?book :topic ?topic . }
}
"""

def q5():
    return """
PREFIX : <http://example.org/library/>
ASK
WHERE {
    ?book a :Book ;
          :author ?a1 ;
          :author ?a2 .
    FILTER (?a1 != ?a2)
}
"""