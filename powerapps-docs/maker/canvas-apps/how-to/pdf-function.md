---
title: Work with the PDF function (experimental) 
description: Learn to use the PDF function in Microsoft Power Apps to generate and work with a PDF file in your apps.
ms.date: 04/07/2023
ms.author: tashas
author: tashaev
ms.reviewer: mkaur
ms.topic: how-to
ms.custom: canvas, bap-template
search.audienceType:
  - maker
contributors:
    - tashaev
    - mduelae  
---

# Work with the PDF function (experimental)

The PDF function in Power Apps generates a PDF document from the contents of a screen or certain types of controls. You can pass the generated file to an action connector&mdash;for example, to send it in an email using the Office 365 Outlook connector&mdash;or to a Power Automate flow as part of an automation scenario.

> [!IMPORTANT]
>
> - This is an experimental feature. Experimental features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. [Understand experimental, preview, and retired features in canvas apps](../working-with-experimental-preview.md).
> - You must turn on the PDF function in [Settings &gt; Upcoming features &gt; Experimental](../working-with-experimental-preview.md#controlling-which-features-are-enabled). As an experimental feature, it's disabled by default.
> - Send your feedback in the [Power Apps experimental features community forum](https://powerusers.microsoft.com/t5/Power-Apps-Experimental-Features/bd-p/PA_ExperimentalFeatures).

## Turn on the PDF function

Since the PDF function is an experimental feature, it's turned off by default. To use it in your apps, you need to turn it on manually.

1. [Sign in to Power Apps](https://make.powerapps.com) and [create a canvas app](../create-blank-app.md) or open an existing app.

1. In Power Apps Studio, on the command bar, select **Settings**.

1. Select **Upcoming features**.

1. On the **Experimental** tab, turn on **PDF function**.

## Use the PDF function to generate a PDF file

In the following example, we use the PDF function in the `OnSelect` property of a button to generate a PDF file. You can also use the PDF function in `OnVisible`, `OnHidden`, or any other [behavior property](../working-with-formulas-in-depth.md).

1. Select an existing button or add a new button to your canvas app.

1. In the button's `OnSelect` property, add the PDF function and enter the target of the function as a parameter. Enter the formula: `PDF(SubmitInspectionScreen);`

    In this example, we're targeting the screen `SubmitInspectionScreen` to generate a PDF file from the contents of our sample app's Inspection screen. Replace it with the name of a screen in your app.

    :::image type="content" source="media/pdf/print-pdf-enter-formula-2.png" alt-text="Screenshot of adding the PDF function to a button's OnSelect property.":::

1. Select [**Save and publish**](../power-apps-studio.md#save).

Play the app and select the button you added. The PDF file is generated and stored in memory for future use. The following section suggests a few ways to work with the PDF file in your app.

The PDF function can only target the screen that's currently visible. You can pass the entire screen, as in our example, or enter [more parameters](/power-platform/power-fx/reference/function-pdf#syntax) to specify a container or gallery to limit the content to pass.

## Work with the generated PDF file

You can use the generated PDF file in many ways. Here are a few, using the example in the previous section.

### View the file with the PDF viewer control

1. In your canvas app, select the button that you created in the previous example or add a new button.

1. In the button's `OnSelect` property, enter the following formula, replacing `SubmitInspectionScreen` with the name of a screen in your app: `Set(myPDF, PDF(SubmitInspectionScreen));`

    :::image type="content" source="media/pdf/print-pdf-button-prop-3.png" alt-text="Screenshot of setting the OnSelect property of a button in a canvas app.":::

1. Select **Insert** > **PDF viewer (experimental)**.

1. From the [properties  list](../power-apps-studio.md#3--properties-list), select the **Document** property and then enter **myPDF** in the formula bar.

    :::image type="content" source="media/pdf/print-pdf-document-prop-4.png" alt-text="Screenshot of setting the Document property of a button in a canvas app.":::

1. Select [**Save and publish**](../power-apps-studio.md#save).

Play the app and select the button you added. The PDF file is generated, stored in the variable `myPDF`, and visible in the PDF viewer control.

The PDF viewer control appears as a black shape inside the generated PDF file. To exclude the control from the generated file, place the content you want to turn into a PDF file inside a container or gallery and target that instead of the screen; for example,`PDF(Container1)` or `PDF(Gallery1).`

### Use an action connector

In this example, we generate a PDF file that we send as an email attachment using the [Office 365 Outlook connector](/connectors/office365).

1. In your canvas app, select the button that you created in the previous example or add a new button.

1. In the button's `OnSelect` property, enter the following formula:

   ```
   Office365Outlook.SendEmailV2( 
      "sample@email.com", 
       "New Safety Inspection" 
       "A new safety inspection has been submitted for your review. Please see attached.", 
       { 
           Attachments: Table( 
                { 
                    Name: "submittedInspection.pdf", 
                    ContentBytes: PDF(SubmitInspectionScreen) 
                } 
            ) 
       } 
    ); 
   ```

    :::image type="content" source="media/pdf/print-pdf-onselect-button-5.png" alt-text="Screenshot of an email added to a button's OnSelect property.":::

1. Select [**Save and publish**](../power-apps-studio.md#save).

Play the app and select the button you added. The PDF file is generated, and an email is sent to the specified email address with the generated PDF file attached.

### Use in a Power Automate flow

In this example, we generate a PDF file and pass it to a Power Automate flow that stores the file in a document library using the [SharePoint connector](/connectors/sharepointonline). This example replaces the default PowerApps trigger in Power Automate with the PowerApps (V2) trigger.

#### Create a flow to use in your app

1. In your canvas app, select the button that you created in the previous example or add a new button.

1. In the [app authoring menu](..//power-apps-studio.md#5--app-authoring-menu), select **Power Automate** > **Create new flow**.

1. Select **Create from blank**.

1. To delete the default PowerApps trigger, select the trigger menu (**&hellip;**), and then select **Delete**.

    :::image type="content" source="media/pdf/print-pdf-delete-flow-8.png" alt-text="Screenshot of deleting the default PowerApps trigger in the Power Automate flow.":::

1. Search for and select **PowerApps (V2)**.

    :::image type="content" source="media/pdf/print-pdf-select-trigger-9.png" alt-text="Screenshot of selecting the PowerApps (V2) trigger.":::

1. Select the **PowerApps V2** trigger to expand the node, and then select **Add an input**.

    :::image type="content" source="media/pdf/print-pdf-add-input-10.png" alt-text="Screenshot of adding an input to the PowerApps (V2) trigger node.":::

1. Select **File** as the type of user input.

1. Select **Add an input** again, and then select **Text** as the type of user input.

1. Rename the input **File Name** and change the description to **Please enter the name of the file**.

    :::image type="content" source="media/pdf/print-pdf-add-input-12.png" alt-text="Screenshot of two user inputs in the PowerApps (V2) trigger node.":::
#### Add the SharePoint connector to the flow

1. Select **New step** to add an action. Search for **SharePoint** and select **Create file**.

    :::image type="content" source="media/pdf/print-pdf-create-file-13.png" alt-text="Screenshot of adding the SharePoint Create file connector to the flow.":::

1. In **Site Address**, select a SharePoint site that you have permission to add files to.

1. In **Folder Path**, select a document library that you have permission to add files to.

1. Select the **File Name** input. In the **Dynamic content** tab, select a file name under **PowerApps (V2)**.

1. Select the **File Content** input, and then select **File Content** in the list.

    :::image type="content" source="media/pdf/print-pdf-create-file-14.png" alt-text="Screenshot of selecting a file to save using the SharePoint Create file connector.":::
    
1. Select **Save**, and then select the **x** in the upper-right corner to close the Power Automate window.

1. The Power Automate pane refreshes, and the new PowerApps (V2) flow, **Create file**, appears in the list.

    :::image type="content" source="media/pdf/print-pdf-flow-created-16.png" alt-text="Screenshot of the flow in the Power Automate list.":::

#### Add the flow to a button in your app

1. Select the button in your app canvas. In the button's `OnSelect` property, enter the following formula, replacing the flow name and generated PDF file name with your own:

    ```
    'PowerAppV2->Createfile'.Run( 
       "NewInspectionReport.pdf", 
        {         
           file: { 
                name: "NewInspectionReport.pdf", 
                contentBytes: PDF(InspectionDetails) 
            }               
        } 
    );  
    ```

    :::image type="content" source="media/pdf/print-pdf-save-17.png" alt-text="Screenshot of the flow added to a button's OnSelect property.":::

1. Select [**Save and publish**](../power-apps-studio.md#save).

Play the app and select the button you added. The Power Automate flow runs and adds the generated PDF file into the document library.

### See also

[PDF function in Power Apps (experimental)](/power-platform/power-fx/reference/function-pdf)
