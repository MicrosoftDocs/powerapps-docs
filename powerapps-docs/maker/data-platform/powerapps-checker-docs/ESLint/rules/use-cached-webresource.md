# `use-cached-webresource`

Do not use a relative or absolute URL that retrieves a web resource from the server rather than from the cache. Web resource URL's should always be relative to ensure caching support. Additionally, do not include '/WebResources/' within the URL path as it will refer to the caller's default organization.