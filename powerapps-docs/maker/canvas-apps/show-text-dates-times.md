---
title: Show text, dates, and times in canvas apps
description: Learn about how to show text, dates, and times in a canvas app.
author: tapanm-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 08/17/2021
ms.subservice: canvas-maker
ms.author: tapanm
search.audienceType: 
  - maker
search.app: 
  - PowerApps
contributors:
  - tapanm-msft
---
# Show text, dates, and times in canvas apps
In Power Apps, add dates and times to a canvas app, and format them to show the right level of detail or to reflect your locale. Calculate the amount of time between two dates, or calculate a date that's a certain amount of time before or after a date that you specify. Convert dates to or from separate values for days, months, and years, and convert times to or from separate values for hours, minutes, and seconds.

For example, add data from users about stock trades or client meetings, data from an external source, or data from another app created in Power Apps. If that data includes times down to the millisecond, round it to the nearest minute for simplicity. Calculate how many days remain before a major milestone. If you want to schedule client meetings every five days, calculate those dates automatically. If May 10, 1985, is stored in separate fields for the day, the month, and the year, consolidate them into a single value. Conversely, break each date into separate values if your app manages them separately.

## Prerequisites

* [Sign up](../signup-for-powerapps.md) for Power Apps, and then [sign in](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc) by providing the same credentials that you used to sign up.
* Create an app or open an existing app in Power Apps.
* Learn how to [configure a control](add-configure-controls.md) in Power Apps.

## Show text in a Label control
Show text in a **[Label](controls/control-text-box.md)** control by setting the value of its **[Text](controls/properties-core.md)** property. Set this property by typing directly into the control or by typing an expression in the formula bar.

* If you type directly into the control, it shows exactly what you type.
* If you type an expression in the formula bar, the control shows the result of the expression.

Here are some examples.

1. Add a **[Label](controls/control-text-box.md)** control named **ShowText**, and set its **[Text](controls/properties-core.md)** property to this formula:
   <br>**Now()**
   
    If your computer is set to the "en-us" locale, the current date and time appears in this format:
    <br>*mm/dd/yyyy hh:mm AM/PM*
   
    If your computer is set to a locale such as "fr-fr", the current date and time appears in this format:
    <br>*dd/mm/yyyy hh:mm AM/PM*
2. Set the **[Text](controls/properties-core.md)** property of **ShowText** to this formula:
   <br>**DateDiff(Today(), DateValue("01/01/2020"))**
   
    ![Number of days between today and Jan. 1, 2020.](./media/show-text-dates-times/date-diff-text.png)
   
    The control shows the number of days between today and January 1, 2020, by using these functions:
   
   * **DateDiff**, which calculates the number of days, quarters, or years between two dates.
   * **Today**, which calculates the current day as a value.
   * **DateValue**, which converts a literal string, as shown between double quotation marks, to a value on which calculations can be performed.
3. Add a **[Text input](controls/control-text-input.md)** control named **BirthDate**, and move it under **ShowText**.

4. In **BirthDate**, type the month and the day of your birth (for example, **05/18**).

5. Set the **[Text](controls/properties-core.md)** property of **ShowText** to this formula:
   <br>**DateDiff(Today(), DateValue(BirthDate.Text))**
   
    ![Number of days between today and your birthday.](./media/show-text-dates-times/birth-diff.png)
   
    **ShowText** shows the number of days between today and whatever date you type into **BirthDate**. If your birthday has already occurred this year, **ShowText** displays a negative value.

## Format dates and times by using DateTimeValue
Convert dates and times from strings of text to values, which you can format in a variety of ways and use in calculations. Specify the format by using built-in and custom options.

> [!NOTE]
> The **[DateTimeValue](functions/function-datevalue-timevalue.md)** and **[DateValue](functions/function-datevalue-timevalue.md)** functions can convert dates in any of these formats into values:  
> 
> * MM/DD/YYYY  
> * DD/MM/YYYY  
> * DD Mon YYYY  
> * Month DD, YYYY  
> 
> 

