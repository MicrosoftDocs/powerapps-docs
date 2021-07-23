---
title: Embed portal in another website using Iframe
description: Learn about how to embed a Power Apps portal in another website.
author: dileepsinghmicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: intro-internal
ms.date: 07/16/2021
ms.subservice: portals
ms.author: dileeps
ms.reviewer: tapanm
contributors:
    - dileepsinghmicrosoft
    - tapanm-msft
    - sandhangitmsft
---

# Embed portal in another website using Iframe

One of the most common way of using portal applications is to embed portal functionality inside another website. Most often, this is seen where another website is already in place but you want to enhance its abilities and add new
functions that work with your data surfaced through portal application.

In this scenario, it's easier to embed your portal functionality rather than building it from scratch.

This article explains the steps that you can do to embed portal application in a different website using an Iframe.

## Step 1. Enable portal for Iframe

Iframe feature by default is disabled on new portals to ensure that no one can embed your portal application externally to avoid ["Clickjacking attacks"](https://owasp.org/www-community/attacks/Clickjacking).

To enable Iframe on your portal:

1. Setup HTTP response headers.

    - You can use two type of headers.
        - [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)
        - [CSP frame-ancestor directive](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors).  

        Out of these two options, CSP frame-ancestor header is preferred and replaces X-frame-options.

    - To set up CSP frame-ancestor header, set up the site setting to enable HTTP header **HTTP/Content-Security-Policy**.

        For complete list of all HTTP headers that can be set, see [Setup HTTP headers in portals](configure/cors-support.md).

    - For the value, follow the syntax described in [CSP: frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors) article.

        For example, to enable a portal that can be embedded using Iframe in a website [www.contoso.com](https://www.contoso.com), the setting will look like the following.

        `Content-Security-Policy: frame-ancestors 'self' <https://www.contoso.com>;`

        > [!NOTE]
        > "self" is important to keep, otherwise the portal won’t be able to  embed its own pages&mdash;which is commonly done for several scenarios such as modal popups for basic forms.
        > It's important to keep the ability to embed portal in an IFrame limited to specific sites rather than using wildcard (\*).
        > CSP consists of a lot of directives whose values depends on various factors (like from where the scripts are loaded). This document doesn’t cover that as it's implementation specific. However, we recommend to first test this setup on a nonproduction portal, and look at the browser console errors to find errors that need to be fixed by adjusting the setting.

1. Set up "SameSite" default for portal cookies.

    [SameSite attribute](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite) for cookies is useful to secure the site against CSRF attacks. However, this also means that site can't be embedded in an Iframe in different kinds of scenarios like if it's for authenticated experiences, or it has dynamic components like forms or lists.

    So, to embed the portal in Iframe, SameSite cookie default for your portal must be changed, and default should be set to “None”. To configure SameSite mode in portals, see [SameSite mode changes](important-changes-deprecations.md#samesite-mode-changes).

    > [!NOTE]
    > Marking SameSite cookie as “None” doesn’t make your portal vulnerable to CSRF attacks as the portals platform uses anti-CSRF tokens to prevent these attacks.

## Step 2. Embed your Portal

After you complete the previous step, all you need to do to embed portal experience into your website is to use [html Iframes](https://www.w3schools.com/html/html_iframe.asp) to Iframe the whole site, or specific pages as required.  
  
We recommend that the portal domain name should be a sibling or a child of domain name of the site where portal embedded in Iframe. For example, if your root website is [www.contoso.com](https://www.contoso.com), then the portal domain name should be `portal.contoso.com`.  This is important to ensure that the cookies used by the portal for various functionalities to work aren't classified as [third party cookies and are blocked by browser](https://blog.chromium.org/2020/01/building-more-private-web-path-towards.html).

Otherwise, functionality such as Captcha, and basic/advanced form redirection might not work properly if third-party cookies are blocked. To set up a custom domain name on your portal, see [Add a custom domain name](admin/add-custom-domain.md).

## Step 3. Handle headers and footers

It's common for the parent site to already have headers and footers where the portal might be embedded using Iframe. In such situations, you might not want to show embedded portal's header and footer.

To handle headers and footers in this scenario, consider the following scenarios.

1. When entire portal is embedded in an Iframe:

    Remove the content of your header and footer by updating the respective header and footer web templates.

1. When a specific portal page is embedded in an Iframe:

    Typically, a specific page is added to a website in an Iframe when you don’t want to show the portal header or footer. However, you still want header and footer to be available when user goes to the portal directly. You can achieve this by modifying headers and footers to render dynamically based on page content.

### Conditional code in header and footers

Headers and footer web template supports full liquid customizations, and hence, can be customized to add a conditional property to render certain properties.

For example, the following code represents showing a search bar in the header if the page is anything other than Search page.

> [!IMPORTANT]
> Since header is common element on all pages, "page.id" will get cached by default for first page that is opened by a user. Hence, this code uses [Substitution tag](liquid/template-tags.md#substitution) to ensure that these elements are not cached, and will always be evaluated based on current page.

```
{% substitution %}
{% assign current_page = page.id %}
{% assign sr_page = sitemarkers[Search].id %}
{% if current_page == sr_page %}
{% assign section_class = section-landing-search %}
<section class=page_section section-landing-{{ current_page }} {{ section_class | h }} color-inverse\>
    <div class=container\>
        <div class=row \>
            <div class=col-md-12 text-center\>
                {% if current_page == sr_page %}
                    <h1 class=section-landing-heading\>{% editable snippets 'Search/Title' default:resx["Discover_Contoso"] %}\</h1\>
                {% include 'Search' %}
                {% endif %}
            </div\>
        </div\>
    </div\>
</section\>
{% endif %}
{% endsubstitution %}
```

Instead, you can also disable header and footer from your template (for read-only scenarios without any lists/forms), or even by using a special rewrite template (`~/Areas/Portal/Pages/Form.aspx`). However, both of these
approaches have limitations, and don't support full functionality.

### See also

[Configure Site Settings in portals](configure/configure-site-settings.md) <br>
[Substitution template tag](liquid/template-tags.md#substitution) <br>
[Enable header and footer output caching on a portal](configure/enable-header-footer-output-caching.md) <br>
[SameSite mode](important-changes-deprecations.md#samesite-mode-changes)

