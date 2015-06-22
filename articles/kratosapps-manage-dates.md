<properties
	pageTitle="Manage dates and times in KratosApps Studio"
	description="Customize how dates and times appear in KratosApps, in addition to calculating dates that are before or after a date that you specify."
	services="kratosapps"
	authors="AFTOwen"
 />

# Manage dates and times in KratosApps Studio #

Add dates and times, and format them to show the right level of detail or to reflect your locale. Calculate the amount of time between two dates, or calculate a date that's a certain amount of time before or after a date that you specify. Convert dates to or from separate values for days, months, and years, and convert times to or from separate values for hours, minutes, and seconds.

For example, add data from users about stock trades or client meetings, data from [an external source](kratosapps-add-data.md), or data from [another app](kratosapps-share.md) created in KratosApps Studio. If that data includes times down to the millisecond, round it to the nearest minute for simplicity. Calculate how many days remain before a major milestone. If you want to schedule client meetings every five days, calculate those dates automatically. If May 10, 1985, is stored in separate fields for the day, the month, and the year, consolidate them into a single value. Conversely, break each date into separate values if your app manages them separately.

**Prerequisite**

[Create an app](kratosapps-tutorial-inventory) to understand how to perform basic tasks, such as adding a control.

## Add dates and times ##
**Show the current date and time**



