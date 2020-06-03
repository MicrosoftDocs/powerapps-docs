---
title: Are there decisions being made based on the data Or business rules to follow | Microsoft Docs
description: Are there decisions being made based on the data Or business rules to follow
author: TGround
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/02/2020
ms.author: thground
ms.reviewer: kvivek
searchScope:  
  - PowerApps
---

# Are there decisions being made based on the data Or business rules to follow?


Do you have any “If ___ , then ___” logic?

At the conclusion of this activity in the process, is a decision being made? Is
there a way that the solution can make the decision automatically based on the
data?

Is this decision communicated to anyone? How is it communicated?

Does this decision determine if the next step of the process is executed? How is
that communicated?

For example, *if* a meal cost \$75 or more, *then* employees need to attach
receipts for meals; and *if* the total amount is greater than \$500, *then* our
expense reports need an extra level of approval.

## Does the decision require approvals?

Are approvals needed before the next step of the process begins? How are those
approvals captured? Is there a specific user or role that can approve the next
step in the process? Should this person have access to the app or is there
another method that is used (such as an e-mail sent to the user to get approval
to move forward)?

How is the next person in the process alerted of the response so they can move
forward with their next step of the process (or not)? Is there a certain way
that the next person in the process is alerted? is there a way that a user
should be made aware when a work item is going to be escalated because it hasn’t
been worked in the allotted timeframe?

As you consider these different methods, always look for the most optimal method
to help reduce the time to respond to an approval.

## Are there escalations required?

Does the business process require escalations?

Should items automatically escalate under certain conditions? Are there
timeframes that this solution must be completed within? If a worker who uses the
solution missed an approval, how long do you wait before the activity moves to
another worker? Or do you send another notice?

Should users be able to escalate an issue?

If an escalation is required, how will it be presented? Do work items that are
overdue float to the top to be worked? Does the solution change color to let a
worker know that there are activities that are behind?

Are there alerts or notifications that need to be generated?

## Example: Expense report approvals


The Expense report process requires approvals. All Salespeople must have the
expense report approved by Nick, their manager. When the employee submits the
report, an alert needs to be sent to Nick to review and approve the expense
report.

We know that Nick is a busy manager – so we should consider an escalation if
expense reports wait for his approval longer than 5 days. We can consider
several escalation methods

-   We can send another alert to Nick – perhaps rather than e-mail, we consider
    sending a text message

-   If Nick still hasn’t responded, then perhaps we send them to Nick’s manager
    for approval – or even to Abhay to review and approve.
