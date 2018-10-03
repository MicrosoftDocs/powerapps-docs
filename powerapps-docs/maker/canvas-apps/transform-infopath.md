---
title: Transform your InfoPath form to a canvas app | Microsoft Docs
description: Start to transform your InfoPath form to PowerApps with information about common scenarios and how to create these items in a canvas app.
author: richardriley99
manager: kvivek
ms.service: powerapps
ms.topic: article
ms.custom: canvas
ms.reviewer: anneta
ms.date: 04/05/2018
ms.author: rriley
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Transform your InfoPath form to PowerApps

Are you a builder of great things in InfoPath who's looking to learn how to deliver those great things on a more robust platform?

## Key advantages of PowerApps over InfoPath

Like most InfoPath power users, you've been using your unique skill set to build awesome forms for a while. You're very satisfied with your forms, but you also know their limitations: the &quot;classic&quot; feel, a less-than-ideal experience for mobile devices, the uncertainty of their future viability, and always being trapped in a box when it comes to connecting to other services without writing code.

The PowerApps team has heard these and many other challenges. They've worked hard to incorporate a better experience and enable you to create canvas apps by leveraging your existing business and technology skills. By using PowerApps, you can quickly build and deploy the right business solutions without writing code.

**PowerApps enable a powerful future**  
PowerApps is a Software as a Service (SaaS) platform that's designed to let you quickly build high-functioning apps that you can deploy to the web, SharePoint, Dynamics 365, Teams, Power BI, or a mobile device without any extra work. Because you can deploy them by just giving someone the URL to your published app, they're also just as easy to update.

**Share your apps**  
Have you ever tried to build an app and then publish it for iOS or Android devices? It's complicated. If you want to deploy a second app or update that existing one, your users must take a lot more steps. Not with PowerApps. Your users install PowerApps Mobile on their devices and sign in. Voila, they have all of the highly functional apps that you have shared with them. In the future, when you update those apps or push new apps out to them, those apps will show up on your users' devices. Mobile apps without the pain of managing devices is a big win for you and your business.

**Speaking of mobile**  
With PowerApps, you can leverage the power of the user's mobile device. You have access to acceleration, the camera, the compass, the connection information, and location signals: all from within your app. This opens up a whole world of possibilities for building apps to get work done. Of course, touch functionality is just automatic in PowerApps: nothing extra to code when you build your app.

