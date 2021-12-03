---
title: Planning - Will your app create or edit data? | Microsoft Docs
description: As part of the planning phase of a Power Apps project, here are some things to consider for each data element your solution needs to capture.
author: TGrounds
ms.service: powerapps
ms.topic: conceptual
ms.custom: guidance
ms.date: 06/16/2020
ms.subservice: guidance
ms.author: thground
ms.reviewer: kathyos

---

# Do they create or edit data?

Understanding the tasks in this step will help you answer the question, does the solution need
to capture any data? If so, what data needs to be captured? Here are some things to
consider for each data element that's captured by the solution.

## Is there an existing form?

Is there a current paper form or electronic form used to capture
this data today? Such a form can serve as a great beginning point as you think about
the layout of screens and how the data is being captured.

Also, think about the form critically:

- Should the data elements be presented in a different order that's more in
    line with how you capture it?

- Can the form be divided into separate, smaller forms that allow parts of the process
    to happen in parallel, rather than one at a time?

## What data is captured? 

What is the data that's being captured? What is it called? Is this the real name from the data source or a common name
used in this part of the business? You might need to map the data name in the data
source to the "friendly" name your users know.

Is there a hierarchy for the data? For example, each expense report can have
multiple expenses, and some expense types require additional
information.

## What data is created from a formula or calculation?

Are there calculations that are done to create the data? If yes, must the calculated result be stored, or is it just shown
while using the app? Data that can be recalculated at any time (such as item
sum totals or counts) might not need to be stored.

For example, our expense report's unique ID is going to be created by using today's
date and the employee name; it needs to be stored so it never changes. We'll
also calculate expense subtotals and totals, but because those can be recalculated any
time from other data in the report, we don't need to save them separately.

## Is the data required?

For this step of the process, is this data *required* to complete the process?
If it's required, why is it required? Is data only required in certain
situations?

## What type of data is it?

What type of data is being captured?

- **Free-form text:** Is there a set length that's allowed? Is the entry of this
field dependent on another field (for example, an associated field value such as a drop-down menu option of **Other**)?
Is there a default entry that should be
populated? Is the text derived from other data?

- **Numbers:** Is it a percent? Is it a whole number? Are there a certain number
of decimal positions required? Is there a set minimum or maximum that's allowed
for this number? Is this number dependent on another number (for example, it can't be
greater than, or less than, another entry)? Is there a default number that
should be provided, or a number that's calculated based on other entries?

- **Dates:** What format should you use for the date? Should it include both date and time? Are there rules
for the date (a minimum, or maximum, can't be before today)? Is it calculated
(for example, "seven days from today")? Is there a default date that should be populated?

- **Choices:** Should the response be limited to a specific set of responses? What
are the valid responses? Are the responses dependent on another data element? Is
there a default choice, or a default based on another data element? Do you allow
only a single choice to be selected, or can multiple choices be selected at the same
time?

- **Images or video:** Should an image or video be captured? Is the image or video being
captured from a camera on the user's device? Is this an image or video that's
coming in via email? Is there any AI that should be run on this image
(detecting elements of the image, for example)?

## Where do you put the data today?

As you solve the business problem today, where does the data get captured? Does
it go back into an existing system? Does it go into a spreadsheet? Does it
get captured at all?

If the data doesn't already get stored digitally, you'll be creating a data
repository for it, which is discussed in [Where is the data?](where-is-data.md)

Another thing to consider is whether this data can be valuable to other
processes in the organization. Could other processes be automated if this data
were available to them?

## Does someone use this data later in the process?

Is there a step later in the process that uses this data? How do they use this
data? If this data were available earlier in the process, could a process further
down the line get started earlier or run in parallel?

Sometimes automating a process helps reduce the total time to solve the
business problem because data becomes available earlier, and other participants
who work on solving the problem can act sooner. This can contribute to the business value
that automating the business process provides.

## Can anyone else benefit from this data outside of this process?

Is there another team or process that can use the data captured in this process?
(Not a later step within the process, but a process elsewhere in the business that
might capture this same information or might be able to use this information?)

Business users sometimes only think within the confines of what they do from
day to day. If you take a step back, can you see opportunities to extend
this data into other processes that can be automated? Many times, processes are
manual because a process in another area doesn't have the means by which to get
data. Now that this process is being automated, is there an opportunity for
other processes to build on this one?

## Example: Expense report data creation

Here are some of the data elements in the worksheet for the expense report capture process.

| Data level | Data item       | Item type | Editable? | Format allowed   | Validation   | Default / Calculation    |
|------------|-----------------|-----------|-----------|------------------|--------------|--------------------------|
| Expense report | Expense report number | Text          | No  |       | Can't be blank  | "EXP" + Date (YYYYMMDD) + UserID |
| Expense item   | Date of expense       | Date          | Yes           | MM-DD-YYYY       | Can't occur in the future    |
| Expense item   | Type of expense       | Choice        | Yes           | Select from list: Travel, Meal, Hotel, Transportation, Parking, Supplies | Can't be blank    |                                  |
| Expense item   | Amount      | Number  | Yes         | \#\#\#,\#\#\#.\#\#    | Can't be blank, can be negative  |
| Expense item   | Receipt     | Image         | Yes           | JPG, PNG   | Required if the amount is greater than \$74.99    |       |
| Expense item   | Reimbursable          | Yes/No        | Yes           | Yes/No   |     | Defaults to No      |
| Expense detail | Guest name            | Text          | Yes           | Anything     | Required for a **Meal**-type expense where the amount is greater than \$75 |                                  |

In this example, three levels of data are being captured. (This
will become very important in the design phase for both screen design and data
storage design.)

- **Expense report**: These elements are captured once for the overall expense
    report .

- **Expense item**: These elements are captured for each expense being
    reported on this expense report. Multiple expense items can be
    associated with the same expense report.

- **Expense detail**: These elements are associated with the specific expense
    items **Meal** and **Hotel**, and helps break down those two expense types. If the
    expense item is **Meal**, **Guest name** and **Guest company** are required. If
    the expense item is **Hotel**, **Type of expense** and **Amount** are required&mdash;and the amount of each of these entries must equal the amount of the expense item.

Data that will be displayed in the app but not stored anywhere are these
on-the-fly calculations:

- Sum the expense items into an expense report total

- Sum the expense details into an expense item total

- Count the number of entries in the expense report

- Determine whether the expense report total is over the approval limit for
    the submitter's manager

The data that's captured during the expense report process ultimately must be
posted in the financial system. However, the expense reports themselves aren't
currently stored online, only on paper. So there's no existing system to put
this data in; we'll have to create one.

Having all this expense data would lend itself to future analysis if we were
capturing it digitally. For example, if all employees stay at the
same hotel when they travel, Procurement can pull expense data and potentially
negotiate better rates. We'll note this in our project plan.

> [!div class="nextstepaction"]
> [Next step: What are the business rules?](decisions-approvals.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]