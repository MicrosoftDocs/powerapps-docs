---
title: "Use the ConditionExpression class (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Read how you can use the ConditionExpression class to compare a table column to a value or set of values by using an operator, such as &quot;equal to&quot; or &quot;greater than&quot;." # 115-145 characters including spaces. This abstract displays in the search result.
ms.date: 03/13/2022
ms.reviewer: "pehecke"

ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
search.audienceType: 
  - developer
---

# Use the ConditionExpression class

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

In Microsoft Dataverse, you can use the <xref:Microsoft.Xrm.Sdk.Query.ConditionExpression> class to compare a table column to a value or set of values by using an operator, such as "equal to" or "greater than". The `ConditionExpression` class lets you pass condition expressions as parameters to other classes, such as <xref:Microsoft.Xrm.Sdk.Query.QueryExpression> and <xref:Microsoft.Xrm.Sdk.Query.FilterExpression>.  
  
 The following table lists the properties you can set to create a condition using the `ConditionExpression` class.  
  
|Property|Description|  
|--------------|-----------------|  
|<xref:Microsoft.Xrm.Sdk.Query.ConditionExpression.AttributeName>|Specifies the logical name of the column in the condition expression.|  
|<xref:Microsoft.Xrm.Sdk.Query.ConditionExpression.Operator>|Specifies the condition operator. This is set by using the <xref:Microsoft.Xrm.Sdk.Query.ConditionOperator> enumeration.|  
|<xref:Microsoft.Xrm.Sdk.Query.ConditionExpression.Values>|Specifies the values of the column.|  
  
 When using the <xref:Microsoft.Xrm.Sdk.Query.FilterExpression.AddCondition(Microsoft.Xrm.Sdk.Query.ConditionExpression)> method (or the constructor for <xref:Microsoft.Xrm.Sdk.Query.ConditionExpression>), it's important to understand whether the array is being added as multiple values or as an array.  
  
 The following code example shows two different outcomes depending on how the array is used.  
  
```csharp  
string[] values = new string[] { "Value1", "Value2" };  
ConditionExpression c = new ConditionExpression("name", ConditionOperator.In, values);  
Console.WriteLine(c.Values.Count); //This will output 2   
string[] values = new string[] { "Value1", "Value2" }object value = values;  
ConditionExpression c = new ConditionExpression("name", ConditionOperator.In, value);  
Console.WriteLine(c.Values.Count); //This will output 1  
  
```  
  
 In some cases, it is necessary to cast to either `object[]` or `object`, depending on the desired behavior.  
  
 When you create a condition that compares a column value to an enumeration, such as a state code, you must use the `ToString` method to convert the value to a string.  
  
## Example: use the ConditionExpression class

 The following code example shows how to use the `ConditionExpression` class.  
  
```csharp  
  
//  Query using ConditionExpression    
ConditionExpression condition1 = new ConditionExpression();  
condition1.AttributeName = "lastname";    
condition1.Operator = ConditionOperator.Equal;    
condition1.Values.Add("Brown");                    
FilterExpression filter1 = new FilterExpression();    
filter1.Conditions.Add(condition1);    
QueryExpression query = new QueryExpression("contact");    
query.ColumnSet.AddColumns("firstname", "lastname");    
query.Criteria.AddFilter(filter1);    
EntityCollection result1 = _serviceProxy.RetrieveMultiple(query);    
Console.WriteLine();    
Console.WriteLine("Query using Query Expression with ConditionExpression and FilterExpression");    
Console.WriteLine("---------------------------------------");    
foreach (var a in result1.Entities)    
{  
      Console.WriteLine("Name: " + a.Attributes["firstname"] + " " + a.Attributes["lastname"]);    
}    
Console.WriteLine("---------------------------------------");  
```  
  
## Example: test for inactive state

 The following code example shows how to use the `ConditionExpression` class to test for the inactive state.  
  
```csharp  
  
ConditionExpression condition3 = new ConditionExpression();  
condition3.AttributeName = "statecode";  
condition3.Operator = ConditionOperator.Equal;  
condition3.Values.Add(AccountState.Active);  
  
```  

## Column comparison

The following example shows how to compare columns with the `ConditionExpression` class:

```csharp
public static EntityCollection ColumnComparisonExample(IOrganizationService service)
{
    QueryExpression query = new("contact")
    {
        Criteria = new FilterExpression(LogicalOperator.And)
        {
            Conditions = {
                {
                    new ConditionExpression(){
                        AttributeName = "firstname",
                        Operator = ConditionOperator.Equal,
                        CompareColumns = true,
                        Values = {
                            {"lastname"}
                        }
                    }
                }
            }
        }
    };
    return service.RetrieveMultiple(query);
}
```

By passing in `true` as the value for the [CompareColumns property](xref:Microsoft.Xrm.Sdk.Query.ConditionExpression.CompareColumns), the `value` is treated as the name of the second column to compare the values in `attributeName` to. The default value is false.

You can also set this property using the optional `compareColumns` `ConditionExpression` constructor. The following example creates a condition to return only records where the first and last names are the same,

```csharp
var expression = new ConditionExpression(
    attributeName: "firstname",
    conditionOperator: ConditionOperator.Equal,
    compareColumns: true,
    value: "lastname");
```

Leave out the `compareColumns` parameter, to create a condition to return only records where the first name is `John`.

```csharp
var expression = new ConditionExpression(
    attributeName: "firstname",
    conditionOperator: ConditionOperator.Equal,
    value: "John");
```

More information: [Use column comparison in queries](../column-comparison.md)

## Use Wildcard characters in conditions using string values

You can use wildcard characters when you construct queries using conditions on string values. More information: [Use wildcard characters in conditions for string values](../wildcard-characters.md)

### See also

[Building Queries](build-queries-with-queryexpression.md)<br />
[Build Queries with QueryExpression](build-queries-with-queryexpression.md)<br />
[Use the FilterExpression Class](use-filterexpression-class.md)<br />
<xref:Microsoft.Xrm.Sdk.Query.ConditionExpression>


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
