---
title: Enable header and footer output caching on a portal
description: Learn how to enable header and footer output caching on a portal for existing users.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.subservice: portals
ms.author: sandhan
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - sandhangitmsft
---

# Enable header and footer output caching on a portal

To improve processing performance for Header and Footer web templates in a portal, enable header and footer output caching. Header and Footer web templates are parsed and rendered every time a page is loaded. Caching header and footer output significantly reduces page processing time.

For a new user, output caching is enabled by default. The following site settings are available and set to true by default to support this functionality:
- Header/OutputCache/Enabled: Set the value to true to enable output caching for header.
- Footer/OutputCache/Enabled: Set the value to true to enable output caching for footer.

For a user who upgraded to a newer version of portals, output caching is disabled by default&mdash;that is, the Header and Footer web templates are parsed and rendered on every page load. To enable output caching, you must update the Header, Footer, and Languages Dropdown web templates and create the required site settings.

> [!Note]
> If you enable output caching only by creating site settings, parts of the header and footer will not render properly and error messages will be displayed.

### Enable header and footer output caching for an existing user

**Step 1: Update the Header web template**

1. Open the [Portal Management app](configure-portal.md).
2. Go to **Portals** > **Web Templates**.
3. Open the Header web template.
4. Update the code in the **Source** field:
    - Find the following code and update it:
    
        **Existing code**

        ```
        <li>
            <a href={% if homeurl%}/{{ homeurl }}{% endif %}/Account/Login/LogOff?returnUrl={{ request.raw_url_encode | escape }} title={{ snippets["links/logout"] | default:resx["Sign_Out"] | escape }}>
            {{ snippets["links/logout"] | default:resx["Sign_Out"] | escape }}
            </a>
        </li>
        </ul>
        </li>
        {% else %}
        <li>
            <a href={% if homeurl%}/{{ homeurl }}{% endif %}/SignIn?returnUrl={{ request.raw_url_encode }}>
            {{ snippets["links/login"] | default:resx["Sign_In"] }}
            </a>
        </li>
        ```
        
        **Updated code**

         ```
        <li>
            <a href={% if homeurl%}/{{ homeurl }}{% endif %}{{ website.sign_out_url_substitution }} title={{ snippets["links/logout"] | default:resx["Sign_Out"] | escape }}>
            {{ snippets["links/logout"] | default:resx["Sign_Out"] | escape }}
            </a>
        </li>
        </ul>
        </li>
        {% else %}
        <li>
            <a href={% if homeurl%}/{{ homeurl }}{% endif %}{{ website.sign_in_url_substitution }}>
            {{ snippets["links/login"] | default:resx["Sign_In"] }}
            </a>
        </li>
        ```
    - Find the following code and update it:

        **Existing code**
        ```
    	{% assign current_page = page.adx_partialurl %}
		{% assign sr_page = sitemarkers[Search].url | remove: '/' %}
		{% assign forum_page = sitemarkers[Forums].url | remove: '/' %}
		{% if current_page == sr_page or current_page == forum_page %}
		  <section class=page_section section-landing-{{ current_page }} color-inverse>
		    <div class=container>
		      <div class=row >
		        <div class=col-md-12 text-center>
		          {% if current_page == sr_page %}
		            <h1 class=section-landing-heading>{% editable snippets 'Search/Title' default: resx["Discover_Contoso"] %}</h1>
		            {% include 'Search' %}
		          {% endif %}
		        </div>
		      </div>
		    </div>
		  </section>
        {% endif %}
        ```

        **Updated code**

        ```
        {% substitution %}
		  {% assign current_page = page.id %}
		  {% assign sr_page = sitemarkers[Search].id %}
		  {% assign forum_page = sitemarkers[Forums].id %}
		  {% if current_page == sr_page or current_page == forum_page %}
		    {% assign section_class = section-landing-search %}
		    {% if current_page == forum_page %}
		      {% assign section_class = section-landing-forums %}
		    {% endif %}
		   <section class=page_section section-landing-{{ current_page }} {{ section_class | h }} color-inverse>
		      <div class=container>
		        <div class=row >
		          <div class=col-md-12 text-center>
		            {% if current_page == sr_page %}
		              <h1 class=section-landing-heading>{% editable snippets 'Search/Title' default: resx["Discover_Contoso"] %}</h1>
		              {% include 'Search' %}
		            {% endif %}
		          </div>
		        </div>
		      </div>
		    </section>
		  {% endif %}
        {% endsubstitution %}
        ```

5. Save the web template.

**Step 2: Update the Footer web template**

1. Open the [Portal Management app](configure-portal.md).
2. Go to **Portals** > **Web Templates**.
3. Open the Footer web template.
4. In the **Source** field, find the following code and update it:
    
    **Existing code**
    
    ```
    <section id=gethelp class=page_section section-diagonal-right color-inverse {% if page %}{% unless page.parent %}home-section{% endunless %}{% endif %} hidden-print>
    ```

    **Updated code**

    ```
    <section id=gethelp class=page_section section-diagonal-right color-inverse {% substitution %}{% if page %}{% unless page.parent %}home-section{% endunless %}{% endif %}{% endsubstitution %} hidden-print>
    ```

5. Save the web template.

**Step 3: Update the Languages Dropdown web template**

1. Open the [Portal Management app](configure-portal.md).
2. Go to **Portals** > **Web Templates**.
3. Open the Languages Dropdown web template.
4. In the **Source** field, find the following code, and ensure that the `language` object uses `url.substitution` attribute instead of `url`:
    
    ```
    <a href=/{{ language.url_substitution }} title={{ language.name }} data-code={{ language.code }}>{{ language.name }}</a>
    ```

5. Save the web template.

**Step 4: Create site settings**

Create the following site settings:

|Name|Value|
|----|-----|
|Header/OutputCache/Enabled|True|
|Footer/OutputCache/Enabled|True|
|||


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]