1. Add a **[Text input](controls/control-text-input.md)** control named **ArrivalDateTime**, and type a date and time in this format:
   <br>**5/10/85 6:15 AM**
2. Add a **[Label](controls/control-text-box.md)** control named **ShowDate**, and set its **[Text](controls/properties-core.md)** property to this formula:
   <br>**DateTimeValue(ArrivalDateTime.Text)**
   
    ![Convert a date/time from text to a value.](./media/show-text-dates-times/date-value.png)
   
    **ShowDate** shows the same information that you typed, but it's been converted from text to a value and formatted differently. For example, the year appears as four digits instead of just two.
3. Change the **[Text](controls/properties-core.md)** property of **ShowDate** to this formula:
   <br>**DateTimeValue(ArrivalDateTime.Text, "fr")**
   
    ![Change ShowDate.](./media/show-text-dates-times/date-value-fr.png "Change ShowDate")
   
    **ShowDate** shows the day before the month, as a French user would expect.
   
   > [!TIP]
   > To display a list of other locales in Intellisense, remove the closing quotation mark and **fr** from the formula, but leave the open quotation mark:
   > 
   > ![Show a list of locales.](./media/show-text-dates-times/locale-list.png)
   > 
   > 
4. To use one of several built-in formats, change the **[Text](controls/properties-core.md)** property of **ShowDate** to this formula:
   <br>**Text(DateTimeValue(ArrivalDateTime.Text), DateTimeFormat.LongDateTime)**
   
    ![Use built-in formulas.](./media/show-text-dates-times/long-date-time.png "Use built-in formulas")
   
    **ShowDate** shows the day of the week, the date, and the time.
   
   > [!TIP]
   > The **DateTimeFormat** parameter supports several other built-in formats. To display that list, remove **LongDateTime** from the formula.
   > 
   > 
5. To use a custom format, change the **[Text](controls/properties-core.md)** property of **ShowDate** to this formula:
   <br>**Text(DateTimeValue(ArrivalDateTime.Text), "mm/dd/yyyy hh:mm:ss.fff AM/PM")**
   
    ![Use custom format.](./media/show-text-dates-times/format-milliseconds.png "Use custom format")
   
    **ShowDate** shows the date/time value in the format that you specified, including milliseconds.
   
   > [!TIP]
   > To round the time to the nearest tenth or hundredth of a second, specify **hh:mm:ss.f** or **hh:mm:ss.ff** in the formula.
   > 
   > 

## Format a date by using DateValue

1. Add a **[Text input](controls/control-text-input.md)** control named **ArrivalDate**, and then type a date in it (for example, **5/10/85**).

2. Add a **[Label](controls/control-text-box.md)** control named **FormatDate**, and set its **[Text](controls/properties-core.md)** property to this formula:
   <br>**DateValue(ArrivalDate.Text)**
   
    **FormatDate** shows the date that you typed, except the year appears as four digits.
3. Set the **[Text](controls/properties-core.md)** property of **FormatDate** to this formula:
   <br>**DateValue(ArrivalDate.Text, "fr")**
   
    **FormatDate** shows the day before the month, just as a French user would expect.
4. To use one of several built-in formats, set the **[Text](controls/properties-core.md)** property of **FormatDate** to this formula:
   <br>**Text(DateValue(ArrivalDate.Text), DateTimeFormat.LongDate)**
   
    **FormatDate** shows the day of the week, the month, the day, and the year.
5. To use a custom format, set the **[Text](controls/properties-core.md)** property of **FormatDate** to this formula:
   <br>**Text(DateValue(ArrivalDate.Text), "yy/mm/dd")**
   
    **FormatDate** shows the date in the format that you specified.

## Format a time using DateTimeValue

1. Add a **[Text input](controls/control-text-input.md)** control named **ArrivalTime**, and then type **6:15 AM** in it.

