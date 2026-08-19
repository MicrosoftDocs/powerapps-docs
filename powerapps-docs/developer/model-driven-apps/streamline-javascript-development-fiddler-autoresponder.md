---
title: "Debug Web Resources with Fiddler Auto Responder"
description: "Learn how to use Fiddler Auto Responder to debug JavaScript web resources from local files without repeated uploads and publishing. Follow the setup steps."
author: anushikhas96
ms.author: anushisharma
ms.date: 08/18/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Script web resource development by using Fiddler Auto Responder

Use [Fiddler Auto Responder](https://www.telerik.com/fiddler) to replace a JavaScript web resource with a local file while you develop and debug it. This approach lets you test changes without uploading and publishing the web resource to your model-driven app each time. Follow these steps to configure Auto Responder.

## Install and configure Fiddler

1. [Download](https://www.telerik.com/download/fiddler) and install Fiddler.
1. Open Fiddler. From the menu bar, go to **Tools**, and then select **Options**.
1. Select the **HTTPS** tab in the dialog box and check the **Capture HTTPS CONNECTS** and **Decrypt HTTPS traffic** checkboxes so that Fiddler captures and decrypts the HTTPS traffic.

   :::image type="content" source="media/fiddler-https-options.png" alt-text="Screenshot of Fiddler HTTPS options with traffic capture and decryption selected.":::

1. Select **OK** to close the dialog box.

> [!NOTE]
> If it's the first time you're enabling this setting, Fiddler prompts you to install a certificate. Install the certificate and restart Fiddler so that the new settings take effect.
> 
> If you ran Fiddler in the past and get a `NET::ERR_CERT_AUTHORITY_INVALID` error, in the **HTTPS** tab, click the **Actions** button and choose **Reset All Certificates**. This action also presents prompts to install new certificates.

## Configure Auto Responder

1. Open the page in the model-driven app that you want to debug.
1. Start the Fiddler trace capture by clicking the **Capturing** button in the bottom left corner.

   :::image type="content" source="media/fiddler-start-capturing.png" alt-text="Screenshot of the Fiddler Capturing button used to start HTTPS traffic capture.":::

   > [!NOTE]
   > To capture HTTPS traffic only from a particular host, on the **Filters** tab, in the **Hosts** area, select **Show only the following Hosts** from the **-No Host Filter-** drop-down menu and enter the list of domains from which you want to see traffic, separated by semicolons. For more information, see [Filters reference](https://www.telerik.com/fiddler/fiddler-classic/documentation/knowledge-base/filters#filters-reference).
   > :::image type="content" source="media/fiddler-filter-traffic.png" alt-text="Screenshot of Fiddler host filters configured to display traffic from selected domains.":::

1. Perform any operation necessary to load the script you're testing. You can stop the capture by clicking the same **Capturing** button again.
1. Select the trace log sessions from the left pane and search for the file you want to set up the Auto Responder for.

   For example, if the code you want to debug is in a JavaScript web resource named `new_testscript.js`, use the **Find** button to open the  **Find Sessions** dialog box and search for the name of the web resource.

   :::image type="content" source="media/fiddler-find-sessions.PNG" alt-text="Screenshot of the Fiddler Find Sessions dialog used to locate a JavaScript web resource.":::

   You see the rows that match your search criteria highlighted in the left pane.

1. Select that row. In the right pane, select the **Auto Responder** tab.

   :::image type="content" source="media/fiddler-auto-responder.png" alt-text="Screenshot of the Fiddler Auto Responder tab for a selected trace session.":::

1. In the **Auto Responder** tab, select the **Enable rules** and **Unmatched requests passthrough** check boxes.

   :::image type="content" source="media/fiddler-select-checkbox.png" alt-text="Screenshot of the Fiddler Auto Responder options with both required checkboxes selected.":::

1. Ensure that you still have the session related to your target file selected and then select the **Add Rule** button in the **Auto Responder** section. This action adds a new entry into the rules table.

   :::image type="content" source="media/fiddler-add-rule.png" alt-text="Screenshot of the Fiddler Auto Responder pane with a newly added rule.":::

1. When the rule is selected, the **Rule Editor** at the bottom has the top row populated with the Session URL related to your file and prefixed with a string like `EXACT:`.

   You can then edit the string to match to simplify it. With web resources, the URL contains generated values in the URL or in a query string to ensure that the latest published version is included in the response. You probably see the `EXACT` value looks something like this:

   ```
   EXACT:https://<org URL>/%7B636556138760000160%7D/WebResources/new_testscript.js?    ver=-1229805553
   ```

   You can simplify this value by removing the generated values.

   ```
   /WebResources/new_testscript.js
   ```

   Leave the bottom row blank. Type the path to your local file on your disk in this bottom row and **Save**.

   :::image type="content" source="media/fiddler-save-rule.PNG" alt-text="Screenshot of the Fiddler Rule Editor with the path to a local JavaScript file.":::


These steps configured Fiddler to listen to the requests and respond with the local file instead of passing the request over the network.

## Update and test your code

1. Apply changes to your local file.
1. Start Fiddler trace capture again. Go back to your browser and hard reload the page with an empty cache.
1. In the browser developer tools, check that the file you receive is the local one.
1. Continue updating your code and repeating this process until you get the results you want.


## See also

[Web resources](web-resources.md)   
[Client scripting using JavaScript](client-scripting.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
