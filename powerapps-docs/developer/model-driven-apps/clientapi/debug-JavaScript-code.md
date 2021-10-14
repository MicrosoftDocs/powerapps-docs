---
title: "Debug your JavaScript code for model-driven apps| MicrosoftDocs"
ms.date: 10/31/2018
ms.service: powerapps
ms.topic: "conceptual"
applies_to: 
  - "Dynamics 365 (online)"
ms.assetid: 3edad039-4397-4984-a29b-9307a7a2aaee 
author: "Nkrb"
ms.subservice: mda-developer
ms.author: "nabuthuk"
manager: "kvivek"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Debug your JavaScript code for model-driven apps



Each browser provides some kind of debugging extension. Microsoft Edge and Internet Explorer provide F12 Developer Tools you can use to debug scripts in model-driven apps. The F12 Developer Tools can be opened by pressing F12 when viewing a page using Microsoft Edge or Internet Explorer. For more information, see Using the [F12 developer tools guide](/microsoft-edge/f12-devtools-guide).

For Google Chrome, press F12 to open developer tools. Firebug is a popular browser extension for web development using Mozilla Firefox. For Apple Safari, you must first select the **Show Develop** menu in menu bar in **Advanced Preferences**. Then you can select **Show Web Inspector** from the **Develop** menu.

When you use JavaScript libraries in model-driven apps, your libraries are loaded with the web page. It can sometimes be difficult to isolate your specific library in the debugging environment. When using debugging tools in Microsoft Edge, on the **Debugger** tab, click on the folder icon at the top-left corner, and expand the available scripts and find the one with the name that corresponds to the name of your JavaScript web resource, such as the **new_myCustomJavaScript.js** web resource shown below. You can also search for your JavaScript library by typing the file name in the search box.

![Debugging JavaScript.](../media/form-script-debugging.png)

Debugging tools for different browsers have similar capabilities. Once you have found your library, you can set a break point and recreate the event that should cause your code to run.

Also look at the following blog post on our team blog site for more ideas on debugging your JavaScript code: [Blog: Debugging custom JavaScript code in CRM using browser developer tools](https://blogs.msdn.microsoft.com/crm/2015/11/29/debugging-custom-javascript-code-in-crm-using-browser-developer-tools/).

## Select appropriate frame to debug your code

model-driven apps forms are composed of several frames. For the code to work in the **Console** of the browser developer tools, you must select the appropriate frame. 
- For the web client forms, select the frame named **ClientApiWrapper**. 
- For the new Unified Interface forms, select the frame named **ClientApiFrame_[n]** where n is the internal page ID. You should select the frame with the highest value for [n].

## Write messages to the console

Using the [window.alert](https://msdn.microsoft.com/library/ms535933(v=vs.85).aspx) method when debugging JavaScript is still a common way to troubleshoot code in the application. But now that all modern browsers provide easy access to debugging tools, it is not a best practice, especially when others might be using the application you are debugging.

Consider writing your messages to the console instead. The following is a small function you can add to your libraries that you can use to send any messages you want to view to the console when it is open.

```JavaScript
function writeToConsole(message)
{
 if (typeof console != 'undefined') {
  console.log(message);
 }
}
```

Unlike using the alert method, if you forget to remove any code that uses this function, people using the application will not see your messages.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]