---
title: "Pass multiple values to a web resource through the data parameter"
description: "Learn how to encode multiple values in a single data parameter and decode them in your web resource. Includes HTML sample code and implementation steps."
author: anushikhas96
ms.author: anushisharma
ms.date: 03/27/2026
ms.reviewer: jdaly
ms.topic: sample
ms.subservice: mda-developer
search.audienceType: 
  - developer
---
# Pass multiple values to a web resource through the data parameter

An (HTML) web resource page can only accept a single query parameter called `data`. To pass more than one value in the data parameter, you need to encode the parameters and decode the parameters in your page.  
  
The [HTML web resource sample](#html-web-resource-sample) demonstrates a technique to pass the additional values within a single parameter and then process them within your web resource.
 
> [!NOTE]
> Only alphanumeric characters are supported as parameters to web resources. All characters included in the query string go through validation to ensure the validity of the parameters passed. If the validation process finds any invalid parameters, the request fails. For example, passing text values enclosed in angular brackets is considered an invalid parameter type.
  
## HTML web resource sample

 The following HTML code represents a webpage (HTML) web resource that includes a script that defines four functions:  
  
- **displayDataParameters**: Called when the DOM is ready, this function uses the URLSearchParams API to extract and parse the `data` parameter from the query string, then displays the results.  
  
- **showMessage**: Creates and displays informational messages to the user, such as error messages or status updates.  
  
- **createParametersTable**: Receives parsed parameters and generates an HTML table using template literals and modern array methods to display the parameter name-value pairs.  
  
- **escapeHtml**: A security helper function that prevents XSS attacks by safely escaping HTML content in parameter values before rendering them in the table.  
  
  > [!NOTE]
  >  All characters included in the query string are encoded by using the [encodeURIComponent function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent). This function uses the JavaScript [decodeURIComponent function](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent) to decode the values passed.  
  
```html  
<!DOCTYPE html>  
<html lang="en-us">  
<head>  
 <meta charset="UTF-8">  
 <meta name="viewport" content="width=device-width, initial-scale=1.0">  
 <title>Show Data Parameters Page</title>  
 <style>  
  body {  
   font-family: 'Segoe UI', Tahoma, Arial, sans-serif;  
   background-color: #d6e8ff;  
   margin: 20px;  
  }  
  table {  
   width: 100%;  
   max-width: 600px;  
   border-collapse: collapse;  
   margin-top: 20px;  
   box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);  
  }  
  th, td {  
   padding: 12px;  
   text-align: left;  
   border: 1px solid #ddd;  
  }  
  th {  
   background-color: #333;  
   color: white;  
   font-weight: 600;  
  }  
  tbody tr {  
   background-color: white;  
  }  
  tbody tr:hover {  
   background-color: #f5f5f5;  
  }  
  .message {  
   font-size: 16px;  
   margin-bottom: 10px;  
  }  
 </style>  
</head>  
<body>  
 <script>  
  // Wait for DOM to be ready  
  document.addEventListener('DOMContentLoaded', () => {  
   displayDataParameters();  
  });  
  
  function displayDataParameters() {  
   // Use URLSearchParams API for modern query string parsing  
   const urlParams = new URLSearchParams(window.location.search);  
   const dataParam = urlParams.get('data');  
   
   if (!dataParam) {  
    showMessage("No data parameter was passed to this page");  
    return;  
   }  
   
   try {  
    // Parse the data parameter  
    const decodedData = decodeURIComponent(dataParam);  
    const params = new URLSearchParams(decodedData);  
    
    if (params.size === 0) {  
     showMessage("No data parameter was passed to this page");  
     return;  
    }  
    
    showMessage("These are the data parameter values that were passed to this page:");  
    createParametersTable(params);  
   } catch (error) {  
    showMessage("Error parsing data parameter: " + error.message);  
   }  
  }  
  
  function showMessage(text) {  
   const message = document.createElement('p');  
   message.className = 'message';  
   message.textContent = text;  
   document.body.appendChild(message);  
  }  
  
  function createParametersTable(params) {  
   // Create table using template literals for cleaner HTML generation  
   const tableHTML = `  
    <table>  
     <thead>  
      <tr>  
       <th>Parameter</th>  
       <th>Value</th>  
      </tr>  
     </thead>  
     <tbody>  
      ${Array.from(params.entries())  
       .map(([key, value]) => `  
        <tr>  
         <td>${escapeHtml(key)}</td>  
         <td>${escapeHtml(value)}</td>  
        </tr>  
       `).join('')}  
     </tbody>  
    </table>  
   `;  
   
   document.body.insertAdjacentHTML('beforeend', tableHTML);  
  }  
  
  // Helper function to prevent XSS by escaping HTML  
  function escapeHtml(text) {  
   const div = document.createElement('div');  
   div.textContent = text;  
   return div.innerHTML;  
  }  
 </script>  
</body>  
</html>
```  
  
### Using this page  
  
1. Create a webpage web resource named `new_/ShowDataParams.htm` by using the sample code.  
  
     The parameters you want to pass are: `first=First Value&second=Second Value&third=Third Value`  
  
    > [!NOTE]
    >  If you add static parameters by using the Web Resource Properties dialog box from the form editor, you can simply paste the parameters without encoding them into the **Custom Parameter(data)** column. The portal encodes these values for you, but you still need to decode them and extract the values in your page.  
  
1. For dynamic values generated in code, use the `encodeURIComponent` method on the parameters. The encoded values are:  
  
     `first%3DFirst%20Value%26second%3DSecond%20Value%26third%3DThird%20Value`  
  
     Open the page passing the encoded parameters as the value of the data parameter:  
  
    ```  
    https://<server name>/WebResources/new_/ShowDataParams.htm?data=first%3DFirst%20Value%26second%3DSecond%20Value%26third%3DThird%20Value  
    ```  
  
    > [!NOTE]
    >  If you add the web resource to a form and paste the unencoded parameters into the **Custom Parameters(data)** column, you can just preview the form.  
  
1. The `new_/ShowDataParams.htm` displays a dynamically generated table:  
  
    |Parameter|Value|  
    |---------------|-----------|  
    |first|First Value|  
    |second|Second Value|  
    |third|Third Value|  
  
## How it works

To access the values embedded within the data query string parameter value, in your webpage web resource, extract the value of the `data` parameter. Then use code to parse the string so you can access each name-value pair individually.  
  
When the DOM is ready, the `displayDataParameters` function is called using the `DOMContentLoaded` event listener. This function uses the [URLSearchParams API](https://developer.mozilla.org/docs/Web/API/URLSearchParams) to extract the `data` parameter from the query string. If the function finds a data parameter, it decodes the value using `decodeURIComponent` and parses it as URL-encoded parameters. If no data parameter is found, the `showMessage` function displays an informative message.  
  
The `createParametersTable` function generates an HTML table using template literals and modern array methods to display the parameter name-value pairs. The `escapeHtml` helper function prevents XSS attacks by safely escaping any HTML content in the parameter values before rendering them in the table.  
  
### See also  

[Web Page (HTML) Web Resources](webpage-html-web-resources.md)   
[Web Resources](web-resources.md)   

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
