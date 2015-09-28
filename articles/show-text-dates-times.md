<properties
	pageTitle=" Identify current user, show text, and format a date or time value in PowerApps | Microsoft Azure"
	description=""
	services="power-apps"
	documentationCenter=""
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="power-apps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload=""
   ms.date="09/24/2015"
   ms.author="mandia"/>

# THIS TOPIC IS IN PROGRESS

https://github.com/AFTOwen/kratosapps-content-pr/blob/old/articles/kratosapps-manage-dates.md

# Identify current user, show text, and format a date or time value

Add dates and times, and format them to show the right level of detail or to reflect your locale. Calculate the amount of time between two dates, or calculate a date that's a certain amount of time before or after a date that you specify. Convert dates to or from separate values for days, months, and years, and convert times to or from separate values for hours, minutes, and seconds.

For example, add data from users about stock trades or client meetings, data from an external source, or data from another app created in KratosApps Studio. If that data includes times down to the millisecond, round it to the nearest minute for simplicity. Calculate how many days remain before a major milestone. If you want to schedule client meetings every five days, calculate those dates automatically. If May 10, 1985, is stored in separate fields for the day, the month, and the year, consolidate them into a single value. Conversely, break each date into separate values if your app manages them separately.

### Prerequisites 

- Install PowerApps. Create a new app or open an existing app in PowerApps.
- To familiarize yourself with PowerApps and creating apps, step through the [Test Drive](get-started-test-drive.md ). It walks you through performing some key tasks.


## Show text in a label
Show text in a label by setting the value of its Text property. You can set this property by typing directly into the label or by specifying an expression in the Function Bar. If you type directly into the label, it shows exactly what you type. If you specify an expression, the label shows the result of the expression.

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

4. In the **ShowText** label (created in step 1), set its **Text** property to the following expression:    
```DateDiff(Today(), DateValue(Birthdate!Text))```  

	![][7]  

	This expression shows the number of days between today and whatever date you type into Birthdate. When you type a date into **Birthdate**, the Text property is automatically set to that value.

5. In **Birthdate**, enter the month and day of your birthday. **ShowText** shows the number of days between today and the birth date you enter.

In these steps, you:

- Used the DateDiff, DateValue, and Today functions to show different date calculations.
- Used a "ShowText" label that is updated to show the output or calculated values from another input text control. 


## Working with dates and times
In this section, we're going demonstrate different date and time functions, including DateTimeValue, DateTimeFormat, and more. The best way to see and use these functions is to create a blank screen within PowerApps. 

Let's get started.

### Use the DateTimeValue, DateTimeFormat, and DateValue functions to format a date and a time

> [AZURE.NOTE] The **DateTimeValue** and **DateValue** functions can convert dates in any of the following formats into values: 
> - MM/DD/YYYY
> - DD/MM/YYYY
> - DD Mon YYYY
> - Month DD, YYYY

1. From the **Insert** tab, select **Text**, add an **Input Text** box, and rename it to **ArrivalDateTime**.
2. In **ArrivalDateTime**, enter a date, a space, and a time. For example, enter ```5/10/85 6:15 AM```. 
3. Add a label, and set its **Text** property to the following expression:   
```DateTimeValue(ArrivalDateTime!Text)```  <br/>
	![][10]  

	The label shows the same information that you typed, but it's been converted from text to a value (as the next step demonstrates):  
	![][11]  

4. Change the **Text** property of the label to the following expression:  
```DateTimeValue(ArrivalDateTime!Text, "fr")```

	The label shows the day before the month, as expected for a French user:  
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

### Use the DateValue and DateTimeFormat functions to format a date
1. Add an **Input Text** box, name it ArrivalDate, and then in a date. For example, enter ```5/10/85```.
2. Add a label, and set its **Text** property to the following expression:  
```DateValue(ArrivalDate!Text)```  <br/>
	The label shows the date that you typed, followed by 12:00 AM. 

4. Change the **Text** property of the label to the following expression:  
```DateValue(ArrivalDate!Text, "fr")```

5. To use one of several built-in formats, change the **Text** property of the label to the following expression:  
```Text(DateValue(ArrivalDate!Text), DateTimeFormat!LongDate)```

	The label shows the day of the week, in addition to the month, the day, and the year.

