---
title: "Write Your First Client Script in Model-Driven Apps"
description: "Learn to write JavaScript client scripts in model-driven apps. Follow step-by-step instructions to create, upload, and test your first custom script."
author: sriharibs-msft
ms.author: srihas
ms.date: 10/30/2026
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
# Write your first client script in model-driven apps

Learn how to write your first JavaScript client script in model-driven apps. This walkthrough shows how to create a script, upload it as a web resource, attach it to form and column events, and test it so you can add custom business logic to your forms.

## Objective

After completing this walkthrough, you know how to use JavaScript code in model-driven apps. This process involves the following high-level steps:

- Locate or create a solution to add your work to
- Write JavaScript code to address a business issue
- Upload your code as a web resource
- Associate your web resource to a form
- Configure form and field events
- Test your code

> [!NOTE]
> To review and verify the completed walkthrough, download the [JavaScriptWebResourceExampleSolution_1_0_managed.zip](https://go.microsoft.com/fwlink/?LinkId=2378308&clcid=0x9). Install this managed solution and review the Account Management app it contains.

## Step 1: Locate or create a solution

Use solutions to transport customizations from one environment to another. Write and test your JavaScript code in a development environment as part of an unmanaged solution. When you finish testing, export the solution as a managed solution and import or install it in your production environment.

An existing solution might already be available for you to use. The model-driven app you want to customize with your script should already be part of a solution. You can edit that solution or create a new solution that depends on another existing solution.

### To create a new solution

1. Go to [Power Apps](https://make.powerapps.com).
1. In the left navigation pane, select **Solutions**, and then select **New solution**.
1. In the fly-out dialog, enter a **Display name**, **Name**, and **Publisher**.

   Most companies have an existing publisher that they always use. Use that publisher. If you're the first person, create your own publisher. 

   Select **New Publisher** to open the **New Publisher** dialog. In this walkthrough, use a publisher with this definition:

   :::image type="content" source="media/create-example-publisher.png" alt-text="Screenshot of the New Publisher form with information for Example Publisher.":::

   Notice the **Prefix** value. This value should identify your company. In this case, use `example`.

   This solution is the one you use in this walkthrough.

   :::image type="content" source="media/first-client-script-solution.png" alt-text="Screenshot of the solution form for the First Client Script Solution.":::

1. Locate or add a model-driven app to your solution.

   A new solution doesn't include any model-driven apps. You need to add an existing model-driven app or create a new one.

   > [!NOTE]
   > For the purpose of this walkthrough, make sure the app includes the Account table. The scripts and instructions below expect fields found in a form for the Account table.

   **Option A: Add an existing model-driven app to your solution**
   
   1. In your solution, select **Add existing** > **App** > **Model-driven app**.

   :::image type="content" source="media/add-existing-model-driven-app.png" alt-text="Screenshot of the menu to add an existing model-driven app to a solution.":::

   1. Select an existing app and select **Add**.

   **Option B: Create a new model-driven app in your solution**

   In your solution, select **New** > **App** > **Model-driven app**.

   See the [Build your first model-driven app](../../../maker/model-driven-apps/build-first-model-driven-app.md) tutorial. Create an app that includes the Account table.


## Step 2: Write your JavaScript code

The first step is to identify the business problem you want to address by using client scripting. When you identify the problem, write your JavaScript code containing the custom business logic that addresses your business problem.

Model-driven apps don't provide a JavaScript editor. Use an external authoring tool that provides features to specifically support editing JavaScript files, such as [Notepad++](https://notepad-plus-plus.org/), [Visual Studio Code](https://code.visualstudio.com/docs/languages/javascript), or [Microsoft Visual Studio](/visualstudio/javascript/javascript-in-visual-studio).

This walkthrough uses the following JavaScript code:

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

Copy this code into a text file and save it as `form-script.js`.


### Detailed code explanation

Let's look at the code in detail:

- **Define namespace**: The code starts by defining a namespace for your custom script. As a best practice, always create namespaced JavaScript libraries to avoid having your functions overridden by functions in another library.

    ```JavaScript
   window.Example ??= {};
    ``` 

   In this case, you can use all the functions defined in this library as `Example.[functionName]`. Choose a namespace that matches your solution publisher name.

- **Define constants**: The following section defines some constants to use in the script. You can access context information globally by using the [Xrm.Utility.getGlobalContext](reference/xrm-utility/getGlobalContext.md) method.

    ```JavaScript
    const notificationId = "_myUniqueId";
    const currentUserName = Xrm.Utility.getGlobalContext().userSettings.userName;
    const message = `${currentUserName}: Your JavaScript code in action!`;
    ```

- **Function to execute on the OnLoad event**: This section contains the function that executes when the account form loads. For example, when you create a new account record or when you open an existing account record.

   The `Example.formOnLoad` function uses the `executionContext` parameter to get the `formContext` object. When you attach your code by using the form event later, select the option to pass the [execution context](clientapi-execution-context.md) to this function.

   This function displays a form level notification by using the [formContext.ui.setFormNotification](reference/formContext-ui/setFormNotification.md) method.

   Finally, this function uses the JavaScript [setTimeOut method](https://developer.mozilla.org/docs/Web/API/setTimeout) to delay the execution of the [formContext.ui.clearFormNotification](reference/formContext-ui/clearFormNotification.md) method to clear the notification after 5 seconds.

    ```JavaScript
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
    ```

- **Function to execute on the OnChange event**: Associate the `Example.attributeOnChange` function with the **Account Name** column in the account form so that it gets executed **only** when you change the account name value.

    This function performs a case-insensitive search for `Contoso` in the account `name`, and if present, sets values for the `websiteurl`, `telephone1`, and `description` columns in the account form.

    ```JavaScript
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
    ```

- **Function to execute on the OnSave event**: The `Example.formOnSave` function displays an alert dialog box by using the [Xrm.Navigation.openAlertDialog](reference/xrm-navigation/openalertdialog.md) method. This dialog box displays a message with an **OK** button. The user can close the alert by selecting **OK**.

    > [!NOTE]
    > This function doesn't use the execution context because the **Xrm.Navigation.** methods don't require it.

    ```JavaScript
    // Code to run in the form OnSave event
    window.Example.formOnSave = () => {
        // Display an alert dialog
        Xrm.Navigation.openAlertDialog({ text: "Record saved." });
    };
    ```

## Step 3: Upload your code as a web resource

Now that your code is ready, upload it into your solution.

1. In your solution, select **New** > **More** > **Web resource**.

   :::image type="content" source="media/add-new-web-resource-to-solution.png" alt-text="Screenshot of the menu to add a new web resource to your solution.":::

1. In the **New web resource** dialog, select **Choose file** and select the `form-script.js` file you saved earlier.
1. Enter the **Display name**, **Name**, and optionally a **Description**. Ensure the **Type** is **JavaScript (JS)**.

   :::image type="content" source="media/create-example-form-script-web-resource.png" alt-text="Screenshot of the New web resource dialog to create the example form script.":::

   > [!NOTE]
   > - The **Name** has a prefix that matches the solution publisher customization prefix. There are other ways to create web resources, but creating a web resource this way ensures that the web resource is part of your solution.
   > - The name of the web resource is `example_form-script.js`.

## Step 4: Associate your web resource to a form

1. In your solution, select **Objects** > **Apps** > **Your App** and select **Edit**.

   :::image type="content" source="media/edit-account-example-app.png" alt-text="Screenshot of the option to edit the model-driven app in the solution.":::

1. Expand **Account** and select the **Account form**. Select the ellipses (**...**) to the right of the **Information** form and select **Edit**.

   :::image type="content" source="media/edit-account-information-form.png" alt-text="Screenshot of the option to edit the account Information form in the app.":::

1. In the left navigation, select **Form Libraries** and select **Add library**.

   :::image type="content" source="media/add-library-to-form.png" alt-text="Screenshot of the Form Libraries pane with the Add library option.":::

1. In the **Add JavaScript Library** dialog, search for the JavaScript web resource you created by name: `Example Script`.

   :::image type="content" source="media/add-javascript-library-dialog.png" alt-text="Screenshot of the Add JavaScript Library dialog used to select the web resource.":::

1. Select the **Example Script** web resource and select **Add**.

## Step 5: Configure form and field events

1. Select the **Events** tab.

   :::image type="content" source="../media/form-event-handlers.png" alt-text="Screenshot of the form event handlers on the Events tab.":::

### Configure form On Load event

1. Select **On Load** event handler and select **+ Event Handler**.

   :::image type="content" source="media/configure-form-onload-handler.png" alt-text="Screenshot of configuring the form On Load event handler.":::

   Ensure that the following settings are correct:

      - The **Event Type** is **On Load**.
      - The **example_example-form-script** library is selected.

   1. Enter the name of the function in the **Function** field. In this case, enter `Example.formOnLoad`.
   1. Select **Pass execution context as first parameter**.
   1. Select **Done**.

### Configure form On Save event

1. Select the **On Save** event handler, and then select **+ Event Handler**.

   :::image type="content" source="media/configure-form-onsave-handler.png" alt-text="Screenshot of configuring the form On Save event handler.":::

   Ensure that the following settings are correct:

      - The **Event Type** is **On Save**.
      - The **example_example-form-script** library is selected.

    1. Type the name of the function in the **Function** field. In this case, enter `Example.formOnSave`.
       > [!NOTE]
       > You don't need to select **Pass execution context as first parameter** for this function because it doesn't use it.
    1. Select **Done**.

### Configure field On Change event

1. Select the **Account Name** field and the **Events** tab.

   :::image type="content" source="media/select-account-name-events.png" alt-text="Screenshot of the Events tab for the selected Account Name field.":::

1. Select the **On Change** event handler and select **+ Event Handler**.

   :::image type="content" source="media/configure-field-onchange-handler.png" alt-text="Screenshot of configuring the On Change event handler for the Account Name field.":::

   Ensure that the following settings are correct:

      - The **Event Type** is **On Change**.
      - The **example_example-form-script** library is selected.

    1. Enter the name of the function in the **Function** field. In this case, `Example.attributeOnChange`.
    1. Select **Pass execution context as first parameter**.
    1. Select **Done**.

### Save and publish your changes

**Save** the form and select **Publish**.

## Step 6: Test your code

Refresh your browser to ensure your changes take effect in your model-driven apps instance.

To test your code:

1. Go to [Power Apps](https://make.powerapps.com).
1. In the left navigation, select **Apps**.
1. Open the model-driven app you just edited, or select it and select **Play**.

   :::image type="content" source="media/open-app-to-test.png" alt-text="Screenshot of opening the model-driven app to test the client script.":::

### Test form On Load function

1. Select any account record in the list to open it.
1. Verify that the notification appears.

   :::image type="content" source="media/form-onload-notification.png" alt-text="Screenshot of the form notification displayed when the account form loads.":::

1. Verify the notification disappears in 5 seconds.

### Test field On Change function

1. Edit the Account Name to include "Contoso" in the name and move to the next column by pressing TAB.
1. Verify the expected values set to the **Main Phone**, **Website**, and **Description** columns.

   :::image type="content" source="media/field-onchange-test.png" alt-text="Screenshot of column values set by the client script when the account name changes.":::

### Test form On Save function

1. Select **Save**.
1. Verify that the alert dialog displays the message you configured in your code. 

   :::image type="content" source="media/form-onsave-test.png" alt-text="Screenshot of the alert dialog displayed when the account form is saved.":::

1. Select **OK** to close the alert.


## Next steps

Learn how to debug your client-side scripts by using browser developer tools.

> [!div class="nextstepaction"]
> [Debug JavaScript web resources using Local Overrides](../debug-javascript-webresources.md)

### Related articles

[Debug JavaScript code for model-driven apps](debug-JavaScript-code.md)<br />
[Events in forms and grids in model-driven apps](events-forms-grids.md)<br />
[Form OnLoad event](reference/events/form-onload.md)<br />
[Form OnSave event (Client API reference) in model-driven apps](reference/events/form-onsave.md)<br />
[Column OnChange event (Client API reference)](reference/events/attribute-onchange.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
