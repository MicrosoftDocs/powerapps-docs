---
title: Working with the PDF function (Experimental)
---

# Intro

The PDF function allows you to generate a PDF document from the contents of a screen or certain types of controls. You can take the generated PDF and pass it to action connectors such as the Office 365 Outlook connector, or pass it to a Power Automate flow to achieve automation scenarios. You can also enable app users to download the generated PDF where they can then store or print a physical copy on an available printer.

In this article, we'll learn how to use the PDF function to create a PDF and use the generated PDF in several different ways.

# Prerequisites

-   [Sign up](https://docs.microsoft.com/en-us/powerapps/maker/signup-for-powerapps) for Power Apps, and then [sign in](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) by providing the same credentials that you used to sign up.

-   Create an app or open an existing app in Power Apps. [Learn more about creating apps.](https://learn.microsoft.com/power-apps/maker/canvas-apps/create-blank-app)

# Enable the PDF feature ** Important**

-   This is an experimental feature.

<!-- -->

-   Experimental features aren't meant for production use and may have restricted functionality. These features are available before an official release so that customers can get early access and provide feedback. More information: [**Understand experimental, preview, and deprecated features in Power Apps**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/working-with-experimental-preview).

-   The behavior that this article describes is available only when the PDF function experimental feature in [**Settings &gt; Upcoming features &gt; Experimental**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/working-with-experimental-preview#controlling-which-features-are-enabled) is turned on (off by default).

-   Your feedback is very valuable to us - please let us know what you think in the [**Power Apps experimental features community forum**](https://powerusers.microsoft.com/t5/Power-Apps-Experimental-Features/bd-p/PA_ExperimentalFeatures).

The PDF function will be disabled/not available by default while in an experimental phase. The setting will need to be enabled manually using the settings toggle switch. To enable the feature:

1.  Open a [new](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/data-platform-create-app) or an [existing](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/edit-app) app in Power Apps Studio. [Learn more about creating apps](https://learn.microsoft.com/power-apps/maker/canvas-apps/create-blank-app) or [create an app from a template](https://learn.microsoft.com/power-apps/maker/canvas-apps/get-started-test-drive).

2.  Select **Settings** at the top.

3.  Select **Upcoming features**.

4.  Under the **Experimental** tab, select **PDF function** to turn on this feature.

![](media/image1.png)

The PDF function is now available to use in Power Apps Studio.

# Use the PDF function to generate a PDF

You can use the PDF function in any [behavior property](https://learn.microsoft.com/power-apps/maker/canvas-apps/working-with-formulas-in-depth) to generate a PDF. In the example below, we'll use the PDF function in the *OnSelect* property of a button, but you can also use *OnVisible*, *OnHidden*, or any other behavior property.

1.  Select an existing button or add a new button to your canvas app.

2.  In the *OnSelect* property of the button, enter the PDF Function and enter the target of the PDF function as a parameter. In this example, we'll target the screen. In our example, the name of the Screen is *SubmitInspectionScreen*. The name of your screen may be different. Enter the formula:

*PDF(SubmitInspectionScreen);*

![A screenshot of the Canvas app designer interface  Button4 shows as selected on the canvas and in the tree view  The property drop down has been set to OnSelect  and PDF SubmitInspectionScreen ](media/ appears in the formula bar. .png)

3.  Save and publish the app.

4.  Play the app.

5.  Select the button you added. When you select the button, the PDF is generated and stored in memory for future use.

The PDF function can only target content on the currently visible screen. You can pass in the entire screen as we are doing in this example, or you can limit what content you pass in by specifying a container or gallery. [Learn more about PDF function targets here.](https://learn.microsoft.com/power-platform/power-fx/reference/function-pdf#syntax)

**Note**

-   These examples work best when using an app with mutliple controls.

-   *SubmitInspectionScreen* is the name of the screen in this example. If the name of the screen where you've placed your button is not *SubmitInspectionScreen*, enter the name of the screen where you've added the button.

-   Note that in order see the generated PDF, additional steps must be taken. See the steps below.

# Work with the generated PDF

## Method 1: Using the PDF Viewer control

In this example, we'll view the generated PDF using the PDF Viewer control.

1.  In the canvas app used in the previous example, select the button created in the previous steps or add a new button.

2.  In the button's *OnSelect* property, enter the formula:

*Set(myPDF, PDF(SubmitInspectionScreen));*

![A screenshot of the Canvas app designer interface  Button4 shows as selected on the canvas and in the tree view  The property drop down has been set to OnSelect  and Set myPDF  PDF SubmitInspectionScreen  ](media/ appears in the formula bar. .png)

6.  Select the Insert menu and add a PDF Viewer control.

7.  Select the *Document* property from the properties drop down menu and enter*myPDF* in the formula bar.

![A screenshot of the Canvas app designer interface  PdfViewer1 shows as selected on the canvas and in the tree view  The property drop down has been set to Document  and myPDF appears in the formula bar  ](media/image4.png)

8.  Save and publish the app.

9.  Play the app.

10. Select the button you added. When you select the button, the PDF is generated and stored in the variable, and is visible in the PDF viewer control.

Note

-   The PDF viewer control will appear as a black shape inside the generated PDF. To exclude the PDF Viewer control from the generated PDF, place the desired PDF content inside of a container or gallery and target that instead of the screen. For example, *PDF(Container1)* or*PDF(Gallery1).*

## Method 2: Use an action connector 

In this example, we'll generate a PDF which we then attach and send as an email. In this example, we use the Office 365 Outlook connector to send the email. [Learn more about the Office 365 Outlook connector.](https://learn.microsoft.com/connectors/office365/)

1.  In the canvas app used in the previous example, select the button created in the previous steps or add a new button.

2.  In the button's *OnSelect* property, enter the formula:

*Office365Outlook.SendEmailV2(*

*"sample@email.com",*

*"New Safety Inspection"*

*"A new safety inspection has been submitted for your review. Please see attached.",*

*{*

*Attachments: Table(*

*{*

*Name: "submittedInspection.pdf",*

*ContentBytes: PDF(SubmitInspectionScreen)*

*}*

*)*

*}*

*);*

![A screenshot of the Canvas app designer interface  Button4 shows as selected on the canvas and in the tree view  The property drop down has been set to OnSelect  and the following formula appears in the formula bar  Office365Outlook SendEmailV2   quot](media/sample@email.com&quot.png ", &quot")

3.  Save and publish the app.

4.  Play the app.

5.  Select the button you added. When you select the button, the PDF is generated and an email is sent to the specified email address with the generated PDF included as an attachment.

Note

-   A sample email address has been included in this formula example.

## Method 3: Use in a Power Automate flow

In this example, we'll generate a PDF which then gets passed to a Power Automate flow for storage. In this example, we use the SharePoint connector to store the PDF in a document library. [Learn more about the SharePoint connector.](https://learn.microsoft.com/connectors/sharepointonline/)

1.  In the canvas app used in the previous example, select the button created in the previous steps or add a new button.

2.  From the left pane, select the Power Automate button and select *Create new flow.*

![A screenshot of the Power Automate pane in the canvas app designer  No flows have been added to the app  so a purple  quot](media/Create new flow&quot.png " button is shown. ")

3.  Select *Create from blank*.

![A screenshot of the top of the flow designer in the canvas app designer  The purple  quot](media/+ Create from blank&quot.png " button is shown. ")

4.  For this example, we'll need the Power Apps V2 trigger. To add it, select the ellipses on the right side of the Power Apps trigger and select Delete.

![A screenshot of the flow designer in the canvas app designer  The Power Apps v1 trigger is shown  with the context menu open from the ellipsis on the right side of the trigger  The Delete option is highlighted  ](media/image8.png)

5.  Search for PowerApps (V2) and select the trigger to add it.

![A screenshot of the flow designer in the canvas app designer  The phrase  quot](media/PowerApps (v2)&quot.png " is shown in the search input field. The filtered search results show the Power Apps V2 trigger under the Triggers tab. ")

6.  Select the Power Apps V2 trigger to expand the flow node. Select *Add an input*.

![A screenshot of the flow designer in the canvas app designer  The Power Apps v2 trigger is shown in its expanded state  with  quot](media/+ Add an input&quot.png " option shown. ")

7.  Choose the File type.

![A screenshot of the flow designer in the canvas app designer  The Power Apps v2 trigger is shown in its expanded state  with a selection of input options shown including the File input type  ](media/image11.png)

8.  Select *Add an input* and choose the Text type. Rename the input to File name and update the description to "Please enter the name of the file."

![A screenshot of the flow designer in the canvas app designer  The Power Apps v2 trigger is shown in its expanded state  now showing the two inputs configured as described in the step  ](media/image12.png)

9.  Select *+New step* to add an action, and search for SharePoint. In the list of available SharePoint actions, select *Create file.*

![A screenshot of the flow designer in the canvas app designer  The  New step menu is expanded with SharePoint typed into the search input field  The create file action is shown highlighted int he filtered search results  ](media/image13.png)

10. Choose a site from the Site Address drop down or select Enter custom value to paste the URL to a site you have permission to add files to. Select the folder icon on the right for Folder Path and select a document library from the list which you have permissions to add files to.

11. In the File Name input area, select File name from the Dynamic Content menu, under PowerApps (V2). In the File Content input area, select File Content.

![A screenshot of the flow designer in the canvas app designer  A new SharePoint node has been added to the flow  The Site address and floder path fields ahve been completed but are obfuscated in the screenshot to protect sensitive information  The File Name and File Content fields show placeholders for data dynamically sent from Power Apps   the two inputs File name and File content from the Power Apps V2 trigger in the node above  A Dynamic Content callout showing the menu containing those placeholders is shown below and to the right of the File Name input field  ](media/image14.png)

12. Select Save.

13. Select the X in the upper right corner of the dialog to close the modal.

![A screenshot of the flow designer in the canvas app designer  The top of the window is shown with the  quot](media/X&quot.png " to close the window on the far right. ")

14. The Power Automate pane refreshes, and the newly created flow now appears.

![A screenshot of the Power Automate Pane in the Canvas app designer  The pane now shows the newly created flow from the previous steps  named PowerAppsV2  gt](media/Create File..png)

15. Select the button on the canvas. In the button's *OnSelect* property, enter the formula:

*'PowerAppV2-&gt;Createfile'.Run(*

*"NewInspectionReport.pdf",*

*{*

*file: {*

*name: "NewInspectionReport.pdf",*

*contentBytes: PDF(InspectionDetails)*

*}*

*}*

*);*

![A screenshot of the Canvas app designer interface  Button4 is selected  The property drop down has been set to OnSelect  and the following formula appears in the formula bar    39](media/PowerAppV2-&gt.png "Createfile&#39")

16. Save and publish the app.

17. Play the app.

18. Select the button you added. When you select the button, the Power Automate flow runs and adds the generated PDF into the document library.

### See also

[PDF function in Power Apps (experimental)](https://learn.microsoft.com/power-platform/power-fx/reference/function-pdf)