6. To use a custom format, change the Text property of the label to the following expression:  
```Text(DateValue(ArrivalDate!Text), "mm/dd/yy")```

	The label shows the date that you entered in the format that you specified.

### Use the DateTimeValue and DateTimeFormat functions to format a time

1. Add an **Input Text** box, name it ArrivalTime, and then type in 6:15 AM.
2. To use one of several built-in formats, set the **Text** property of the label to the following expression:  
```Text(DateTimeValue(ArrivalTime!Text), DateTimeFormat!LongTime)```

	The label shows 6:15:00 AM.

3. To use a custom format, change the **Text** property of the label to the following expression:  
```Text(DateTimeValue(ArrivalTime!Text), "hh:mm:ss.fff AM/PM")```

	The label shows 06:15:00.000 AM.

	> [AZURE.TIP] To round the time to the nearest tenth or hundredth of a second, enter **hh:mm:ss.f** or **hh:mm:ss.ff** in the expression.


## More examples and fun stuff with dates and times

Task | Steps | Output
--- | --- | ---
Use the Now function to display the current date and time | On the **Insert** tab, add a **Label**, and rename it to **MyLabel**. Set the **Text** property of the label to ```Now()```: <br/>![][8] | The date and time displayed depends on your computer's localization settings:  <ul><li>For the "en" locale, the date and time is ```5/10/2015 5:27 PM``` (month/day/year).</li><li>If using another locale, like "fr", it displays as ```10/5/2015 5:27 PM``` (day/month/year).</li></ul>
Enter a date and a time, and have them displayed in another label  | <ol><li>On the **Insert** tab, select **Text**, add two **Input Text** boxes, and name them **ArrivalDate** and **ArrivalTime**.</li><li>In **ArrivalDate**, type in a date. For example, enter ```5/10/85```. </li><li>In **ArrivalTime**, type in a time. For example, enter ```6:15 AM```.</li><li>From the **Insert** tab, add a **Label**, and set its **Text** property to the following expression: ```"The product was launched on " & ArrivalDate!Text & " at " & ArrivalTime!Text & "."```</li></ol> | When done, your screen looks similar to the following: ![][9]  

#### Use the Now function to display the current date and time
On the **Insert** tab, add a **Label**, and rename it to **MyLabel**. Set the **Text** property of the label to ```Now()```:  
![][8]

The date and time displayed depends on your computer's localization settings: 
- For the "en" locale, the date and time is ```5/10/2015 5:27 PM``` (month / day / year).
- If using another locale, like "fr", it displays as ```10/5/2015 5:27 PM``` (day / month / year).

#### Enter a date and a time, and have them displayed in another label 
1. On the **Insert** tab, select **Text**, add two **Input Text** boxes, and name them **ArrivalDate** and **ArrivalTime**.
2. In **ArrivalDate**, type in a date. For example, enter ```5/10/85```. 
3. In **ArrivalTime**, type in a time. For example, enter ```6:15 AM```.
4. From the **Insert** tab, add a **Label**, and set its **Text** property to the following expression:  
```"The product was launched on " & ArrivalDate!Text & " at " & ArrivalTime!Text & "."```  

When done, your screen looks similar to the following:  
![][9]  

[1]: ./media/show-text-dates-times/preview.png
[2]: ./media/show-text-dates-times/label.png
[3]: ./media/show-text-dates-times/renamelabel.png
[4]: ./media/show-text-dates-times/datedifftext.png
[5]: ./media/show-text-dates-times/inputtext.png
[6]: ./media/show-text-dates-times/renamebirthdate.png
[7]: ./media/show-text-dates-times/birthdateexpression.png
[8]: ./media/show-text-dates-times/textnow.png
[9]: ./media/show-text-dates-times/datetimeprompt.png
[10]: ./media/show-text-dates-times/textdatetimevalue.png
[11]: ./media/show-text-dates-times/datelabelinputtext.png
[12]: ./media/show-text-dates-times/datelabelfr.png
[13]: ./media/show-text-dates-times/otherlocales.png
[14]: ./media/show-text-dates-times/longdate.png
[15]: ./media/show-text-dates-times/longdatelabel.png
[16]: ./media/show-text-dates-times/custom.png
[17]: ./media/show-text-dates-times/milliseconds.png

