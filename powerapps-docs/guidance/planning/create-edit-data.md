Do they create or edit data?
============================

Understanding the tasks in this step, is there any data that the solution needs
to capture? What is the data that needs to be captured? Here are some things to
consider for each data element that is captured by the solution.

Is there an existing form that is used?
---------------------------------------

Is there a current paper form or electronic form that is being used to capture
this data today? This can serve as a great beginning point as you think about
the layout of screens and how the data is being captured.

Also think about the form critically:

-   Should the data elements be presented in a different order that is more in
    line with how you capture it?

-   Can the form be divided into separate smaller forms that allow the process
    to happen in parallel, rather than one part at a time?

What data is captured? 
-----------------------

What is the data that is being captured?

What is it called? (Is this the real name from the data source or a common name
used in this part of the business? You may need to map the data name in the data
source to the “friendly” name your users know.)

Is there a hierarchy of the data? (For example, each expense report can have
multiple expenses, and some expense types require specific additional
information.)

What data is created from a formula or calculation?
---------------------------------------------------

Are there calculations that are done to create the data?

If yes, is the calculated result required to be stored, or is it just shown
while using the app? (Data that can be recalculated at any time (such as item
sum totals or counts) may not need to be stored.)

For example, our expense report’s unique ID is going to be created using today’s
date and the employee name; it needs to be stored so it never changes. We’ll
also calculate expense subtotals and totals; since those can be recalculated any
time from the other data in the report, we don’t need to save them separately.

Is the data required?
---------------------

For this step of the process, is this data *required* to complete the process?
If it is required, why is it required? Is data only required in certain
situations?

What type of data is it?
------------------------

What type of data is being captured?

**Free-form text:** Is there a set length that is allowed? Is the entry of this
field dependent on another field (an associated field value such as a dropdown
with an option of ‘other’, for example)? Is there a default entry that should be
populated? Is the text derived from other data?

**Numbers:** Is it a percent? Is it a whole number? Are there a certain number
of decimal positions required? Is there a set minimum or maximum that is allowed
for this number? Is this number dependent on another number (eg: it cannot be
greater than, or less than, another entry). Is there a default number that
should be provided? Or a number calculated based on other entries?

**Dates:** What format for the date? Include both date and time? Are there rules
for the date (a minimum, or maximum, can’t be before today)? Is it calculated
(eg, 7 days from today)? Is there a default date that should be populated?

**Choices:** Should the response be limited to a specific set of responses? What
are the valid responses? Are the responses dependent on another data element? Is
there a default choice, or a default based on another data element? Do you allow
only a single choice to be selected, or can multiple be selected at the same
time?

**Images/Video:** Should an image or video be captured? Is the image/video being
captured from a camera on the user’s device? Is this an image/video that is
coming in via e-mail? Is there any AI that should be run on this image
(detecting elements of the image, for example)?

Where do we put the data today?
-------------------------------

Today as you solve the business problem, where does the data get captured? Does
the data go back into an existing system? Does it go into a spreadsheet? Does it
get captured at all?

If the data doesn’t already get stored digitally, you will be creating a data
repository for it, which is discussed in Handling information and data.

Another thing to consider is whether this data can be valuable to other
processes in the organization. Could other processes be automated if this data
were available to them?

Does someone use this data later in the process?
------------------------------------------------

Is there a step later in this process that uses this data? How do they use this
data? If this data was available earlier in the process, could a process further
down the line get started earlier or run in parallel?

Sometimes automation of a process helps reduce the total time to solve the
business problem because data becomes available earlier and other participants
in solving the problem can act sooner. This may contribute to the business value
that automating the business process provides.

Can anyone else benefit from this data outside of this process? 
----------------------------------------------------------------

Is there another team or process that can use the data captured in this process?
(Not a step later in this process, but a process elsewhere in the business that
may be capturing this same information, or can leverage this information?)

Business users sometimes only think within the confines of what they do from
day-to-day. If you were to take a step back, are there opportunities to extend
this data into other processes that can be automated? Many times, processes are
manual because a process in another area does not have a means by which to get
data. Now that this process is being automated, is there an opportunity for
other processes to build on this one?

Example: Expense report data creation
-------------------------------------

Here are some of the data elements in the worksheet for the expense report
capture process:

| **Data level** | **Data item**         | **Item Type** | **Editable?** | **Format Allowed**                                                  | **Validation**                                            | **Default/**                     |
|                |                       |               |               |                                                                     |                                                           | **Calculation**                  |
|----------------|-----------------------|---------------|---------------|---------------------------------------------------------------------|-----------------------------------------------------------|----------------------------------|
| Expense Report | Expense Report Number | Text          | No            |                                                                     | Cannot be blank                                           | “EXP” + Date (YYYYMMDD) + UserID |
| Expense Item   | Date of Expense       | Date          | Yes           | MM-DD-YYYY                                                          | Cannot be in the future                                   |                                  |
| Expense Item   | Type of Expense       | Choice        | Yes           | Select from list:                                                   | Cannot be blank                                           |                                  |
|                |                       |               |               | -Travel                                                             |                                                           |                                  |
|                |                       |               |               | -Meal                                                               |                                                           |                                  |
|                |                       |               |               | -Hotel                                                              |                                                           |                                  |
|                |                       |               |               | -Transportation                                                     |                                                           |                                  |
|                |                       |               |               | -Parking                                                            |                                                           |                                  |
|                |                       |               |               | -Supplies                                                           |                                                           |                                  |
| Expense Item   | Amount                | Number        | Yes           | \#\#\#,\#\#\#.\#\#                                                  | Cannot be blank, can be negative                          |                                  |
| Expense Item   | Receipt               | Image         | Yes           | JPG, PNG                                                            | Required if the Amount \> \$74.99                         |                                  |
| Expense Item   | Reimbursable          | Yes/No        | Yes           | Yes/No                                                              |                                                           | Defaults to 'No'                 |
| Expense Detail | Guest Name            | Text          | Yes           | Anything                                                            | Required for 'Meal' type expense where the amount \> \$75 |                                  |

In this example there are three levels of data that is being captured. (This
will become very important in the Design section for both screen design and data
storage design.)

-   **Expense Report** – these elements are captured one for the overall expense
    report .

-   **Expense Item** – these elements are captured for each expense being
    reported on this expense report. There can be multiple expense items
    associated with the same expense report

-   **Expense Detail** – these elements are associated with the specific expense
    items Meal and Hotel and helps break those two expense types down. If the
    expense item is Meal, then the Guest Name and Guest Company are required. If
    the expense item is Hotel, then the Type of charge and Amount are required –
    and the amount of each of these entries must equal the amount of the Expense
    Item

Data that will be displayed in the app but not stored anywhere are these
on-the-fly calculations:

-   Sum the expense items into an Expense Report total

-   Sum up the expense details into an Expense Item total

-   Count the number of entries in the expense report

-   Determine whether the expense report total is over the approval limit for
    the submitter’s manager

The data that is captured during the expense report process ultimately must be
posted in the financial system. However, the expense reports themselves aren’t
currently stored online, only on paper. So there’s no existing system to put
this data in; we’ll have to create one.

Having all this expense data lends itself to future analysis if we were
capturing it digitally. For example, if all the employees are staying at the
same hotel when they travel, Procurement can pull expense data and potentially
negotiate better rates for employees. We’ll note this in our project plan.
