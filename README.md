# Mission to Mars

## Overview
This project was undertaken to scrape data from multiple sites and display them on a webpage. 

Data was scraped from the below sites using Spliter, Beautiful Soup and Pandas modules:
- News about Mars: https://redplanetscience.com 
- Featured Mars Image: https://spaceimages-mars.com
- Mars facts datasheet: https://galaxyfacts-mars.com/
- Hemisphere images of Mars: https://marshemispheres.com/

The scraped data was stored on MongoDB, retrieved and displayed on a webpage with the assistance of Flask and a custom index.html template. Bootstrap 3.3.7 was used for CSS customization.

## Additional components - Deliverable 3

The following additional components were added as part of deliverable 3 to customize the webpage:

- Grid structure was made mobile friendly
- The table was added to a 'div' tag of class 'table-responsive'
- The table was converted to class 'table' from class 'dataframe' and additional classes 'table-bordered' and 'table-hover' were added 
- The button was changed to a default, block, active type from primary, large type
- The grid size for hemisphere thumbnails was changed to accomodate 4 in a row instead of 2 in a row
- The background color was changed from default white color, likewise the jumbotron class element's background color was also modified
- All main headings were made bold