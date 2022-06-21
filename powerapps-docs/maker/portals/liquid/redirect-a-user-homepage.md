---
title: Redirect a user to a default page after signing in
description: Learn how to redirect a user to a default page after signing in.
author: gitanjalisingh33msft

ms.topic: conceptual
ms.custom: 
ms.date: 06/20/2022
ms.subservice: portals
ms.author: gisingh
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - GitanjaliSingh33msft
---

# Redirect a user to a default page after signing in

You can configure a portal to redirect a user to a default page after signing in. 

To achieve this functionality, you will need to replace the default studio template used by default for the home page and replace it with a custom template with JavaScript code to redirect the user to the page of your choosing.

- Make a copy of the *default studio template* web template.
- Add JavaScript code to the web template copy.
- Create a corresponding page template
- Modify the home page to use the modified template

## Make a copy of the default studio template

1. Launch the Portal Management app and go to **Web Templates** and open the **Default studio template**.

1. Copy all of the content below the `<!-- Default studio template. Please do not modify -->` line.

    :::image type="content" source="media/redirect-a-user/default-webtemplate.png" alt-text="Copying the default studio template.":::

1. Select **New** to create a new web template record.

1. Give the template a name (e.g. *home page template*) and select the **Website**. Paste the content from the **Default studio template**. Select **Save**. 

## Add JavaScript code

1. In the new template, add the following JavaScript code, replace the `./page/` with the partial url of the page you want to direct the user to:

    ```javascript
    {% if user %}
    //if any user logs in
    <script>
      window.location.href='./page/'
    </script>
    {% else %}
    //Home web page code, if you don't want to display the page when the user is being redirected
    {% endif %}
    //Home web page code, if you want to display the page when the user is being redirected
    ```
1. Select **Save**.

## Create a page template

1. In the Portal Management app, select **Page templates**.

1. Select **New** and create a new page template record.

1. Give the page template a name (e.g. *Home page template*). Select the **Website**, choose the **Type** as **Web Template**, and select the **Web Template** you created in the previous step.

    :::image type="content" source="media/redirect-a-user/page-template.png" alt-text="Creating a new page template.":::

## Update home page



### See also

[Create a custom page template to render an RSS feed](render-rss-custom-page-template.md)  
[Render the list associated with the current page](render-entity-list-current-page.md)  
[Render a website header and primary navigation bar](render-site-header-primary-navigation.md)  
[Render up to three levels of page hierarchy by using hybrid navigation](hybrid-navigation-render-page-hierachy.md)  

