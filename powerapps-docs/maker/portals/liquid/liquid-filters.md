---
title: Available Liquid filters
description: Learn about the available liquid filters in a portal.
author: gitanjalisingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2020
ms.subservice: portals
ms.author: gisingh
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - GitanjaliSingh33msft
---

# Available Liquid filters

Liquid filters are used to modify the output of strings, numbers, variables, and objects. They are separated from the value to which they are being applied by a |.

`{{ 'hal 9000' | upcase }} <!-- Output: HAL 9000 -->`

Some filters accept parameters. Filters can also be combined, and are applied in order from left to right.

```
{{ 2 | times: 2 | minus: 1 }} <!-- Output: 3 -->

{{ "Hello, " | append: user.firstname }} <!-- Output: Hello, Dave -->
```
The below section describes various filters. 

## Array filters

Array filters are used to work with [arrays](liquid-types.md#array).  

### batch

Divides an array into multiple arrays of a given size.

**Code**

```
{% assign batches = entityview.records | batch: 2 %}

{% for batch in batches %}

<ul>

{% for item in batch %}

<li>{{ item.fullname }}</li>

{% endfor %}

</ul>

{% endfor %}
```

**Output**

```
<ul>

<li>John Smith</li>

<li>Dave Thomas</li>

</ul>

<ul>

<li>Jake Johnson</li>

<li>Jack Robinson</li>

</ul>
```

### concat

Concatenates two arrays into a single new array.

Given a single item as a parameter, concat returns a new array that consists of the original array, with the given item as the last element.

**Code**

```
Group #1: {{ group1 | join: ', ' }}

Group #2: {{ group2 | join: ', ' }}

Group #1 + Group #2: {{ group1 | concat: group2 | join: ', ' }}

Group #1 + Leslie: {{ group1 | concat: 'Leslie' | join: ', ' }}
```

**Output**

```
Group #1: John, Pete, Hannah

Group #2: Joan, Bill

Group #1 + Group #2: John, Pete, Hannah, Joan, Bill

Group #1 + Leslie: John, Pete, Hannah, Leslie
```

### except

Select all the objects in an array where a given attribute does not have a given value. (This is the inverse of**where**.)

**Code**

```
{% assign redmond = entityview.records | except: 'address1_city', 'Redmond' %}

{% for item in redmond %}

{{ item.fullname }}

{% endfor %}
```

**Output**

```
Jack Robinson
```

### first

Returns the first element of an array.

first can also be used with a special dot notation, in cases where it needs to be used inside a tag.

**Code**

```
{% assign words = This is a run of text | split:   %}

{{ words | first }}

{% if words.first == This %}

The first word is This.

{% endif %}
```

**Output**

```
This

The first word is This.
```

### group_by

Group the items in an array by a given attribute.

**Code**

```
{% assign groups = entityview.records | group_by: 'address1_city' %}

{% for group in groups %}

{{ group.key }}:

{% for item in group.items %}

{{ item.fullname }}

{% endfor %}

{% endfor %}
```

**Output**

```
Redmond:

John Smith

Dave Thomas

Jake Johnson

New York:

Jack Robinson
```

### join

Joins the elements of an array with the character passed as the parameter. The result is a single string.

**Code**

```
{% assign words = This is a run of text | split:   %}

{{ words | join: ,  }}
```

**Output**

```
This, is, a, run, of, text
```

### last

Returns the last element of an array.

last can also be used with a special dot notation, in cases where it needs to be used inside a tag.

**Code**

```
{% assign words = This is a run of text | split:   -%}

{{ words | last }}

{% if words.last == text -%}

The last word is text.

{% endif -%}
```

**Output**

```
text

The last word is text.
```

### order\_by

Returns the elements of an array ordered by a given attribute of the elements of the array.

Optionally, you can provide desc as a second parameter to sort the elements in descending order, rather than ascending.

**Code**

```
{{ entityview.records | order_by: 'fullname' | join: ', ' }}

{{ entityview.records | order_by: 'fullname', 'desc' | join: ', ' }}
```

**Output**

```
Dave Thomas, Jack Robinson, Jake Johnson, John Smith

John Smith, Jake Johnson, Jack Robinson, Dave Thomas
```

### random

Returns a single randomly-selected item from the array.

**Code**

```
{{ group1 | join: ', ' }}

{{ group1 | random }}
```

**Output**

```
John, Pete, Hannah

Pete
```

### select

Selects the value of a given attribute for each item in an array, and returns these values as an array.

**Code**

```
{{ entityview.records | select: 'address1_city' | join: ', ' }}
```

**Output**

```
Redmond, New York
```

### shuffle

Applied to an array, returns a new array with the same items, in randomized order.

**Code**

```
{{ group1 | join: ', ' }}

{{ group1 | shuffle | join: ', ' }}
```

**Output**

```
John, Pete, Hannah

Hannah, John, Pete
```

### size

Returns the number of items in an array.

size can also be used with a special dot notation, in cases where it needs to be used inside a tag.

**Code**

```
{% assign words = This is a run of text | split:   -%}

{{ words | size }}

{% if words.size == 6 -%}

The text contains 6 words.

{% endif -%}
```

**Output**

```
6

The text contains 6 words.
```

### skip

Skips a given number of items in an array, and returns the rest.

**Code**

```
{% assign words = This is a run of text | split:   %}

{{ words | skip: 3 | join: ', ' }}
```

**Output**

```
run, of, text
```

### take

Takes a given number of items from the array, returning the taken items.

**Code**

```
{% assign words = This is a run of text | split:   %}

{{ words | take: 3 | join: ', ' }}
```
**Output**

```

This, is, a
```

### then\_by

Adds additional subsequent ordering to an array already ordered by**order\_by**.

Optionally, you can provide desc as a second parameter to sort the elements in descending order, rather than ascending.

**Code**

```
{{ entityview.records | order_by: 'address1_city' | then_by: 'fullname' | join: ', ' }}

{{ entityview.records | order_by: 'address1_city' | then_by: 'fullname', 'desc' | join: ', ' }}
```

**Output**

```
Dave Thomas, Jack Robinson, Jake Johnson, John Smith

John Smith, Jake Johnson, Jack Robinson, Dave Thomas
```

### where

Select all the objects in an array where a given attribute has a given value.

**Code**

```
{% assign redmond = entityview.records | where: 'address1_city', 'Redmond' %}

{% for item in redmond %}

{{ item.fullname }}

{% endfor %}
```

**Output**

```
John Smith

Dave Thomas

Jake Johnson
```


## Date filters

Date filters can be used for date arithmetic or to convert DateTime values into various formats.

### date

Formats a DateTime value using a .NET format string.

[Standard Date and Time Format Strings](/dotnet/standard/base-types/standard-date-and-time-format-strings)  

[Custom Date and Time Format Strings](/dotnet/standard/base-types/custom-date-and-time-format-strings)  

**Code**

```
{{ now | date: 'g' }}

{{ now | date: 'MMMM dd, yyyy' }}
```

**Output**

```
5/7/2018 7:20 AM

May 07, 2018
```

### date\_add\_days

Adds the specified number of whole and fractional days to the DateTime value. The parameter can be positive or negative.

**Code**

```
{{ now }}

{{ now | date_add_days: 1 }}

{{ now | date_add_days: -2.5 }}
```

**Output**

```
5/7/2018 7:20:46 AM

5/8/2018 7:20:46 AM

5/4/2018 7:20:46 PM
```

### date\_add\_hours

Adds the specified number of whole and fractional hours to the DateTime value. The parameter can be positive or negative.

**Code**

```
{{ now }}

{{ now | date_add_hours: 1 }}

{{ now | date_add_hours: -2.5 }}
```

**Output**

```
5/7/2018 7:20:46 AM

5/7/2018 8:20:46 AM

5/7/2018 4:50:46 AM
```

### date\_add\_minutes

Adds the specified number of whole and fractional minutes to the DateTime value. The parameter can be positive or negative.

**Code**

```
{{ now }}

{{ now | date_add_minutes: 10 }}

{{ now | date_add_minutes: -2.5 }}
```


**Output**

```
5/7/2018 7:20:46 AM

5/7/2018 7:30:46 AM

5/7/2018 7:18:16 AM
```

### date\_add\_months

Adds the specified number of whole months to the DateTime value. The parameter can be positive or negative.

**Code**

```
{{ now }}

{{ now | date_add_months: 1 }}

{{ now | date_add_months: -2 }}
```

**Output**

```
5/7/2018 7:20:46 AM

6/7/2018 7:20:46 AM

3/7/2018 7:20:46 AM
```

### date\_add\_seconds

Adds the specified number of whole and fractional seconds to the DateTime value. The parameter can be positive or negative.

**Code**

```
{{ now }}

{{ now | date_add_seconds: 10 }}

{{ now | date_add_seconds: -1.25 }}
```

**Output**

```
5/7/2018 7:20:46 AM

5/7/2018 7:20:56 AM

5/7/2018 7:20:45 AM
```

### date\_add\_years

Adds the specified number of whole years to the DateTime value. The parameter can be positive or negative.

**Code**

```
{{ now }}

{{ now | date_add_years: 1 }}

{{ now | date_add_years: -2 }}
```

**Output**

```
5/7/2018 7:20:46 AM

5/7/2019 7:20:46 AM

5/7/2016 7:20:46 AM
```

### date\_to\_iso8601

Formats a DateTime value according to the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard. Useful when creating [*Atom feeds*](https://tools.ietf.org/html/rfc4287), or the HTML5 &lt;time&gt; element.  

**Code**

```
{{ now | date_to_iso8601 }}
```

**Output**

```
2018-05-07T07:20:46Z
```

### date\_to\_rfc822

Formats a DateTime value according to the [RFC 822](https://www.ietf.org/rfc/rfc0822.txt) standard. Useful when creating [*RSS feeds*](https://cyber.law.harvard.edu/rss/rss.html).  

**Code**

```
{{ now | date_to_rfc822 }}
```

**Output**

```
Mon, 07 May 2018 07:20:46 Z
```


## List filters

List filters are used to work with certain [entitylist](liquid-objects.md#entitylist) attribute values, and to help create list views.  

### current\_sort

Given a sort expression, returns the current sort direction for a given attribute.

**Code**

```
{{ 'name ASC, createdon DESC' | current_sort: 'createdon' }}
```

**Output**

```
DESC
```

### metafilters

Parses an [entitylist](liquid-objects.md#entitylist) filter\_definition JSON value into filter option group objects.  

metafilters can be optionally provided with a current attribute filter query and current [entitylist](liquid-objects.md#entitylist), allowing the returned filter objects to be flagged as either selected or unselected.

**Code**

```
{% assign filters = entitylist | metafilters: params.mf, entityview %}
{% if filters.size > 0 %}
  <ul id=entitylist-filters>
    {% for filter in filters %}
      <li class=entitylist-filter-option-group>
        {% if filter.selection_mode == 'Single' %}
          {% assign type = 'radio' %}
        {% else %}
          {% assign type = 'checkbox' %}
        {% endif %}
        <h4 class=entitylist-filter-option-group-label
          data-filter-id={{ filter.id | h }}>
          {{ filter.label | h }}
        </h4>
        <ul>
          {% for option in filter.options %}
            <li class=entitylist-filter-option>
              {% if option.type == 'text' %}
                <div class=input-group entitylist-filter-option-text>
                  <span class=input-group-addon>
                    <span class=fa fa-filter aria-hidden=true></span>
                  </span>
                  <input class=form-control
                    type=text
                    name={{ filter.id | h }}
                    value={{ option.text | h }} />
                </div>
              {% else %}
                <div class={{ type | h }}>
                  <label>
                    <input
                      type={{ type | h }}
                      name={{ filter.id | h }}
                      value={{ option.id | h }}
                      {% if option.checked %}
                        checked=checked
                        data-checked=true{% endif %}
                      />
                    {{ option.label | h }}
                  </label>
                </div>
              {% endif %}
            </li>
          {% endfor %}
        </ul>
      </li>
    {% endfor %}
  </ul>
  <button class=btn btn-default data-serialized-query=mf data-target=#entitylist-filters>Apply Filters</button>
{% endif %}
```

### reverse\_sort

Given a sort direction, returns the opposite sort direction.

**Code**

```
<!-- Sort direction is not case-sensitive -->

{{ 'ASC' | reverse_sort }}

{{ 'desc' | reverse_sort }}
```

**Output**

```
DESC

ASC
```


## Math filters

Math filters allow you to perform mathematical operations on [numbers](liquid-types.md#number).  

As with all filters, math filters can be chained, and are applied in order from left to right.

**Code**

```
{{ 10 | times: 2 | minus: 5 | divided_by: 3 }}
```

**Output**

```
5
```

### ceil

Rounds a value up to the nearest integer.

**Code**

```
{{ 4.6 | ceil }}

{{ 4.3 | ceil }}
```

**Output**

```
5

5
```

### divided\_by

Divides a number by another number.

**Code**

```
{{ 10 | divided_by: 2 }}

{{ 10 | divided_by: 3 }}

{{ 10.0 | divided_by: 3 }}
```

**Output**

```
5

3

3.333333
```

### floor

Rounds a value down to the nearest integer.

**Code**

```
{{ 4.6 | floor }}

{{ 4.3 | floor }}
```

**Output**

```
4

4
```

### minus

Subtracts a number from another number.

**Code**

```
<!-- entityview.page = 11 -->

{{ entityview.page | minus: 1 }}

{{ 10 | minus: 1.1 }}

{{ 10.1 | minus: 1 }}
```

**Output**

```
10

9

9.1
```

### modulo

Divides a number by another number and returns the remainder.

**Code**

```
{{ 12 | modulo: 5 }}
```

**Output**

```
2
```

### plus

Adds a number to another number.

**Code**

```
<!-- entityview.page = 11 -->

{{ entityview.page | plus: 1 }}

{{ 10 | plus: 1.1 }}

{{ 10.1 | plus: 1 }}
```

**Output**

```
12

11

11.1
```

### round

Rounds a value to the nearest integer or specified number of decimals.

**Code**

```
{{ 4.6 | round }}

{{ 4.3 | round }}

{{ 4.5612 | round: 2 }}
```

**Output**

```
5

4

4.56
```

### times

Multiplies a number by another number.

**Code**

```
{{ 10 | times: 2 }}

{{ 10 | times: 2.2 }}

{{ 10.1 | times: 2 }}
```

**Output**

```
20

20

20.2
```


## String filters

String filters manipulate [strings](liquid-types.md#string).  

### append

Appends a string to the end of another string.

**Code**

```
{{ 'filename' | append: '.js' }}
```

**Output**

```
filename.js
```

### **capitalize**

capitalizes the first word in a string.

**Code**

```
{{ 'capitalize me' | capitalize }}
```

**Output**

```
Capitalize Me
```

### **downcase**

Converts a string into lowercase.

**Code**

```
{{ 'MIxed Case TExt' | downcase }}
```

**Output**

```
mixed case text
```

### **escape**

HTML-escapes a string.

**Code**

```
{{ '<p>test</p>' | escape }}
```

**Output**

```
&lt;p&gt;test&lt;/p&gt;
```

### **newline\_to\_br**

Inserts a &lt;br /&gt; line break HTML tag at each line break in a string.

**Code**

```
{% capture text %}

A

B

C

{% endcapture %}

{{ text | newline_to_br }}
```

**Output**

```
A<br />

B<br />

C<br />
```

### **prepend**

Prepends a string to the beginning of another string.

**Code**

```
{{ 'Jane Johnson' | prepend: 'Dr. ' }}
```

**Output**

```
Dr. Jane Johnson
```

### **remove**

Remove all occurrences of a substring from a string.

**Code**

```
{{ 'Hello, Dave. How are you, Dave?' | remove: 'Dave' }}
```

**Output**

```
Hello, . How are you, ?
```

### **remove\_first**

Removes the first occurrence of a substring from a string.

**Code**

```
{{ 'Hello, Dave. How are you, Dave?' | remove_first: 'Dave' }}
```

**Output**

```
Hello, . How are you, Dave?
```

### **replace**

Replaces all occurrences of a string with a substring.

**Code**

```
{{ 'Hello, Dave. How are you, Dave?' | replace: 'Dave', 'John' }}
```

**Output**

```
Hello, John. How are you, John?
```

### **replace\_first**

Replaces the first occurrence of a string with a substring.

**Code**

```
{{ 'Hello, Dave. How are you, Dave?' | replace_first: 'Dave', 'John' }}
```

**Output**

```
Hello, John. How are you, Dave?
```

### **split**

The split filter takes on a substring as a parameter. The substring is used as a delimiter to divide a string into an array.

**Code**

```
{% assign words = This is a demo of the split filter | split: ' ' %}

First word: {{ words.first }}

First word: {{ words[0] }}

Second word: {{ words[1] }}

Last word: {{ words.last }}

All words: {{ words | join: ', ' }}
```

**Output**

```
First word: This

First word: This

Second word: is

Last word: filter

All words: This, is, a, demo, of, the, split, filter
```

### **strip\_html**

Strips all HTML tags from a string.

**Code**

```
<p>Hello</p>
```

**Output**

```
Hello
```

### **strip\_newlines**

Strips any line breaks from a string.

**Code**

```
{% capture text %}

A

B

C

{% endcapture %}

{{ text | strip_newlines }}
```

**Output**

```
ABC
```

### **text\_to\_html**

Formats a plain text string as simple HTML. All text will be HTML encoded, blocks of text separated by a blank line will be wrapped in paragraph &lt;p&gt; tags, single line breaks will be replaced with &lt;br&gt;, and URLs will be converted to hyperlinks.

**Code**

```
{{ note.notetext | text_to_html }}
```

**Output**

```
<p>This is the first paragraph of notetext. It contains a URL: <a href="https://example.com/" rel="nofollow">https://example.com</a></p>

<p>This is a second paragraph.</p>
```

### **truncate**

Truncates a string down to a given number of characters. An ellipsis (...) is appended to the string and is included in the character count.

**Code**

```
{{ 'This is a long run of text.' | truncate: 10 }}
```

**Output**

```
This is...
```

### **truncate\_words**

Truncates a string down to a given number of words. An ellipsis (...) is appended to the truncated string.

**Code**

```
{{ 'This is a long run of text.' | truncate_words: 3 }}
```

**Output**

```
This is a...
```

### **upcase**

Converts a string into uppercase.

**Code**

```
{{ 'MIxed Case TExt' | upcase }}
```

**Output**

```
MIXED CASE TEXT
```

### **url\_escape**

URI-escape a string, for inclusion in a URL.

**Code**

```
{{ 'This & that//' | url_escape }}
```

**Output**

```
This+%26+that%2F%2F
```

### **xml\_escape**

XML-escape a string, for inclusion in XML output.

**Code**

```
{{ '<p>test</p>' | xml_escape }}
```

**Output**

```
&lt;p&gt;test&lt;/p&gt;
```


## Type filters

Type filters allow you to convert values of one type into other types.

### **boolean**

Attempts to convert a string value into a Boolean. If the value is already a Boolean, it will be returned unchanged. If the value cannot be converted into a Boolean, null will be returned.

This filter will also accept on, enabled, or yes as true, and off, disabled, and no as false.

**Code**

```
{{ true | boolean }}

{{ 'false' | boolean }}

{{ 'enabled' | boolean }}

{{ settings['something/enabled'] | boolean | default: false }}
```

**Output**

```
true

false

true

false
```

### **decimal**

Attempts to convert a string value into a decimal number. If the value is already a decimal number, it will be returned unchanged. If the value cannot be converted into a decimal number, null will be returned.

**Code**

```
{{ 10.1 | decimal }}

{{ '3.14' | decimal }}

{{ 'text' | decimal | default: 3.14 }}
```

**Output**

```
10.1

3.14

3.14
```

### **integer**

Attempts to convert a string value into an integer. If the value is already an integer, it will be returned unchanged. If the value cannot be converted into an integer, null will be returned.

**Code**

```
{{ 10 | integer }}

{{ '10' | integer }}

{{ '10.1' | integer }}

{{ 'text' | integer | default: 2 }}
```

**Output**

```
10

10


2
```

### **string**

Attempts to convert a value into its string representation. If the value is already a string, it will be returned unchanged. If the value is null, null will be returned.



## URL filters

URL filters allow you to build or extract parts of URLs.

### **add\_query**

Appends a query string parameter to a URL. If the parameter already exists in the URL, the parameter value will be updated.

If this filter is applied to a full absolute URL, an updated absolute URL will be the result. If it is applied to a path, an updated path will be the result.

**Code**

```
{{ 'https://example.com/path?page=1' | add_query: 'foo', 'bar' }}

{{ '/path?page=1' | add_query: 'page', 2 }}
```

**Output**

```
https://example.com/path?page=1&foo=bar

/path?page=2
```

### **base**

Gets the base URL of a given URL.

**Code**

```
{{ 'https://example.com/path?foo=bar&page=2' | base }}
```

**Output**

```
https://example.com
```

### **host**

Gets the host part of a URL.

**Code**

```
{{ 'https://example.com/path?foo=bar&page=2' | host }}
```

**Output**

```
example.com
```

### **path**

Gets the path part of a URL.

**Code**

```
{{ 'https://example.com/path?foo=bar&page=2' | path }}

{{ '/path?foo=bar&page=2' | path }}
```

**Output**

```
/path

/path
```

### **path\_and\_query**

Gets the path and query part of a URL.

**Code**

```
{{ 'https://example.com/path?foo=bar&page=2' | path_and_query }}

{{ '/path?foo=bar&page=2' | path_and_query }}
```

**Output**

```
/path?foo=bar&page=2

/path?foo=bar&page=2
```

### **port**

Gets the port number of a URL.

**Code**

```
{{ 'https://example.com/path?foo=bar&page=2' | port }}

{{ 'https://example.com/path?foo=bar&page=2' | port }}

{{ 'https://example.com:9000/path?foo=bar&page=2' | port }}
```

**Output**

```
80

443

9000
```

### **remove\_query**

Removes a query string parameter from a URL. If the parameter does not exists in the URL, the URL will be returned unchanged.

If this filter is applied to a full absolute URL, an updated absolute URL will be the result. If it is applied to a path, an updated path will be the result.

**Code**

```
{{ 'https://example.com/path?page=1' | remove_query: 'page' }}

{{ '/path?page=1' | remove_query: 'page' }}
```

**Output**

```
https://example.com/path

/path
```

### **scheme**

Gets the scheme part of a URL.

**Code**

```
{{ 'https://example.com/path?foo=bar&page=2' | scheme }}

{{ 'https://example.com/path?foo=bar&page=2' | scheme }}
```

**Output**

```
http

https
```


## Additional filters

These filters provide useful general functionality.

### **default**

Returns a default value for any variable with no assigned value (i.e. null).

**Code**

```
{{ snippets[Header] | default: 'My Website' }}
```

**Output**

```
<!-- If a snippet with the name Header returns null -->

My Website
```

### **file\_size**

Applied to a number value representing a number of bytes, returns a formatted file size with a unit of appropriate scale.

Optionally, a precision parameter can be passed, to control the number of decimal places in the result. The default precision is 1.

**Code**

```
{{ 10000000 | file_size }}

{{ 2050 | file_size: 0 }}

{{ entity.notes.first.filesize | file_size: 2 }}
```

**Output**

```
9.5 MB

2 KB

207.14 KB
```

### **has\_role**

Applied to a [user](liquid-objects.md#user), returns true if the user belongs to the given role. Returns false if not.  

**Code**

```
{% assign is_admin = user | has_role: 'Administrators' %}

{% if is_admin %}

User is an administrator.

{% endif %}
```

### **liquid**

Renders a string as Liquid code. This code will have access to the current Liquid execution context (variables, etc.).

> [!Note] 
> This filter should be used with caution and should generally only be applied to values that are under the exclusive control of portal content authors, or other users that can be trusted to write Liquid code.

**Code**

```
{{ page.adx_copy | liquid }}
```

### See also

[Store source content by using web templates](store-content-web-templates.md)  
[Understand Liquid operators](liquid-operators.md) 
[Liquid types](liquid-types.md)  
[Liquid Objects](liquid-objects.md)  
[Liquid Tags](liquid-tags.md)  
[Liquid Filters](liquid-filters.md)  


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]