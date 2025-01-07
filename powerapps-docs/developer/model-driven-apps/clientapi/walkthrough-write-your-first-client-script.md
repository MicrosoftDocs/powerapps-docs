---
title: "Walkthrough: Write your first client script in model-driven apps"
description: "This walkthrough will help you write your first client script in model-driven apps."
author: sriharibs-msft
ms.author: srihas
ms.date: 10/18/2022
ms.reviewer: jdaly
ms.topic: how-to
applies_to: "Dynamics 365 (online)"
ms.subservice: mda-developer
search.audienceType: 
  - developer
contributors: 
  - JimDaly
  - caburk
---
# Walkthrough: Write your first client script

Ready to write your first client script to see things in action? Lets get started. We'll keep it simple.

## Objective

After completing this walkthrough, you will know how to use JavaScript code in model-driven apps, which involves the following steps at a high level:

- Locate or create a solution to add your work to
- Write JavaScript code to address a business issue
- Upload your code as a web resource
- Associate your web resource to a form
- Configure form and field events
- Test your code

## Step 1: Locate or create a solution

Solutions are the way that customizations can be transported from one environment to another. You should write and test your Javascript code in a development environment as part of an unmanaged solution. When you have finished testing, export the solution as a managed solution and import/install it in your production environment.

There may already be an existing solution that you should use. The model-driven app you want to customize with your script should already be part of a solution. You may edit that solution or create a new solution that depends on another existing solution.

### To create a new solution:

