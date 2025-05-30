---
title: "Script web resource development using Fiddler Auto Responder (model-driven apps)"
description: "Learn about how to setup and use Auto Responder in Fiddler for local debugging of JavaScript web resources."
author: anushikhas96
ms.author: anushisharma
ms.date: 12/04/2022
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Script web resource development using Fiddler Auto Responder

 Use Auto Responder in [Telerik Fiddler](https://www.telerik.com/fiddler) while developing and debugging JavaScript web resources to replace the content of a web resource with content from a local file rather than uploading it in your Model-driven Apps instance and publishing each time. Use the following steps to set up Auto Responder in Fiddler.

## Install and configure Fiddler

1. [Download](https://www.telerik.com/download/fiddler) and install Fiddler.
1. Open Fiddler and from the menu bar, go to **Tools**, and then select **Options**.
1. Select the **HTTPS** tab in the dialog box and check the **Capture HTTPS CONNECTS** and **Decrypt HTTPS traffic** checkboxes so that the HTTPS traffic is captured and then decrypted.

   :::image type="content" source="media/fiddler-https-options.png" alt-text="Select the marked checkboxes in the HTTP tab":::

1. Select **OK** to close the dialog box.

> [!NOTE]
> If it is the first time you are enabling this setting, Fiddler will prompt you to install a certificate. Install the certificate and restart Fiddler so that the new settings take effect.
> 
> If you have run Fiddler in the past and get a `NET::ERR_CERT_AUTHORITY_INVALID` error, in the **HTTPS** tab, click the **Actions** button and choose **Reset All Certificates**. This will also present a number of prompts for the new certificates to be installed.

## Configure Auto Responder

1. Open the page in the model-driven app that you want to debug.
1. Start the Fiddler trace capture by clicking the **Capturing** button in the bottom left corner.

   :::image type="content" source="media/fiddler-start-capturing.png" alt-text="select on Capturing button to start capturing HTTPS traffic.":::

   > [!NOTE]
   > If you want to capture HTTPS traffic only from a particular host, on the **Filters** tab, in the **Hosts** area, in the **-No Host Filter-** drop-down select **Show only the following Hosts** from the menu and enter the list of domains from which you wish to see traffic, separated by semi-colon. More information: [Filters reference](https://docs.telerik.com/fiddler/KnowledgeBase/Filters).
   > ![Filter traffic displayed in Fiddler UI.](media/fiddler-filter-traffic.png "Filter traffic displayed in Fiddler UI")

1. Perform any operation necessary to load the script you're testing. You can stop the capture by clicking the same **Capturing** button again.
1. Select the trace log sessions from the left pane and search for the file you want to set up the Auto Responder for.

   For example, if the code you want to debug is in a JavaScript web resource named `new_testscript.js`, use the **Find** button to open the  **Find Sessions** dialog box and search for the name of the web resource.

   :::image type="content" source="media/fiddler-find-sessions.PNG" alt-text="Find a session in fiddler.":::

   You see the rows that match with your search criteria highlighted in the left pane.

1. Select that row. In the right pane, select the **Auto Responder** tab.

   :::image type="content" source="media/fiddler-auto-responder.png" alt-text="Select the Auto Responder tab.":::

1. In the **Auto Responder** tab, select the **Enable rules** and **Unmatched requests passthrough** check boxes.

   :::image type="content" source="media/fiddler-select-checkbox.png" alt-text="Select the two highlighted checkboxes":::

1. Ensure that you still have the session related to your target file selected and then select on the **Add Rule** button in the **Auto Responder** section. This adds a new entry into the rules table.

   :::image type="content" source="media/fiddler-add-rule.png" alt-text="Add new rule":::

1. When the rule is selected, the **Rule Editor** at the bottom has the top row populated with the Session URL related to your file and prefixed with a string like `EXACT:`.

   You can then edit the string to match to simplify it. With web resources, the URL contains generated values in the URL or in a query string to make sure that the latest published version is included in the response. You'll probably see the `EXACT` value looks something like this:

   ```
   EXACT:https://<org URL>/%7B636556138760000160%7D/WebResources/new_testscript.js?    ver=-1229805553
   ```

   You can simplify this to remove the generated values and use this instead:

   ```
   /WebResources/new_testscript.js
   ```

   The bottom row is left blank. Type the path to your local file on your disk on this bottom row and **Save**.

   :::image type="content" source="media/fiddler-save-rule.PNG" alt-text="Add path to your local file in Rule editor":::


These steps configured Fiddler to listen to the requests and responds with the local file instead of passing the request over the network.

## Update and test your code

1. Apply changes to your local file.
1. Start Fiddler trace capture again and go back to your browser and hard reload the page with empty cache.
1. In the browser developer tools, you can see that the file that is now received is the local one.
1. Continue repeating this process while updating your code until you get the results you require.


## See Also

[Web resources](web-resources.md)   
[Client scripting using JavaScript](client-scripting.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
