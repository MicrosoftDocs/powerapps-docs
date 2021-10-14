---
title: Render the list associated with the current page
description: Sample code to render the list associated with the current page in a portal.
author: gitanjalisingh33msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/29/2021
ms.subservice: portals
ms.author: gisingh
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - GitanjaliSingh33msft
---

# Render the list associated with the current page

Render the List associated with the current page as a paginated sortable table. Uses [entitylist](liquid-objects.md#entitylist), [entityview](liquid-objects.md#entityview), [Dataverse entity tags](portals-entity-tags.md), [page](liquid-objects.md#page), and [request](liquid-objects.md#request) parameters, and includes search and multiple view selection.  

```xml
{% entitylist id:page.adx_entitylist.id %}
  <div class="navbar navbar-default">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle"
          data-toggle="collapse"
          data-target="#entitylist-navbar-{{ entitylist.id | h }}">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="{{ page.url | h }}">{{ entitylist.adx_name | h }} </a>
      </div>
      <div class="collapse navbar-collapse" id="entitylist-navbar-{{ entitylist.id | h }} ">

        {% if entitylist.views.size > 1 %}
          <ul class="nav navbar-nav">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                <i class="fa fa-list"></i> Views <span class="caret"></span>
              </a>
              <ul class="dropdown-menu" role="menu">
                {% for view in entitylist.views -%}
                  <li{% if params.view == view.id %} class="active"{% endif %}>
                    <a href="{{ request.path | add_query:'view', view.id | h }}">{{view.name | h }}</a>
                  </li>
                {% endfor -%}
              </ul>
            </li>
          </ul>
        {% endif %}
      
        {% if entitylist.search_enabled %}
          <form class="navbar-form navbar-left" method="get">
            <div class="input-group">
              {% if params.search.size > 0 %}
                <div class="input-group-btn">
                  <a class="btn btn-default"
                    href="{{ request.path_and_query | remove_query:'search' | h }}">&times;</a>
                </div>
              {% endif %}
              <input name="search" class="form-control"
                value="{{ params.search  | h }}"
                placeholder="{{ entitylist.search_placeholder | default: 'Search'  | h }}"
                type="text"/>
              <div class="input-group-btn">
                <button type="submit" class="btn btn-default"
                  title="{{ entitylist.search_tooltip  | h }}">
                  <i class="fa fa-search">&nbsp;</i>
                </button>
              </div>
            </div>
          </form>
        {% endif %}
        
        {% if entitylist.create_enabled %}
          <ul class="nav navbar-nav navbar-right">
            <li>
              <a href="{{ entitylist.create_url  | h }}">
                <i class="fa fa-plus"></i> {{ entitylist.create_label | default: 'Create' | h }}
              </a>
            </li>
          </ul>
        {% endif %}
        
      </div>
    </div>
  </div>
  
  {% entityview id:params.view, search:params.search, order:params.order, page:params.page, pagesize:params.pagesize, metafilter:params.mf %}
    {% assign order = params.order | default: entityview.sort_expression %}
    <table class="table" data-order="{{ order  | h }}" >
      <thead>
        <tr>
          {% for c in entityview.columns -%}
            <th width="{{ c.width  | h }}" data-logicalname="{{ c.logical_name  | h }} ">
              {% if c.sort_enabled %}
                {% assign current_sort = order | current_sort:c.logical_name %}
                {% case current_sort %}
                {% when 'ASC' %}
                  <a href="{{ request.path_and_query | add_query:'order', c.sort_descending  | h }}">
                    {{ c.name  | h }} <i class="fa fa-sort-asc"></i>
                  </a>
                {% when 'DESC' %}
                  <a href="{{ request.path_and_query | add_query:'order', c.sort_ascending  | h }}">
                    {{ c.name  | h }} <i class="fa fa-sort-desc"></i>
                  </a>
                {% else %}
                  <a href="{{ request.path_and_query | add_query:'order', c.sort_ascending  | h }}">
                    {{ c.name  | h }} <i class="fa fa-unsorted"></i>
                  </a>
                {% endcase %}
              {% else %}
                {{ c.name  | h }}
              {% endif %}
            </th>
          {% endfor -%}
          <th width="1"></th>
        </tr>
      </thead>

      <tbody>
        {% for e in entityview.records -%}
          <tr>

            {% for c in entityview.columns -%}
              {% assign attr = e[c.logical_name] %}
              {% assign attr_type = c.attribute_type | downcase %}

              <td data-logicalname="{{ c.logical_name  | h }}" >
                {% if attr.is_entity_reference -%}
                  {{ attr.name  | h }}
                {% elsif attr_type == 'datetime' %}
                  {% if attr %}
                    <time datetime="{{ attr | date_to_iso8601  | h }}" >
                      {{ attr  | h }}
                    </time>
                  {% endif %}
                {% elsif attr_type == 'picklist' %}
                  {{ attr.label  | h }}
                {% else %}
                  {{ attr  | h }}
                {% endif -%}
              </td>
            {% endfor -%}

            <td>
              {% if entitylist.detail_enabled -%}
                <a class="btn btn-default btn-xs"
                  href="{{ entitylist.detail_url}}?{{ entitylist.detail_id_parameter  | h }}={{ e.id }}"
                  title="{{ entitylist.detail_label  | h }}" >
                  <i class="fa fa-external-link"></i>
                </a>
              {% endif -%}
            </td>

          <tr>
        {% endfor -%}
      </tbody>
    </table>
    
    {% if entityview.pages.size > 0 %}
      {% assign first_page = entityview.first_page %}
      {% assign last_page = entityview.last_page %}
      {% assign page_offset = entityview.page | minus:1 | divided_by:10 | times:10 %}
      {% assign page_slice_first_page = page_offset | plus:1 %}
      {% assign page_slice_last_page = page_offset | plus:10 %}

      <ul class="pagination" >
        <li {% unless first_page and entityview.page > 1 %}class="disabled"{% endunless %}>
          <a
            {% if first_page and entityview.page > 1 %}
              href="{{ request.url | add_query:'page', first_page | path_and_query  | h }}"
            {% endif %}>
            &laquo;
          </a>
        </li>

        <li {% unless entityview.previous_page %}class="disabled"{% endunless %}>
          <a
            {% if entityview.previous_page %}
              href="{{ request.url | add_query:'page', entityview.previous_page | path_and_query  | h }}"
            {% endif %}>
            &lsaquo;
          </a>
        </li>

        {% if page_slice_first_page > 1 %}
          {% assign previous_slice_last_page = page_slice_first_page | minus:1 %}
          <li>
            <a href="{{ request.url | add_query:'page', previous_slice_last_page | path_and_query  | h }}">
              &hellip;
            </a>
          </li>
        {% endif %}

        {% for page in entityview.pages offset:page_offset limit:10 -%}
          <li{% if page == entityview.page %} class="active"{% endif %}>
            <a href="{{ request.url | add_query:'page', page | path_and_query  | h }}">
              {{ page  | h }}
            </a>
          </li>
        {% endfor -%}

        {% if page_slice_last_page < entityview.pages.size %}
          {% assign next_slice_first_page = page_slice_last_page | plus:1 %}
          <li>
            <a href="{{ request.url | add_query:'page', next_slice_first_page | path_and_query  | h }}">
              &hellip;
            </a>
          </li>
        {% endif %}

        <li {% unless entityview.next_page %}class="disabled"{% endunless %}>
          <a
            {% if entityview.next_page %}
              href="{{ request.url | add_query:'page', entityview.next_page | path_and_query  | h }}"
            {% endif %}>
            &rsaquo;
          </a>
        </li>

        <li {% unless last_page and entityview.page < last_page %}class="disabled"{% endunless %}>
          <a
            {% if last_page and entityview.page < last_page %}
              href="{{ request.url | add_query:'page', last_page | path_and_query  | h }}"
            {% endif %}>
            &raquo;
          </a>
        </li>
      </ul>

    {% endif %}
    
  {% endentityview %}
{% endentitylist %}
```

### See also

[Create a custom page template by using Liquid and a web template page template](create-custom-template.md)  
[Create a custom page template to render an RSS feed](render-rss-custom-page-template.md)  
[Render a website header and primary navigation bar](render-site-header-primary-navigation.md)  
[Render up to three levels of page hierarchy by using hybrid navigation](hybrid-navigation-render-page-hierachy.md)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]