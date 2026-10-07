---
title: "Debug JavaScript Web Resources with Local Overrides"
description: "Learn how to use Microsoft Edge DevTools Local Overrides to edit and debug a JavaScript web resource used as an event handler in a model-driven app."
author: anushikhas96
ms.author: anushisharma
ms.date: 08/31/2026
ms.reviewer: jdaly
ms.topic: how-to
ms.subservice: mda-developer
search.audienceType:
  - developer
contributors:
  - JimDaly
ai-usage: ai-assisted
---
# Debug JavaScript web resources by using Local Overrides

When you develop and debug JavaScript web resources that you use as an event handler in a model-driven app, you typically need to make several changes and test how they work. Uploading and publishing the web resource after every change slows down this process.

Modern browser developer tools provide capabilities to  save a local copy of the web resource. When the model-driven app requests the web resource, the browser loads your local copy instead of the file from the server. You can edit the local copy, refresh the page, and test your changes without repeatedly uploading and publishing the web resource. You don't need to install proxy software, browser extensions, or certificates.

Learn more about how modern browsers provide these capabilities.

- Microsoft Edge [Local Overrides](/microsoft-edge/devtools/javascript/overrides)
- Google Chrome [local overrides](https://developer.chrome.com/docs/devtools/overrides)
- Firefox [Network Overrides](https://firefox-source-docs.mozilla.org/devtools-user/network_monitor/network_overrides/index.html)
- Safari [WebKit Web Inspector Local Overrides](https://webkit.org/web-inspector/local-overrides/)

> [!IMPORTANT]
> A local override only changes the resource loaded by your browser. It doesn't update the JavaScript web resource in Microsoft Dataverse, and other users don't see your changes. After you finish troubleshooting, copy the changes you want to keep into your source file and use your normal process to update and publish the web resource. This article doesn't describe that process.

## Prerequisites

Before you begin: 

- You need a model-driven app that has a JavaScript web resource used to provide event handlers for a form.

   This article uses the JavaScript web resource described in [Write your first client script](clientapi/walkthrough-write-your-first-client-script.md). That walkthrough creates a JavaScript web resource named `example_form-script.js`, adds it to the **Account** form, and registers functions for the form **On Load** and **On Save** events and the **Name** column **On Change** event.

   > [!NOTE]
   > You can download the [JavaScriptWebResourceExampleSolution_1_0_managed.zip](https://go.microsoft.com/fwlink/?LinkId=2378308&clcid=0x9). Install this managed solution and you find a model-driven application that represents the completed outcome of the [Write your first client script](clientapi/walkthrough-write-your-first-client-script.md) walkthrough article.

- This article uses [Microsoft Edge](https://www.microsoft.com/edge), but Google Chrome, Firefox, and Safari developer tools have similar capabilities.
- Create an empty folder on your computer for Microsoft Edge DevTools to store local overrides. Don't use a folder that contains source files, credentials, certificates, or other sensitive information. DevTools creates the folder structure it needs within this folder. This article uses `C:\temp\overrides` but you might want to use `C:\Users\<your user name>\overrides`.

This article uses this script from [Write your first client script](clientapi/walkthrough-write-your-first-client-script.md):

```javascript
// Define a unique namespace for the sample library.
window.Example ??= {};

(() => {
    const notificationId = "_myUniqueId";
    const currentUserName = Xrm.Utility.getGlobalContext().userSettings.userName;
    const message = `${currentUserName}: Your JavaScript code in action!`;

    // Code to run in the form OnLoad event
    window.Example.formOnLoad = (executionContext) => {
        const formContext = executionContext.getFormContext();

        // Display the form level notification as an INFO
        formContext.ui.setFormNotification(message, "INFO", notificationId);

        // Wait for 5 seconds before clearing the notification
        window.setTimeout(
            () => formContext.ui.clearFormNotification(notificationId),
            5000
        );
    };

    // Code to run in the column OnChange event
    window.Example.attributeOnChange = (executionContext) => {
        const formContext = executionContext.getFormContext();

        // Automatically set some column values if the account name contains "Contoso"
        const accountName = formContext.getAttribute("name").getValue();
        if (accountName?.toLowerCase().includes("contoso")) {
            formContext.getAttribute("websiteurl").setValue("https://www.contoso.com");
            formContext.getAttribute("telephone1").setValue("425-555-0100");
            formContext.getAttribute("description").setValue("Website URL, Phone and Description set using custom script.");
        }
    };

    // Code to run in the form OnSave event
    window.Example.formOnSave = () => {
        // Display an alert dialog
        Xrm.Navigation.openAlertDialog({ text: "Record saved." });
    };
})();
```

This JavaScript web resource provides three functions that are registered for the following events:


|Function|Event|
|---------|---------|
|`Example.formOnLoad`|Form OnLoad|
|`Example.attributeOnChange`|Field OnChange|
|`Example.formOnSave`|Form OnSave|


The steps also work with any JavaScript web resource that's registered as a form event handler. Use the name of your web resource and trigger its event when the steps refer to the sample.

## Confirm that the published script works

Before you create an override, confirm the current behavior of the published web resource:

1. Open the model-driven app in Microsoft Edge.
1. Open an existing account record or create a new one.
1. Confirm that a form notification similar to the following message appears for five seconds:

   `<Your Name>: Your JavaScript code in action!`

This step confirms that the form loads the web resource and calls the `Example.formOnLoad` event handler.

## Set up Local Overrides

You only need to select an overrides folder the first time you use Local Overrides in a Microsoft Edge browser profile.

1. With the account form open, press <kbd>F12</kbd> or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> to open DevTools.
1. Select the **Sources** tool.
1. In the **Navigator** pane, select the **Overrides** tab. If the tab isn't visible, select **More tabs**, and then select **Overrides**.
1. Select **Select folder for overrides**.
1. Select the empty folder you created for overrides, and then select **Select Folder**.
1. When DevTools requests full access to the folder, select **Allow**.

   :::image type="content" source="clientapi/media/debug-javascript-webresources/allow-devtools-full-access-to-overrides-folder.png" alt-text="Screenshot of the DevTools prompt requesting full access to the Local Overrides folder.":::

1. Confirm that **Enable Local Overrides** is selected.

   :::image type="content" source="clientapi/media/debug-javascript-webresources/local-overrides-enabled.png" alt-text="Screenshot of the Sources tool Overrides tab after an overrides folder is selected, showing Enable Local Overrides selected.":::

## Enable bypass for network for service workers

> [!IMPORTANT]
> Enabling **Bypass for network** ensures that DevTools Local Overrides are applied by preventing Service Workers from serving cached responses. If you don't do this step, local overrides won't work with model-driven apps.

1. In DevTools, select the **Application** tab.

   If the tab isn't visible, select **+** (More tabs) and then **Application**.

1. In the left navigation pane, select **Service Workers**.
1. Select **Bypass for network** to force requests to bypass the Service Worker and use the network instead.

   :::image type="content" source="clientapi/media/debug-javascript-webresources/bypass-service-workers.png" alt-text="Screenshot of the Service Workers pane with Bypass for network selected.":::

1. Refresh the page to apply the change.


## Create an override for the web resource

Use the **Network** tool to find the JavaScript file loaded by the account form:

1. Select the **Network** tool.
1. If network activity isn't being recorded, select **Record network log**.
1. Refresh the page so that the form loads the web resource again.
1. In the **Filter** box, start typing the name of the web resource, such as: `example_form-script.js`.
1. In the list of network requests, right-click `example_form-script.js`, and then select **Override content**.

   :::image type="content" source="clientapi/media/debug-javascript-webresources/select-override-content.png" alt-text="Screenshot of the Network tool filtered for example_form-script.js with the Override content command selected.":::

1. Select the **Sources** tool, and then select the **Overrides** tab.
1. Expand the folders that DevTools created, and then select `example_form-script.js`.

   :::image type="content" source="clientapi/media/debug-javascript-webresources/form-script-in-overrides-tab.png" alt-text="Screenshot of example_form-script.js in the Overrides tab with the purple override indicator.":::

   DevTools copies the web resource into the overrides folder. A purple dot on the file icon indicates that DevTools has overridden the resource.

> [!TIP]
> You can also create the override from the **Page** tab in the **Sources** tool. Locate the web resource, right-click it, and then select **Override content**.

## Verify that Microsoft Edge loads the local copy

Make a change that's easy to recognize so that you can confirm the override is working:

1. In the DevTools editor, find the following line:

   ```javascript
   const message = `${currentUserName}: Your JavaScript code in action!`;
   ```

1. Replace it with this line:

   ```javascript
   const message = `${currentUserName}: Local override in action!`;
   ```

   > [!NOTE]
   > If you try pasting code into the DevTools editor, you see this dialog. You need to type `allow pasting` and select **Allow** to continue. This dialog doesn't appear if you type changes directly.
   >
   > :::image type="content" source="clientapi/media/debug-javascript-webresources/do-you-trust-this-code-dialog.png" alt-text="Screenshot of the DevTools paste warning dialog with the Allow button.":::

1. Change the notification duration from `5000` to `15000`.
1. Press <kbd>Ctrl</kbd>+<kbd>S</kbd> to save the local file.
1. Refresh the account form.
1. Confirm that the notification displays **Local override in action!** and stays visible for 15 seconds.

   :::image type="content" source="clientapi/media/debug-javascript-webresources/local-override-in-action.png" alt-text="Screenshot of the account form notification showing Local override in action.":::

The changed message and duration confirm that Microsoft Edge loaded the local override instead of the published web resource.

## Debug the event handlers

After you confirm that the override works, use the DevTools debugger to investigate the script.

### Debug the form OnLoad event

1. In the **Sources** tool, open the overridden `example_form-script.js` file.
1. Select the line number for this statement to set a breakpoint:

   :::image type="content" source="clientapi/media/debug-javascript-webresources/debug-formonload.png" alt-text="Screenshot of the DevTools editor with a breakpoint in the Example.formOnLoad event handler.":::

1. Refresh the account form.
1. When script execution pauses, use the **Scope** pane to inspect `executionContext` and `formContext`.

   :::image type="content" source="clientapi/media/debug-javascript-webresources/inspect-scope-pane.png" alt-text="Screenshot of the DevTools Scope pane showing executionContext and formContext values.":::

1. Step through the function and observe the call to `setFormNotification`.
1. Select **Resume script execution** to continue.

### Debug the Account Name OnChange event

1. Set a breakpoint on this statement in `Example.attributeOnChange`:

   ```javascript
   const accountName = formContext.getAttribute("name").getValue();
   ```

1. In the account form, change **Account Name**, and then move focus away from the column to trigger the **On Change** event.
1. When execution pauses, inspect the value of `accountName`.

   :::image type="content" source="clientapi/media/debug-javascript-webresources/debug-onchange.png" alt-text="Screenshot of DevTools paused in the Example.attributeOnChange event handler while inspecting accountName.":::

1. Use an account name that contains `Contoso`, and step through the function to observe how the script sets the Website, Main Phone, and Description values.

### Debug the form OnSave event

1. Set a breakpoint on the `Xrm.Navigation.openAlertDialog` statement in `Example.formOnSave`.
1. Save the record.
1. When execution pauses, inspect the call stack to confirm that the form **On Save** event called the expected function.

   :::image type="content" source="clientapi/media/debug-javascript-webresources/debug-onsave.png" alt-text="Screenshot of the DevTools debugger call stack paused in the Example.formOnSave event handler.":::

1. Resume script execution and confirm that the alert dialog opens.

You can edit and save the override whenever you want to test a possible fix. Refresh the form to test changes to code that runs when the form loads. Trigger the relevant form or column event to test other event handlers. Use the **Console** tool to review errors and log output.

## Compare the override with the published web resource

To confirm whether a problem is caused by your local changes:

1. In the **Sources** tool, select the **Overrides** tab.
1. Clear **Enable Local Overrides**.
1. Refresh the account form and test the event again.

Microsoft Edge now loads the published web resource from the server. Select **Enable Local Overrides** and refresh the form to resume using the local copy.

## Finish troubleshooting

Local override files aren't connected to the web resource in Dataverse or to the source files for your solution.

1. Copy the changes you want to keep from the override file into the source file you use to maintain the web resource.
1. Use your normal development and deployment process to update and publish the JavaScript web resource.
1. Test the published web resource with **Enable Local Overrides** cleared.
1. When you no longer need the override configuration, select **Clear configuration** in the **Overrides** tab.

> [!CAUTION]
> Don't treat the file in the overrides folder as the source file for the web resource. Preserve any changes you want to keep before you clear the configuration or delete local override files.

## Troubleshoot Local Overrides

The following are problems you might encounter when using Local Overrides.

### The web resource doesn't appear in the Network tool

Confirm that the Network tool is recording, clear any filters, and refresh the form. The form must load the web resource before it appears. Also confirm that the JavaScript library is added to the form and that the form customizations are published.

### The Override content command isn't available

Return to the **Sources** tool and confirm that you selected an overrides folder, allowed DevTools to access it, and selected **Enable Local Overrides**. Then refresh the form and try again.

### The form still uses the published script

Keep DevTools open, confirm that **Enable Local Overrides** is selected, and verify that the web resource has a purple dot in the **Network** or **Sources** tool. Save the override, and then refresh the form.

### A breakpoint isn't reached

Confirm that you set the breakpoint in the overridden file and that it appears enabled. Trigger the event associated with that function: refresh the form for **On Load**, change the configured column for **On Change**, or save the record for **On Save**. Also check the **Console** tool for a syntax error that prevents the script from loading.

## Related information

- [Override webpage resources with local copies (Overrides tab)](/microsoft-edge/devtools/javascript/overrides)
- [Sources tool overview](/microsoft-edge/devtools/sources/)
- [Debug JavaScript](/microsoft-edge/devtools/javascript/)
- [Client scripting using JavaScript](client-scripting.md)
- [JavaScript web resources](script-jscript-web-resources.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
