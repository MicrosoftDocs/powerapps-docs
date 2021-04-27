---
title: "Sample: Pass multiple values to a  web resource through the data parameter (model-driven apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "The sample represents a technique to pass the additional values within a single parameter and then process them within your web resource." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: powerapps
ms.topic: "article"
author: "KumarVivek" # GitHub ID
ms.author: "kvivek" # MSFT alias of Microsoft employees only
manager: "shilpas" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Sample: Pass multiple values to a  web resource through the data parameter

<!-- https://docs.microsoft.com/dynamics365/customer-engagement/developer/sample-pass-multiple-values-web-resource-through-data-parameter -->

An (HTML) web resource page can only accept a single custom parameter called `data`. To pass more than one value in the data parameter, you need to encode the parameters and decode the parameters in your page.  
  
 The page here represents a technique to pass the additional values within a single parameter and then process them within your web resource. 
  
## Sample HTML web resource  
 The HTML code below represents a webpage (HTML) web resource that includes a script that defines three functions:  
  
- **getDataParam**: Called from the `body.onload` event, this function retrieves any query string parameters passed to the page and locates one named `data`.  
  
- **parseDataValue**: Receives the data parameter from `getDataParam` and builds a DHTML table to display any values passed within the `data` parameter.  
  
  > [!NOTE]
  >  All characters included in the query string will be encoded using the [encodeURIComponent method](https://msdn.microsoft.com/library/xh9be5xc\(v=VS.85\).aspx). This function uses the JavaScript [decodeURIComponent method](https://msdn.microsoft.com/library/91b80x6x\(VS.85\).aspx) to decode the values passed.  
  
- **noParams**: Displays a message when no parameters are passed to the page.  
  
```html  
<!DOCTYPE html >  
<html lang="en-us">  
<head>  
 <title>Show Data Parameters Page</title>  
 <style type="text/css">  
  body  
  {  
   font-family: Segoe UI, Tahoma, Arial;  
   background-color: #d6e8ff;  
  }  
  tbody  
  {  
   background-color: white;  
  }  
  th  
  {  
   background-color: black;  
   color: White;  
  }  
 </style>  
 <script type="text/javascript">  
  document.onreadystatechange = function () {  
   if (document.readyState == "complete") {  
    getDataParam();  
   }  
  }  
  
  function getDataParam() {  
   //Get the any query string parameters and load them  
   //into the vals array  
  
   var vals = new Array();  
   if (location.search != "") {  
    vals = location.search.substr(1).split("&");  
    for (var i in vals) {  
     vals[i] = vals[i].replace(/\+/g, " ").split("=");  
    }  
    //look for the parameter named 'data'  
    var found = false;  
    for (var i in vals) {  
     if (vals[i][0].toLowerCase() == "data") {  
      parseDataValue(vals[i][1]);  
      found = true;  
      break;  
     }  
    }  
    if (!found)  
    { noParams(); }  
   }  
   else {  
    noParams();  
   }  
  }  
  
  function parseDataValue(datavalue) {  
   if (datavalue != "") {  
    var vals = new Array();  
  
    var message = document.createElement("p");  
    setText(message, "These are the data parameters values that were passed to this page:");  
    document.body.appendChild(message);  
  
    vals = decodeURIComponent(datavalue).split("&");  
    for (var i in vals) {  
     vals[i] = vals[i].replace(/\+/g, " ").split("=");  
    }  
  
    //Create a table and header using the DOM  
    var oTable = document.createElement("table");  
    var oTHead = document.createElement("thead");  
    var oTHeadTR = document.createElement("tr");  
    var oTHeadTRTH1 = document.createElement("th");  
    setText(oTHeadTRTH1, "Parameter");  
    var oTHeadTRTH2 = document.createElement("th");  
    setText(oTHeadTRTH2, "Value");  
    oTHeadTR.appendChild(oTHeadTRTH1);  
    oTHeadTR.appendChild(oTHeadTRTH2);  
    oTHead.appendChild(oTHeadTR);  
    oTable.appendChild(oTHead);  
    var oTBody = document.createElement("tbody");  
    //Loop through vals and create rows for the table  
    for (var i in vals) {  
     var oTRow = document.createElement("tr");  
     var oTRowTD1 = document.createElement("td");  
     setText(oTRowTD1, vals[i][0]);  
     var oTRowTD2 = document.createElement("td");  
     setText(oTRowTD2, vals[i][1]);  
  
     oTRow.appendChild(oTRowTD1);  
     oTRow.appendChild(oTRowTD2);  
     oTBody.appendChild(oTRow);  
    }  
  
    oTable.appendChild(oTBody);  
    document.body.appendChild(oTable);  
   }  
   else {  
    noParams();  
   }  
  }  
  
  function noParams() {  
   var message = document.createElement("p");  
   setText(message, "No data parameter was passed to this page");  
  
   document.body.appendChild(message);  
  }  
  //Added for cross browser support.  
  function setText(element, text) {  
   if (typeof element.innerText != "undefined") {  
    element.innerText = text;  
   }  
   else {  
    element.textContent = text;  
   }  
  
  }  
 </script>  
</head>  
<body>  
</body>  
</html>  
  
```  
  
#### Using this page  
  
1.  Create a webpage web resource called "new_/ShowDataParams.htm" using the sample code.  
  
     The parameters you want to pass are: `first=First Value&second=Second Value&third=Third Value`  
  
    > [!NOTE]
    >  If you’re adding static parameters using the Web Resource Properties dialog box from the form editor, you can simply paste the parameters without encoding them into the **Custom Parameter(data)** column. These values will be encoded for you, but you’ll still need to decode them and extract the values in your page.  
  
2.  For dynamic values generated in code, use the `encodeURIComponent` method on the parameters. The encoded values should be:  
  
     `first%3DFirst%20Value%26second%3DSecond%20Value%26third%3DThird%20Value`  
  
     Open the page passing the encoded parameters as the value of the data parameter:  
  
    ```  
    https://<server name>/WebResources/new_/ShowDataParams.htm?data=first%3DFirst%20Value%26second%3DSecond%20Value%26third%3DThird%20Value  
    ```  
  
    > [!NOTE]
    >  If you have added the web resource to a form and have pasted the un-encoded parameters into the **Custom Parameters(data)** column, you can just preview the form.  
  
3.  The `new_/ShowDataParams.htm` will display a dynamically generated table:  
  
    |Parameter|Value|  
    |---------------|-----------|  
    |first|First Value|  
    |second|Second Value|  
    |third|Third Value|  
  
### How it works  
 To access the values embedded within the data query string parameter value, in your webpage web resource you can extract the value of the data parameter and then use code to split the string into an array so you can access each name value pair individually.  
  
 When the page loads the `getDataParam` function is called. This function simply identifies the data parameter and passes the value to the `ParseDataValue` function. If no data parameter is found the `noParams` function will add a message to the page in place of the table.  
  
 The `ParseDataValue` function uses similar logic found in `getDataParam` to locate the custom parameter delimiters to create an array of name value pairs. Then it generates a table and appends it to the otherwise empty document.body.  
  
### See also  

 [Web Resources](web-resources.md)   
 [Sample: Import Files as Web Resources](sample-import-files-web-resources.md)   
 [Web Page (HTML) Web Resources](webpage-html-web-resources.md)   


[!INCLUDE[footer-include](../../includes/footer-banner.md)]