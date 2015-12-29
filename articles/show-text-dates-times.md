<properties
	pageTitle=" Show text and format a date or time in PowerApps | Microsoft PowerApps"
	description="Add and format dates and times using PowerApps"
	services=""
	suite="powerapps"
	documentationCenter=""
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/25/2015"
   ms.author="mandia"/>


# Show text and format dates and times in your app

Add dates and times, and format them to show the right level of detail or to reflect your locale. Calculate the amount of time between two dates, or calculate a date that's a certain amount of time before or after a date that you specify. Convert dates to or from separate values for days, months, and years, and convert times to or from separate values for hours, minutes, and seconds.

For example, add data from users about stock trades or client meetings, data from an external source, or data from another app created in PowerApps. If that data includes times down to the millisecond, round it to the nearest minute for simplicity. Calculate how many days remain before a major milestone. If you want to schedule client meetings every five days, calculate those dates automatically. If May 10, 1985, is stored in separate fields for the day, the month, and the year, consolidate them into a single value. Conversely, break each date into separate values if your app manages them separately.

### Prerequisites

- Install [PowerApps](http://aka.ms/powerappsinstall) and sign-in with your work or organization account.
- Create a new app or open an existing app in PowerApps.
- To familiarize yourself with configuring controls in PowerApps, step through the [configure a control](get-started-test-drive.md#configure-a-control).

## Show text in a label
Show text in a label by setting the value of its **Text** property. You can set this property by typing directly into the label or by entering an expression in the Function Bar. If you type directly into the label, it shows exactly what you type. If you enter an expression, the label shows the result of the expression.

Here are some examples.

1. On the **Insert** tab, select **Label**, and rename it to **ShowText**:  
![][2]  
![][3]  

2. Set the **Text** property to the following expression:  
```DateDiff(Today(), DateValue("01/01/2020"))```  
![][4]  

	The label shows the number of days between today and January 1, 2020. This expression uses the following functions:  

	Function | Description
--- | ---
DateDiff | Calculates the number of days, quarters, or years between two dates.
Today | Calculates the current day as a value.
DateValue | Converts a literal string, as shown between quotation marks, to a value on which calculations can be performed.

3. On the **Insert** tab, select **Text**, and select **Input Text**. Rename it to **Birthdate**:  
![][5]  
![][6]  

4. Move the Birthdate text so all controls are shown.
5. In the **ShowText** label (created in step 1), set its **Text** property to the following expression:    
```DateDiff(Today(), DateValue(Birthdate!Text))```  

	![][7]  

	This expression shows the number of days between today and whatever date you type into Birthdate. When you type a date into **Birthdate**, the Text property is automatically set to that value.

5. In **Birthdate**, enter the month and day of your birthday. **ShowText** shows the number of days between today and the birth date you enter. You can type in text (March 17) or enter number date (3/17). If you don't enter a year, the current year is assumed.

In these steps, you:

- Used the DateDiff, DateValue, and Today functions to show different date calculations.
- Used a "ShowText" label that is updated to show the output or calculated values from another input text control.

## Working with dates and times
In this section, we're going demonstrate different date and time functions, including DateTimeValue, DateTimeFormat, and more. The best way to see and use these functions is to create a blank screen within your app.

Let's get started.

### Format date and time values
There are many functions you can use to format dates and times. You can even use custom formats. This section provides some examples of using dates and times with your apps. We suggest creating a blank screen and stepping through the different scenarios.

#### Format date time using the DateTimeValue, DateTimeFormat, and DateValue functions

> [AZURE.NOTE] The **DateTimeValue** and **DateValue** functions can convert dates in any of the following formats into values:  
> - MM/DD/YYYY  
> - DD/MM/YYYY  
> - DD Mon YYYY  
> - Month DD, YYYY  

1. From the **Insert** tab, select **Text**, select **Input Text**, and rename it to **ArrivalDateTime**.
2. Directly in **ArrivalDateTime**, enter a date, a space, and a time. For example, enter ```5/10/85 6:15 AM```.
3. Add a label, and set its **Text** property to the following expression:   
```DateTimeValue(ArrivalDateTime!Text)```  <br/>
	![][10]  

	The label shows the same information that you typed, but it's been converted from text to a value (as the next step demonstrates):  
	![][11]  

4. Change the **Text** property of the label to the following expression:  
```DateTimeValue(ArrivalDateTime!Text, "fr")```

	The label shows the day and then the month, as expected for a French user:  
	![][12]  
	> [AZURE.TIP] To use intellisense to see the other locales, in the expression in the function bar, remove the *closing quotation mark* and *fr*; but leave the *open quotation mark*:  
	>![][13]  

5. To use one of several built-in formats, change the **Text** property of the label to the following expression:  
```Text(DateTimeValue(ArrivalDateTime!Text), DateTimeFormat!LongDateTime)```

	![][14]  
	The label shows the day of the week, the date, and the time:  
	![][15]  

	> [AZURE.TIP] The **DateTimeFormat** parameter supports several other built-in formats. To use intellisense to see the other formats, remove *LongDateTime* from the Text property in the function bar.

6. To use a custom format, change the **Text** property of the label to the following expression:  
```Text(DateTimeValue(ArrivalDateTime!Text), "mm/dd/yyyy hh:mm:ss.fff AM/PM")```  

	![][16]  

	The label shows the format you entered, including milliseconds:  
	![][17]  

	> [AZURE.TIP] To round the time to the nearest tenth or hundredth of a second, enter **hh:mm:ss.f** or **hh:mm:ss.ff** in the expression.

#### Format a date using the DateValue and DateTimeFormat functions
1. Add an **Input Text** box, name it ArrivalDate, and then type in a date. For example, enter ```5/10/85```.
2. Add a label, and set its **Text** property to the following expression:  
```DateValue(ArrivalDate!Text)```  <br/>
	The label shows the date that you typed, and formatted it to include the full year.

3. Change the **Text** property of the label to the following expression:  
```DateValue(ArrivalDate!Text, "fr")```  
	Now you see the day, the month, and the year, just as a French user would.
4. To use one of several built-in formats, change the **Text** property of the label to the following expression:  
```Text(DateValue(ArrivalDate!Text), DateTimeFormat!LongDate)```

	The label shows the day of the week, in addition to the month, the day, and the year.

5. To use a custom format, change the **Text** property of the label to the following expression:  
```Text(DateValue(ArrivalDate!Text), "mm/dd/yy")```

	The label shows the date that you entered in the format that you entered.

#### Format a time using the DateTimeValue and DateTimeFormat functions

1. Add an **Input Text** box, name it ArrivalTime, and then type in 6:15 AM.
2. To use one of several built-in formats, set the **Text** property of the label to the following expression:  
```Text(DateTimeValue(ArrivalTime!Text), DateTimeFormat!LongTime)```

	The label shows 6:15:00 AM.

3. To use a custom format, change the **Text** property of the label to the following expression:  
```Text(DateTimeValue(ArrivalTime!Text), "hh:mm:ss.fff AM/PM")```

	The label shows 06:15:00.000 AM.

	> [AZURE.TIP] To round the time to the nearest tenth or hundredth of a second, enter **hh:mm:ss.f** or **hh:mm:ss.ff** in the expression.


### Compare dates using the DateDiff and DateAdd functions
Use the DateDiff function to calculate time between dates, or use the DateAdd function to identify the date that's a certain number of days, months, quarters, or years before or after a specified date.

#### Show the time between dates

1. Add two **Input Text** boxes. Rename them **Start** and **End**.
2. In **Start**, type ```4/1/2015```. In **End**, type ```1/1/2016```.
3. Add a label, and set its **Text** property to the following function:  
```DateDiff(DateValue(Start!Text), DateValue(End!Text))```

	The label shows **275**, which is the number of days between April 1, 2015, and January 1, 2016:  
	![][18]
4. Change the **Text** property of the label to the following function:  
```DateDiff(DateValue(Start!Text), DateValue(End!Text), Months)```

	The label shows **9**, which is the number of months between April 1, 2015, and January 1, 2016. Instead of Months, choose **Quarters** or **Years** to show the time in those units.


#### Identify a date before or after another date

1. Add an **Input Text** box. Name it **Start**, and type ```5/10/1985``` in the text box.
2. Add a label, and set its **Text** property to the following expression:  
```Text(DateAdd(DateValue(Start!Text), 3), "mm/dd/yyyy")```

	The label shows **5/13/1985**, which is three days *after* the date in the Start box.

3. Change the **Text** property of the label to the following expression:  
```Text(DateAdd(DateValue(Start!Text), -3), "mm/dd/yyyy")```

	The label shows **5/7/1985**, which is three days *before* the date in the Start box.

4. Change the **Text** property of the label to the following expression:  
```Text(DateAdd(DateValue(Start!Text), 3, Months), "mm/dd/yyyy")```

	The label shows **8/10/1985**, which is three months *after* the date in the Start box. Instead of Months, choose **Quarters** or **Years** to identify a date that's the number of quarters or years before or after the date in the Start box.


### Calculate dates and times using the Date and Time functions
Use a Table within drop-down lists to select a differet day, month, and year. You can then use the Text and Date functions to display the output based on the choices in the drop-down lists. You can also calculate dates based on separate values for years, months, and days, even from from an external source. For example, you can use "sale" dates, month-end dates, or inventory restocking dates.

#### Calculate dates based on years, months, and days using the Date function

1. From the **Insert** menu, **Controls**, add three **Drop-down** lists. Name them **Year**, **Month**, and **Day**.
2. Set the **Items** property of the **Year** list to the following expression:  
```Table({Year:"2014"}, {Year:"2015"}, {Year:"2016"})```  

3. Set the **Items** property of the **Month** list to the following expression:  
```Table({Month:"1"}, {Month:"2"}, {Month:"3"}, {Month:"4"}, {Month:"5"}, {Month:"6"}, {Month:"7"}, {Month:"8"}, {Month:"9"}, {Month:"10"}, {Month:"11"}, {Month:"12"})```  

4. Set the **Items** property of the **Day** list to the following expression:  
```Table({Day:"1"}, {Day:"2"}, {Day:"3"}, {Day:"4"}, {Day:"5"}, {Day:"6"}, {Day:"7"}, {Day:"8"}, {Day:"9"}, {Day:"10"}, {Day:"11"}, {Day:"12"}, {Day:"13"}, {Day:"14"}, {Day:"15"}, {Day:"16"}, {Day:"17"}, {Day:"18"}, {Day:"19"}, {Day:"20"}, {Day:"21"}, {Day:"22"}, {Day:"23"}, {Day:"24"}, {Day:"25"}, {Day:"26"}, {Day:"27"}, {Day:"28"}, {Day:"29"}, {Day:"30"}, {Day:"31"})```  

5. Add a label, and set its **Text** property to the following function:  
```Text(Date(Value(Year!Selected!Value), Value(Month!Selected!Value), Value(Day!Selected!Value)), DateTimeFormat!LongDate)```

	**Wednesday, January 1, 2014** is listed by default. Choose different options in the dropdown lists to update the label:  
	![][19]

You may need to convert data that you didn't expect. If you create **Input Text** boxes instead of Drop-down lists, a user may enter an incorrect date, such as May 45. The **Date** function handles atypical data in the following ways:

- If a year value is between 0 and 1899 (inclusive), the function adds that value to 1900 to calculate the year.
- If a year value is between 1900 and 9999 (inclusive), the function uses that value as the year.
- If a year value is less than 0 or is 10000 or greater, the function returns an error value.
- If a month value is greater than 12, the function adds that number of months to the first month of the specified year.
- If a month value is less than 1, the function subtracts that many months, plus 1, from the first month of the specified year.
- If a day value is greater than the number of days in the specified month, the function adds that many days to the first day of the month and returns the corresponding date from a subsequent month.
- If a day value is less than 1, the function subtracts that many days, plus 1, from the first day of the specified month.


#### Calculate times based on hours, minutes, and seconds using the Time function

1. From the **Insert** menu, **Controls**, add two **Drop-down** lists. Name them **Hour** and **Minute**.
2. Set the **Items** property of the **Hour** list to the following expression:  
```Table({Hour:"9"}, {Hour:"10"}, {Hour:"11"}, {Hour:"12"}, {Hour:"13"}, {Hour:"14"}, {Hour:"15"}, {Hour:"16"}, {Hour:"17"})```

3. Set the **Items** property of the **Minute** list to the following expression:  
```Table({Minute:"0"}, {Minute:"15"}, {Minute:"30"}, {Minute:"45"})```

4. Add a label, and set its **Text** property to the following expression:  
```Text(Time(Value(Hour!Selected!Value), Value(Minute!Selected!Value), 0), DateTimeFormat!ShortTime)```

5. Choose 15 in the Hour list and 45 in the Minute list. The label shows **3:45 PM**:  
![][20]

	You can add entries to the lists so that users can choose a bigger range of hours and a more precise number of minutes. You can also add a third dropdown list so that users can choose seconds. If you add a third list, change the **Text** property of the label to the following expression:  
	```Text(Time(Value(Hour!Selected!Value), Value(Minute!Selected!Value), Value(Second!Selected!Value)), DateTimeFormat!LongTime)```

## More examples and fun stuff

Task | Steps | Output
--- | --- | ---
Use the **Now** function to display the current date and time | On the **Insert** tab, add a **Label**, and rename it to **MyLabel**. Set the **Text** property of the label to this function:<br>```Now()```<br><br>![][8] | The date and time displayed depends on your computer's localization settings:  <ul><li>For the "en" locale, the date and time is ```5/10/2015 5:27 PM``` (month/day/year).</li><li>If using another locale, like "fr", it displays as ```10/5/2015 5:27 PM``` (day/month/year).</li></ul>
Enter a date and a time, and show them in another label  | <ol><li>On the **Insert** tab, select **Text**, add two **Input Text** boxes, and name them **ArrivalDate** and **ArrivalTime**.</li><li>In **ArrivalDate**, type in a date. For example, enter ```5/10/85```. </li><li>In **ArrivalTime**, type in a time. For example, enter ```6:15 AM```.</li><li>From the **Insert** tab, add a **Label**, and set its **Text** property to the following expression: ```"The product was launched on " & ArrivalDate!Text & " at " & ArrivalTime!Text & "."```</li></ol> | When done, your screen looks similar to this example: ![][9]  


## Tips and Tricks
- At anytime, you can select the Preview button (![][1]) to see what you've created. You can also test your controls.
- When designing your app, you can re-size the controls and move them around using click-and-drag.
- When working with dates and times, there are many built-in functions that let you get creative with your output. For example, you can use LongDateTime, LongTime, and even create your own custom format.

## What you learned
In this topic, you:

- Displayed text in a label by typing it directly in the label, and by using the label to show output from another control. In this example, we used an Input Text box with an Excel-like expression and displayed the output in the label.
- Formatted different date and time values to include different languages, show milliseconds, calculate days and months between dates, calculate time in hours and minutes, and more.
- Used different date and time functions, including DateDiff, DateValue, Today,   DateTimeValue, DateValue, DateAdd, Date, and Time.


[1]: ./media/show-text-dates-times/preview.png
[2]: ./media/show-text-dates-times/label.png
[3]: ./media/show-text-dates-times/renamelabel.png
[4]: ./media/show-text-dates-times/datedifftext.png
[5]: ./media/show-text-dates-times/inputtext.png
[6]: ./media/show-text-dates-times/renamebirthdate.png
[7]: ./media/show-text-dates-times/birthdateexpression.png
[8]: ./media/show-text-dates-times/textnow2.png
[9]: ./media/show-text-dates-times/datetimeprompt2.png
[10]: ./media/show-text-dates-times/textdatetimevalue.png
[11]: ./media/show-text-dates-times/datelabelinputtext.png
[12]: ./media/show-text-dates-times/datelabelfr.png
[13]: ./media/show-text-dates-times/otherlocales.png
[14]: ./media/show-text-dates-times/longdate.png
[15]: ./media/show-text-dates-times/longdatelabel.png
[16]: ./media/show-text-dates-times/custom.png
[17]: ./media/show-text-dates-times/milliseconds.png
[18]: ./media/show-text-dates-times/datediff.png
[19]: ./media/show-text-dates-times/datedropdownlists.png
[20]: ./media/show-text-dates-times/timedropdownlists.png
