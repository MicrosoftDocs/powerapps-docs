---
title: Customize the Azure AD B2C user interface for portals
description: Learn how to customize the Azure AD B2C user interface for portals.
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2021
ms.subservice: portals
ms.author: sandhan
ms.reviewer: tapanm
contributors:
    - tapanm-msft
    - sandhangitmsft
    - dileepsinghmicrosoft
---

# Customize the Azure AD B2C user interface for portals

Azure Active Directory B2C (Azure AD B2C) supports user interface customization for sign-up and sign-in experience. With this feature, you can configure Azure AD B2C tenant with a custom sign-up and sign-in page created inside your portal. In this article, you'll learn about how to create, and configure a custom sign-up/sign-in web page with sample HTML in portals for use with Azure AD B2C authentication.

## Prerequisites

Before you begin, ensure you've configured Azure AD B2C authentication for your portal with [automatic](configure-azure-ad-b2c-provider.md), or [manual](configure-azure-ad-b2c-provider-manual.md) steps. You'll need to use this Azure AD B2C configuration to customize the user interface for portals while following below steps.

## Step 1: Create a web template

1. Open [Portal Management](configure-portal.md) app.

1. From the left pane, under **Content**, select **Web Templates**.

1. Select **New**.

1. Enter **Name**, such as *Azure AD B2C Custom Page*.

1. For **Website**, select your portal website.