- Set the **Text** property of a label to **Now()** to show the current date and time.

	The month appears before the day if your computer is set to the "en" locale, as in this example for May 10 at 5:27 PM:

	**5/10/2015 5:27 PM**

	The day appears before the month if your computer is set to the "fr" locale, as in this example for May 10 at 5:27 PM:

	**10/5/2015 5:27 PM**

	[Format dates and times](#Format-dates-and-times) (for example, show seconds) by using the **Text** function.

- Set the **Text** property of a label to **Today()** to show the current date.

	The month appears before the day if your computer is set to the "en" locale, as in this example for May 10:

	**5/10/2015 12:00 AM**

	The day appears before the month if your computer is set to the "fr" locale, as in this example for May 10:

	**10/5/2015 12:00 AM**

	[Format dates and times](#Format-dates-and-times) (for example, hide the time) by using the **Text** function.

**Prompt the user for a date, a time, or both**

1. Add two input-text boxes, and name them **ArrivalDate** and **ArrivalTime**.

1. In **ArrivalDate**, type your birthday (for example, 5/10/1985).

1. In **ArrivalTime**, type the approximate time you woke up this morning (for example, 6:15 AM).

1. Add a label, and set its **Text** property to this function:

	**"The product was launched on " & ArrivalDate!Text & " at " & ArrivalTime!Text & "."**

	The label shows **The product was launched on 5/10/1985 at 6:15 AM**.


## Format dates and times ##
Format dates and times by using the **Text** function or by specifying a language code. If the data is stored as text instead of values, convert it by using the **DateTimeValue**, **DateValue**, or **TimeValue** function.

Data might be stored as text if you import it from an external source or get it from the user (for example, if you prompt the user as the previous section describes). You can display data that's stored as text exactly as you imported it or as the user typed it, but you can't easily reformat it or perform other operations. If you convert that data from text to values, you can, for example, format a date for a different locale or calculate the number of days since a previous milestone.

The **DateTimeValue** and **DateValue** functions can convert dates in any of the following syntaxes into values:

- *MM/DD/YYYY*

- *DD/MM/YYYY*

- *DD Mon YYYY*

- *Month DD, YYYY*

**Format a date and a time**

1. Add an input-text box, and name it **ArrivalDateTime**.

1. In **ArrivalDateTime**, type your birthday, a space, and the approximate time you woke up this morning (for example, 5/10/1985 6:15 AM).

1. Add a label, and set its **Text** property to this expression:

	**DateTimeValue(ArrivalDateTime!Text)**

	The label shows the same information that you typed, but it's been converted from text to a value, as the next step demonstrates.

1. Change the **Text** property of the label to this expression:

	**DateTimeValue(ArrivalDateTime!Text, "fr")**

	The label shows the day before the month as appropriate for a French user. To list other locales, delete the closing quotation mark and fr (but leave the open quotation mark).

1. To use one of several built-in formats, change the **Text** property of the label to this expression:

	**Text(DateTimeValue(ArrivalDateTime!Text), DateTimeFormat!LongDateTime)**

	The label shows the day of the week, in addition to the date and time information.

	The **DateTimeFormat** parameter supports several other built-in formats. To list them, remove **LongDateTime** from the **Text** property (but leave the exclamation mark).

1. To specify a custom format, change the **Text** property of the label to this expression:

	**Text(DateTimeValue(ArrivalDateTime!Text), "mm/dd/yyyy hh:mm:ss.fff AM/PM")**

	The label shows the format you specified, including milliseconds.

	To round the time to the nearest tenth or hundredth of a second, specify **hh:mm:ss.f** or **hh:mm:ss.ff** in the expression.

**Format a date**

1. Add an input-text box, and name it **ArrivalDate**.

1. In **ArrivalDate**, type your birthday (for example, 5/10/1985).

1. Add a label, and set its **Text** property to this expression:

	**DateValue(ArrivalDate!Text)**

	The label shows the date that you typed, followed by **12:00 AM**. 

1. Change the **Text** property of the label to this expression:

	**DateValue(ArrivalDate!Text, "fr")**

	The label shows the day before the month as they do in France. To list other locales, delete the closing quotation mark and **fr** (but leave the open quotation mark).

1. To use one of several built-in formats, change the **Text** property of the label to this expression:

	**Text(DateValue(ArrivalDate!Text), DateTimeFormat!LongDate)**

	The label shows the day of the week, in addition to the month, the day, and the year.

	The **DateTimeFormat** parameter supports several other options. To list them, remove **LongDate** from the **Text** property (but leave the exclamation mark).

1. To specify a custom format, change the **Text** property of the label to this expression:

	**Text(DateValue(ArrivalDate!Text), "mm/dd/yy")**

	The label shows the date that you specified in the format that you specified.

**Format a time**

1. Add an input-text box, name it **ArrivalTime**, and then type **6:15 AM** in it.

1. To use one of several built-in formats, set the **Text** property of a label to this expression:

	**Text(DateTimeValue(ArrivalTime!Text), DateTimeFormat!LongTime)**

	The label shows **6:15:00 AM**.

	The **DateTimeFormat** parameter supports several other formats. To list them, remove **LongTime** from the **Text** property (but leave the exclamation mark).

1. To specify a custom format, change the **[Text](kratosapps-add-data.md)** property of the label to this expression:

	**Text(DateTimeValue(ArrivalTime!Text), "hh:mm:ss.fff AM/PM")**

	The label shows **06:15:00.000 AM**.

	To round the time to the nearest tenth or hundredth of a second, specify **hh:mm:ss.f** or **hh:mm:ss.ff** in the expression.

## Compare dates ##

Use the **DateDiff** function to calculate time between dates, or use the **DateAdd** function to identify the date that's a certain number of days, months, quarters, or years before or after a specified date.

**Calculate time between dates**

1. Add two input-text boxes, and name them **Start** and **End**.

1. Type **4/1/2015** in **Start** and **1/1/2016** in **End**.

1. Add a label, and set its **Text** property to this function:

	**DateDiff(DateValue(Start!Text), DateValue(End!Text))**

	The label shows **275**, which is the number of days between April 1, 2015, and January 1, 2016.

1. Change the **Text** property of the label to this function:

	**DateDiff(DateValue(Start!Text), DateValue(End!Text), Months)**

	The label shows **9**, which is the number of months between April 1, 2015, and January 1, 2016. Instead of **Months**, specify **Quarters** or **Years** to show the time in those units.

**Identify a date before or after another date**

1. Add an input-text box, name it **Start**, and then type **5/10/1985** in it.

1. Add a label, and set its **Text** property to this expression:

	**Text(DateAdd(DateValue(Start!Text), 3), "mm/dd/yyyy")**

1. The label shows **5/13/1985**, which is three days after the date in the **Start** box.

1. Change the **Text** property of the label to this expression:

	**Text(DateAdd(DateValue(Start!Text), -3), "mm/dd/yyyy")**

	The label shows **5/7/1985**, which is three days before the date in the **Start** box.

1. Change the **Text** property of the label to this expression:

	**Text(DateAdd(DateValue(Start!Text), 3, Months), "mm/dd/yyyy")**

	The label shows **8/10/1985**, which is three months after the date in the **Start** box. Instead of **Months**, specify **Quarters** or **Years** to identify a date that's a certain number of quarters or years before or after the date in the **Start** box.

## Calculate dates and times based on units ##

Calculate dates based on separate values for years, months, and days (for example, from [an external source](kratosapps-add-data.md)), or calculate times based on values for hours, minutes, and seconds.

**Calculate dates based on values for years, months, and days**

1. Add three dropdown lists, and name them **Year**, **Month**, and **Day**.

1. Set the **Items** property of the **Year** list to this expression:

	**Table({Year:"2014"}, {Year:"2015"}, {Year:"2016"})**

1. Set the **Items** property of the **Month** list to this expression:

	**Table({Month:"1"}, {Month:"2"}, {Month:"3"}, {Month:"4"}, {Month:"5"}, {Month:"6"}, {Month:"7"}, {Month:"8"}, {Month:"9"}, {Month:"10"}, {Month:"11"}, {Month:"12"})**

1. Set the **Items** property of the **Day** list to this expression:

	**Table({Day:"1"}, {Day:"2"}, {Day:"3"}, {Day:"4"}, {Day:"5"}, {Day:"6"}, {Day:"7"}, {Day:"8"}, {Day:"9"}, {Day:"10"}, {Day:"11"}, {Day:"12"}, {Day:"13"}, {Day:"14"}, {Day:"15"}, {Day:"16"}, {Day:"17"}, {Day:"18"}, {Day:"19"}, {Day:"20"}, {Day:"21"}, {Day:"22"}, {Day:"23"}, {Day:"24"}, {Day:"25"}, {Day:"26"}, {Day:"27"}, {Day:"28"}, {Day:"29"}, {Day:"30"}, {Day:"31"})**

1. Add a label, and set its **Text** property to this function:

	**Text(Date(Value(Year!Selected!Value), Value(Month!Selected!Value), Value(Day!Selected!Value)), DateTimeFormat!LongDate)**

	**Wednesday, January 1, 2014** appears by default. If you choose different options in the dropdown lists, the label reflects your changes.

You might need to convert data that you didn't expect. If you create input-text boxes instead of drop-down lists, for example, a user might specify an impossible date, such as May 45.

The **Date** function handles atypical data in these ways:

- If a year value is between 0 and 1899 (inclusive), the function adds that value to 1900 to calculate the year.

- If a year value is between 1900 and 9999 (inclusive), the function uses that value as the year.

- If a year value is less than 0 or is 10000 or greater, the function returns an error value.

- If a month value is greater than 12, the function adds that number of months to the first month of the specified year.

- If a month value is less than 1, the function subtracts that many months, plus 1, from the first month of the specified year.

- If a day value is greater than the number of days in the specified month, the function adds that many days to the first day of the month and returns the corresponding date from a subsequent month.

- If a day value is less than 1, the function subtracts that many days, plus 1, from the first day of the specified month.

**Calculate times based on values for hours, minutes, and seconds**

1. Add two dropdown lists, and name them **Hour** and **Minute**.

1. Set the **Items** property of the **Hour** list to this expression:

	**Table({Hour:"9"}, {Hour:"10"}, {Hour:"11"}, {Hour:"12"}, {Hour:"13"}, {Hour:"14"}, {Hour:"15"}, {Hour:"16"}, {Hour:"17"})**

1. Set the **Items** property of the **Minute** list to this expression:

	**Table({Minute:"0"}, {Minute:"15"}, {Minute:"30"}, {Minute:"45"})**

1. Add a label, and set its **Text** property to this expression:

	**Text(Time(Value(Hour!Selected!Value), Value(Minute!Selected!Value), 0), DateTimeFormat!ShortTime)**

1. Choose **15** in the **Hour** list and **45** in the **Minute** list.

	The label shows **3:45 PM**.

You can add entries to the lists so that users can specify a bigger range of hours and a more precise number of minutes. You can also add a third dropdown list so that users can specify seconds. If you add a **Second** list, change the **Text** property of the label to this expression:

**Text(Time(Value(Hour!Selected!Value), Value(Minute!Selected!Value), Value(Second!Selected!Value)), DateTimeFormat!LongTime)**

## Separate dates and times into units ##

Separate dates (for example, from [an external source](kratosapps-add-data.md)) into values for years, months, and days, or separate times into values for hours, minutes, and seconds.

**Separate dates into values for years, months, and days**

1. Add an input-text box, name it **Source**, and then type your birthday into it (for example, 5/10/1985).

1. Add three labels, and set the **Text** property of each label to one of these expressions:

	- **Month(DateValue(Source!Text))**

	- **Day(DateValue(Source!Text))**

	- **Year(DateValue(Source!Text))**

	Each label shows the month, day, or year of the date you specified.

1. (optional) Type **3/13/2017** in the **Source** box, and then set the **Text** property of each label to one of these expressions:

	- **If(Month(DateValue(Source!Text))<4 || Month(DateValue(Source!Text))>10, "Off-peak bookings are 20% cheaper!")**

	The message between quotation marks appears if the **Source** date is anywhere in January, February, March, October, November or December.

	- **If(Day(DateValue(Source!Text))=13, "Bookings for the 13th of any month are 35% off!")**

	The message between quotation marks appears if the **Source** date falls on the 24th day of any month in any year.

	- **If(Year(DateValue(Source!Text))=2017, "Celebrating 40 years in business with 10% off all 2017 bookings!")**

	The message between quotation marks appears if the **Source** date is anywhere in the year 2017.

**Separate times into values for hours, minutes, and seconds**

1. Add an input-text box, name it **Source**, and then type **6:15:24 AM** into it.

1. Add three labels, and set the **Text** property of each label to one of these expressions:

	- **Hour(DateTimeValue(Source!Text))**

	This label shows **6**, which represents the number of hours past midnight in the time you specified.

	- **Minute(DateTimeValue(Source!Text))**

	This label shows **15**, which represents the number of minutes past the hour in the time you specified.

	- **Second(DateTimeValue(Source!Text))**

	This label shows **24**, which represents the number of seconds past the minute in the time you specified.
