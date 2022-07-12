---
title: Redirect a user to a default page on sign-in
description: Learn how to redirect a user to a default page after signing in.
author: nageshbhat-msft

ms.topic: conceptual
ms.custom: 
ms.date: 06/23/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - nageshbhat-msft
---

# Redirect a user to a default page on sign-in

You can configure a portal to redirect a user to a default page after the user signs in. 

To achieve this, you replace the default studio template that's used as the page layout for the home page. You replace this default template with a custom template that includes JavaScript code to redirect the user to the page of your choosing. The steps are:

1. Make a copy of the default studio template web template.
1. Add JavaScript code to the web template copy.
1. Create a corresponding page template.
1. Modify the home page to use the modified template.

## Make a copy of the default studio template

1. Open the Portal Management app, go to **Web Templates**, and open the **Default studio template**.

1. Copy all of the content that follows the `<!-- Default studio template. Please do not modify -->` line.

    :::image type="content" source="media/redirect-a-user/default-webtemplate.png" alt-text="Copying the default studio template.":::

1. Select **New** to create a new web template record.

1. Give the template a name (for example, **Home page template**), and select the **Website** you want to redirect users to when they sign in<!--note from editor: Edit okay?-->. Paste the content from the default studio template, and then select **Save**. 

## Add JavaScript code

1. In the new template, add the following JavaScript code. Replace `./page/` with the partial URL of the page you want to direct the user to:

    ```javascript
    {% if user %}
    //if any user logs in
    <script>
      window.location.href='./page/'
    </script>
    {% else %}
    //Home webpage code, if you don't want to display the page when the user is being redirected
    {% endif %}
    //Home webpage code, if you want to display the page when the user is being redirected
    ```

    :::image type="content" source="media/redirect-a-user/new-webtemplate.png" alt-text="New web template with JavaScript added.":::

1. Select **Save**.

## Create a page template

1. In the Portal Management app, select **Page templates**.

1. Select **New**, and then create a new page template record.

1. Give the page template a name (for example, **Home page template**). Select the **Website**<!--note from editor: Will the reader know which website you mean?-->, choose the **Type** as **Web Template**, and select the **Web Template** you created in the previous step.

    :::image type="content" source="media/redirect-a-user/page-template.png" alt-text="Creating a new page template.":::

## Update the home page

1. Go to the Portal Management app.

1. In **Web Pages**, locate the **Home** webpage record. Change the **Page Template** to the page template record you created earlier. Select **Save & Close**.

    :::image type="content" source="media/redirect-a-user/update-home-page.png" alt-text="Update the home page.":::

Now, when a user signs in, they'll be redirected to the page you specified in the JavaScript code in the updated web template.<!--note from editor: Edit okay? I wasn't sure what the "Navigate to the site" step was saying.-->

### See also

[Create a custom page template to render an RSS feed](render-rss-custom-page-template.md)  
[Render the list associated with the current page](render-entity-list-current-page.md)  
[Render a website header and primary navigation bar](render-site-header-primary-navigation.md)  
[Render up to three levels of page hierarchy by using hybrid navigation](hybrid-navigation-render-page-hierachy.md)  