1. For **Source**, copy and paste the following sample web template source HTML.

    ```html
    <!DOCTYPE html>
    <html lang="en-US">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width", initial-scale="1.0">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>
          {{ page.title | h }}
        </title>
                            <link href={{ request.url | base }}/bootstrap.min.css rel="stylesheet">
                            <link href={{ request.url | base }}/theme.css rel="stylesheet">
                            <style>
                              .page-heading {
                padding-top: 20px;
          }
          .page-copy {
                margin-bottom: 40px;
          }
          .highlightError {
            border: 1px solid #cb2027!important;
            background-color: #fce8e8!important;
          }
          .attrEntry .error.itemLevel {
            display: none;
            color: #cb2027;
            font-size: .9em;
          }
          .error {
            color: #cb2027;
          }
          .entry {
            padding-top: 8px;
            padding-bottom: 0!important;
          }
          .entry-item {
            margin-bottom: 20px;
          }
          .intro {
            display: inline;
            margin-bottom: 5px;
          }
          .pageLevel {
              width: 293px;
              text-align: center;
              margin-top: 5px;
              padding: 5px;
              font-size: 1.1em;
              height: auto;
          }
          #panel, .pageLevel, .panel li, label {
              display: block;
          }
          #forgotPassword {
              font-size: .75em;
              padding-left: 5px;
          }
          #createAccount {
              margin-left: 5px;
          }
          .working {
              display: none;
              background: url(data:image/gif;base64,R0lGODlhbgAKAPMAALy6vNze3PTy9MTCxOTm5Pz6/Ly+vNTS1Pz+/�N0Jp6BUJ9EBIISAQAh+QQJCQAKACxRAAIABgAGAAAEE1ClYU4RIIMTdCaegVCfRASCEgEAOw==) no-repeat;
              height: 10px;
              width: auto;
          }
          .divider {
            margin-top: 20px;
            margin-bottom: 10px;
          }
          .divider h2 {
            display: table;
            white-space: nowrap;
            font-size: 1em;
            font-weight: 700;
          }
          .buttons {
            margin-top: 10px;
          }
          button {
                width:auto;
                min-width:50px;
                height:32px;
                margin-top:2px;
                -moz-border-radius:0;
                -webkit-border-radius:0;
                border-radius:0;
                background:#2672E6;
                border:1px solid #FFF;
                color:#fff;
                transition:background 1s ease 0s;
                font-size:100%;
                padding:0 2px
          }
    
          button:hover {
                background:#0F3E83;
                border:1px solid #3079ed;
                -moz-box-shadow:0 0 0;
                -webkit-box-shadow:0 0 0;
                box-shadow:0 0 0
          }
          .password-label label {
            display: inline-block;
            vertical-align: baseline;
          }
          img {
                border:0
          }
          .divider {
                margin-top:20px;
                margin-bottom:10px
          }
          .divider h2 {
                display:table;
                white-space:nowrap;
                font-size:1em;
                font-weight:700
          }
          .divider h2:after,.divider h2:before {
                border-top:1px solid #B8B8B8;
                content:'';
                display:table-cell;
                position:relative;
                top:.7em;
                width:50%
          }
          .divider h2:before {
                right:1.8%
          }
          .divider h2:after {
                left:1.8%
          }
          .verificationErrorText {
                color:#D63301
          }
          .options div {
                display:inline-block;
                vertical-align:top;
                margin-top:7px
          }
          .accountButton,.accountButton:hover {
                background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAh1BMVEX///9QUFBOTk5LS0tERERCQkI/Pz9ISEg6OjpGRkZNTU08PDyAgID09PSlpaWWlpZxcXFgYGBZWVlUVFT6+vrx8fHt7e3s7Ozo6Oji4uLJycnGxsa4uLiqqqqgoKCNjY2JiYmGhoZra2tmZmb7+/vu7u7d3d3U1NTNzc2+vr67u7usrKx7e3vprNQnAAAA8klEQVQ4y63Q127DMAxAUZpDwyMeSdqsNqu7/f/va6zahgGJKAr0vgk6DyQh+6V/BiTOOeNRA9zuAWBdM6WBlPDTvaUUoAuMrT0mgNvA1IJjQB3MKjACvp6DK0WAH+agtH8H9jQHLUUgz7Uhx8xOXzNESxirLCYA2mw8tacI5FyIYXq8A9ge2Qs6oTnw2e2ruho2rjBcXJ4ADh3jBOQLQnVhRFx2gNDZ4ACogbHXj/ft9Dj5AcgbJFu5AThQWuYBIGmgtAFQo4EFB+CPGthJAPypgY3BHsheA5UNwLyAvsYNoDyroKUe4EoFTQ/yDtTONvsGUJ8KTUYyH+UAAAAASUVORK5CYII=);
                background-repeat:no-repeat
          }
          .accountButton {
                border:1px solid #FFF;
                color:#FFF;
                margin-left:0;
                margin-right:2px;
                transition:background-color 1s ease 0s;
                -moz-border-radius:0;
                -webkit-border-radius:0;
                border-radius:0;
                text-align:center;
                word-wrap:break-word;
                height:34px;
                width:158px;
                padding-left:30px;
                background-color:#505050;
          }
          .accountButton:hover {
                background-color:#B9B9B9;
                border:1px solid #FFF;
                -moz-box-shadow:0 0 0;
                -webkit-box-shadow:0 0 0;
                box-shadow:0 0 0
          }
          .accountButton:focus {
                outline:gold solid 1px
          }
          #MicrosoftAccountExchange {
                background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAPFBMVEU1pe/////t+v4uoe5btvNixPVVwfUsoe9tyfXU7/y95vu24vrd9f5NtfLH6/ys3/o/sPE6qfD2/f+f2vnAysuQAAAAaElEQVQ4y93SORKAIAwFUEGCsoT1/nd1JkkDFhY24qt+8VMkk20lu6DAaVBOBsVKsuO8aYo08IqlYyxoRTQExfyKheRIgu5Yl4KoVhSUgNOhoiYRsmb5g2u+LtzXDNOhjKgoAZ9/8k8uZWsGqcIav5wAAAAASUVORK5CYII=);
                background-color:#33A7F2
          }
          #MicrosoftAccountExchange:hover {
                background-color:#ADDBF9
          }
          #GoogleExchange {
                background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEXcTkH////cTD/bSj3ZQDLYOyzaRDbeV0vbSDrZPS/66Obyv7rsnpfpkorjcWfgZlvXOCr++Pj5393haFz88/L88fD67Or319T1zsv1zsrxuLPuqaLuqKLoi4LlfXTgYlbWMyTWMiPwtrHwta/fXVH/sCIIAAAAmElEQVQ4y+2RyQ7DIBBDMcwAIXvovqXb/39jRaX0AEmr5px3tSV7PGLhX6TVRFpN61l9zPNS6kn9gDcXO67zDnCnO2BCiNIyMtgKKJgyY2zQ68JEDtqju0nFTcOsxPUMw1GDDUqt+tY51/YNVlhvacTgEfCDIY0Q/lkBSg4RaUmmDo4/JdMzHy1Q2ejMeCj6PrXQP5+1MI8X0Y4HL4c826EAAAAASUVORK5CYII=);
                background-color:#DC4E41
          }
          #GoogleExchange:hover {
                background-color:#F1B8B3
          }
          #TwitterExchange {
                background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAdVBMVEVgqd3///9Ypdtdp9xaptxSotpQodlNn9lWo9pUo9rX6Pa+2vGTw+iLvuZlqt79/P7K4PO62O+y0+6hyutysuD2+fzi7vne6/fT5PTE3fKs0O2lzeuZx+l7tuJqrd71+Pzz9vzn8PnQ4/SCueSAueNsrt9InNh7sQwBAAAAwklEQVQ4y92PRw6EMAwAXeIkdBbY3uv/n7gSAoLDD5hbPCPZgZVihEgYgNSUpmfS7bfbtHS2nReyL2Qoc+yp8ZRAwCEWjgGAPQ7sssKoAGsWBrrgyMZCwD77Uel+59E3Tt14xZ7qlY7BRf1CDgeMKMw8sBXGlKxWtLGvHCgkQ80m0YHpjjq4sQ74pn1mISLJVSAMiwJO98l/TWSNF1eGKzqKfZ7Vj0mnHHwodpP+WIYlZP373DTtVWxYr2FD3pOBdfIHhOAHYHQI9VgAAAAASUVORK5CYII=);
                background-color:#60A9DD
          }
          #TwitterExchange:hover {
                background-color:#BFDCF1
          }
          #FacebookExchange {
                background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAaVBMVEU7W5z///85Wps3WJsiRo8xU5fw8vYyUpY0VZiAj70pS5OBkb0vUpb7+fwsTpTR1ud6irllerBPaqX09fnx8vfs7fSQoMZxg7VsgLNGY6FCX58ZP4v++/7r7vTZ3OupstGIlsFWcalDYaCK3qwDAAAAnklEQVQ4y+XQyw7CIBAFUBgc5VUoWGtb3/7/RyoYkyZAiSsXvdt7kstA/hRg/B0GpZ6byQ3Dw0NBaH+lMYRle3T0kwayACRdBrr/gnN+QtpQWv8cR4DswiUAjozlz4RdF8AmlnmwjaDQImoZwQkRedoToUS7D+ColGoTwQidx8oEQDMHN1MBva5MOL70SCHuE1TOhOpHrRt0FWAOP4IX8PsG2qEOR30AAAAASUVORK5CYII=);
                background-color:#3B5B9C
          }
          #FacebookExchange:hover {
                background-color:#B0BDD7
          }
          #LinkedInExchange {
                background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAb1BMVEUAe7b///8AdrMklscAc7EAeLUAcbB5ttifzeMqmckAdLIAaqz7+/6PxeAShr0CgLkAba4nmMctksTv9Puw1eij0OWGvNtfrNJNo80YjMAeib/D4vGt3Oy82+yfzOOCvtyJvdx3tddirtI/ncoxmMj9KsrQAAAAw0lEQVQ4y9WSVw7DIAxAG8CkjJDVzO5x/zMWk0RNJaB/kfo+sGUeCMvstgI4J7F9aS5NxSLnTWLpZVDgexTqIiycUNBhgTxRyCKPYJ3dl7sITCkO+FyLXaWU310DscASOesf3ahWChGJ5cb4ASO5Joiu2EegWEmZa1c3yUwOHmHNuQgJup4CgF8YlKpcMhKvkNmb1REz6hdetsyziIBldv8lpH8ouGm28zQFCu2SOSAXlJYGYCgpFThEMFPm/zCryja8Acy7CRfMrcKPAAAAAElFTkSuQmCC);
                background-color:#0077B5
          }
          #LinkedInExchange:hover {
                background-color:#99CAE1
          }
          #AmazonExchange {
                background-image:url(https://images-na.ssl-images-amazon.com/images/G/01/lwa/btnLWA_gold_156x32.png);
                background-color:#FFF;
                color:transparent
          }
    
          #next {
                -moz-user-select:none;
                user-select:none;
                cursor:pointer;
                width:auto;
                padding-left:10px;
                padding-right:10px;
                height:30.5px;
                -moz-border-radius:0;
               -webkit-border-radius:0;
                border-radius:0;
                background:#2672E6;
                border:1px solid #FFF;
                color:#fff;
                transition:background 1s ease 0s;
                font-size:100%
          }
          #next:hover {
                background:#0F3E83;
                border:1px solid #FFF;
                box-shadow:0 0 0
          }
          #next:hover,.accountButton:hover {
                -moz-box-shadow:0 0 0;
                -webkit-box-shadow:0 0 0;
                box-shadow:0 0 0;
          }
                            </style>
      </head>
      <body>
        <div class="navbar navbar-inverse navbar-static-top" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <div class="visible-xs-block">
                {{ snippets["Mobile Header"] }}
              </div>
              <div class="visible-sm-block visible-md-block visible-lg-block navbar-brand">
                {{ snippets["Navbar Left"] }}
              </div>
            </div>
          </div>
        </div>
        <div class="container">
          <div class="page-heading">
            <ul class="breadcrumb">
              <li>
                <a href={{ request.url | base }} title="Home">Home</a>
              </li>
              <li class="active">{{ page.title | h}}</li>
            </ul>
            {% include 'Page Header' %}
         </div>
         <div class="row">
          <div class="col-md-12">
            {% include 'Page Copy' %}
            <div id="api"></div>
          </div>
         </div>
        </div>
        <footer role="contentinfo">
          <div class="footer-top hidden-print">
            <div class="container">
              <div class="row">
                <div class="col-md-6 col-sm-12 col-xs-12 text-left">
                   {{ snippets["About Footer"] }}
                </div>
                <div class="col-md-6 col-sm-12 col-xs-12 text-right">
                  <ul class="list-social-links">
                    <li><a href=#><span class="sprite sprite-facebook_icon"></span></a></li>
                    <li><a href=#><span class="sprite sprite-twitter_icon"></span></a></li>
                    <li><a href=#><span class="sprite sprite-email_icon"></span></a></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="footer-bottom hidden-print">
            <div class="container">
              <div class="row">
                <div class="col-md-4 col-sm-12 col-xs-12 text-left">
                   {{ snippets["Footer"] | liquid }}
                </div>
                <div class="col-md-8 col-sm-12 col-xs-12 text-left">
                </div>   
              </div>
            </div>
          </div>
        </footer>
      </body>
    </html>
    ```