2. Add a **[Label](controls/control-text-box.md)** control named **ShowTime**.

3. To use one of several built-in formats, set the **[Text](controls/properties-core.md)** property of **ShowTime** to this formula:
   <br>**Text(DateTimeValue(ArrivalTime.Text), DateTimeFormat.LongTime)**
   
    **ShowTime** shows the time that you specified, including seconds.
4. To use a custom format, set the **[Text](controls/properties-core.md)** property of **ShowTime** to this formula:
   <br>**Text(DateTimeValue(ArrivalTime.Text), "hh:mm:ss.fff AM/PM")**
   
    **ShowTime** shows the time that you specified, including seconds and milliseconds.
   
   > [!TIP]
   > To round the time to the nearest tenth or hundredth of a second, enter **hh:mm:ss.f** or **hh:mm:ss.ff** in the formula.
   > 
   > 

## Show the time between dates

1. Add two **[Text input](controls/control-text-input.md)** controls named **Start** and **End**.

2. Type **4/1/2015** in **Start**, and type **1/1/2016** in **End**.

3. Add a **[Label](controls/control-text-box.md)** control named **DateDiff**, and set its **[Text](controls/properties-core.md)** property to this formula:
   <br>**DateDiff(DateValue(Start.Text), DateValue(End.Text))**
   
    ![Compare two dates.](./media/show-text-dates-times/date-diff.png)
   
    **DateDiff** shows **275**, which is the number of days between April 1, 2015, and January 1, 2016.
4. Set the **[Text](controls/properties-core.md)** property of **DateDiff** to this formula:  <br>**DateDiff(DateValue(Start.Text), DateValue(End.Text), Months)**
   
    **DateDiff** shows **9**, which is the number of months between April 1, 2015, and January 1, 2016. Replace **Months** with **Quarters** or **Years** to show the time in those units.

## Identify a date before or after another date

1. Add a **[Text input](controls/control-text-input.md)** control named **Start**, and type **5/10/1985** in it.

2. Add a **[Label](controls/control-text-box.md)** control named **DateAdd**, and set its **[Text](controls/properties-core.md)** property to this formula:
   <br>**DateAdd(DateValue(Start.Text), 3)**
   
    ![Add three days.](./media/show-text-dates-times/date-add.png)
   
    **DateAdd** shows **5/13/1985**, which is three days after the date in **Start**.
3. Set the **[Text](controls/properties-core.md)** property of **DateAdd** to this formula:
   <br>**DateAdd(DateValue(Start.Text), -3)**
   
    ![Subtract three days.](./media/show-text-dates-times/date-subtract.png)
   
    **DateAdd** shows **5/7/1985**, which is three days before the date in **Start**.
4. Change the **[Text](controls/properties-core.md)** property of **DateAdd** to this formula:
   <br>**DateAdd(DateValue(Start.Text), 3, Months)**
   
    ![Add three months.](./media/show-text-dates-times/date-add-months.png)
   
    The label shows **8/10/1985**, which is three months after the date in **Start**. Replace **Months** with **Quarters** or **Years** to identify a date that's the specified number of quarters or years before or after the date in **Start**.

## Calculate dates based on years, months, and days

1. Add three **[Drop down](controls/control-drop-down.md)** controls named **Year**, **Month**, and **Day**.

2. Set the **[Items](controls/properties-core.md)** property of **Year** to this formula:
   <br>**Table({Year:"2014"}, {Year:"2015"}, {Year:"2016"})**

3. Set the **[Items](controls/properties-core.md)** property of **Month** to this formula:
   <br>**Table({Month:"1"}, {Month:"2"}, {Month:"3"}, {Month:"4"}, {Month:"5"}, {Month:"6"}, {Month:"7"}, {Month:"8"}, {Month:"9"}, {Month:"10"}, {Month:"11"}, {Month:"12"})**

