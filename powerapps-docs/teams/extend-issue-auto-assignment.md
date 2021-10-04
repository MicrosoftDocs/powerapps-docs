---
title: Add business logic for automated task assignment
description: Learn how to add logic to automatically assign tasks to a manager in the Issue reporting template app for Microsoft Teams.
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/13/2021
author: joel-lindstrom
ms.author: namarwah
ms.reviewer: tapanm
contributors:
  - joel-lindstrom
  - navjotm
  - tapanm-msft
---

# Add business logic for automated task assignment

In the Issue reporting template Power App for Microsoft Teams, you can specify a specific user for a type of issue. This will make tasks for that issue type automatically assigned in Planner to that user.

But what if you want additional logic to further automate issue assignment?

Let’s say you want any urgent issues to be automatically assigned to a manager. Power Automate is a great option to automate conditional logic like task creation.

Watch this video to learn how to add business logic for automated task assignment:
> [!VIDEO https://www.microsoft.com/videoplayer/embed/RWLiBY]

## Open Power Automate

In this step, we'll open Power Automate to edit the flow we previously created.

1. Log in to [Power Automate](http://www.powerautomate.com), and select the environment for your Team.

1. Select **My flows**.

1. Open the flow **Create Planner Task**.

1. Select **Edit**.

## Retrieve the assigned user’s manager

We're going to use the Office 365 Users connector to get the manager of the user to whom the task is assigned.

1. In Power Automate, hover the cursor under the Power Apps trigger.

1. Select **Insert a new step.**

    ![Insert new flow step](media/extend-issue-auto-assignment/insert-new-step.png "Insert new flow step")

1. Select **Add an action.**

1. In the operation picker, enter **Office 365 Users**, and select the **Get manager (V2)** action.

1. In the Get manager (V2) action, select the **User (UPN)** field.

1. Select the variable for assigned users from the dynamic field selector. In our example, it's called **Createtask_AssignedUserIds**. This was the variable created when we added the **Ask in Power Apps** option in the Assigned field.

1. Save your flow.

The flow now will get the manager of the assigned user to use for escalation.

## Escalate urgent issues to a manager

In this step, we'll add logic to the flow to conditionally assign tasks to managers if the task is urgent. There are multiple ways to perform conditional logic in Power Automate. In this lesson, we'll cover two options:

- Using condition step
- Using an expression

> [!NOTE]
> Each of the following two expressions modify the flow, you should select one of these methods.

### Method 1: Use a condition action (For beginners)

If you're a beginning flow maker, you may find using a condition step to be the easiest approach as it doesn't involve any formulas.

1. Under the **Template** step in your flow, add a new action.

1. Select **Condition**.

    ![Insert condition step](media/extend-issue-auto-assignment/condition-step.png "Insert condition step")

1. In the condition action, select the **Choose a value** field.

1. In the dynamic field selector, select the **Createtask_Priority** variable.

1. Select the **Choose a value** field and enter **1**.

1. Drag the **Create a task** and **Update task details** actions to the **If yes** box.

    ![Condition yes branch](media/extend-issue-auto-assignment/create-task.png "Condition yes branch")

1. Select the **…** on the right of the **Create a task** action, and select **Copy to my clipboard (preview)**.

1. Select the **…** on the right of the **Update task details** action, and select **Copy to my clipboard (preview)**.

1. In the **If no** box, select **Add an action**.

1. Select **My clipboard**, and select **Create a task (preview)**.

1. Select **My clipboard**, and select **Update task details**.

    Your flow should now look like this:

    ![Condition no branch](media/extend-issue-auto-assignment/create-task-no-branch.png "Condition no branch")

    Next, we'll update the task creation action in the **If yes** path to assign the task to the manager.

1. In the **If yes** box, expand the **Create a task (preview)** step.

1. Clear the **Assigned to id** by selecting the X on the field reference.

    ![Clear assigned User Ids](media/extend-issue-auto-assignment/create-task-details.png "Clear Assigned User Ids")

1. From the dynamic content panel, select the **ID** field from the Office 365 Users step.

    ![Set ID to manager](media/extend-issue-auto-assignment/assign-user.png "Set ID to manager")

1. In the **If no** box, expand the **Update task details 2** step.

    - Clear the **Task id** field.
    - In the Dynamic content panel, select the ID from the "Create a Task (preview) 2" step.

1. Save the flow.

Your flow will now assign the task to the manager if priority is urgent, and assign it to the person specified in the app when the priority isn't urgent.

### Method 2: Use a conditional expression (Advanced)

The first method used a condition step to conditionally set the properties of the task. This is effective, but there are more efficient methods you can use to conditionally set values in power Automate.

In this step, we'll use an expression to conditionally set the value of the Assigned on the task.

Benefits of using an expression:

- By using a conditional expression, we don’t need to duplicate the create task step—this means that if we make further changes to the task creation step we only need to make it one place.
- Expressions may be faster than conditional branches.

Set the assignment logic using the following steps:

1. Open the Create Planner Task flow.

1. Expand the **Create a task (preview)**  step.

1. Clear the **Assigned user Id** field.

1. In this step, we are going to use an **if** formula to set the Assigned user ID. This is going to be similar to the expression used in the priority field, but instead of setting the value to a numeric value we'll be setting it to the manager if the task is urgent.

1. Select **Expression** in the Dynamics content panel.

1. Enter the following expression.

    ```powerapps-dot
    if(equals(triggerBody()'Createatask_Priority'],1),outputs('Get_manager_(V2)')?['body/id'],triggerBody()['Createatask_AssignedUserIds'])
    ```

    ![Formula to assign to manager](media/extend-issue-auto-assignment/priority.png "Formula to assign to manager")

> [!NOTE]
> If you want to know how to refer to a field value in an expression, add the field to your step, then select **..** in the upper right corner of the step definition, and select **Peek code.** This will reveal the expression syntax for referencing the field value.

## Test your flow

1. In the Teams environment in which you modified the flow, run the Issue reporting app.

1. Create an issue.

1. Check the **Urgent** checkbox.

1. Wait a few seconds then verify that the task is created.

1. Verify that the task was assigned to the manager of the person you selected in the app.

    > [!NOTE]
    > This flow will work if a single assigned to was selected for the task in the Issue reporting app. The selected person must also have a manager defined in Active Directory.

## Next steps

You can use this method to add other conditional business logic to Issue reporting. Some examples include:

- Conditionally assigning based on time of day.
- Conditionally assigning based on responses to issue form questions.
- Conditionally assigning to a manager if the original assignee is out of the office (the Outlook connector can check to see if there's an out-of-office message on the person’s mailbox).
- Conditionally assigning based on the location of the user submitting the issue.
- Conditionally assigning based on who is on shift (using Teams Shifts connector).

### See also

- [Understand Issue reporting sample app architecture](issue-reporting-architecture.md)
- [Customize Issue reporting app](customize-issue-reporting.md)
- [Sample apps FAQs](sample-apps-faqs.md)
- [Use sample apps from the Microsoft Teams store](use-sample-apps-from-teams-store.md)


[!INCLUDE[footer-include](../includes/footer-banner.md)]