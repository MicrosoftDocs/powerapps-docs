<properties
	pageTitle="Use Logic Flows in a PowerApp"
	description="Business User: How to use a Logic Flow in a PowerApp"
	services=""
	suite="powerapps"
	documentationCenter=""
	authors="aftowen"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/09/2015"
   ms.author="aftowen"/>

# Logic Flows in PowerApps

Logic Flows provides an easy way to run a series of actions from a PowerApp that can read or update data, send notifications on email, update your calendar or tasks in Office 365 or SharePoint, and even wait on tasks to be updated by you or other people you work with. Logic Flows run in the cloud even when you have closed PowerApps on your phone to carry out the steps in automatically.

## Creating Logic Flows for your PowerApp

To create a PowerApp that uses Logic Flows, you need to install PowerApps on your Windows PC. Once you've installed and signed in to PowerApps, choose the option to create a new app. You can add Logic Flows to any kind of app, so you can choose any of the options to create a new app (from a template, from data or blank). Once your new app is open, you can add a variety of controls onto the screen, like a button to associate a Logic Flow with.

To create a new Logic Flow, select "Action" from the ribbon menu and select "Logic Flows".

![][1]

The Logic Flows pane will slide out on the right. Select the + Create a new Logic Flow button.

![][2]

The PowerApps portal will open up in the browser and you may need to log in with your work email address. Once you are logged in, you can choose the option to create a new Logic Flow to open the flow designer.

![][3]

In the first box, enter when do you want the Logic Flow to run. For running the flow from a PowerApp, select "PowerApp - When a control is selected".

![][4]

You can now add one or more actions to your Logic Flow to carry out the steps you need the flow to run. Here's another great article that explains in more detail on [how to run multiple steps in a Logic Flow](http://link-to-create-flow-doc.com).

Once your flow is complete, type in a name of the flow at the bottom and select "Done" to save the flow in PowerApps.

![][5]

Your Logic Flow is now ready to be used in an app.

Switch back to PowerApps and open the flows task pane if it is not open already. The new flow that you created on the PowerApps portal would now appear in the list of flows on the task pane under "All Logic Flows".

**Note: Only flows that are have the trigger "When a control is selected" will be available to run in the Task Pane**

## Using a Logic Flow in a PowerApp
You can associate your Logic Flow as an action with any control in PowerApps:
1. Select the control using which you want to run the flow (for example, you can add a button in your app and configure it to run a flow when the button is selected by a user).
2. Open "Actions">"Logic Flows" to open the task pane.
3. From the list of "All flows", select the flow you want to run. It may take a few seconds while the flow is added to your app:

![][6]

4. Once the flow is added, the formula bar will be partly filled with the formula to run the flow. It will look something like this:

![][7]

5. If your flow doesn't require any parameters, simply close the parenthesis to complete the formula.

Your app is now ready to run the flow when this button is selected.

## Sending data to a flow
With Logic Flows, you can not only pass data between the various steps of the flow, but also send data to a flow to use when the steps execute. This can be useful in cases where you don't know all the settings for each of the steps when you create the flow, but these would be known when users of your app fill in data in the app.
For example, let's say you have a PowerApp that registers information about a new user into a SharePoint list and sends a welcome email to the user who just registered. For this, your Logic Flow will need to use the email address provided by the user when filling up data in the app.
This can be achieved by doing the following steps:

First, when creating your flow, when you come across steps that require input from the PowerApp, simply fill in the value with the "Ask in PowerApps" token. The value will be automatically filled in with the name of the action and the setting. For example, if you need to use the email address provided by a user of the app, just select the "To" configuration of the "Send Email" action. This tells the flow that the "SendEmail_To" value will be provided later when using the flow in a PowerApp.

![][8]

![][9]

Next, when you use the flow in a PowerApp (as described in the "Using a Logic Flow in a PowerApp" section, the formula will be partly filled and PowerApps will assist you in filling up the values for the formula to run the Logic Flow. Any values you choose when filling up the formula will be used at the corresponding places when the flow runs.

![][10]


[1]: ./media/add-logic-flow/LogicFlowsInRibbon.png
[2]: ./media/add-logic-flow/Day0TaskPane.png
[3]: ./media/add-logic-flow/FlowDesigner.png
[4]: ./media/add-logic-flow/ManualTrigger.png
[5]: ./media/add-logic-flow/SaveFlowWhenDone.png
[6]: ./media/add-logic-flow/AddingFlow.png
[7]: ./media/add-logic-flow/FormulaBarPrefilled.png
[8]: ./media/add-logic-flow/AskInPowerAppsParameterBeforeSelection.png
[9]: ./media/add-logic-flow/AskInPowerAppsParameterAfterSelection.png
[10]: ./media/add-logic-flow/FlowFilledIn.png
