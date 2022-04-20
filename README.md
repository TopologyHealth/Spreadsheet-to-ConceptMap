# Spreadsheet-to-ConceptMap
Scripts to convert csv data to Concept Maps for the CAP project

The work flow to utilize these scripts is as follows:

1) script.py - handles the majority of the work by reading the csv file row by row and breaking down and extracting information to build the correct JSON format. It automatically creates a new file to print its output when the title changes. All files are printed to a folder named "NotFormatted" as there are still some issues to be dealt with by other scripts at this point in the process.
2) script2Vulva.py - works identically to the first script but handles an edge case in the file. Run this directly after you run the first script.
3) removeEmpty.js - this script contains a recursive function that will loop through every key value pair in every JSON file found in the "NotFormatted" folder and remove any key value pairs that have an empty value. This is to meet FHIR requirements. Once this script is completed, the folder with name "Formatted" will be populated but there is still once script required to complete the process.
4) scriptRemoveFirstandLast.py - handles the removal of the first and last bracket from each file in the "Formatted" folder. After this script has been completed, all JSON files found in the "Formatted" folder should be valid FHIR Concept Maps.
