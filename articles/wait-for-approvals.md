<properties
    pageTitle="Wait for approval in Logic Flows | Microsoft PowerApps"
    description="Logic flows can wait for external events, such as users indicating approval in email or SharePoint."
    services=""
    suite="powerapps"
    documentationCenter="na"
    authors="stepsic-microsoft-com"
    manager="dwrede"
    editor=""
    tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/14/2015"
   ms.author="stepsic"/>

# Wait for approval in Logic Flows #

Create a logic flow that performs one or more tasks only after a user indicates approval by either clicking a link in email or updating an item in a SharePoint list.

**Prerequisites**
- [Create a logic flow from scratch](get-started-logic-flow.md)

## Request approval in email ##

1. In Chrome, open  [powerapps.com](http://go.microsoft.com/fwlink/?LinkId=708209), and then select **Flows** in the left navigation bar.

	![Flows option in left navigation bar](./media/wait-for-approvals/nav-flows.png)

1. In the list of logic flows, select the edit icon for the logic flow that you created from scratch.

	![Icon to edit a logic flow](./media/wait-for-approvals/edit-flow.png)

1. Select the plus icon after the action, and then select **Add action**.

	![Option to add an action](./media/wait-for-approvals/add-action.png)

1. In the box that shows **What would you like to do next?**, type or paste **approval**, and then select **Office 365 Outlook - Send approval email**.

	![Search for approval](./media/wait-for-approvals/approval-search.png)

1. (optional) Edit the subject line, the approval options, or both.

    ![Options](./media/wait-for-approvals/approval-mail.png)

1. In the **TO** box, type or paste the email address of the approver.

1. Drag the approval action so it appears just below the trigger, and then save your logic flow.

	![Move the approval action between the trigger and the other action](./media/wait-for-approvals/flow-sequence.png)

If you add an item to the SharePoint list, an email message should be sent to the approver, as you specified in the first action. If the approver selects **Yes** in that message, a second message should be sent, as you specified in the second action.

## Request approval in SharePoint
1. Create a SharePoint list with a column called **Status**.

2. Instead of adding the approval action, add **Create an item** and create an item in the list with the **Status** equal to pending.

3. Add a step **When an item is updated in a list**. Flow the ID into the step.

Now, the approver can updated the status in the list, and the item will be approved (or rejected).