1. Select **Save & Close**.

## Step 2: Create a page template

1. From the left pane, under **Website**, select **Page Templates**.

1. Select **New**.

1. Enter **Name**, such as *Azure AD B2C Custom Page*.

1. For **Website**, select your portal website.

1. Select **Type** as **Web Template**.

1. For **Web Template**, select the web template that you created in [step 1](#step-1-create-a-web-template).

1. Uncheck **Use Website Header and Footer**.

1. Select **Save & Close**.

## Step 3: Create a webpage

1. From the left pane, under **Content**, select **Web Pages**.

1. Select **New**.

1. Enter **Name**, such as *Sign-in*.

1. For **Website**, select your portal website.

1. For **Parent Page**, select *Home*.

1. Enter **Partial URL** for the webpage, such as `azure-ad-b2c-sign-in`.

1. For **Page Template**, select the page template that you created in [step 2](#step-2-create-a-page-template).

1. For **Publishing State**, select *Published*.

1. Select **Save & Close**.

## Step 4: Create site settings

Site settings are required to configure cross-origin resource sharing (CORS) to allow [!include[Azure](../../../includes/pn-azure-shortest.md)] AD B2C to request the custom page and inject the sign-in or sign-up user interface. Create the following site settings.

| Name                              | Value                             |
|-----------------------------------|-----------------------------------|
| HTTP/Access-Control-Allow-Methods | `GET, OPTIONS`                      |
| HTTP/Access-Control-Allow-Origin  | `https://tenant-name.b2clogin.com` <br> For example, if tenant name is ContosoOrg, enter `https://contosoorg.b2clogin.com`. <br> **Note**: You can get this value by copying the domain name part of the [Issuer URL](configure-azure-ad-b2c-provider-manual.md). Ensure you exclude the non-domain part of the Issuer URL value&mdash;for example, exclude&mdash;`/tfp/799f7b50-f7b9-49ec-ba78-67eb67210998/b2c_1_contoso/v2.0`. |

To create site settings:

1. From the left pane, under **Website**, select **Site Settings**.

1. Select **New**.

1. Enter **Name** as listed in the table above.

1. For **Website**, select your portal website.

1. Enter **Value**, as listed in the table above.

1. Select **Save & Close**.

For a complete list of other CORS settings, see [CORS protocol support](../add-web-resource.md#cors-protocol-support).

## Step 5: Azure configuration

1. Sign in to Azure portal.

1. From the top-left corner of the Azure portal, select ![Show portal menu.](media/authentication/show-portal-menu.png "Show portal menu").

1. Select **All resources**.

1. Select your B2C tenant.

1. If not already, select **Overview** from the left pane. 

1. From the right middle section of the screen, select **Azure AD B2C Settings** for the B2C tenant. <br> This action opens B2C tenant in a separate browser tab.

1. In the B2C tenant browser tab, under **Policies** in the left pane, select **User flows**.

1. Select the user flow that you created for portals. For example, `B2C_1_Contoso`.

1. From the left pane, under **Customize**, select **Page layouts**.

1. Under **Unified sign up or sign in page**, select **Yes** for **Use custom page content**.

1. For **Custom page URI**, enter the complete URL of your portal's custom webpage that you created in [step 3](#step-3-create-a-webpage). <br> For example, for the page named `azure-ad-b2c-sign-in` in portal `https://contoso.powerappsportals.com`, use the custom page URI as `https://contoso.powerappsportals.com/azure-ad-b2c-sign-in`.

Your Azure AD B2C tenant is now configured to use the custom page for sign-up and sign-in experience.

### See also

[Configure the Azure Active Directory B2C provider (Preview)](configure-azure-ad-b2c-provider.md) <br>
[Configure the Azure Active Directory B2C provider manually](configure-azure-ad-b2c-provider-manual.md) <br>
[Customize the user interface with HTML templates in Azure Active Directory B2C](/azure/active-directory-b2c/customize-ui-with-html)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]