4. Set the **[Items](controls/properties-core.md)** property of **Day** to this formula:
   <br>**Table({Day:"1"}, {Day:"2"}, {Day:"3"}, {Day:"4"}, {Day:"5"}, {Day:"6"}, {Day:"7"}, {Day:"8"}, {Day:"9"}, {Day:"10"}, {Day:"11"}, {Day:"12"}, {Day:"13"}, {Day:"14"}, {Day:"15"}, {Day:"16"}, {Day:"17"}, {Day:"18"}, {Day:"19"}, {Day:"20"}, {Day:"21"}, {Day:"22"}, {Day:"23"}, {Day:"24"}, {Day:"25"}, {Day:"26"}, {Day:"27"}, {Day:"28"}, {Day:"29"}, {Day:"30"}, {Day:"31"})**

5. Add a **[Label](controls/control-text-box.md)** control, and set its **[Text](controls/properties-core.md)** property to this formula:
   <br>**Text(Date(Value(Year.SelectedText.Value), Value(Month.SelectedText.Value), Value(Day.SelectedText.Value)), DateTimeFormat.LongDate)**
   
    **Wednesday, January 1, 2014** is listed by default. Select different values in the **[Drop down](controls/control-drop-down.md)** controls to change the date in the **[Label](controls/control-text-box.md)** control.

You may need to convert data that you didn't expect. If you add **[Text input](controls/control-text-input.md)** controls instead of **[Drop down](controls/control-drop-down.md)** controls, a user may enter an incorrect date, such as May 45. The **[Date](functions/function-date-time.md)** function handles atypical data in the following ways:

* If a year value is between 0 and 1899 (inclusive), the function adds that value to 1900 to calculate the year.
* If a year value is between 1900 and 9999 (inclusive), the function uses that value as the year.
* If a year value is less than 0 or is 10000 or greater, the function returns an error value.
* If a month value is greater than 12, the function adds that number of months to the first month of the specified year.
* If a month value is less than 1, the function subtracts that many months, plus 1, from the first month of the specified year.
* If a day value is greater than the number of days in the specified month, the function adds that many days to the first day of the month and returns the corresponding date from a subsequent month.
* If a day value is less than 1, the function subtracts that many days, plus 1, from the first day of the specified month.

## Calculate times based on hours, minutes, and seconds

1. Add two **Drop-down** lists named **Hour** and **Minute**.

2. Set the **[Items](controls/properties-core.md)** property of **Hour** to this formula:
   <br>**Table({Hour:"9"}, {Hour:"10"}, {Hour:"11"}, {Hour:"12"}, {Hour:"13"}, {Hour:"14"}, {Hour:"15"}, {Hour:"16"}, {Hour:"17"})**

3. Set the **[Items](controls/properties-core.md)** property of **Minute** to this formula:
   <br>**Table({Minute:"0"}, {Minute:"15"}, {Minute:"30"}, {Minute:"45"})**

4. Add a **[Label](controls/control-text-box.md)** control, and set its **[Text](controls/properties-core.md)** property to this formula:  
   <br>**Text(Time(Value(Hour.Selected.Value), Value(Minute.Selected.Value), 0), DateTimeFormat.ShortTime)**

5. Select **15** in **Hour** and **45** in **Minute**.
   
    The **[Label](controls/control-text-box.md)** control shows **3:45 PM**.
   
    You can add entries to **Hour** and **Minute** so that users can select from a bigger range of hours and a more precise number of minutes. You can also add a third **[Drop down](controls/control-drop-down.md)** control so that users can specify seconds. If you add a third list, set the **[Text](controls/properties-core.md)** property of the **[Label](controls/control-text-box.md)** control to the following expression:<br>**Text(Time(Value(Hour.Selected.Value), Value(Minute.Selected.Value), Value(Second.Selected.Value)), DateTimeFormat.LongTime)**

### See also

[Date picker control examples](controls/control-date-picker.md#examples)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]