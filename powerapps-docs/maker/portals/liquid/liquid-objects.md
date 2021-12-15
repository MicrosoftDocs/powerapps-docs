---
title: Available Liquid objects
description: Learn about the available liquid objects in a portal.
author: gitanjalisingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/27/2021
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - GitanjaliSingh33msft
---

# Available Liquid objects

Liquid objects contain attributes to output dynamic content to the page. For example, the page object has an attribute called title that can be used to output the title of the current page.

To access an object attribute by name, use a period (.). To render an object's attribute in a template, wrap it in {{ and }}.

> [!IMPORTANT]
> To avoid potential cross-site scripting (XSS) issues, always use [escape filter](liquid-filters.md#escape) to HTML encode data whenever using Liquid objects to read untrusted data provided by the user.

```
{{ page.title }}
```
Attributes of an object can also be accessed by using a string name and \[\]. This format is useful in cases where the required attribute is determined dynamically, or the attribute name contains characters, spaces, special characters, and so on, that would be invalid when using a period (.) inside the syntax.

```
{{ page[title] }}

{% assign attribute_name = Name with spaces %}

{{ object[attribute_name] }}
```

The following objects can be used and accessed anywhere, in any template.


|   Object    |                                                                                                                                                                                          Description                                                                                                                                                                                           |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  entities   |                                                                                                 Allows you to load any Power Apps table by ID. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [entities](#entities)                                                                                                 |
|     now     |                                          A date/time object that refers to the current UTC time at the time the template is rendered.<br>**Note**: This value is cached by the portal web app and isn't refreshed every time. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [Date filters](liquid-filters.md#date-filters)                                          |
|    page     | Refers to the current portal request page. The page object provides access to things like the breadcrumbs for the current page, the title or URL of the current page, and any other attributes or related entities of the underlying Power Apps record. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [page](#page) |
|   params    |                                                                                                                             A convenient shortcut for request.params. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [request](#request)                                                                                                                              |
|   request   |                                                                                                                        Contains information about the current HTTP request. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [request](#request)                                                                                                                        |
|  settings   |                                                                                                            Allows you to load any [Site Setting](../configure/configure-site-settings.md) by name. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [settings](#settings)                                                                                                            |
|   sitemap   |                                                                                                                               Allows access to the portal site map. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [sitemap](#sitemap)                                                                                                                                |
| sitemarkers |                                                                                                                        Allows you to load any Site Markers by name. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [sitemarkers](#sitemarkers)                                                                                                                        |
|  snippets   |                                                                                                         Allows you to load any [Content Snippet](../configure/customize-content-snippets.md) by name. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [snippets](#snippets)                                                                                                         |
|    user     |                             Refers to the current portal user, allowing access to all attributes of the underlying Power Apps contact record. If no user is signed in, this variable will be [null](liquid-types.md#null). [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [user](#user)                              |
|  weblinks   |                                                                                                                        Allows you to load any Web Link Set by name or ID. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [weblinks](#weblinks)                                                                                                                        |
|   website   |                                                      Refers to the portal Website record, allowing access to all attributes of the Power Apps Website (adx\_website) record for the portal. [!INCLUDE[proc-more-information](../../../includes/proc-more-information.md)] [website](#website)                                                       |

## ads


Provides the ability to access and render an ad.

The ads object allows you to select a specific ad or ad placement:

```
<div>

{% assign ad = ads[Ad Name] %}

<h4>{{ ad.title }}</h4>

<a href={{ ad.redirect_url }}>

<img src={{ ad.image.url }} alt={{ ad.image.alternate_text }} />

</a>

</div>
```

### Ads attributes

|Attribute   |Description   |
|---|---|
| placements        | Returns the adplacements object.    |
| \[ad name or id\] | You can access any ad by its Name or Id properties. <br> `{% assign ad = ads[Ad Name] %}`<br>`{% assign ad = ads["da8b8a92-2ee6-476f-8a21-782b047ff460"] %}`  |


### Ad Placements attributes

|Attribute   |Description   |
|---|---|
| \[ad placement name or id\] | You can access any adplacement by its Name or Id properties.<br>`{% assign placement = ads.placements[Placement Name or Id] %}`<br>`{% assign placement = ads.placements[2423d713-abb3-44c3-8a7d-c445e16fccad] %}`  |

### Ad Placement attributes

An ad placement is a table object with the same general attributes, and the attributes listed below.

|Attribute   |Description   |
|---|---|
| Ads            | Returns the collection of ad objects associated with the placement.  [Iteration tags](iteration-tags.md) and [Array filters](liquid-filters.md#array-filters) may be used with this collection.  |  
| Name           | Returns the Name field for the ad placement.                                                                |
| placement\_url | The URL that can be used to retrieve the ad placement fully rendered by a template.                         |
| random\_url    | The URL that can be used to retrieve a random ad from the placement fully rendered by a template.           |

### Ad attributes

> [!Note]
> An ad is a table object, with all of the same attributes in addition to those listed below.

|Attribute   |Description   |
|---|---|
| ad\_url |  The URL that can be used to retrieve the ad fully rendered by a template.   |
| Copy| Returns the Copy field for the ad.|
| image| Returns the image object (if any) for the ad.|
| Name| Returns the Name field for the ad.|
| open\_in\_new\_window | Returns true if the URL specified by redirect\_url should open in a new window. |
| redirect\_url| The URL that the user will be directed to by selecting the ad.|

### Ad Image attributes

|Attribute   |Description   |
|---|---|
| alternate\_text | Return the text that is intended to appear in the tag's alt attribute. |
| height          | Returns the height in pixels for the image                             |
| url             | Returns the URL source for the image.                                  |
| width           | Returns the width in pixels for the image                              |


## blogs

Provides the ability to access and render Blogs and Blog Posts.

The blogs object allows you to select a specific blog or blog posts.

```
{% assign posts = blogs.posts | paginate: 0,4 %}

<div class=content-panel panel panel-default>

<div class=panel-heading>

{% assign sitemarker = sitemarkers["Blog Home"] %}

{% assign snippet = snippets[Home Blog Activity Heading] %}

<a class=pull-right href={{sitemarker.url}}> All Blogs </a>

<h4>

<a class=feed-icon fa fa-rss-square href={{ blogs.feedpath }} />

{{ snippet.adx_value }}

</h4>

</div>

<ul class=list-group>

{% for post in posts.all %}

<li class=list-group-item >

<a class=user-avatar href={{ post.author_url }}>

<img src={{ post.user_image_url }} />

</a>

<h4 class=list-group-item-heading>

<a href={{ post.app_relative_path }}>{{ post.title }}</a>

</h4>

<div class=content-metadata>

<abbr class=timeago>{{ post.publish_date }}</abbr>

&ndash;

<a href={{ post.author_url }}> {{ post.author_name }} </a>

&ndash;

<a href={{ post.application_path }}#comments>

<span class=fa fa-comment aria-hidden=true></span> {{ post.comment_count }}

</a>

</div>

</li>

{% endfor %}

</ul>

</div>
```

### blogs Object

The blogs object allows you to access any specific blog in the portal, or to access all blog posts in the portal.

The following table explains the attributes associated with the blogs object.

|Attribute   |Description   |
|---|---|
| posts               | Returns a blogposts object containing all blog posts in the portal.     |
| \[blog name or id\] | You can access any blog by its Name or Id properties.                   

```
{% assign blog = blogs[Blog Name] %}                             

{% assign blog = blogs[da8b8a92-2ee6-476f-8a21-782b047ff460] %}  |
```

### blog Object

The blog object allows you to work with a single blog, allowing you to access the posts for that blog.

The following table explains various attributes associated with blog Object.

|Attribute   |Description   |
|---|---|
| posts | Returns a blogposts object containing all blog posts for the blog. |
| Name  | The name of the blog.                                              |
| title | The title of the blog.                                             |
| url   | The URL of the blog.                                               |

### blogposts Object

The blogposts object allows you to access a collection of blog post objects. You can order the blog posts and achieve pagination in addition to using liquid filters:

```
{% assign blogposts = blogs.posts | order\_by “adx\_name”, “desc” | paginate: 0,4 | all %}
```

Other possible options:

- `blogs.posts.all` (to get all blog posts)
- `blogs.posts | from\_index: 0 | take: 2`

The following table explains various attributes associated with blogposts Object.

|Attribute   |Description   |
|---|---|
| All | Returns all blogpost objects in the collection |

### blogpost Object

Refers to a single blog post.

The following table explains various attributes associated with blogpost Object.

|Attribute   |Description   |
|---|---|
| url            | The URL of the post.                                                                |
| content        | Returns the Content field for the post.                                             |
| author         | Returns the authors for the post (which is simply a contact table object.          |
| title          | The Title of the post.                                                              |
| comment\_count | Returns the integer value of the count of how many comments there for a given post. |
| publish\_date  | The date at which the post was published.                                           |

## entities

> [!CAUTION]
> To avoid potential cross-site scripting (XSS) issues, always use [escape filter](liquid-filters.md#escape) to HTML encode data whenever using **entities** Liquid object to read data provided by the user that can't be trusted.

Allows you to load any Power Apps table by ID. If the table exists, a table object will be returned. If a table with the given ID isn't found, [null](liquid-types.md#null) will be returned.  

```
{% assign account = entities.account['936DA01F-9ABD-4d9d-80C7-02AF85C822A8'] | escape %}

{% if account %}

{{ account.name }} ({{ account.statecode.label }})

{% endif %}

{% assign entity_logical_name = 'contact' %}

{% assign contact = entities[entity_logical_name][request.params.contactid] | escape %}

{% if contact %}

{{ contact.fullname }} ({{ contact.parentcustomerid.name }})

{% endif %}
```

### Entity

A entity object provides access to the attributes of a Power Apps table record.


|             Attribute              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 Id                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    The GUID ID of the table, as a string. For example, 936DA01F-9ABD-4d9d-80C7-02AF85C822A8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|           logical\_name            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   The Power Apps logical name of the table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|               Notes                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Loads any notes (annotation) associated with the table, ordered from oldest to newest (createdon). Notes are returned as note objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|            permissions             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Loads Table Permission assertion results for the table. Results are returned as a permissions object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                url                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    Returns the Power Apps portals content management system URL path for the table. If the table has no valid URL in the current website, returns null. Generally, this will only return a value for certain table types that have been integrated into the portal CMS, unless you've customized the URL Provider in your application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| \[attribute or relationship name\] | You can access any attribute of the Power Apps table by logical name. `{{ entity.createdon }}{% assign attribute_name = 'name' %}{{ entity[attribute_name] }}` <br>The values of most table attributes map directly to [Liquid types](liquid-types.md): Two Option fields map to Booleans, text fields to strings, numeric/currency fields to numbers, date/time fields to date objects. But some attribute types are returned as objects:<ul><li>Lookup (Associated Table Reference) fields are returned as associated table reference objects.</li><li>Option Set/Picklist fields are returned as option set value objects.</li><li>You can also load any related entities by relationship schema name.</li>`{{ page.adx_webpage_entitylist.adx_name }}`In the case that a relationship is reflexive (that is, self-referential), a reflexive relationship object will be returned. (Otherwise, the result would be ambiguous.)`{{ page.adx_webpage_webpage.referencing.adx_name }}` <br>**Note**: Loading large numbers of related entities, or accessing large numbers of relationships in a single template, can have a negative impact on template rendering performance. Avoid loading related entities for each item in an array, within a loop. Where possible, use [Dataverse table tags](portals-entity-tags.md) to load collections of entities. |

### Associated Table Reference

Lookup attribute values are returned as associated table reference objects, with the following attributes.


|   Attribute   |                                                Description                                                |
|---------------|-----------------------------------------------------------------------------------------------------------|
|      Id       | The GUID ID of the referenced table, as a string. <br> For example, 936DA01F-9ABD-4d9d-80C7-02AF85C822A8 |
| logical\_name |  The Power Apps logical name of the referenced table.   |
|     Name      |                           The primary name attribute of the referenced table.                            |

### Note

A note is a table object that provides access to the attributes and relationships of an annotation record. In addition to all the attributes of a table object, a note has the following additional attributes.


|  Attribute   |                                                                                                                                                                                                                                  Description                                                                                                                                                                                                                                  |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| documentbody | Loads the documentbody attribute of the note annotation record, as a Base64-encoded string. Because the content of this attribute may be large, it isn't loaded with the rest of the note attributes, it is only loaded on demand. <br> **Note**: Use of the documentbody attribute could have a negative impact on template rendering performance, and should be done with caution.<br>Use the url attribute to provide a link to the note attachment instead, if possible. |
|     url      |                                                                                                                                   Returns the URL path for the built-in portal annotation attachment handler. If the user has permission, and the note has an attached file, a request to this URL will download the note file attachment.                                                                                                                                    |

>[!Note]
> [Additional filters](liquid-filters.md#additional-filters)                     

### Option Set Value

Option Set/Picklist attribute values are returned as associated table reference objects, with the following attributes.

| Attribute | Description                                                     |
|-----------|-----------------------------------------------------------------|
| Label     | The localized label of the option set/picklist attribute value. For example, Active|
| Value     | The integer value of the option set/picklist attribute value. For example, 0                                                           |

### Table Permissions

The Table Permissions object provides access to aggregated permission assertion results for a table.

| Attribute       | Description                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| can\_append     | Returns true if the current user has permission to append records to relationships of this record. Returns false otherwise.                                                                                              |
| can\_append\_to | Returns true if the current user has permission to append this record to a relationship of another table. Returns false otherwise.                                                                                      |
| can\_create     | Returns true if the current user has permission to create new records of this table type. Returns false otherwise.                                                                                                      |
| can\_delete     | Returns true if the current user has permission to delete this record. Returns false otherwise.                                                                                                                          |
| can\_read       | Returns true if the current user has permission to read this record. Returns false otherwise.                                                                                                                            |
| can\_write      | Returns true if the current user has permission to update this record. Returns false otherwise.                                                                                                                          |
| rules\_exist    | Returns true if the permission results represented by this object are the result of explicitly defined permission rules. Returns false if they are the default results in the absence of explicitly defined permissions. |

### Reflexive Relationship

Attempts to load reflexive (that is, self-referential) relationships on entities are returned as objects with the following attributes.

| Attribute     | Description                                                                                                   |
|---------------|---------------------------------------------------------------------------------------------------------------|
| is\_reflexive | Returns true. Can be used to test whether an object returned by a relationship is a reflexive relationship object. |
| referenced    | Returns an array of referenced entities for the given relationship.                                           |
| referencing   | Returns a referencing table for the given relationship. Returns null if no referencing table exists. If the relationship is many-to-many (N:N), returns an array of referencing entities.                          

## entitylist

The entitylist object is used within the [Power Apps Dataverse table tags](portals-entity-tags.md). It provides access to all the attributes of a given list.  

> [!Note]                                                       
> [Render the list associated with the current page](render-entity-list-current-page.md)

### Attributes

> [!Note]
> [entities](#entities)

|               Attribute               |                                                                                                                            Description                                                                                                                            |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            create\_enabled            |                                                                                Returns true if creation of new records is configured for the list. Returns false otherwise.                                                                                |
|              create\_url              |                                                                                          Returns the configured URL path for a creation link/button for the list.                                                                                          |
|            detail\_enabled            |                                                                         Returns true if a detail view for individual records is configured for the list. Returns false otherwise.                                                                          |
|         detail\_id\_parameter         |               Returns the query string parameter name to use for the record ID when constructing a record detail view URL. See [URL filters](liquid-filters.md#url-filters) for details on using Liquid filters to construct URLs. For example, id                |
|             detail\_label             |                                                                                     Returns the configured localized label for detail view links/buttons for the list.                                                                                     |
|              detail\_url              |                                                                                       Returns the configured URL path for a detail view links/buttons for the list.                                                                                        |
|           empty\_list\_text           |                                                                                Returns the configured localized text to be displayed when the list view returns no results.                                                                                |
|      enable\_entity\_permissions      |                                                                               Returns true if Table Permission filtering is enabled for this list. Returns false otherwise.                                                                               |
|         entity\_logical\_name         |                                                 Returns the Power Apps table logical name for records to be displayed by this list. For example, contact                                                 |
|   filter\_account\_attribute\_name    |                                            Returns the attribute logical name for the lookup to account that will be used to filter result records by the current portal user's parent account. For example, accountid                                            |
|         filter\_apply\_label          |                                                            Returns the configured localized label to be used for the link/button that applies an advanced attribute filter to the list results.                                                            |
|          filter\_definition           |                      Returns the JSON attribute filter definition for the list. See [List filters](liquid-filters.md#list-filters) for details on how to use the metafilters Liquid filter to process this definition.                       |
|            filter\_enabled            |                                                                               Returns true if advanced attribute filtering is enabled for the list. Returns false otherwise.                                                                               |
| filter\_portal\_user\_attribute\_name |                                                 Returns the attribute logical name for the lookup to contact that will be used to filter result records by current portal user's contact. For example, contactid                                                  |
|   filter\_website\_attribute\_name    |                                              Returns the attribute logical name for the lookup to adx\_website that will be used to filter result records by the current portal website. For example, adx\_websiteid                                              |
|            language\_code             |                                               Returns the Power Apps integer language code that will be used to select all localized labels for this list.                                                |
|              page\_size               |                                                                                                   Returns the configured result page size for the list.                                                                                                    |
|          primary\_key\_name           |                                                                                  Returns the primary key attribute logical name for records to be displayed by this list.                                                                                  |
|            search\_enabled            |                                                                                         Returns true if search is enabled for this list. Returns false otherwise.                                                                                          |
|          search\_placeholder          |                                                                                        Returns the configured localized text for the list search field placeholder.                                                                                        |
|            search\_tooltip            |                                                                                             Returns the configured localized text for the list search tooltip.                                                                                             |
|                 views                 |                                                                                           Returns the available views for the list, as list view objects.                                                                                           |
|      \[attribute logical name\]       | You can access any attribute of the list (adx\_entitylist) Power Apps record by logical name, in the same manner as a [table](liquid-objects.md#entity) object. For example, {{ entitylist.adx\_name }} |

### List View Attributes

|          Attribute          |                                                                                     Description                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           columns           |                                                         Returns the columns of the view as list view column objects.                                                         |
|    entity\_logical\_name    |               Returns the Power Apps table logical name for the records included in the view. For example, contact                |
|             Id              |                                                                          Returns the GUID ID of the view.                                                                           |
|       language\_code        | Returns the Power Apps integer language code that will be used to select all localized labels (column headers, etc.) for the view. |
|            Name             |                                          Returns the Power Apps display name of the view.                                          |
| primary\_key\_logical\_name |        Returns the Power Apps table primary key logical name for the records included in the view. For example, contactid         |
|      sort\_expression       |                                               Returns the default sort expression for the view. For example, name ASC, createdon DESC                                               |

### List View Column Attributes

|    Attribute     |                                                                                    Description                                                                                    |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attribute\_type  | Returns the Power Apps attribute type name for the column, as a string. For example, Lookup, Picklist, String, Boolean, DateTime |
|  logical\_name   |                       Returns the Power Apps attribute logical name for the column. For example, createdon                       |
|       Name       |                      Returns the localized Power Apps display name for the column. For example, Created On                       |
| sort\_ascending  |                                      Returns a sort expression string for sorting the column in ascending order. For example, createdon ASC                                       |
| sort\_descending |                                     Returns a sort expression string for sorting the column in descending order. For example, createdon DESC                                      |
|  sort\_disabled  |                                                   Returns true if sorting is disabled for the column. Returns false otherwise.                                                    |
|  sort\_enabled   |                                                    Returns true if sorting is enabled for the column. Returns false otherwise.                                                    |
|      width       |                                                              Returns the configured width for the column, in pixels.                                                              |

## entityview

The entityview object is used within the entityview tag, and provides access to the metadata for the view, in addition to view result records.

### Attributes

|          Attribute          |                                                                               Description                                                                                |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           columns           |                         Returns the columns in the view, as [table view column objects](liquid-objects.md#list-view-column-attributes).                          |
| entity\_permission\_denied  | Returns true if access to view results was denied due to insufficient Table Permissions for the current user. Returns false if read access to view results was granted. |
|    entity\_logical\_name    |                   The Power Apps table logical name of the view result records. For example, contact                   |
|         first\_page         |                 The page number of the first page of view results. This will be 1 unless there were no results returned, in which case it will be null.                  |
|             Id              |                            The GUID ID of the Power Apps view that defines this entityview.                             |
|       language\_code        |             The Power Apps integer language code being used to load localized labels for the current view.              |
|         last\_page          |                                 The page number of the last page of view results. If there were no results returned, this will be null.                                  |
|            name             |              The name of the Power Apps view that defines this entityview., for example, Active Contacts.               |
|         next\_page          |                                The page number of the next page of view results. If there is no next page of results, this will be null.                                 |
|            Page             |                                                           The page number of the current page of view results.                                                           |
|            pages            |                                          Returns an array of page numbers containing all pages of results for the current view.                                          |
|         page\_size          |                                                      The number of results returned per page for the current view.                                                       |
|       previous\_page        |                              The page number of the next page of view results. If there is no previous page of results, this will be null.                               |
| primary\_key\_logical\_name |  The Power Apps logical name of the primary key attribute of the result table for this view. For example, contactid.   |
|           records           |                                                   The current page of result records for the view, as table objects.                                                    |
|      sort\_expression       |                                             The default sort expression for the view. For example, nameASC, createdon DESC.                                              |
|        total\_pages         |                                                              The total number of result pages for the view.                                                              |
|       total\_records        |                                                       The total number of results for the view (across all pages).                                                       |

## events

Provides the ability to access and render Events. The events object allows you to select a specific event or all events.

### events Object

The events object allows you to access any specific event in the portal, or to access all events in the portal (regardless of the event).

The events object has following attributes:

|Attribute   |Description   |
|---|---|
|occurences |Returns an eventoccurancessobject containing all event occurrences in the portal |
|[event name or id] |You can access any event by its Name or Id properties.<br>{% assign event = events[&quot;Event Name&quot;] %}<br>{% assign event = events[&quot;da8b8a92-2ee6-476f-8a21-782b047ff460&quot;] %} |

### event Object

The event object allows you to work with a single event, allowing you to access the schedules and occurrences for that event.

The event object has following attributes:

|Attribute   |Description   |
|---|---|
| occurrences | Returns an eventoccurrencesobject containing all occurrences for the event. |
| name       | The name of the event.                                                     |
| url        | The URL of the event.                                                      |

### eventoccurences Object

The eventoccurrences object allows you to access a collection of event occurrences objects. You can order the event occurrences and specify a date range for the occurrences to retrieve, and achieve pagination as well by using liquid filters

```
{% assign occurances = event.occurrences.from[today].to[advance_date] %}
```

note that

```
{% assign occurances = event.occurrences.min[today].max[advance_date] %}
```

is also possible.

Following attributes are associated with eventoccurrences object

|Attribute   |Description   |
|---|---|
| All | Returns all eventoccurance objects in the collection. |

### eventoccurence Object

Represents a single event occurrence. The associated attributes are given below:

|Attribute   |Description   |
|---|---|
| url                 | The URL of the occurrence.    |
| is\_all\_day\_event | Is this an all-day event?     |
| start\_time         | The start time for the event. |
| end\_time           | The end time for the event.   |


## forloop

Contains properties useful within a [for](iteration-tags.md#for) loop block.  

> [!Note]
> forloop can only be used within a [for](iteration-tags.md#for) tag.

**Code**

```
{% for child in page.children %}

{% if forloop.first %}

This is the first child page!

{% else %}

This is child page number {{ forloop.index }}.

{% endif %}

{% endfor %}
```

**Output**

```
This is the first child page!

This is child page number 2.

This is child page number 3.
```

### Attributes

|Attribute   |Description   |
|---|---|
| first   | Returns true if it's the first iteration of the loop. Returns false if it's not the first iteration.       |
| index   | The current item's position in the collection, where the first item has a position of 1.                   |
| index0  | The current item's position in the collection, where the first item has a position of 0.                   |
| Last    | Returns true if it's the last iteration of the loop. Returns false if it's not the last iteration.         |
| length  | Returns the number of iterations for the loop ߝ the number of items in the collection being iterated over. |
| rindex  | Number of items remaining in the loop (length - index) where 1 is the index of the last item.              |
| rindex0 | Number of items remaining in the loop (length - index) where 0 is the index of the last item.              |


## forums

Provides the ability to access and render Forums and Forum Threads. The ability to use liquid to render forum data extends to posts, but to create a new post or thread, you must use an ASP.NET advanced forms Page Template with said functionality built in (such as the default Forum Thread and Forum Post Page Templates).

The forums object allows you to select a Forum or Forum Threads:

```
<div class=content-panel panel panel-default>

<div class=panel-heading>

<h4>

<span class=fa fa-comments aria-hidden=true></span>

{{ snippets[Home Forum Activity Heading] | default: Forum Activity | h }}

</h4>

</div>

{% for forum in website.forums %}

<ul class=list-group>

<li class=list-group-item>

<div class=row>

<div class=col-sm-6>

<h4 class=list-group-item-heading><a href="{{ forum.url | h }}"> {{ forum.name | h }}</a></h4>

<div class=list-group-item-text content-metadata>{{ forum.adx_description | h }}</div>

</div>

<div class=col-sm-3 content-metadata>{{ forum.thread_count }} threads</div>

<div class=col-sm-3 content-metadata>{{ forum.post_count }} posts</div>

</div>

</li>

</ul>

{% endfor %}

</div>
```

### forums Object

The forums object allows you to access any specific forum in the portal, or to access all forum threads in the portal (regardless of the forum).

The forum object allows you to work with a single forum, allowing you to access the threads for that forum.

The forumthreads object allows you to access a collection of forumthread objects. You can order the forum threads and achieve pagination as well by using liquid filters.

```
{% assign threads = forum.threads | order_by adx_name, desc | paginate: 0,4 | all %}
```

A Single Forum Thread

The forumposts object allows you to access a collection of forumpost objects.

### Attributes

|Attribute   |Description   |
|---|---|
| threads              | Returns a forumthreads object containing all forumthread objects in the portal.             |
| All                  | Returns all forum objects in the portal. Note that website.forums Is also an equivalent.    |
| thread\_count        | Returns the integer value of the count of how many threads there are in the entire website. |
| post\_count          | Returns the integer value of the total number of posts in the portal.                       |
| \[forum name or id\] | You can access any forum by its Name or Id properties. <br>`{% assign forum = forums[Forum Name] %}<br>{% assign forum = forums[da8b8a92-2ee6-476f-8a21-782b047ff460] %} 

### forum Object

### Attributes

> [!Note]
> [entities](#entities)

|Attribute   |Description   |
|---|---|
| threads       | Returns a forumthreads object containing all forum threads for the forum.               |
| Name          | The Name of the Forum.                                                                  |
| thread\_count | Returns the integer value of the count of how many threads there are in the forum.      |
| post\_count   | Returns the integer value of the count of how many posts there are in the entire forum. |

### forumthreads Object

### Attributes

|Attribute   |Description   |
|---|---|
| All | Returns all forumthread objects in the collection. |

### forumthread Object

### Attributes

> [!Note]
> [entities](#entities)

|Attribute   |Description   |
|---|---|
| posts        | Returns a forumposts object containing all forum posts for the thread.            |
| author       | Returns the author for the thread (which is simply a contact table object).      |
| latest\_post | Returns the latest post in the thread.                                            |
| first\_post  | Returns the first post in the thread.                                             |
| post\_count  | Returns the integer value of the count of how many posts there are in the thread. |
| is\_answered | Is the thread answered or not?                                                    |
| is\_sticky   | Is the thread a sticky thread?                                                    |

### forumposts Object

### Attributes

|Attribute   |Description   |
|---|---|
| All | Returns all forumthread objects in the collection. |

A Single Forum Post

### Attributes

> [!Note] 
> [entities](#entities)

|Attribute   |Description   |
|---|---|
| author     | Returns the author for the post (which is simply a contact table object). |
| content    | The content of the post.                                                   |
| is\_answer | Is this post an answer to the thread?                                      |


## knowledge

Provides access to Power Apps knowledgearticle and category table records to render articles and categories in a portal.

### Attributes

|Attribute|Description|
|---|---|
|articles|Returns an articles object containing article objects for the knowledgearticle table records available in the portal.|
|categories|Returns a categories object containing category objects for the category table records available in the portal.|
|||

### articles object

The articles object allows you to access a collection of article objects. You can order the articles and achieve pagination as well by using liquid filters.

```
{% assign count = count | default: 3 %}
{% assign languagecode = website.selected_language.code %}
{% assign popular_articles = knowledge.articles | popular: count,languagecode  %}
{% if popular_articles %}
    <div class=list-group>
    {% for article in popular_articles %}
      <div class=list-group-item clearfix>
        <a class=title href={{ article.url | escape }}>{{ article.title | escape }}</a>
        <p class=description>{{ article.description | escape }}</p>
      </div>
    {% endfor %}
    </div>
{% endif %}
```

### Attributes

|Attribute|Description|
|---|---|
|popular |Returns a collection of article objects containing the most views. `{% assign popular_articles = knowledge.articles.popular %}` |
|recent |Returns a collection of article objects containing the latest modified date. `{% assign recent_articles = knowledge.articles.recent %}` |
|top |Returns a collection of article objects containing the highest rating. `{% assign top_articles = knowledge.articles.top  %}` |
| | |

### Filters

The following filters can accept optional parameters for page size and language. First parameter is the number or records to retrieve. The default page size is 5. The second parameter is the code of a language to retrieve articles for a given language. Filters may be combined with other [Liquid filters](liquid-filters.md).

```
{% assign page_size = 5 %}
{% assign language_code = website.selected_language.code %}
{% assign recent_articles = knowledge.articles | recent: page_size, language_code %}
```

|Attribute|Description|
|---|---|
|popular |Returns a collection of article objects containing the most views. `{% assign popular_articles = knowledge.articles \| popular: 10, en-US %}` |
|recent |Returns a collection of article objects containing the latest modified date. `{% assign recent_articles = knowledge.articles \| recent: 5 %}` |
|top |Returns a collection of article objects containing the highest rating. `{% assign top_articles = knowledge.articles \| top: 3, en-US %}` |
| | |

### categories object

The categories object allows you to access a collection of category objects. You can order the categories and achieve pagination as well by using liquid filters.

```
{% assign category_url = sitemarkers['Category'].url %}
  {% assign count = count | default: 0 %}  
  {% assign categories = knowledge.categories | top_level: count %}
  {% if categories %}
    <div class=list-group unstyled>
    {% for category in categories %}
      <a href={{ category_url | add_query: 'id', category.categorynumber }} class=list-group-item>
        {{ category.title }}
      </a>
    {% endfor %}
    </div>
  {% endif %}
```

### Attributes

|Attribute|Description|
|---|---|
|recent |Returns a collection of category objects containing the latest modified date. |
|top_level |Returns a collection of category objects that don't have a parent category. |
|||

### Filters

The following filters can accept an optional parameter indicating the page size. The default page size is 5. Filters may be combined with other [Liquid filters](liquid-filters.md).

```
{% assign page_size = 5 %}
{% assign recent_categories = knowledge.categories | recent: page_size %}
```

|Attribute|Description|
|---|---|
|recent |Returns a collection of category objects containing the latest modified date. You can provide parameters `{% assign recent_categories = knowledge.categories \| recent: 10 %}` |
|top_level |Returns a collection of category objects that don't have a parent category. `{% assign root_categories = knowledge.categories \| top_level %}` |
|||

### article Object

The article object allows you to work with a single knowledgearticle to display details of that article in the portal.

### Attributes

article is an [entity](#entity) object, with all of the same attributes, in addition to those listed below.

|Attribute|Description|
|---|---|
|article_public_number| The Article Public Number of the article.|
|comment_count| The integer value of the count of how many comments there are for a given article.|
|content|The content of the article.|
|current_user_can_comment|Returns a Boolean value indicating whether the current user can add comments on the article.|
|is_rating_enabled|Returns a boolean value indicating whether rating on an article is enabled.|
|keywords|The keywords on the article.|
|name|An alternate alias for the title of the article.|
|rating|The decimal rating value on the article.|
|title|The title of the article.|
|view_count|The integer value of the number of times the article has been viewed.|
|||

### category Object

The category object allows you to work with a single category to display its details in the portal.

### Attributes

category is an [entity](#entity) object, with all of the same attributes, in addition to those listed below.

|Attribute|Description|
|---|---|
|categorynumber|The Category Number of the category.|
|name|An alternate alias for the title of the category.|
|title|The title of the category.|
|||

## language

Provides the current language name, and language code if  [multiple-language support](../configure/enable-multiple-language-support.md) is enabled.

### Attributes

| Attribute | Description |
| - | - |
| url | The current request URL prefixed with the current language code. |
| url_substitution | The current request URL prefixed with the current language code bypassing the page output cache. |
| name | Title of the current language. |
| code | The language code of the language. |

For example, the **Languages Dropdown** web template by default uses this liquid object to list the available languages when multiple-languages are available.

## page

Refers to the current portal request page. This object combines the attributes of the [sitemap](#sitemap) and the current request [entities](#entities) (usually a webpage).  

The page object provides access to things like the breadcrumbs for the current page, the title or URL of the current page, and any other attributes or related entities of the underlying Power Apps record.

```
<ul class=breadcrumb>

{% for crumb in page.breadcrumbs %}

<li><a href={{ crumb.url | escape }}>{{ crumb.title | escape }}</a></li>

{% endfor %}

<li class=active>{{ page.title | escape }}</li>

</ul>

<div class=page-header>

<h1>{{ page.title | escape }}</h1>

</div>

<div class=page-copy>

{{ page.adx_copy }}

</div>

<div class=list-group>

{% for child in page.children %}

<a class=list-group-item href={{ child.url | escape }}>

{{ child.title | escape }}

</a>

{% endfor %}

</div>

<!-- Page {{ page.id }} was last modified on {{ page.modifiedon }}. -->
```

### Page attributes

> [!Note]  
> [entities](#entities)

|             Attribute              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            breadcrumbs             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Returns the breadcrumb site map node objects for the page, starting from the site map root node and ending at parent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|              children              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Returns the child site map node objects of the page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|               parent               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Returns the parent site map node of the page. If the page is the Home page, parent will be null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|               title                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                The title of the page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                url                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 The URL of the page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \[attribute or relationship name\] | You can access any attribute of the page's underlying Power Apps record by logical name.<br>`{{ page.createdon }}`<br>`{% assign attribute_name = 'name' %}`<br>`{{ page[attribute_name] }}`<br>The values of most table attributes map directly to [Liquid types](liquid-types.md): Two Option fields map to Booleans, text fields to strings, numeric/currency fields to numbers, date/time fields to date objects. But some attribute types are returned as objects:<ul><li>Lookup (Associated Table Reference) fields are returned as [associated table reference objects](#associated-table-reference).</li><li>Option Set/Picklist fields are returned as [option set value objects](#option-set-value).</li> You can also load any related entities by relationship schema name. <br> `{{ page.adx_webpage_entitylist.adx_name }}`<br>In the case that a relationship is reflexive (that is, self-referential), a [entities](#entities) object will be returned. (Otherwise, the result would be ambiguous.)`{{ page.adx_webpage_webpage.referencing.adx_name }}` <br>**Note**: Loading large numbers of related entities, or accessing large numbers of relationships in a single template, can have a negative impact on template rendering performance. Avoid loading related entities for each item in an array, within a loop. Where possible, prefer use of the [Power Apps Dataverse table tags](portals-entity-tags.md) to load collections of entities. |

## polls

Provides the ability to access and render a poll.

The polls object allows you to select a specific poll or poll placement:

```
<div>

{% assign poll = polls[Poll Name] %}

<h4>{{ poll.question }}</h4>

{% for option in poll.options %}

<div>

<input type=radio name={{ poll.name }} id={{ option.id }} />

<label for={{ option.id }}>{{ option.answer }}</label>

</div>

{% endfor %}

<button type=button>{{ poll.submit_button_label }}</button>

</div>
```

### Polls Attributes

|Attribute   |Description   |
|---|---|
| placements          | Returns the pollplacements object.                                      |
| \[poll name or id\] | You can access any poll by its Name or Id properties. `{% assign poll = polls[Poll Name] %}`<br>`{% assign poll = polls["41827a5c-33de-49b8-a0c7-439e6a02eb98"] %}`  |

### Poll Placements Attributes

|Attribute   |Description   |
|---|---|
| \[poll placement name or id\] | You can access any poll placement by its Name or Id properties.`{% assign placement = polls.placements[Placement Name or Id] %}`<br>`{% assign placement = polls.placements[7677c5d4-406e-4b6c-907c-916ac17dba0f] %} `|

### Poll Placement Attributes

> [!Note] 
> [entities](#entities)                                       

|Attribute   |Description   |
|---|---|
| Name           | Returns the Name field for the poll placement.                            
| placement\_url | The URL that can be used to retrieve the poll placement fully rendered by a template.                       |
| polls          | Returns the collection of poll objects associated with the placement. [Iteration tags](iteration-tags.md) and [Array filters](liquid-filters.md#array-filters) may be used with this collection.  |  
| random\_url    | The URL that can be used to retrieve a random poll from the placement fully rendered by a template.         |
| submit\_url    | The URL to which a completed poll is submitted.                                                             |

### Poll Attributes

> [!Note] 
> [entities](#entities)                                          

|Attribute   |Description   |
|---|---|
| has\_user\_voted       | Returns true if the current user (signed in or anonymous) has already voted in this poll.         |
| Name                   | Returns the Name field for the poll.                                                              |
| options                | Returns the collection of poll option objects associated with the poll. [Iteration tags](iteration-tags.md) and [entities](#entities) may be used with this collection.  |  
| poll\_url              | The URL that can be used to retrieve the poll fully rendered by a template.                       |
| question               | Returns the Question field for the poll.                                                          |
| submit\_button\_label  | Returns a string that can be used to override the submit button label for the poll.               |
| submit\_url            | The URL to which a completed poll is submitted.                                                   |
| user\_selected\_option | Returns the polloption object selected by the user (if they have already voted).                  |
| votes                  | Returns the number of votes that have been tabulated for the poll.                                |

### Poll Option Attributes

>[!Note]
> [entities](#entities)                                         

|Attribute   |Description   |
|---|---|
| answer     | Returns the Answer field for the poll. |
| percentage | Returns the percentage of votes in the poll for the option as a decimal number from 0 through 100. |
| votes      | Returns the number of votes that have been tabulated for the option.                              |


## request

Contains information about the current HTTP request.

```
{% assign id = request.params['id'] | escape %}

<a href={{ request.url | add_query: 'foo', 1 | escape }}>Link</a>
```

> [!NOTE]
> - You can build URLs dynamically in Liquid by using URL Filters.
> - The URL used in request.url can be any requested value, and gets [cached](../configure/enable-header-footer-output-caching.md) for subsequent requests. To ensure correct value in request.url, consider using [substitution tag](../liquid/template-tags.md#substitution), partial URL such as ~\{WebFile path} or storing the portal URL in [Site Settings](../configure/configure-site-settings.md).
> - Power Apps portals release version [9.3.8.x](/power-platform/released-versions/portals/portalupdate938x) or later will by default have [escape](../liquid/liquid-filters.md#escape) Liquid filter enforced for [user](../liquid/liquid-objects.md#user) and [request](../liquid/liquid-objects.md#request) Liquid objects. To disable this default configuration and allow these Liquid objects without escape Liquid filter, see [portal site settings - Site/EnableDefaultHtmlEncoding](../configure/configure-site-settings.md#portal-site-settings).

### Attributes

|Attribute   |Description   |
|---|---|
| params           | Named parameter values for the current request. params is a combination of URL query string parameters, form post parameters, and cookies.  |
| Path             | The path of the current request URL. <br> /profile/|
| path\_and\_query | The path and query of the current request URL.<br> /profile/?foo=1&bar=something|
| query            | The query part of the current request URL. <br> ?foo=1&bar=something |
| url              | The full URL of the current request.<br>  https://www.example.com/profile/?foo=1&bar=something  |


## searchindex

The searchindex object is used within the [Power Apps Dataverse table tags](portals-entity-tags.md), and provides access to the results of a query.  

```
{% searchindex query: 'support', page: params.page, page_size: 10 %}

{% if searchindex.results.size > 0 %}

<p>Found about {{ searchindex.approximate_total_hits }} matches:</p>

<ul>

{% for result in searchindex.results %}

<li>

<h3><a href={{ result.url | escape }}>{{ result.title | escape }}</a></h3>

<p>{{ result.fragment }}</p>

</li>

{% endfor %}

</ul>

{% else %}

<p>Your query returned no results.</p>

{% endif %}

{% endsearchindex %}
```

### Attributes

|Attribute   |Description   |
|---|---|
| approximate\_total\_hits | Returns an approximate count of total hits matching the index query. Due to the way the search index works in regard to security filtering and other design factors, this number is only an approximation, and may not exactly match the total number of results available to the current user in some situations.  |
| Page                     | Returns the page number of the current query.                                                                                                                                                                                                           |
| page\_size               | Returns the maximum page size of the current query. If you want the actual number of results returned for the current page (because this may be less than the specified maximum page size), use results.size.                                                                                           |
| results                  | Returns the query result page, as search index result objects.                                                                                                                                                                                          |

### Search Index Results

|   Attribute   |                                                                                                                                                Description                                                                                                                                                 |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    entity     |                                                                                                                            The underlying [entities](#entities) for the result.                                                                                                                            |
|   fragment    | A relevant short text fragment for the result, with terms matching the specified query highlighted using the &lt;em&gt; HTML tag. Certain types of queries do not support highlighted fragments, such as fuzzy queries (~) and wildcard queries (\*). This property will be null in those cases. |
|      Id       |                                                             The Power Apps table ID of the underlying record for the result, as a string. For example, 936DA01F-9ABD-4d9d-80C7-02AF85C822A8                                                              |
| logical\_name |                                                                           The Power Apps table logical name of the underlying record for the result. For example, adx\_webpage                                                                           |
|    number     |                                                            The number of the result, across all result pages, starting from 1. For example, for the first result of the second page of results, with a page size of 10, this value will be 11.                                                             |
|     score     |                                                                                                 The Lucene score of the result, as a floating-point value. Results will be returned ordered by this value.                                                                                                 |
|     title     |                                                                                                                                          The title of the result.                                                                                                                                          |
|      url      |                                                            The URL for the result. This will usually&mdash;but not necessarily&mdash;be an absolute path for the current application, rather than a full URL. For example: /articles/article1/                                                             |

## settings

Allows you to load any [site setting](../configure/configure-site-settings.md) by name. If a setting with the given name isn't found, [null](liquid-types.md#null) will be returned.  

> [!Note]
> Settings are returned as [strings](liquid-types.md#string), but you can use [Type filters](liquid-filters.md#type-filters) to convert them to other types.

```
{{ settings[My Setting] }}

{% assign search_enabled = settings[Search/Enabled] | boolean %}

{% if search_enabled %}

Search is enabled.

{% endif %}

{% assign pagesize = settings['page size'] | integer | default: 10 %}

{% if pagesize > 10 %}

Page size is greater than 10.

{% endif %}
```

> [!Note]
> [Render a website header and primary navigation bar](render-site-header-primary-navigation.md)


## sitemap

Allows access to the portal site map.

```
<h1>{{ sitemap.root.title }}</h1>

<ul class=breadcrumb>

{% for crumb in sitemap.current.breadcrumbs %}

<li><a href={{ crumb.title }}>{{ crumb.title }}</a></li>

{% endfor %}

<li class=active>{{ sitemap.current.title }}</li>

</ul>

{% for child in sitemap.current.children %}

<a href={{ child.url }}>{{ child.title }}</a>

{% endfor %}

It's also possible to load a site map node by URL path:

{% assign node = sitemap[/content/page1/] %}

{% if node %}

{% for child in node.children %}

<a href={{ child.url }}>{{ child.title }}</a>

{% endfor %}

{% endif %}
```

### Site Map Attributes

|Attribute   |Description   |
|---|---|
| Current | Returns the site map node object for the current page.                    |
| Root    | Returns the site map node object for the root (home) page of the website. |

### Site Map Node Attributes

|Attribute   |Description   |
|-------|-------|
| Breadcrumbs           | Returns the breadcrumb site map node objects for the node, starting from the site map root node and ending at parent. |
| Children              | Returns the child site map node objects of the node.                                                                  |
| Description           | The description/summary content for the node. (This field may contain HTML.)                                          |
| Entity                | Returns the underlying [entities](#entities) of the node. If the node has no underlying table, this value will be null.                                                         |
| is\_sitemap\_ancestor | Returns true if the sitemap node is an ancestor of the current node, otherwise false.                                                                                                         |
| is\_sitemap\_current  | Returns true if the sitemap node is the current node, otherwise false.                                                                                                         |
| Parent                | Returns the parent site map node of the node. If the node is the root node, parent will be null.                                                                     |
| Title                 | The title of the node.                                                                                                |
| url                   | The URL of the node.                                                                                                  |


## sitemarkers

Allows you to load any site marker by name. If the sitemarker exists, a sitemarker object will be returned. If a sitemarker with the given name isn't found, [null](liquid-types.md#null) will be returned.  

```
{{ sitemarkers[Login].url }}

{% assign my_sitemarker = sitemarkers["My Site Marker"] %}

{% if my_sitemarker %}

<a href={{ my_sitemarker.url }}>{{ my_sitemarker.adx_name }}</a>

{% else %}

Site marker My Site Marker does not exist.

{% endif %}
```

> [!Note]
> [Render a website header and primary navigation bar](render-site-header-primary-navigation.md)  

### Sitemarker Attributes

|         Attribute          |                                                                                    Description                                                                                    |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            url             |                                                                         The URL of the sitemarker target.                                                                         |
| \[attribute logical name\] | You can access any attribute of the sitemarker target Power Apps record by logical name. For example, {{ sitemarker.adx\_name }} |

## snippets

Allows you to load any content snippets by name. If a snippet with the given name isn't found, [null](liquid-types.md#null) will be returned.  

```
{{ snippets[Header] }}

{% assign footer = snippets[Footer] %}

{% if footer %}

{{ footer }}

{% else %}

No footer snippet was found.

{% endif %}
```


## tablerowloop

Contains properties useful within a [Iteration tags](iteration-tags.md) loop block.  

> [!Note] 
> tablerowloop can only be used within a [Iteration tags](iteration-tags.md) tag.

### Attributes

|Attribute   |Description   |
|---|---|
| Col        | Returns the index of the current row, starting at 1.                                                       |
| col0       | Returns the index of the current row, starting at 0.                                                       |
| col\_first | Returns true if the current column is the first column in a row, returns false if it isn't.               |
| col\_last  | Returns true if the current column is the last column in a row, returns false if it isn't.                |
| First      | Returns true if it's the first iteration of the loop. Returns false if it's not the first iteration.       |
| Index      | The current item's position in the collection, where the first item has a position of 1.                   |
| index0     | The current item's position in the collection, where the first item has a position of 0.                   |
| Last       | Returns true if it's the last iteration of the loop. Returns false if it's not the last iteration.         |
| Length     | Returns the number of iterations for the loop ߝ the number of items in the collection being iterated over. |
| Rindex     | Number of items remaining in the loop (length - index) where 1 is the index of the last item.              |
| rindex0    | Number of items remaining in the loop (length - index) where 0 is the index of the last item.              |



## user

Refers to the current portal user, allowing access to all attributes of the underlying Power Apps contact record. If no user is signed in, this variable will be [null](liquid-types.md#null).  

user is an [entity](#entity) object.  

```
{% if user %}
 
Hello, {{ user.fullname | escape }}!
 
{% else %}
 
Hello, anonymous user!
 
{% endif %}
```

> [!NOTE]
> Power Apps portals release version [9.3.8.x](/power-platform/released-versions/portals/portalupdate938x) or later will by default have [escape](../liquid/liquid-filters.md#escape) Liquid filter enforced for [user](../liquid/liquid-objects.md#user) and [request](../liquid/liquid-objects.md#request) Liquid objects. To disable this default configuration and allow these Liquid objects without escape Liquid filter, see [portal site settings - Site/EnableDefaultHtmlEncoding](../configure/configure-site-settings.md#portal-site-settings).

### Attributes

In addition to having all of the attributes of an [entity](#entity) object, user has the following attributes.


|    Attribute     |                                                                                                                                                                                     Description                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      roles       |                                                      Returns the roles to which the user belongs, as an [array](liquid-types.md#array).<br>`{% if user.roles contains 'Administrators' %} User is an administrator. {% endif %}`<br>**Note**: You can also use the `has_role` filter to test for individual role memberships.                                                       |
| basic_badges_url | Returns the service url to retrieve a user's badges.<br>To render badges for a user you must include a tag with the attributes "data-badge" and "data-uri". To render the current user's badges:<br>`<div data-badge data-uri='{{user.basic_badges_url }}'></div>`<br>To render out a user's badges by id (variable userid):<br>\`<div data-badge data-uri='{{user.basic_badges_url |
|                  |                                                                                                                                                                                                                                                                                                                                                                                     |

## weblinks

Allows you to load any weblinks by name or ID.  

If the web link set exists, a [web link set object](#web-link-set-attributes) will be returned. If a web link set with the given name or ID isn't found, [null](liquid-types.md#null) will be returned.


```
<!-- Load web link set by ID -->

{{ weblinks[page.adx_navigation.id].name }}

<!-- Load web link set by name -->

{% assign nav = weblinks[Primary Navigation] %}

{% if nav %}

<h1>{{ nav.title | escape }}</h1>

<ul>

{% for link in nav.weblinks %}

<li>

<a href={{ link.url | escape }} title={{ link.tooltip | escape }}>

{% if link.image %}

<img src={{ link.image.url | escape }} alt={{ link.image.alternate_text | escape }} />

{% endif %}

{{ link.name | escape }}

</a>

</li>

{% endfor %}

</ul>

{% endif %}
```

> [!Note]
> [Render a website header and primary navigation bar](render-site-header-primary-navigation.md) |  

### Web Link Set Attributes

> [!Note]
> A web link set is an [entity](#entity) object, with all of the same attributes, in addition to those listed below.                                         

|         Attribute          |                                                                                 Description                                                                                  |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|            Copy            |                                                                      The HTML copy of the web link set.                                                                      |
|            Name            |                                                                        The name of the web link set.                                                                         |
|           Title            |                                                                        The title of the web link set.                                                                        |
|          Weblinks          |                                                       The array of web link objects associated with the web link set.                                                        |
| \[attribute logical name\] | You can access any attribute of the web link set Power Apps record by logical name. For example, {{ weblinkset.createdon }} |

### Web Link Attributes

> [!Note]
> A web link is an [entity](#entity) object, with all of the same attributes, in addition to those listed below.

|          Attribute          |                                                                              Description                                                                              |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         Description         |                                                                 The HTML description of the web link.                                                                 |
|    display\_image\_only     |                              Boolean attribute indicating whether the web link should be displayed as an image only, with no link text.                               |
| display\_page\_child\_links |            Boolean attribute indicating whether the web link should show links to the [*sitemap*](#sitemap) child pages of the linked page, as sub-links.             |
|            Image            |                                     The web link image object for this link. This attribute will be null if no image is present.                                      |
|        is\_external         |                 Boolean attribute indicating whether the target URL of the web link is to an external site (rather than to an internal portal page).                  |
|    is\_sitemap\_ancestor    |                                Returns true if the weblink's URL references an ancestor of the current sitemap node, otherwise false.                                 |
|    is\_sitemap\_current     |                                        Returns true if the weblink's URL references the current sitemap node, otherwise false.                                        |
|            Name             |                                                                    The name/title of the web link.                                                                    |
|          Nofollow           |                                         Boolean attribute indicating whether the web link should be marked as rel=nofollow.                                         |
|    open\_in\_new\_window    |                             Boolean attribute indicating whether the web link should be opened in a new browser window/tab when selected.                             |
|           Tooltip           |                                                                    Tooltip text for the web link.                                                                     |
|             url             |                                                                       The URL of the web link.                                                                        |
|          Weblinks           |                                                   The array of child web link objects associated with the web link.                                                   |
| \[attribute logical name\]  | You can access any attribute of the web link Power Apps record by logical name. For example, {{ weblink.createdon }} |

### Web Link Image Attributes

| alternate\_text | Alternate text for the image.                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------|
| Height          | Integer containing the specified height of the image. If no height value was provided, this attribute will be null. |
| url             | The URL of the image.                                                                                               |
| Width           | Integer containing the specified width of the image. If no width value was provided, this attribute will be null.   |


## website

Refers to the portal website, allowing access to all attributes of the Power Apps Website (adx\_website) record for the portal.  

> [!Note]
> Website is an [entity](#entity) object, with all of the same attributes.

**Code**

```
{{ website.adx_name }} ({{ website.id }})
```

**Output**

```
Community Portal (936DA01F-9ABD-4d9d-80C7-02AF85C822A8)
```

### Attributes

The following table lists the attributes for this tag that can be used replacing the defaults to avoid caching.

| Default | Substitute (avoids caching) | Example |
| - | - | - |
| sign_in_url  | sign_in_url_substitution | **Default**: *website.sign_in_url*: `/en-US/SignIn?returnUrl=%2Fen-US%2F` <br>  **Substitution (avoids caching)**: *website.sign_in_url_substitution*: `/en-US/SignIn?returnUrl=%2Fen-US%2Fsubstitute-page%2F` <br> ("substitute-page" in this example replaces default cached URL.)
| sign_out_url | sign_out_url_substitution | **Default**: *website.sign_out_url*: `/en-US/Account/Login/LogOff?returnUrl=%2Fen-US%2F` <br>  **Substitution (avoids caching)**: *website.sign_out_url_substitution*: `/en-US/Account/Login/LogOff?returnUrl=%2Fen-US%2Fsubstitute-page%2F` <br> ("substitute-page" in this example replaces default cached URL.)

### See also

[Liquid types](liquid-types.md)  
[Liquid Tags](liquid-tags.md)  
[Liquid Filters](liquid-filters.md)  


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]