1. Navigate to [Power Apps](https://make.powerapps.com).
1. In the left navigation pane, select **Solutions** and then select **New solution**.
1. In the fly-out dialog, specify **Display name**, **Name**, and **Publisher**.

   Most companies will have an existing publisher that they will always use. You should use that publisher. If you are the very first person, you get to create your own. 

   Click **New Publisher** to open the **New Publisher** dialog. In this walkthrough, we will use a publisher with this definition:

   :::image type="content" source="media/create-example-publisher.png" alt-text="Form to create a new publisher with information for Example Publisher":::

   Notice the **Prefix** value. This should be something that identifies your company. In this case, we are using `example`.

   This is the solution we will use in this walkthrough

   :::image type="content" source="media/first-client-script-solution.png" alt-text="Solution form for the First Client Script Solution":::

1. Locate or add a model-driven app to your solution.

   A new solution will not have any model-driven apps included in it. You will need to add an existing model-driven app or create a new one.

   > [!NOTE]
   > For the purpose of this walkthrough, make sure the app includes the Account table. The scripts and instructions below expects fields found in a form for the Account table.

   **Option A: Add an existing model-driven app to your solution**
   
   1. In your solution, select **Add existing** > **App** > **Model-driven app**.

   :::image type="content" source="media/add-existing-model-driven-app.png" alt-text="Add existing model-driven app":::

   1. Select an existing app and click **Add**.

   **Option B: Create a new model-driven app in your solution**

   In your solution, you can select **New** > **App** > **Model-driven app**.

   See the [Build your first model-driven app](../../../maker/model-driven-apps/build-first-model-driven-app.md) tutorial. Create an app that includes the Account table.


## Step 2: Write your JavaScript code

The first step is to identify the business issue you are trying to address using client scripting. Once you have identified it, you need to write your JavaScript code containing the custom business logic that addresses your business issue.

Model-driven apps do not provide a JavaScript editor. Use an external authoring tool that provides features to specifically support editing JavaScript files, such as [Notepad++](https://notepad-plus-plus.org/), [Visual Studio Code](https://code.visualstudio.com/docs/languages/javascript), or [Microsoft Visual Studio](/visualstudio/javascript/javascript-in-visual-studio).

This is the JavaScript code that this walkthrough uses:

```javascript
// A namespace defined for the sample code
// As a best practice, you should always define 
// a unique namespace for your libraries
var Example = window.Example || {};
(function () {
    // Define some global variables
    var myUniqueId = "_myUniqueId"; // Define an ID for the notification
    var currentUserName = Xrm.Utility.getGlobalContext().userSettings.userName; // get current user name
    var message = currentUserName + ": Your JavaScript code in action!";

    // Code to run in the form OnLoad event
    this.formOnLoad = function (executionContext) {
        var formContext = executionContext.getFormContext();

        // Display the form level notification as an INFO
        formContext.ui.setFormNotification(message, "INFO", myUniqueId);

        // Wait for 5 seconds before clearing the notification
        window.setTimeout(function () { formContext.ui.clearFormNotification(myUniqueId); }, 5000);
    }

    // Code to run in the column OnChange event 
    this.attributeOnChange = function (executionContext) {
        var formContext = executionContext.getFormContext();

        // Automatically set some column values if the account name contains "Contoso"
        var accountName = formContext.getAttribute("name").getValue();
        if (accountName.toLowerCase().search("contoso") != -1) {
            formContext.getAttribute("websiteurl").setValue("https://www.contoso.com");
            formContext.getAttribute("telephone1").setValue("425-555-0100");
            formContext.getAttribute("description").setValue("Website URL, Phone and Description set using custom script.");
        }
    }

    // Code to run in the form OnSave event 
    this.formOnSave = function () {
        // Display an alert dialog
        Xrm.Navigation.openAlertDialog({ text: "Record saved." });
    }
}).call(Example);
```

Copy this code into a text file and save it with the name: `Example-form-script.js`.


### Detailed code explanation

Let's look at the code in detail:

- **Define namespace**: The code starts by defining a namespace for your custom script. As a best practice, you should always create namespaced JavaScript libraries to avoid having your functions overridden by functions in another library.

    ```JavaScript
    var Example = window.Example || {};
    ``` 

   In this case, all the functions defined in this library can be used as `Example.[functionName]`. You should choose a namespace that matches your solution publisher name.

- **Define global variables**: The following section defines some global variables to be used in the script. Context information is available globally using the [Xrm.Utility.getGlobalContext](reference/xrm-utility/getGlobalContext.md) method.

    ```JavaScript
    // Define some global variables
    var myUniqueId = "_myUniqueId"; // Define an ID for the notification
    var currentUserName = Xrm.Utility.getGlobalContext().userSettings.userName; // get current user name
    var message = currentUserName + ": Your JavaScript code in action!";
    ```

- **Function to execute on the OnLoad event**: This section contains the function that will be executed when the account form loads. For example, when you create a new account record or when you open an existing account record.

   The `Example.formOnLoad` function uses the `executionContext` parameter to get the `formContext` object. When you attach your code with the form event later, you must remember to select the option to pass the [execution context](clientapi-execution-context.md) to this function.

   This function displays a form level notification using the [formContext.ui.setFormNotification](reference/formContext-ui/setFormNotification.md) method.

   Finally, this function uses the JavaScript [setTimeOut method](https://developer.mozilla.org/docs/Web/API/setTimeout) to delay the execution of the [formContext.ui.clearFormNotification](reference/formContext-ui/clearFormNotification.md) method to clear the notification after 5 seconds.

    ```JavaScript
    // Code to run in the form OnLoad event
    this.formOnLoad = function (executionContext) {
        var formContext = executionContext.getFormContext();

        // Display the form level notification as an INFO
        formContext.ui.setFormNotification(message, "INFO", myUniqueId);
        
        // Wait for 5 seconds before clearing the notification
        window.setTimeout(function () { formContext.ui.clearFormNotification(myUniqueId); }, 5000);        
    }
    ```

- **Function to execute on the OnChange event**: The `Example.attributeOnChange` function will be associated with the **Account Name** column in the account form so that it gets executed **only** when you change the account name value.

    This function performs a case-insensitive search for `Contoso` in the account `name`, and if present, sets values for the `websiteurl`, `telephone1`, and `description` columns in the account form.

    ```JavaScript
    // Code to run in the column OnChange event 
    this.attributeOnChange = function (executionContext) {
        var formContext = executionContext.getFormContext();

        // Automatically set some column values if the account name contains "Contoso"
        var accountName = formContext.getAttribute("name").getValue();
        if (accountName.toLowerCase().search("contoso") != -1) {
            formContext.getAttribute("websiteurl").setValue("https://www.contoso.com");
            formContext.getAttribute("telephone1").setValue("425-555-0100");
            formContext.getAttribute("description").setValue("Website URL, Phone and Description set using custom script.");
        }
    }
    ```

- **Function to execute on the OnSave event**: The `Example.formOnSave` function displays an alert dialog box using the [Xrm.Navigation.openAlertDialog](reference/xrm-navigation/openalertdialog.md) method. This dialog box displays a message with an **OK** button. The user can close the alert by clicking **OK**.

    > [!NOTE]
    > This function doesn't use the execution context because the **Xrm.Navigation.** methods don't require them.

    ```JavaScript
    // Code to run in the form OnSave event 
    this.formOnSave = function () {
        // Display an alert dialog
        Xrm.Navigation.openAlertDialog({ text: "Record saved." });
    }
    ```

## Step 3: Upload your code as a web resource

Now that your code is ready, you need to upload it into your solution.

1. In your solution select **New** > **More** > **Web resource**

   :::image type="content" source="media/add-new-web-resource-to-solution.png" alt-text="Add a new web resource to your solution":::

1. In the **New web resource** dialog, click **Choose file** and select the `Example-form-script.js` file you saved earlier.
1. Type in the **Display name**, **Name**, and optionally a **Description**. Make sure the **Type** is **JavaScript (JS)**.

   :::image type="content" source="media/create-example-form-script-web-resource.png" alt-text="New web resource dialog to create example form script":::

   > [!NOTE]
   > - Notice how the **Name** has a prefix that matches the solution publisher customization prefix. There are other ways to create web resources, but creating a web resource this way ensures that the Web Resource is part of your solution.
   > - The name of the web resource is `example_example-form-script`.

## Step 4: Associate your web resource to a form

1. In your solution, select **Objects** > **Apps** > **Your App** and click **Edit**.

   :::image type="content" source="media/edit-account-example-app.png" alt-text="Edit the app in the solution":::

1. Expand **Account** and select the **Account form**, click the ellipses (**...**) to the right of the **Information** form and select **Edit**.

   :::image type="content" source="media/edit-account-information-form.png" alt-text="Edit the account information form":::

1. In the left navigation, select **Form Libraries** and click **Add library**.

   :::image type="content" source="media/add-library-to-form.png" alt-text="Add library to form":::

1. In the **Add JavaScript Library** dialog, search for the JavaScript web resource you created by name: `Example Script`.

   :::image type="content" source="media/add-javascript-library-dialog.png" alt-text="Add JavaScript Library dialog":::

1. Select the **Example Script** web resource and click **Add**.

## Step 5: Configure form and field events

1. Select the **Events** tab.

   :::image type="content" source="../media/form-event-handlers.png" alt-text="Form event handlers":::

### Configure form On Load event

1. Select **On Load** event handler and click **+ Event Handler**.

   :::image type="content" source="media/configure-form-onload-handler.png" alt-text="Configure form On Load handler":::

   Make sure that:

      - The **Event Type** is **On Load**.
      - The **example_example-form-script** library is selected.

   1. Type the name of the function in the **Function** field. In this case `Example.formOnLoad`.
   1. Select **Pass execution context as first parameter**.
   1. Click **Done**.

### Configure Form On Save event

1. Select **On Save** event handler and click **+ Event Handler**.

   :::image type="content" source="media/configure-form-onsave-handler.png" alt-text="Configure form On Save handler":::

   Make sure that:

      - The **Event Type** is **On Save**.
      - The **example_example-form-script** library is selected.

    1. Type the name of the function in the **Function** field. In this case `Example.formOnSave`.
       > [!NOTE]
       > It is not necessary to elect **Pass execution context as first parameter** for this function because it doesn't use it.
    1. Click **Done**

### Configure Field On Change event

1. Select the **Account Name** field and the **Events** tab.

   :::image type="content" source="media/select-account-name-events.png" alt-text="Select Account Name field events":::

1. Select the **On Change** event handler and click **+ Event Handler**.

   :::image type="content" source="media/configure-field-onchange-handler.png" alt-text="Configure field OnChange handler":::

   Make sure that:

      - The **Event Type** is **On Change**.
      - The **example_example-form-script** library is selected.

    1. Type the name of the function in the **Function** field. In this case `Example.attributeOnChange`.
    1. Select **Pass execution context as first parameter**.
    1. Click **Done**

### Save and publish your changes

**Save** the form an click **Publish**.

## Step 6: Test your code

It is recommended that you refresh your browser for the changes to take effect in your model-driven apps instance.

To test your code:

1. Navigate to [Power Apps](https://make.powerapps.com).
1. In the left navigation area select **Apps**.
1. Double-click the model-driven app you just edited, or select it and click **Play**.

   :::image type="content" source="media/open-app-to-test.png" alt-text="Open the app to test":::

### Test form On Load function

1. Click on any account record in the list to open it.
1. Verify that the notification appears.

   :::image type="content" source="media/form-onload-notification.png" alt-text="Notification on form load":::

1. Verify the notification disappears in 5 seconds.

### Test field On Change function

1. Edit the Account Name to include "Contoso" in the name and move to the next column by pressing TAB.
1. Verify the expected values set to the **Main Phone**, **Website**, and **Description** columns.

   :::image type="content" source="media/field-onchange-test.png" alt-text="Values set on field change":::

### Test form On Save function

1. Click **Save**.
1. Verify that the alert dialog with a message that you configured in your code. 

   :::image type="content" source="media/form-onsave-test.png" alt-text="Alert Dialog when form saved":::

1. Click **OK** to close the alert.


### Related articles

[Debug JavaScript code for model-driven apps](debug-JavaScript-code.md)<br />
[Events in forms and grids in model-driven apps](events-forms-grids.md)<br />
[Form OnLoad event](reference/events/form-onload.md)<br />
[Form OnSave event (Client API reference) in model-driven apps](reference/events/form-onsave.md)<br />
[Column OnChange event (Client API reference)](reference/events/attribute-onchange.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