**Get out of the box**  
With InfoPath, you normally work with data from one source. However, things got tricky if you wanted to update another source (such as a SharePoint list in another site collection) or connect to external services. Concepts such as code behind kept you awake at night. PowerApps is designed to allow you to work with multiple data sources and service connections in one app. Currently, [more than 200 connectors](connections-list.md#all-connectors) support a combination of on-premises and cloud data, including Microsoft Office 365 and Azure services such as Microsoft Flow and Dynamics 365. You can also connect to a multitude of third-party services such as Dropbox, Google, Salesforce, Slack, and other popular targets.

Now you can build solutions to scale where your users need to take you, not just where the original data lived.

## PowerApps and SharePoint: even better together

PowerApps is a great tool for making your SharePoint experience better in two ways. You have the option to either customize the forms for a SharePoint list or to create a standalone app for working with SharePoint data.

**Customizing a SharePoint form** is great if you want to customize how users add, view, or edit items in a list that they use for their everyday work. Clicking **Customize Forms** will create a single-screen &quot;forms app&quot; that will change modes (new/edit/view) based on context. SharePoint manages these apps; their permissions are the same as the list permissions for editing/viewing.

**Creating a PowerApps canvas app from SharePoint** allows you to run the app by itself on a mobile device. You can also embedd the app in a SharePoint page. Clicking this will create a three-screen app (browse list, view details, and create/update an item). The permission/sharing model for these apps isn't tied to SharePoint but instead is managed from PowerApps.

Now that you understand the difference between the two options, the following section will give you an overview of using each.

## SharePoint forms

The PowerApps and SharePoint teams have worked together to create a customization story for you to use with SharePoint. If you're like most InfoPath developers, you learned InfoPath to interact with SharePoint. SharePoint is great, but the default forms are a bit pedestrian and don't allow for customization or business logic without InfoPath. Well, that was the old way.

With PowerApps you can now customize your list forms as native functionality. And when you do so, you get the full power of PowerApps. In the screenshot below, you can see an example of a PowerApps form with a Power BI report embedded. The entire solution was done in less than 15 minutes.

![SharePoint integration](./media/transform-infopath/sharepoint-integration.png)

Another important feature of PowerApps is the ability to easily connect to another SharePoint site collection or a different environment from the same form. For example, do you want to make one form that displays and updates data from your SharePoint Online and SharePoint on-premises environment at the same time? No problem. If you install the [on-premises data gateway](gateway-management.md), you are up and running in a few minutes, connecting PowerApps, Power BI, Microsoft Flow, and Azure Logic Apps with your on-premises data. No changes to firewall rules are required. You can go a step further by connecting this app with Microsoft Flow.

## A standalone SharePoint app

Use this technique if, instead of just updating the list-form experience, you want to build a full, standalone app based on your SharePoint data. This is also the best way to get started, so you can start to learn how the PowerApps canvas works and build future apps from any of the multitudes of data sources.

To get started, follow these steps:

1. Open the SharePoint list from which you would like to build an app.
1. On the menu bar, select **PowerApps**, and then select **Create an app**.
1. Provide a name, and then select **Create**.

PowerApps will build you an app that you can customize.

Start with a simple custom list that contains just a couple of fields of different types for your first app. This will let you build a solid foundation without being overwhelmed. Don't worry; you'll be a pro in no time and ready to tackle those complex apps. For help walking through this first app, check out this [documentation](generate-app-from-sharepoint-list-interface.md) or this community [video](https://youtu.be/BnYe_7fpZRM). The examples below will show common InfoPath tasks and how to do them in PowerApps. Each of these builds on a simple SharePoint list app.

## How do you do that with PowerApps?

Now that you know the fundamental concepts, let's go further. With your first app under your belt, this section will help you apply some of the common InfoPath concepts in PowerApps.

**Hide/show/lock a field based on a value**  
Successful forms often enforce strong business logic by, for example, changing the state of a field based on a value or an action. With PowerApps, you can set the **DisplayMode** property of a control to **Edit** or **View** to specify whether a user can change the field. You can also use a simple **If** formula to do so conditionally. First, select the label that you want to edit, and then select the lock icon. This step unlocks the card so that you can change the value.

![Hide Show Lock Data Cards](./media/transform-infopath/hide-show-lock.png)

Now scroll to the bottom of the card on the right, and edit the **DefaultMode** property.

![If Else Statement Expressions](./media/transform-infopath/if-else-statement.png)

In this example, use an **If** formula:

```If(ThisItem.Color = &quot;Blue&quot;, DisplayMode.View, DisplayMode.Edit)```

This formula says that, if the current item's **Color** field is **Blue**, the **Animal** field is read-only. Otherwise, the field is editable.

If you wanted to hide the card instead of making it read-only, you could insert a similar function in the **Visible** property right above **DisplayMode**.

Other things to play with here would be hiding an approval button so that it only displays if the user's email address matches the approver's email address. Hint: User().Email is how to access the current user's email address. So you could make the button Visible value If(YourDataCard.Text = User().Email, true, false) where YourDataCard is the card where you are storing the Approver's email address.

**Conditional formatting**  
In a similar manner as above where you hid the field, you can also provide visual feedback to users. Maybe you want to highlight text in red if the entered value falls out of the acceptable range or change the upload buttons text and color to delete after the upload a file. This is all done by using functions, such as If, in property fields like color or visible.

For example, you could use the If function paired with the [IsMatch](https://docs.microsoft.com/powerapps/functions/function-ismatch) function to change the text color of the email field to red if the user did not enter a properly formatted email in the input box. You would do this by setting the Color value of TextInput1 to If(IsMatch(TextInput1.Text, Email), Black, Red) where TextInput1 is the field where the user types in an email address. IsMatch supports a plethora of predefined patterns like Email or the ability to create your own. For more information on conditional formatting check out this [community video](https://powerusers.microsoft.com/t5/Video-Webinar-Gallery/PowerApps-Conditional-Formatting-and-Popups/m-p/84962).

**Implementing role-based security**  
The first function to consider is [DataSourceInfo](https://docs.microsoft.com/powerapps/functions/function-datasourceinfo). What information you get back from the data source will vary by the data source, but often you can use DataSourceInfo(YourDataSource, DataSourceInfo.EditPermission) to check if the user has access to edit the data. Replace YourDataSource with the name of your data source. With this, you can only show a form or button if the user has access to edit. Check out the DataSourceInfo documentation for the full list of information you can query for in the function.

If instead, you want to use Active Directory groups to manage access to buttons or forms in your app then you will need to go deeper. To do this, you will take advantage of the flexibility of PowerApps and create your own connector using the Microsoft Graph API. And while that sounds daunting, there is step-by-step [documentation](https://powerapps.microsoft.com/blog/implementing-role-based-permission/) available to guide you.

**Send an email from your app**  
There are many ways to send an email from PowerApps. The easiest way is to use the Office 365 Outlook Connector. With this connector, you can send an email as yourself from your app. You can also get email messages and other tasks that interact with your mailbox. There is [documentation](https://docs.microsoft.com/powerapps/connections/connection-office365-outlook) or this community [video](https://powerusers.microsoft.com/t5/Video-Webinar-Gallery/Send-an-email-from-PowerApps/m-p/74349) on sending your email.

If you need to send a more complex email, maybe by creating a SharePoint approval workflow approval chain for example, then creating a Microsoft Flow and connecting your app to it is your answer. Once you connect your app to Microsoft Flow, you have opened up the full power of a workflow engine that like PowerApps is very well connected to external data and services. For more information on connecting PowerApps and Microsoft Flow check out this [documentation](https://docs.microsoft.com/powerapps/using-logic-flows).

And if you still haven't found the email option you are looking for you can also leverage the PowerApps connectors for Benchmark Email, Gmail, MailChimp, Outlook.com, SendGrid, or SMTP. That is the beauty of PowerApps, connectivity.

**Workflows**  
Hard to talk about business apps and business logic without a workflow engine. The good news is the PowerApps team didn't reinvent the wheel and give you another workflow engine. Instead, they provide you with a robust connector to the Microsoft Flow service. Now you can automate processes and tasks across more than [200 different services](https://flow.microsoft.com/connectors/) through their easy to use workflow engine. For more information on connecting PowerApps and Microsoft Flow, check out this [documentation](https://docs.microsoft.com/powerapps/using-logic-flows).

**Variables with PowerApps**  
When you build solutions, it's natural to think variables must be involved. PowerApps offers multiple types of variables, but you want to use them only when you have to. Instead of thinking about getting data, storing it in a variable, and then referencing that variable, think about just referencing that data directly. The best way to equate it is Excel. In Excel, Total isn't a variable; it's the sum of other fields. So, if you want to use that value elsewhere on the sheet, you specify the field you calculated the total in. The [documentation](working-with-variables.md) has a great explanation of all of this you can read. Be open to a different thought process.

If you still need variables (there are many cases that you do), this will help you understand the different options. Keep in mind with PowerApps you don't have to define variables. Just use one of the functions to specify a name and a value to store, and your variable is created. You can view the variables you have created by clicking View in the menu bar and selecting Variables. Variables are held in memory, and their values are lost when you close the app. The three types of variable are as follows:

- Global variables are what you most commonly think of first. Here you can use the [Set](functions/function-set.md) function to specify a value for the variable and then it is available throughout your app. An example of how you use the function is Set(YourVariable, YourValue). Then you can reference YourVariable by name throughout your app.
- Context variables are variables that are only available on the screen where they are defined. When you leave the screen, they are reset. They are often used to store information passed from a previous screen or to track if the form has been submitted for example. Common use of [UpdatedContext](functions/function-updatecontext.md) is UpdateContext( { Submitted: "true" } ) This would set the Submitted variable to true. You might make this part of the submit button on the page to track that the information has been submitted and change all of the fields to read-only. Note: You use ":" Collections are used to store tables of information that can be updated individually. Look at [Collect](functions/function-clear-collect-clearcollect.md) to get started. An example of use might be creating a shopping cart as the user tags various SharePoint items they want to send. A community [video](https://powerusers.microsoft.com/t5/Video-Webinar-Gallery/Learn-about-PowerApps-Collections/m-p/89180) shows that concept in action.

**Cascading dropdowns**  
Cascading dropdowns are very useful. They allow you to filter the choices in one dropdown based on the value selected in the previous dropdown. In PowerApps, these are often created by having two data sources in your app. The first data source is the data you are working with or updating and the second data source is used to store the values to build the cascading effect you want. Below is an example of the second data source with the choice options.

![Cascading dropdowns](./media/transform-infopath/cascading-dropdowns.png)

Now you would create your first dropdown control, and for the Items property, you would use the formula Distinct(Impacts, Title) to only show Cost, Program Impact, and Schedule in the dropdown. Then you would add a second dropdown and set the Items property to Filter(Impacts,ddSelectType.Selected.Value in SCategory) where ddSelectType is the name of the first dropdown box. Just like that you have cascading dropdowns. For more information check out this post from the PowerApps team [SharePoint: Cascading Dropdowns in 4 Easy Steps!](https://powerusers.microsoft.com/t5/PowerApps-Community-Blog/SharePoint-Cascading-Dropdowns-in-4-Easy-Steps/ba-p/16248) or this [community video](https://powerusers.microsoft.com/t5/Video-Webinar-Gallery/PowerApps-Cascading-Dropdown/m-p/92813) and don't worry, you can do it just as easy without SharePoint.

**Don't build one super app**  
With PowerApps, you can call one app from another. So, instead of the mass InfoPath form you built that's held together with bubble gum, you can build a group of apps that call each other, and even pass data across, making development simpler.

## Next steps

With the information in this topic, you're now ready to go out into the world and start to conquer it one PowerApps app at a time. As you continue on your journey, below are some handy links to help, such as the link to the PowerApps community site. Engage today with the community, and grow your skills much faster than you would on your own.

[**Formula reference**](https://docs.microsoft.com/powerapps/formula-reference) - Always a great way to become inspired, just browsing some of the default functions.

[**PowerApps community**](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1) - See examples, engage with others, ask and answer questions, and help the PowerApps community grow.
