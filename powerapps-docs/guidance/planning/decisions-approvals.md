---
title: Planning - Data-driven decisions (business rules) | Microsoft Docs
description: As part of the planning phase of a Power Apps project, determine what decisions are being made based on the data and what business rules need to be followed.
author: TGrounds
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.subservice: guidance
ms.author: thground
ms.reviewer: kathyos

---

# Are there decisions being made based on the data, or business rules to follow?

## Does the data determine the outcome of any decisions?

- At the conclusion of this activity in the process, is a decision being made? Is
there a way that the solution can make the decision automatically based on the
data?

- Is this decision communicated to anyone? How is it communicated?

- Does this decision determine whether the next step of the process will be executed? How is that communicated?

- Do you have any "if/then" logic?
For example, *if* a meal cost \$75 or more, *then* employees need to attach
receipts for meals; and *if* the total amount is greater than \$500, *then* our
expense reports need an extra level of approval.

## Does the decision require approvals?

- Are approvals needed before the next step of the process begins? How are those
approvals captured? Is there a specific user or role that can approve the next
step in the process? Should this person have access to the app or can
another method be used (such as an email sent to the user to get approval
to move forward)?

- How is the next person in the process alerted about the response, so they can move
forward (or not) with their next step of the process? Is there a particular way
that the next person in the process is alerted

- Is there a way for a user
to be made aware when a work item is going to be escalated because it hasn't
been worked in the allotted timeframe?

> [!TIP]
> As you consider these different aspects, always look for the most optimal method
to help reduce the time to respond to an approval.

## Are escalations required?

- Does this business process require escalations?

- Should items automatically be escalated under certain conditions? Are there
timeframes that this solution must be completed within? If a worker who uses the
solution missed an approval, how long do you wait before the activity moves to
another worker? Or do you send another notice?

- Should users be able to escalate an issue?

- If an escalation is required, how will it be presented? Do work items that are
overdue float to the top to be worked on? Does the solution change color to let a
worker know that some activities are behind schedule?

- Do any alerts or notifications need to be generated?

## Example: Expense report approvals

The expense report process requires approvals. All salespeople must have the
expense report approved by Nick, their manager. When an employee submits a
report, an alert needs to be sent to Nick to review and approve the expense
report.

We know that Nick is a busy manager, so we should consider escalation for
expense reports that wait for his approval longer than five days. We can consider
several escalation methods:

- We can send another alert to Nick&mdash;perhaps rather than email, we consider
    sending a text message.

- If Nick still hasn't responded, perhaps we send the report to Nick's manager&mdash;or even to Abhay&mdash;to review and approve.

> [!div class="nextstepaction"]
> [Next step: Moving to the next task in the process](next-task.md)

> [!div class="nextstepaction"]
> [I've documented all the tasks](visually-map-process.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]